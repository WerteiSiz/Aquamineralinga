from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ChemicalParametersSchema(BaseModel):
    aluminum: float
    ammonium: float
    iron: float
    manganese: float
    copper: float
    nitrite: float
    phenols: float
    formaldehyde: float
    phosphates: float
    fluorides: float


class TerrainSchema(BaseModel):
    id: UUID
    description: str
    latitude: str
    longitude: str
    chemical_parameters: ChemicalParametersSchema
    created_at: datetime
    updated_at: datetime | None = None


class CreateTerrainRequestSchema(BaseModel):
    description: str
    latitude: str
    longitude: str
    chemical_parameters: ChemicalParametersSchema


class UpdateTerrainRequestSchema(BaseModel):
    description: str | None = None
    latitude: str | None = None
    longitude: str | None = None
    chemical_parameters: ChemicalParametersSchema | None = None
