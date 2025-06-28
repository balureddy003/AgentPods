from __future__ import annotations

import logging
from typing import Any, Dict

from fastapi import Depends, FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator
from starlette.middleware.cors import CORSMiddleware

from .orchestrator import Orchestrator
from .registry.registry import AgentRegistry
from .db.chat_memory import ChatMemory
from .marketplace import Marketplace
from .config import get_settings
from .models import ChatRequest, MarketplaceItem, PodConfig

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

settings = get_settings()

app = FastAPI(title="AgentPods Orchestrator")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if settings.allow_all_origins else [],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

registry = AgentRegistry()
memory = ChatMemory()
orchestrator = Orchestrator(registry, memory)
marketplace = Marketplace()
Instrumentator().instrument(app).expose(app)


def get_orchestrator() -> Orchestrator:
    return orchestrator


def get_marketplace() -> Marketplace:
    return marketplace


@app.get("/health")
async def health() -> Dict[str, str]:
    return {"status": "ok"}


@app.post("/pods/admin_create")
async def admin_create(config: PodConfig, orch: Orchestrator = Depends(get_orchestrator)) -> Dict[str, Any]:
    pod = await orch.create_pod(config.dict())
    return {"pod_id": pod.pod_id}


@app.post("/pods/{pod_id}/chat")
async def chat(pod_id: str, payload: ChatRequest, orch: Orchestrator = Depends(get_orchestrator)) -> Dict[str, str]:
    result = await orch.chat(pod_id, payload.message)
    return {"response": result}


@app.get("/pods/{pod_id}/history")
async def history(pod_id: str, orch: Orchestrator = Depends(get_orchestrator)) -> Any:
    return await orch.history(pod_id)


@app.delete("/pods/{pod_id}")
async def delete_pod(pod_id: str, orch: Orchestrator = Depends(get_orchestrator)) -> Dict[str, str]:
    await orch.delete_pod(pod_id)
    return {"status": "deleted"}


@app.post("/marketplace/publish")
async def publish(item: MarketplaceItem, mp: Marketplace = Depends(get_marketplace)) -> Dict[str, str]:
    item_id = await mp.publish(item.dict())
    return {"id": item_id}


@app.get("/marketplace/list")
async def list_items(mp: Marketplace = Depends(get_marketplace)) -> Any:
    return await mp.list_items()
