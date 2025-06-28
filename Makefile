.PHONY: all ai-orchestrator studio bench mcp opa opal keycloak

# Build all containers
all: ai-orchestrator studio bench mcp opa opal keycloak

ai-orchestrator:
	docker build -t agentpods/ai-orchestrator ./ai_orchestrator

studio:
	docker build -t agentpods/studio ./docker/studio



mcp:
	docker build -t agentpods/mcp-gateway ./docker/mcp

opa:
	docker build -t agentpods/opa ./docker/opa

opal:
	docker build -t agentpods/opal ./docker/opal

keycloak:
	docker build -t agentpods/keycloak ./docker/keycloak