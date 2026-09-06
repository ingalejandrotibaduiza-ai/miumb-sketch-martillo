# Joyería Martillo Dorado ERP - Sprint 1

Repositorio académico para el avance del proyecto final de Ingeniería Web I.

## Descripción del proyecto

Joyería Martillo Dorado S.A.S. es una empresa ficticia que necesita modernizar su operación. Actualmente controla joyas, proveedores, clientes y ventas mediante hojas de cálculo y mensajes informales, lo que genera errores en inventario y poca trazabilidad de piezas valiosas.

La solución propuesta es un ERP web para centralizar la administración de la joyería.

## Sprint Goal

Al finalizar el Sprint 1 se tendrá un prototipo funcional de front-end para registrar joyas, consultar referencias, visualizar indicadores de inventario y documentar la arquitectura inicial del sistema ERP.

## MVP

- Registro de joyas con referencia, material, precio, stock, proveedor y certificado.
- Dashboard ejecutivo con total de joyas, valor de inventario y unidades disponibles.
- Consulta de joya por referencia.
- Backlog inicial real en Jira para el Sprint 1.
- Documentación de arquitectura arc42.
- Uso de localStorage para simular persistencia.

## Jira real

Sitio: https://ingalejandrotibaduiza.atlassian.net

Proyecto: SCRUM - Equipo Krono

### Épicas

- SCRUM-3: EPIC - Inventario de joyas.
- SCRUM-4: EPIC - Ventas y facturación de joyas.
- SCRUM-5: EPIC - Clientes y reservas.
- SCRUM-6: EPIC - Proveedores y compras.
- SCRUM-7: EPIC - Reportes y administración.

### Sprint 1

- SCRUM-8: HU-01 Registrar joya nueva en inventario.
- SCRUM-9: HU-02 Consultar joya por referencia.
- SCRUM-10: HU-03 Visualizar dashboard de inventario.
- SCRUM-11: HU-04 Registrar proveedor asociado.
- SCRUM-12: Tarea - Definir contratos API REST de joyas.
- SCRUM-13: Tarea - Implementar localStorage en el ERP.
- SCRUM-14: Tarea - Validar diseño responsive del ERP.
- SCRUM-15: Tarea - Documentar arquitectura inicial del ERP.

## Pull Requests de evidencia

- PR #22: feature/HU-01-inventario-joyas → develop.
- PR #23: develop → main.

## Temas del curso aplicados

- Tema 11: Float.
- Tema 12: Contenido centrado.
- Tema 13: Flexbox.
- Tema 14: Position.
- Tema 15: Transform.
- Tema 16: Formulario.
- Tema 17: Iframe.
- Tema 18: Transition.
- Tema 19: Columnas.
- Tema 20: Video.
- Tema 21: Audio.
- Tema 22: Transparencias y degradados.
- Tema 23: Animaciones.
- Tema 24: SVG.
- Tema 25: Canvas.
- Tema 26: Responsive.
- Tema 27: Contenteditable.
- Tema 28: localStorage.

## Estructura

```text
index.html
script.js
favicon.svg
styles/styles.css
docs/sprint-1.md
docs/pruebas-sprint1.md
docs/sprint-review-retrospective.md
docs/arc42/
docs/evidencias/
src/inventario.py
tests/test_inventario.py
```

## Arquitectura objetivo

```text
Frontend: HTML, CSS, JavaScript y en fase posterior React
Backend: Node.js + Express
Base de datos: MongoDB
API REST: /api/joyas, /api/clientes, /api/ventas, /api/proveedores
```

## Flujo Git ejecutado

```text
main → develop → feature/HU-01-inventario-joyas → Pull Request #22 → develop → Pull Request #23 → main
```

## Evidencias principales

- Documentación arc42: docs/arc42/
- Plan de pruebas: docs/pruebas-sprint1.md
- Sprint Review y Retrospectiva: docs/sprint-review-retrospective.md
- Evidencia Jira: docs/evidencias/jira-real-sprint1.md
- Wireframes: docs/evidencias/wireframe-dashboard.svg, wireframe-formulario.svg y wireframe-consulta.svg
