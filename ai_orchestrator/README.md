# AgentPods AI Orchestrator

This service orchestrates pods of AI agents. It exposes a FastAPI application that can create pods, run chats through multiple agents and publish configurations to a marketplace. The design borrows ideas from the `dream-team` and `azure-ai-travel-agents` samples such as containerized deployment, pluggable agent tools and a lightweight marketplace for sharing agents.

## Quick start

```bash
# Build container
make ai-orchestrator

# Or run locally
cd ai_orchestrator
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Environment

- `MONGO_URL` / `MONGO_DB` – MongoDB connection
- `REDIS_URL` – Redis cache URL
- `MCP_URL` – MCP Gateway URL
- `KEYCLOAK_URL` – Keycloak auth server URL
- `ALLOW_ALL_ORIGINS` – allow CORS from any origin

### Endpoints

- `POST /pods/admin_create` – create a pod from config
- `POST /pods/{pod_id}/chat` – send a chat message
- `GET /pods/{pod_id}/history` – list chat history
- `DELETE /pods/{pod_id}` – delete a pod
- `POST /marketplace/publish` – publish to marketplace
- `GET /marketplace/list` – list marketplace items
- `GET /health` – health check
- `GET /metrics` – Prometheus metrics
