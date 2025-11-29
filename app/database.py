"""Configuration de la base de données et gestion des sessions.

Ce module gère la connexion à la base de données PostgreSQL
et fournit une fonction générateur pour obtenir des sessions de base de données.
"""

import os
from collections.abc import Generator

from sqlmodel import Session, create_engine

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    raise ValueError("DATABASE_URL environment variable is not set")

POOL_SIZE: int = 10

engine = create_engine(DATABASE_URL, pool_size=POOL_SIZE)


def get_db() -> Generator[Session]:
    """Fournit une session de base de données pour la durée de la requête."""
    with Session(engine) as session:
        yield session
