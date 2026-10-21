# Ambiente de desenvolvimento do laboratório gha-lab
FROM python:3.12-slim

# git: útil para inspecionar o repositório dentro do contêiner
RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/src \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Instala as dependências primeiro (camada reaproveitada no cache do Docker)
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt setuptools actionlint-py \
    && git config --system --add safe.directory /app

CMD ["bash"]
