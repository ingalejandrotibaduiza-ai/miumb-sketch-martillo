const permisosPorRol = {
  Admin: ['inventario:leer', 'inventario:crear', 'ventas:crear', 'proveedores:crear', 'reportes:leer', 'usuarios:gestionar'],
  Vendedor: ['inventario:leer', 'ventas:crear', 'clientes:crear'],
  Inventario: ['inventario:leer', 'inventario:crear', 'inventario:actualizar'],
  Compras: ['proveedores:leer', 'proveedores:crear', 'compras:crear'],
  Consulta: ['inventario:leer']
};

function tienePermiso(rol, permiso) {
  return (permisosPorRol[rol] || []).includes(permiso);
}

module.exports = { permisosPorRol, tienePermiso };
