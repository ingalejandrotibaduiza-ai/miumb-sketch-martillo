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
- Backlog inicial tipo Jira para el Sprint 1.
- Documentación de arquitectura y contratos API.
- Uso de localStorage para simular persistencia.

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
docs/jira_backlog_sprint1.csv
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

## Flujo Git sugerido

```bash
git status
git add .
git commit -m "Sprint 1 ERP joyeria Martillo Dorado"
git push
```
