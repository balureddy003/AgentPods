FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y gcc python3-dev build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir opal-server

EXPOSE 7002

CMD ["opal-server", "run", "--server", "--log-level=info"]