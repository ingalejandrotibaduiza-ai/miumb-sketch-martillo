"""Incremento funcional mínimo del módulo Inventario para el taller Scrum ERP."""

class Inventario:
    def __init__(self):
        self.productos = {}
        self.movimientos = []

    def registrar_producto(self, codigo, nombre, categoria, unidad, stock_inicial=0):
        if not all([codigo, nombre, categoria, unidad]):
            raise ValueError("Todos los campos obligatorios deben estar completos")
        if codigo in self.productos:
            raise ValueError("El código ya existe")
        if stock_inicial < 0:
            raise ValueError("El stock inicial no puede ser negativo")
        self.productos[codigo] = {
            "codigo": codigo,
            "nombre": nombre,
            "categoria": categoria,
            "unidad": unidad,
            "stock": stock_inicial,
        }
        return self.productos[codigo]

    def registrar_movimiento(self, codigo, tipo, cantidad, observacion=""):
        if codigo not in self.productos:
            raise ValueError("Producto inexistente")
        if tipo not in {"entrada", "salida"}:
            raise ValueError("Tipo de movimiento inválido")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")
        producto = self.productos[codigo]
        nuevo_stock = producto["stock"] + cantidad if tipo == "entrada" else producto["stock"] - cantidad
        if nuevo_stock < 0:
            raise ValueError("La salida no puede dejar stock negativo")
        producto["stock"] = nuevo_stock
        mov = {"codigo": codigo, "tipo": tipo, "cantidad": cantidad, "observacion": observacion}
        self.movimientos.append(mov)
        return mov

    def consultar_stock(self, termino="", categoria=None):
        termino = termino.lower().strip()
        items = list(self.productos.values())
        if termino:
            items = [p for p in items if termino in p["codigo"].lower() or termino in p["nombre"].lower()]
        if categoria:
            items = [p for p in items if p["categoria"] == categoria]
        return items
