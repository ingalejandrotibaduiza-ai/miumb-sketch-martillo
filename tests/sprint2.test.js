const assert = require('assert');
const { calcularComision, calcularPagoNeto } = require('../src/sprint2/payrollEngine');
const { estaEnStockCritico, obtenerProductosCriticos } = require('../src/sprint2/stockAlertEngine');
const { tienePermiso } = require('../src/sprint2/rbac');

assert.strictEqual(calcularComision(5000000, 5), 250000);
const pago = calcularPagoNeto({ salarioBase: 1500000, ventasPeriodo: 5000000, porcentajeComision: 5, porcentajeDeduccion: 4 });
assert.strictEqual(pago.comision, 250000);
assert.strictEqual(pago.neto, 1680000);
assert.strictEqual(estaEnStockCritico({ stockActual: 1, stockMinimo: 3 }), true);
assert.strictEqual(estaEnStockCritico({ stockActual: 5, stockMinimo: 3 }), false);
assert.strictEqual(obtenerProductosCriticos([{ stockActual: 1, stockMinimo: 3 }, { stockActual: 8, stockMinimo: 2 }]).length, 1);
assert.strictEqual(tienePermiso('Admin', 'usuarios:gestionar'), true);
assert.strictEqual(tienePermiso('Vendedor', 'proveedores:crear'), false);
console.log('Pruebas Sprint 2 ejecutadas correctamente.');
