# Verificación cruzada de arquitectura - Sprint 2

## Objetivo
Verificar coherencia entre arc42 Sección 5, Sección 7 y Sección 10.

## Sección 5 - Building Block View
Módulos: Inventario, Ventas, Clientes, Proveedores, Seguridad/RBAC, Comisiones y Reportes.

## Sección 7 - Deployment View
Frontend, backend futuro Node.js + Express, MongoDB futura e IaC con Terraform. No se aplica infraestructura real.

## Sección 10 - Architecture Concepts
Modelo de seguridad RBAC con roles Admin, Vendedor, Inventario, Compras y Consulta.

## Coherencia
Inventario se despliega en la arquitectura futura, RBAC protege módulos de alto valor, stock crítico se relaciona con compras, y Terraform documenta el entorno base del ERP.

## Guion de video corto
El ERP está dividido en bloques funcionales. La sección 5 muestra módulos; la sección 7 muestra el despliegue futuro; la sección 10 explica roles y permisos. La coherencia está en que cada módulo tiene una responsabilidad, cada componente tiene ubicación de despliegue y cada acceso se controla por roles.
