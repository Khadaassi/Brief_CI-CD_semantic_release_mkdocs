from sqlmodel import Field, SQLModel


class ItemBase(SQLModel):
    nom: str = Field(min_length=1, max_length=255)
    prix: float = Field(gt=0)


class ItemCreate(ItemBase):
    """Schéma utilisé pour la création d'un item."""

    pass


class ItemUpdate(SQLModel):
    """Schéma utilisé pour la mise à jour : tous les champs sont optionnels."""

    nom: str | None = Field(default=None, min_length=1, max_length=255)
    prix: float | None = Field(default=None, gt=0)


class ItemResponse(ItemBase):
    """Schéma retourné au client."""

    id: int
