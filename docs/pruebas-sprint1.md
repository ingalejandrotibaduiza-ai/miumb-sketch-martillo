# Plan de pruebas Sprint 1

## Objetivo
Validar el comportamiento funcional básico del prototipo ERP Joyería Martillo Dorado S.A.S.

| ID | Prueba | Pasos | Resultado esperado | Estado |
|---|---|---|---|---|
| ERP-JOY-01 | Registrar joya válida | Completar formulario con referencia, nombre, categoría, material, precio, stock y proveedor. Presionar Guardar. | La joya aparece en la tabla y se actualizan métricas. | Aprobada |
| ERP-JOY-02 | Validar campos vacíos | Intentar guardar sin nombre o referencia. | El sistema muestra alerta y no registra la joya. | Aprobada |
| ERP-JOY-03 | Consultar por referencia existente | Buscar MD-AN-1001. | Se muestran datos de la joya. | Aprobada |
| ERP-JOY-04 | Consultar referencia inexistente | Buscar una referencia que no existe. | Se muestra mensaje controlado de no encontrado. | Aprobada |
| ERP-JOY-05 | Guardar notas editables | Editar notas y presionar Guardar. | El texto permanece después de recargar la página. | Aprobada |
| ERP-JOY-06 | Diseño responsive | Reducir pantalla a tamaño móvil. | Las columnas se reorganizan en una sola columna. | Aprobada |
| ERP-JOY-07 | Canvas | Dibujar en el canvas y limpiar. | El usuario puede dibujar y borrar el contenido. | Aprobada |

## Observación
Las pruebas son manuales porque el Sprint 1 es un prototipo front-end. En Sprint 2 se propone agregar pruebas automatizadas para API REST y componentes.