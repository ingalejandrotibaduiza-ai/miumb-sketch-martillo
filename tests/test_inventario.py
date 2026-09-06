import pytest

from src.inventario import InventarioJoyeria, Joya


def crear_joya():
    return Joya(
        referencia="MD-AN-1001",
        nombre="Anillo Aurora Oro 18K",
        categoria="Anillo",
        material="Oro 18K",
        precio=1250000,
        stock=2,
        proveedor="Gemas Andinas SAS",
        certificado=True,
    )


def test_registrar_joya_y_consultar_por_referencia():
    inventario = InventarioJoyeria()
    joya = crear_joya()
    inventario.registrar_joya(joya)
    assert inventario.consultar_por_referencia("MD-AN-1001").nombre == "Anillo Aurora Oro 18K"


def test_no_permite_referencia_duplicada():
    inventario = InventarioJoyeria()
    joya = crear_joya()
    inventario.registrar_joya(joya)
    with pytest.raises(ValueError):
        inventario.registrar_joya(joya)


def test_calcula_valor_total_inventario():
    inventario = InventarioJoyeria()
    inventario.registrar_joya(crear_joya())
    assert inventario.valor_total_inventario() == 2500000
