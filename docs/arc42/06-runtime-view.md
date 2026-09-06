# 6. Vista en tiempo de ejecución

## Flujo: registrar joya
1. El administrador abre la página del ERP.
2. Diligencia referencia, nombre, categoría, material, precio, stock, proveedor y certificado.
3. JavaScript valida campos obligatorios.
4. La joya se agrega al arreglo de inventario.
5. El arreglo se guarda en localStorage.
6. El dashboard se actualiza automáticamente.

## Flujo: consultar joya
1. El vendedor ingresa una referencia.
2. JavaScript busca en el inventario local.
3. Si encuentra la joya, muestra datos completos.
4. Si no existe, muestra mensaje de error controlado.

## Flujo futuro con API
El front-end enviará peticiones HTTP al backend Express y este consultará MongoDB.