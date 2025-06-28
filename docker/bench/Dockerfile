FROM python:3.10-slim

# Install dependencies
RUN pip install --upgrade pip && pip install autogenbench

# Copy scenarios and config into image
COPY scenarios /scenarios
COPY OAI_CONFIG_LIST.json /config/OAI_CONFIG_LIST.json

# Expose a port if needed (optional for autogenbench)
EXPOSE 8082

# Run the default scenario with config
CMD ["autogenbench", "run", "/scenarios/simple_scenario.jsonl", "--config", "/config/OAI_CONFIG_LIST.json", "--repeat", "1"]