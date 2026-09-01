import unittest
from src.inventario import Inventario

class TestInventario(unittest.TestCase):
    def setUp(self):
        self.inv = Inventario()

    def test_registrar_producto(self):
        p = self.inv.registrar_producto("P-001", "Teclado", "Tecnología", "und", 10)
        self.assertEqual(p["stock"], 10)

    def test_codigo_duplicado(self):
        self.inv.registrar_producto("P-001", "Teclado", "Tecnología", "und", 10)
        with self.assertRaises(ValueError):
            self.inv.registrar_producto("P-001", "Otro", "Tecnología", "und", 1)

    def test_movimiento_entrada_y_salida(self):
        self.inv.registrar_producto("P-001", "Teclado", "Tecnología", "und", 10)
        self.inv.registrar_movimiento("P-001", "entrada", 5)
        self.inv.registrar_movimiento("P-001", "salida", 3)
        self.assertEqual(self.inv.productos["P-001"]["stock"], 12)

    def test_no_permite_stock_negativo(self):
        self.inv.registrar_producto("P-001", "Teclado", "Tecnología", "und", 2)
        with self.assertRaises(ValueError):
            self.inv.registrar_movimiento("P-001", "salida", 3)

if __name__ == "__main__":
    unittest.main()
