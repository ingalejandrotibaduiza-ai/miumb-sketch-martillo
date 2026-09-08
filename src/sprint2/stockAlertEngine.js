function estaEnStockCritico(producto) {
  if (!producto || typeof producto.stockActual !== 'number' || typeof producto.stockMinimo !== 'number') {
    throw new Error('Producto inválido');
  }
  return producto.stockActual <= producto.stockMinimo;
}

function obtenerProductosCriticos(productos) {
  return productos.filter(estaEnStockCritico);
}

module.exports = { estaEnStockCritico, obtenerProductosCriticos };
