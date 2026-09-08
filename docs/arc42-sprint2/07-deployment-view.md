# arc42 Sprint 2 - Sección 7: Deployment View

## Vista de despliegue propuesta
- Cliente: navegador web.
- Frontend: HTML/CSS/JavaScript actual; React en fase posterior.
- Backend futuro: Node.js + Express.
- Base de datos futura: MongoDB o servicio gestionado equivalente.
- IaC: Terraform para definir red, subredes y base de datos futura.
- CI/CD: GitHub Actions para ejecutar terraform plan en Pull Requests.

## Decisión académica
No se ejecuta terraform apply sobre proveedor real porque podría generar costos. Se entrega código base de Terraform versionado, validable y documentado.

## Relación con la guía
Responde a la solicitud de documentar Deployment View con diagrama de infraestructura y código IaC versionado.
