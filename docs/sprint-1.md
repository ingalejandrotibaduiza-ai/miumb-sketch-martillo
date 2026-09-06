# Sprint 1 - ERP Joyería Martillo Dorado

## 1. Contexto

Joyería Martillo Dorado S.A.S. requiere una solución tipo ERP para administrar inventario de joyas, clientes, proveedores, ventas y reportes. El Sprint 1 se enfoca en construir una primera versión funcional del módulo de inventario.

## 2. Sprint Goal

Al finalizar el Sprint 1 se tendrá un prototipo funcional del módulo de inventario de joyas, con formulario de registro, dashboard de indicadores, consulta por referencia, almacenamiento local y documentación inicial de arquitectura.

## 3. Product Backlog priorizado

1. Registrar joya nueva.
2. Consultar joya por referencia.
3. Visualizar dashboard de inventario.
4. Registrar proveedor asociado.
5. Documentar contratos API.
6. Diseñar arquitectura objetivo.
7. Probar almacenamiento local.
8. Validar responsive.

## 4. Sprint Backlog

| ID | Historia | Puntos | Estado |
|---|---|---:|---|
| HU-01 | Registrar joya nueva en inventario | 5 | En proceso |
| HU-02 | Consultar joya por referencia | 3 | En proceso |
| HU-03 | Visualizar dashboard de inventario | 5 | En proceso |
| HU-04 | Registrar proveedor asociado | 3 | Sprint Backlog |
| HU-05 | Documentar contratos API | 2 | Hecho |
| HU-06 | Probar localStorage | 2 | Hecho |
| HU-07 | Validar responsive | 1 | En revisión |

## 5. Definition of Done

- El código está guardado en GitHub.
- La página carga correctamente en navegador.
- El formulario valida los campos principales.
- Los datos se guardan en localStorage.
- El dashboard se actualiza después del registro.
- La documentación del Sprint 1 está actualizada.
- El backlog está listo para importar o copiar en Jira.
- El diseño es responsive.

## 6. Contrato API propuesto

### GET /api/joyas/:referencia

```json
{
  "referencia": "MD-AN-1001",
  "nombre": "Anillo Aurora Oro 18K",
  "categoria": "Anillo",
  "material": "Oro 18K",
  "precio": 1250000,
  "stock": 2,
  "estado": "Disponible"
}
```

### POST /api/joyas

```json
{
  "referencia": "MD-CD-1006",
  "nombre": "Cadena Toscana",
  "material": "Plata 925",
  "precio": 420000,
  "proveedor": "Gemas Andinas SAS"
}
```

## 7. Arquitectura objetivo

Frontend: HTML, CSS y JavaScript en el avance inicial. En una fase posterior puede migrarse a React.

Backend: Node.js con Express para exponer API REST.

Base de datos: MongoDB para almacenar joyas, clientes, proveedores y ventas.

## 8. Evidencias esperadas

- Captura del repositorio.
- Captura de la página funcionando.
- Captura del formulario de inventario.
- Captura del dashboard.
- Captura del backlog tipo Jira.
- Captura del código en GitHub.
