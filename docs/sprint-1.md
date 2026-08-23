# Martillo - Sprint 1

**Periodo supuesto:** 2 semanas  · **Equipo:** 1 desarrollador  · **Capacidad comprometida:** 21 SP  · **Objetivo ampliado:** 3 SP

## Objetivo del Sprint
Entregar una base funcional y segura que permita autenticar al personal administrativo, registrar consignantes y piezas, y formalizar acuerdos de consignación con trazabilidad.

## Definición de Terminado (DoD)
- Código integrado en la rama principal mediante revisión.
- Criterios de aceptación aprobados.
- Pruebas unitarias y de integración ejecutadas sin fallos.
- Validaciones, control de acceso y auditoría implementados.
- API documentada y pantalla usable en escritorio.
- Sin defectos críticos o altos abiertos.

## Priorización y estimación
| ID | Historia | MoSCoW | SP | Sprint |
|---|---|---:|---:|---|
| HU-01 | Iniciar sesión de forma segura | Must | 3 | Comprometida |
| HU-02 | Registrar y consultar consignantes | Must | 5 | Comprometida |
| HU-03 | Registrar una pieza del catálogo | Must | 8 | Comprometida |
| HU-04 | Crear un acuerdo de consignación | Must | 5 | Comprometida |
| HU-05 | Buscar y filtrar piezas | Should / ampliado | 3 | Objetivo ampliado |

La estimación se realizó individualmente con Planning Poker Fibonacci (1, 2, 3, 5, 8, 13), considerando lógica de negocio, integración frontend-backend, seguridad, persistencia, incertidumbre y esfuerzo de pruebas. Total comprometido: **21 SP**; con objetivo ampliado: **24 SP**.

## HU-01 - Iniciar sesión de forma segura
**Historia:** Como personal administrativo, quiero autenticarme con correo y contraseña, para acceder únicamente a las funciones autorizadas.
**Prioridad:** Must  · **Estimación:** 3 SP

### Criterios de aceptación
1. Dado un usuario activo, cuando ingresa credenciales válidas, entonces accede al panel y recibe una sesión JWT.
2. Dado un correo o contraseña incorrectos, cuando intenta ingresar, entonces el sistema rechaza el acceso sin revelar cuál dato falló.
3. Dado un usuario inactivo, cuando intenta ingresar, entonces el acceso es rechazado.
4. Dada una sesión vencida, cuando solicita un recurso protegido, entonces recibe estado 401 y debe autenticarse nuevamente.
5. Dado un usuario autenticado, cuando consulta un recurso sin permiso, entonces recibe estado 403.

### Tareas técnicas
- Diseñar entidad Usuario y roles
- Configurar Spring Security y JWT
- Crear endpoint POST /auth/login
- Crear pantalla React de inicio de sesión
- Implementar rutas protegidas y cierre de sesión
- Crear pruebas unitarias y de integración

### Casos de prueba
- **CP-01-01 - un usuario activo, cuando ingresa credenciales válidas** (Funcional positivo, prioridad Alta): Dado un usuario activo, cuando ingresa credenciales válidas. Verificar que accede al panel y recibe una sesión JWT. **Resultado esperado:** accede al panel y recibe una sesión JWT.
- **CP-01-02 - un correo o contraseña incorrectos, cuando intenta ingresar** (Funcional negativo, prioridad Alta): Dado un correo o contraseña incorrectos, cuando intenta ingresar. Verificar que el sistema rechaza el acceso sin revelar cuál dato falló. **Resultado esperado:** el sistema rechaza el acceso sin revelar cuál dato falló.
- **CP-01-03 - un usuario inactivo, cuando intenta ingresar** (Funcional negativo, prioridad Alta): Dado un usuario inactivo, cuando intenta ingresar. Verificar que el acceso es rechazado. **Resultado esperado:** el acceso es rechazado.
- **CP-01-04 - una sesión vencida, cuando solicita un recurso protegido** (Funcional positivo, prioridad Media): Dada una sesión vencida, cuando solicita un recurso protegido. Verificar que recibe estado 401 y debe autenticarse nuevamente. **Resultado esperado:** recibe estado 401 y debe autenticarse nuevamente.
- **CP-01-05 - un usuario autenticado, cuando consulta un recurso sin permiso** (Funcional positivo, prioridad Media): Dado un usuario autenticado, cuando consulta un recurso sin permiso. Verificar que recibe estado 403. **Resultado esperado:** recibe estado 403.

