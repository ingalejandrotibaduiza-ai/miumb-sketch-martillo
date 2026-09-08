function calcularComision(ventasPeriodo, porcentajeComision) {
  if (ventasPeriodo < 0 || porcentajeComision < 0) {
    throw new Error('Los valores no pueden ser negativos');
  }
  return ventasPeriodo * (porcentajeComision / 100);
}

function calcularPagoNeto({ salarioBase, ventasPeriodo, porcentajeComision, porcentajeDeduccion }) {
  const comision = calcularComision(ventasPeriodo, porcentajeComision);
  const bruto = salarioBase + comision;
  const deduccion = bruto * (porcentajeDeduccion / 100);
  const neto = bruto - deduccion;
  return { salarioBase, ventasPeriodo, comision, bruto, deduccion, neto };
}

module.exports = { calcularComision, calcularPagoNeto };
