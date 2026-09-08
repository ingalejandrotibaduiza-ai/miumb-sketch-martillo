# Joyería Martillo Dorado ERP - Sprint 1 y Sprint 2

Repositorio académico para el proyecto final de Ingeniería Web I y Arquitectura de Software.

## Descripción del proyecto

Joyería Martillo Dorado S.A.S. es una empresa ficticia que necesita modernizar su operación. Actualmente controla joyas, proveedores, clientes y ventas mediante hojas de cálculo y mensajes informales, lo que genera errores en inventario y poca trazabilidad de piezas valiosas.

La solución propuesta es un ERP web para centralizar inventario, ventas, clientes, proveedores, reportes, roles de acceso y futuras integraciones con backend.

## Sprint 1

### Sprint Goal
Al finalizar el Sprint 1 se obtiene un prototipo funcional de front-end para registrar joyas, consultar referencias, visualizar indicadores de inventario y documentar la arquitectura inicial.

### MVP Sprint 1
- Registro de joyas con referencia, material, precio, stock, proveedor y certificado.
- Dashboard ejecutivo.
- Consulta por referencia.
- Backlog inicial real en Jira.
- Documentación arc42 inicial.
- Uso de localStorage.

## Sprint 2

### Sprint Goal
Al finalizar el Sprint 2, el ERP contará con control de stock crítico, cálculo simulado de comisiones y nómina de vendedores, control de acceso por roles, documentación arc42 actualizada y una base de Infraestructura como Código con Terraform versionada en GitHub.

### Alcance Sprint 2
- HU-04 Calcular comisiones y nómina de vendedores.
- HU-05 Implementar alerta de stock crítico.
- HU-06 Implementar control de acceso por roles RBAC.
- HU-07 Crear infraestructura base con Terraform.
- HU-08 Actualizar documentación de seguridad y despliegue.
- Workflow GitHub Actions para terraform plan.
- PlantUML de componentes, RBAC, stock crítico y deployment.
- Guion en inglés para video de mínimo 2 minutos.

## Jira real

Sitio: https://ingalejandrotibaduiza.atlassian.net
Proyecto: SCRUM - Equipo Krono

### Sprint 1
- SCRUM-3: EPIC - Inventario de joyas.
- SCRUM-4: EPIC - Ventas y facturación de joyas.
- SCRUM-5: EPIC - Clientes y reservas.
- SCRUM-6: EPIC - Proveedores y compras.
- SCRUM-7: EPIC - Reportes y administración.
- SCRUM-8: HU-01 Registrar joya nueva en inventario.
- SCRUM-9: HU-02 Consultar joya por referencia.
- SCRUM-10: HU-03 Visualizar dashboard de inventario.
- SCRUM-11: HU-04 Registrar proveedor asociado.
- SCRUM-12: Tarea - Definir contratos API REST de joyas.
- SCRUM-13: Tarea - Implementar localStorage en el ERP.
- SCRUM-14: Tarea - Validar diseño responsive del ERP.
- SCRUM-15: Tarea - Documentar arquitectura inicial del ERP.

### Sprint 2
- SCRUM-16: EPIC - Sprint 2 Funcionalidades avanzadas e IaC.
- SCRUM-17: HU-04 Calcular comisiones y nómina de vendedores.
- SCRUM-18: HU-05 Implementar alerta de stock crítico.
- SCRUM-19: HU-06 Implementar control de acceso por roles RBAC.
- SCRUM-20: HU-07 Crear infraestructura base con Terraform.
- SCRUM-21: HU-08 Actualizar documentación de seguridad y despliegue.
- SCRUM-22: Tarea - Crear workflow Terraform Plan en GitHub Actions.
- SCRUM-23: Tarea - Realizar verificación cruzada de arquitectura.
- SCRUM-24: Tarea - Evidencia final Sprint 2 en Word.

## Pull Requests de evidencia

### Sprint 1
- PR #22: feature/HU-01-inventario-joyas → develop.
- PR #23: develop → main.

### Sprint 2
- PR #24: feature/HU-07-terraform-sprint2 → develop.
- PR #25: develop → main.

Nota: GitHub no permite aprobar formalmente Pull Requests propios, por eso se registró comentario de revisión académica.

## Temas y conceptos aplicados

- Scrum: Sprint Planning, Sprint Backlog, Sprint Review y Sprint Retrospective.
- Arquitectura: arc42, Building Block View, Runtime View, Deployment View y Architecture Concepts.
- DevOps: ramas feature/develop/main, Pull Requests y GitHub Actions.
- IaC: Terraform académico sin despliegue real para evitar costos.
- Seguridad: RBAC.
- Front-end: HTML, CSS, JavaScript, SVG, Canvas, responsive, localStorage.

## Estructura principal

```text
index.html
script.js
favicon.svg
styles/styles.css
docs/sprint-1.md
docs/sprint-2.md
docs/arc42/
docs/arc42-sprint2/
docs/plantuml/
infra/terraform/
.github/workflows/terraform-plan.yml
src/sprint2/
tests/sprint2.test.js
```

## Comandos útiles

```bash
npm run test:sprint2
cd infra/terraform
terraform fmt -check
terraform init
terraform validate
terraform plan
```

## Integrante

Alejandro Tibaduiza Morales.
