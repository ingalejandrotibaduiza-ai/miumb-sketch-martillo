# Plan de pruebas - Sprint 2

| ID | Prueba | Entrada | Resultado esperado | Estado |
|---|---|---|---|---|
| PT-01 | Calcular comisión | salario 1500000, ventas 5000000, comisión 5% | Comisión 250000 y neto calculado | Planeada |
| PT-02 | Stock crítico | stock actual 1, mínimo 3 | Producto crítico | Planeada |
| PT-03 | Permiso Admin | rol Admin, permiso usuarios:gestionar | Acceso permitido | Planeada |
| PT-04 | Permiso Vendedor | rol Vendedor, permiso proveedores:crear | Acceso denegado | Planeada |
| PT-05 | Terraform validate | archivos .tf | Validación sin errores sintácticos | Planeada |
| PT-06 | Workflow CI | PR a develop con cambios .tf | Ejecuta terraform fmt/init/validate/plan | Planeada |
| PT-07 | arc42 | secciones 5, 7 y 10 | Coherencia entre bloques, despliegue y roles | Planeada |

Nota: no se despliega infraestructura real para evitar costos.
