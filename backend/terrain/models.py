from datetime import datetime
import uuid

from sqlalchemy import String, UUID, ForeignKey, Float, DateTime
from sqlalchemy.orm import mapped_column, Mapped, relationship

from core.base_model import Base


class Terrain(Base):
    __tablename__ = 'terrains'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    description: Mapped[str] = mapped_column(String, nullable=False)
    latitude: Mapped[str] = mapped_column(String, nullable=False)
    longitude: Mapped[str] = mapped_column(String, nullable=False)
    chemical_parameters: Mapped["ChemicalParameters"] = relationship("ChemicalParameters", back_populates="terrain", uselist=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

class ChemicalParameters(Base):
    __tablename__ = 'chemical_parameters'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    terrain_id: Mapped[UUID] = mapped_column(ForeignKey('terrains.id', ondelete='CASCADE'), unique=True)

    aluminum: Mapped[float] = mapped_column(Float, nullable=False)
    ammonium: Mapped[float] = mapped_column(Float, nullable=False)
    iron: Mapped[float] = mapped_column(Float, nullable=False)
    manganese: Mapped[float] = mapped_column(Float, nullable=False)
    copper: Mapped[float] = mapped_column(Float, nullable=False)
    nitrite: Mapped[float] = mapped_column(Float, nullable=False)
    phenols: Mapped[float] = mapped_column(Float, nullable=False)
    formaldehyde: Mapped[float] = mapped_column(Float, nullable=False)
    phosphates: Mapped[float] = mapped_column(Float, nullable=False)
    fluorides: Mapped[float] = mapped_column(Float, nullable=False)

    terrain: Mapped["Terrain"] = relationship("Terrain", back_populates="chemical_parameters")




