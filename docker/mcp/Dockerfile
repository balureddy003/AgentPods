# Use the official MCP Context Forge image as base
FROM ghcr.io/ibm/mcp-context-forge:0.2.0

# Set environment variables for configuration
ENV DATABASE_URL=sqlite:////data/mcp.db
ENV HOST=0.0.0.0
ENV JWT_SECRET_KEY=my-test-key
ENV BASIC_AUTH_USER=admin
ENV BASIC_AUTH_PASSWORD=changeme

# Expose the MCP Gateway port
EXPOSE 4444

# Define the volume for persistent data
VOLUME ["/data"]

# Use the default entrypoint and command from the base image