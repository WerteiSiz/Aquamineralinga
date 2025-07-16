from datetime import datetime

from fastapi import APIRouter
from sqlalchemy.orm import scoped_session

from auth.security import manager, limiter

from core.database import get_session
from terrain.models import Terrain, ChemicalParameters
from terrain.schemas import TerrainSchema, CreateTerrainRequestSchema, UpdateTerrainRequestSchema, \
    ChemicalParametersSchema

router = APIRouter()

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import joinedload
from uuid import UUID

router = APIRouter()


@router.post('/', response_model=TerrainSchema)
async def create_terrain(data: CreateTerrainRequestSchema, db: scoped_session = Depends(get_session),
                         user=Depends(manager)):
    terrain_data = data.model_dump(exclude={'chemical_parameters'})
    terrain = Terrain(**terrain_data, user_id=user.id)
    db.add(terrain)
    db.flush()

    if data.chemical_parameters:
        chem_params = ChemicalParameters(**data.chemical_parameters.model_dump(), terrain_id=terrain.id)
        db.add(chem_params)

    db.commit()
    db.refresh(terrain)
    return terrain


@router.patch("/{terrain_id}", response_model=TerrainSchema)
async def update_terrain(
        terrain_id: UUID,
        data: UpdateTerrainRequestSchema,
        db: scoped_session = Depends(get_session),
        user=Depends(manager)
):
    terrain = db.query(Terrain).filter(Terrain.id == terrain_id, Terrain.user_id == user.id).first()
    if not terrain:
        raise HTTPException(status_code=404, detail="Terrain not found")

    terrain_data = data.dict(exclude_unset=True,
                             exclude={'chemical_parameters'})
    for field, value in terrain_data.items():
        setattr(terrain, field, value)

    def upsert_related(related_name, related_class, data_dict):
        if not data_dict:
            return
        related_obj = getattr(terrain, related_name)
        if related_obj:
            for field, val in data_dict.items():
                setattr(related_obj, field, val)
        else:
            new_obj = related_class(**data_dict, terrain_id=terrain.id)
            db.add(new_obj)

    upsert_related(
        'chemical_parameters',
        ChemicalParameters,
        data.chemical_parameters.dict(exclude_unset=True) if data.chemical_parameters else None
    )
    terrain.updated_at = datetime.now()
    db.add(terrain)
    db.commit()
    db.refresh(terrain)
    return terrain


def admin_only(user=Depends(manager)):
    if user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin privileges required"
        )
    return user

@router.get("/", response_model=list[TerrainSchema])
async def get_terrains(
        db: scoped_session = Depends(get_session),
        user=Depends(admin_only)
):
    terrains = db.query(Terrain).options(
        joinedload(Terrain.chemical_parameters)
    ).all()
    return terrains



@router.get("/{terrain_id}", response_model=TerrainSchema)
async def get_terrain_by_id(
        terrain_id: UUID,
        db: scoped_session = Depends(get_session),
        user=Depends(manager)
):
    terrain = db.query(Terrain).filter(
        Terrain.id == terrain_id,
        Terrain.user_id == user.id
    ).options(
        joinedload(Terrain.chemical_parameters)
    ).first()
    if not terrain:
        raise HTTPException(status_code=404, detail="Terrain not found")
    return terrain


@router.delete("/{terrain_id}")
async def delete_terrain(
        terrain_id: UUID,
        db: scoped_session = Depends(get_session),
        user=Depends(manager)
):
    deleted = db.query(Terrain).filter(Terrain.id == terrain_id, Terrain.user_id == user.id).delete()
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Terrain not found")
    db.commit()
    return {"id": terrain_id}