## HU-02 - Registrar y consultar consignantes
**Historia:** Como personal administrativo, quiero crear y consultar consignantes, para identificar correctamente al propietario de cada pieza.
**Prioridad:** Must  · **Estimación:** 5 SP

### Criterios de aceptación
1. Dado el formulario, cuando se registran nombre, tipo y número de documento, teléfono y correo válidos, entonces el consignante queda creado con identificador único.
2. Dado un número de documento ya registrado, cuando se intenta crear otro consignante, entonces el sistema impide el duplicado.
3. Dado un correo con formato inválido, cuando se guarda, entonces se muestra una validación y no se persiste.
4. Dado un usuario autorizado, cuando busca por nombre o documento, entonces obtiene coincidencias paginadas.
5. Dado un usuario sin permiso administrativo, cuando intenta crear o editar, entonces la operación es rechazada y auditada.

### Tareas técnicas
- Modelar Consignante y migración PostgreSQL
- Crear DTO y validaciones
- Implementar API CRUD y búsqueda paginada
- Construir formulario y listado React
- Aplicar permisos y auditoría
- Crear pruebas unitarias, API y UI

### Casos de prueba
- **CP-02-01 - el formulario, cuando se registran nombre, tipo y número de documento, teléfono y correo válidos** (Funcional positivo, prioridad Alta): Dado el formulario, cuando se registran nombre, tipo y número de documento, teléfono y correo válidos. Verificar que el consignante queda creado con identificador único. **Resultado esperado:** el consignante queda creado con identificador único.
- **CP-02-02 - un número de documento ya registrado, cuando se intenta crear otro consignante** (Funcional negativo, prioridad Alta): Dado un número de documento ya registrado, cuando se intenta crear otro consignante. Verificar que el sistema impide el duplicado. **Resultado esperado:** el sistema impide el duplicado.
- **CP-02-03 - un correo con formato inválido, cuando se guarda** (Funcional negativo, prioridad Alta): Dado un correo con formato inválido, cuando se guarda. Verificar que se muestra una validación y no se persiste. **Resultado esperado:** se muestra una validación y no se persiste.
- **CP-02-04 - un usuario autorizado, cuando busca por nombre o documento** (Funcional positivo, prioridad Media): Dado un usuario autorizado, cuando busca por nombre o documento. Verificar que obtiene coincidencias paginadas. **Resultado esperado:** obtiene coincidencias paginadas.
- **CP-02-05 - un usuario sin permiso administrativo, cuando intenta crear o editar** (Funcional positivo, prioridad Media): Dado un usuario sin permiso administrativo, cuando intenta crear o editar. Verificar que la operación es rechazada y auditada. **Resultado esperado:** la operación es rechazada y auditada.

## HU-03 - Registrar una pieza del catálogo
**Historia:** Como personal administrativo, quiero registrar una pieza con sus datos, estado y fotografías, para mantener un catálogo centralizado y trazable.
**Prioridad:** Must  · **Estimación:** 8 SP

### Criterios de aceptación
1. Dado un formulario válido, cuando se registra título, categoría, descripción, estado, precio de reserva y consignante, entonces la pieza queda con código único.
2. Dado un precio de reserva menor que cero, cuando se intenta guardar, entonces el sistema rechaza el registro.
3. Dado un consignante inexistente, cuando se intenta asociar, entonces la pieza no se crea.
4. Dadas imágenes JPG o PNG válidas, cuando se cargan hasta cinco archivos dentro del límite configurado, entonces quedan asociadas a la pieza.
5. Dado un usuario autorizado, cuando consulta el detalle, entonces ve datos, fotografías, consignante, estado y fecha de registro.

### Tareas técnicas
- Modelar Pieza, categoría, estado y relaciones
- Crear migraciones e índices
- Implementar API de alta y detalle
- Implementar almacenamiento/validación de imágenes
- Construir formulario y vista de detalle
- Registrar auditoría de creación
- Crear pruebas unitarias, integración y UI

