"""Módulo base de inventario para el ERP de Joyería Martillo Dorado."""

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Joya:
    referencia: str
    nombre: str
    categoria: str
    material: str
    precio: float
    stock: int
    proveedor: str
    certificado: bool
    estado: str = "Disponible"


class InventarioJoyeria:
    """Servicio de dominio para registrar y consultar joyas."""

    def __init__(self) -> None:
        self._joyas: Dict[str, Joya] = {}

    def registrar_joya(self, joya: Joya) -> None:
        if joya.referencia in self._joyas:
            raise ValueError("La referencia ya existe en el inventario.")
        if joya.precio <= 0:
            raise ValueError("El precio debe ser mayor a cero.")
        if joya.stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._joyas[joya.referencia] = joya

    def consultar_por_referencia(self, referencia: str) -> Joya:
        if referencia not in self._joyas:
            raise KeyError("No existe una joya con esa referencia.")
        return self._joyas[referencia]

    def listar_joyas(self) -> List[Joya]:
        return list(self._joyas.values())

    def valor_total_inventario(self) -> float:
        return sum(joya.precio * joya.stock for joya in self._joyas.values())

    def stock_total(self) -> int:
        return sum(joya.stock for joya in self._joyas.values())
