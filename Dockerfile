# 1) Base commune : Python + uv
FROM python:3.13-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Dépendances système (build + PostgreSQL)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    curl \
 && rm -rf /var/lib/apt/lists/*

# Installer uv (gestionnaire de paquets ultra rapide)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
ENV UV_SYSTEM_PYTHON=1

WORKDIR /app


# 2) Builder : installation des dépendances + appli
FROM base AS builder

# Copier uniquement les fichiers de config d'abord pour profiter du cache
COPY pyproject.toml ./
# Si tu ajoutes un uv.lock plus tard, tu pourras décommenter :
# COPY uv.lock ./

# On copie ensuite le reste du code
COPY . .

# Installation du projet dans l'environnement système
# -e . = editable, pratique en dev, tu peux le remplacer par juste "."
RUN uv pip install --system --no-cache-dir -e .


# 3) Runtime : image finale plus propre
FROM python:3.13-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# On copie uniquement ce qui est nécessaire depuis le builder
COPY --from=builder /usr/local /usr/local
COPY --from=builder /app /app

# Utilisateur non-root
RUN groupadd -r app && useradd -r -g app app
USER app

EXPOSE 8000

# Commande de lancement FastAPI (prod, pas dev)
CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "8000"]