### Casos de prueba
- **CP-03-01 - un formulario válido, cuando se registra título, categoría, descripción, estado, precio de reserva y consignante** (Funcional positivo, prioridad Alta): Dado un formulario válido, cuando se registra título, categoría, descripción, estado, precio de reserva y consignante. Verificar que la pieza queda con código único. **Resultado esperado:** la pieza queda con código único.
- **CP-03-02 - un precio de reserva menor que cero, cuando se intenta guardar** (Funcional negativo, prioridad Alta): Dado un precio de reserva menor que cero, cuando se intenta guardar. Verificar que el sistema rechaza el registro. **Resultado esperado:** el sistema rechaza el registro.
- **CP-03-03 - un consignante inexistente, cuando se intenta asociar** (Funcional negativo, prioridad Alta): Dado un consignante inexistente, cuando se intenta asociar. Verificar que la pieza no se crea. **Resultado esperado:** la pieza no se crea.
- **CP-03-04 - imágenes JPG o PNG válidas, cuando se cargan hasta cinco archivos dentro del límite configurado** (Funcional positivo, prioridad Media): Dadas imágenes JPG o PNG válidas, cuando se cargan hasta cinco archivos dentro del límite configurado. Verificar que quedan asociadas a la pieza. **Resultado esperado:** quedan asociadas a la pieza.
- **CP-03-05 - un usuario autorizado, cuando consulta el detalle** (Funcional positivo, prioridad Media): Dado un usuario autorizado, cuando consulta el detalle. Verificar que ve datos, fotografías, consignante, estado y fecha de registro. **Resultado esperado:** ve datos, fotografías, consignante, estado y fecha de registro.

## HU-04 - Crear un acuerdo de consignación
**Historia:** Como personal administrativo, quiero vincular una pieza a un acuerdo con comisión, fechas y condiciones, para formalizar la custodia y las reglas de liquidación.
**Prioridad:** Must  · **Estimación:** 5 SP

### Criterios de aceptación
1. Dada una pieza disponible y un consignante válido, cuando se crea el acuerdo con porcentaje, fecha inicial y condiciones, entonces queda activo y vinculado.
2. Dado un porcentaje fuera del rango de 0 a 100, cuando se guarda, entonces el sistema rechaza el acuerdo.
3. Dada una fecha final anterior a la inicial, cuando se guarda, entonces se informa el error y no se persiste.
4. Dada una pieza con acuerdo activo, cuando se intenta crear otro acuerdo activo, entonces el sistema impide la duplicidad.
5. Dado un acuerdo creado, cuando se consulta, entonces muestra la versión vigente y el registro de auditoría.

### Tareas técnicas
- Modelar AcuerdoConsignación y restricciones
- Crear migración y regla de acuerdo activo único
- Implementar API de creación y consulta
- Construir formulario y detalle React
- Implementar auditoría
- Crear pruebas unitarias, integración y UI

### Casos de prueba
- **CP-04-01 - una pieza disponible y un consignante válido, cuando se crea el acuerdo con porcentaje, fecha inicial y condiciones** (Funcional positivo, prioridad Alta): Dada una pieza disponible y un consignante válido, cuando se crea el acuerdo con porcentaje, fecha inicial y condiciones. Verificar que queda activo y vinculado. **Resultado esperado:** queda activo y vinculado.
- **CP-04-02 - un porcentaje fuera del rango de 0 a 100, cuando se guarda** (Funcional negativo, prioridad Alta): Dado un porcentaje fuera del rango de 0 a 100, cuando se guarda. Verificar que el sistema rechaza el acuerdo. **Resultado esperado:** el sistema rechaza el acuerdo.
- **CP-04-03 - una fecha final anterior a la inicial, cuando se guarda** (Funcional negativo, prioridad Alta): Dada una fecha final anterior a la inicial, cuando se guarda. Verificar que se informa el error y no se persiste. **Resultado esperado:** se informa el error y no se persiste.
- **CP-04-04 - una pieza con acuerdo activo, cuando se intenta crear otro acuerdo activo** (Funcional positivo, prioridad Media): Dada una pieza con acuerdo activo, cuando se intenta crear otro acuerdo activo. Verificar que el sistema impide la duplicidad. **Resultado esperado:** el sistema impide la duplicidad.
- **CP-04-05 - un acuerdo creado, cuando se consulta** (Funcional positivo, prioridad Media): Dado un acuerdo creado, cuando se consulta. Verificar que muestra la versión vigente y el registro de auditoría. **Resultado esperado:** muestra la versión vigente y el registro de auditoría.

