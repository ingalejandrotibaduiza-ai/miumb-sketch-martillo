# arc42 Sprint 2 - Sección 10: Architecture Concepts

## Seguridad y roles RBAC
| Rol | Permisos principales |
|---|---|
| Admin | Acceso total a módulos y configuración |
| Vendedor | Consulta inventario, clientes y ventas |
| Inventario | Registro, edición y stock crítico |
| Compras | Proveedores y órdenes de compra |
| Consulta | Solo lectura |

## Conceptos transversales
- Validación de entradas.
- Separación entre interfaz, lógica de negocio y persistencia.
- Registro de decisiones arquitectónicas.
- No exponer credenciales.
- Uso de variables para infraestructura.

## Riesgos
Acceso no autorizado, modificación indebida de stock y exposición de credenciales.

## Mitigaciones
Roles, permisos, variables protegidas, revisión PR y validaciones GitHub Actions.
