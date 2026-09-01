# Taller Scrum ERP - Un solo tablero

Repositorio principal del taller aplicado de Scrum para un ERP, integrando Jira, Figma, PlantUML, GitHub, código, pruebas y documentación viva.

## Alcance ERP

El ERP se organiza en un único tablero Jira con cinco módulos como épicas:

- Compras: solicitud, orden de compra y recepción.
- Inventario: altas/bajas, movimientos y stock.
- Facturación: emisión, impuestos y pagos.
- Contabilidad: asientos y conciliación.
- RR. HH.: nómina simplificada y ausencias.

El Sprint 1 se concentra en Inventario con 3 historias y 13 puntos.

## Enlaces principales

- Jira - épica Inventario: https://academia-team-g3jymqx2.atlassian.net/browse/SCRUM-8
- Jira - SCRUM-12: https://academia-team-g3jymqx2.atlassian.net/browse/SCRUM-12
- Jira - SCRUM-13: https://academia-team-g3jymqx2.atlassian.net/browse/SCRUM-13
- Jira - SCRUM-14: https://academia-team-g3jymqx2.atlassian.net/browse/SCRUM-14
- Figma: https://www.figma.com/design/bKDiVKHWbJTkElWHEXYL2N
- Issues GitHub: https://github.com/ingalejandrotibaduiza-ai/miumb-sketch-martillo/issues

## Historias Sprint 1

- SCRUM-12 - Registrar producto en inventario - 5 puntos.
- SCRUM-13 - Registrar movimiento de inventario - 5 puntos.
- SCRUM-14 - Consultar stock de productos - 3 puntos.

## Estructura

- `/docs`: documentación, DoR, DoD y trazabilidad.
- `/design`: referencia al prototipo editable en Figma.
- `/diagrams`: componentes, secuencia, clases y despliegue en PlantUML.
- `/src`: incremento funcional mínimo del módulo Inventario.
- `/tests`: casos de prueba y pruebas automatizadas.
- `/.github/workflows`: CI básico.

## Flujo Git

El trabajo del taller se integra mediante la rama `feature/erp-scrum-inventario` y Pull Request. Los commits, ramas e issues usan las claves Jira para mantener trazabilidad.

## Historial anterior

Este repositorio nació como el proyecto académico Martillo para casas de subastas. Sus documentos e issues anteriores se conservan como historial; el alcance actual del repositorio es el Taller Scrum ERP solicitado.