## HU-05 - Buscar y filtrar piezas
**Historia:** Como personal administrativo, quiero buscar piezas por código, título, categoría, estado o consignante, para localizar rápidamente el inventario.
**Prioridad:** Should / ampliado  · **Estimación:** 3 SP

### Criterios de aceptación
1. Dadas piezas registradas, cuando se busca por código exacto, entonces se muestra la pieza correspondiente.
2. Dado un texto parcial del título, cuando se busca, entonces se muestran coincidencias sin distinguir mayúsculas.
3. Dados filtros de categoría y estado, cuando se aplican, entonces solo aparecen piezas que cumplen ambos.
4. Dado un consignante, cuando se filtra por él, entonces se muestran únicamente sus piezas.
5. Dado un resultado mayor al tamaño de página, cuando se consulta, entonces la respuesta es paginada y conserva filtros y orden.

### Tareas técnicas
- Definir contrato de filtros y paginación
- Crear consultas e índices de búsqueda
- Implementar endpoint GET /piezas
- Construir barra de búsqueda y filtros
- Manejar estados vacío, carga y error
- Crear pruebas de API, UI y rendimiento básico

### Casos de prueba
- **CP-05-01 - piezas registradas, cuando se busca por código exacto** (Funcional positivo, prioridad Alta): Dadas piezas registradas, cuando se busca por código exacto. Verificar que se muestra la pieza correspondiente. **Resultado esperado:** se muestra la pieza correspondiente.
- **CP-05-02 - un texto parcial del título, cuando se busca** (Funcional negativo, prioridad Alta): Dado un texto parcial del título, cuando se busca. Verificar que se muestran coincidencias sin distinguir mayúsculas. **Resultado esperado:** se muestran coincidencias sin distinguir mayúsculas.
- **CP-05-03 - filtros de categoría y estado, cuando se aplican** (Funcional negativo, prioridad Alta): Dados filtros de categoría y estado, cuando se aplican. Verificar que solo aparecen piezas que cumplen ambos. **Resultado esperado:** solo aparecen piezas que cumplen ambos.
- **CP-05-04 - un consignante, cuando se filtra por él** (Funcional positivo, prioridad Media): Dado un consignante, cuando se filtra por él. Verificar que se muestran únicamente sus piezas. **Resultado esperado:** se muestran únicamente sus piezas.
- **CP-05-05 - un resultado mayor al tamaño de página, cuando se consulta** (Funcional positivo, prioridad Media): Dado un resultado mayor al tamaño de página, cuando se consulta. Verificar que la respuesta es paginada y conserva filtros y orden. **Resultado esperado:** la respuesta es paginada y conserva filtros y orden.

## Riesgos y dependencias
- La carga de imágenes puede requerir almacenamiento externo; en Sprint 1 se admite almacenamiento local configurable.
- La seguridad JWT debe quedar lista antes de exponer los módulos.
- Los datos de consignantes requieren control por roles y auditoría.
- HU-05 solo entra si las cuatro historias comprometidas cumplen la DoD.

## Estructura sugerida en herramientas
- **Jira:** épica → historias HU-01 a HU-05 → subtareas técnicas; Sprint “Martillo - Sprint 1”.
- **GitHub:** milestone “Sprint 1”; una issue por historia, labels `sprint-1`, `must/should`, `3/5/8-sp`, `seguridad/catalogo/consignacion`.
- **Notion:** base “Sprint Backlog” con ID, historia, prioridad, SP, estado, criterios y tareas; segunda base “Plan de pruebas” relacionada por ID de historia.