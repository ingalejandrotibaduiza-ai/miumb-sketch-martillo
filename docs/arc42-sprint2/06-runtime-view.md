# arc42 Sprint 2 - Sección 6: Runtime View

## Flujo HU-05 Stock crítico
1. El administrador registra o actualiza una joya.
2. El sistema lee stock actual y stock mínimo.
3. StockAlertEngine ejecuta la regla.
4. Si el stock actual es menor o igual al mínimo, se marca alerta.
5. El dashboard muestra alerta.

## Flujo HU-04 Comisiones
1. El administrador registra ventas del periodo.
2. El sistema recibe salario base y porcentaje de comisión.
3. PayrollEngine calcula comisión bruta.
4. Se aplican deducciones simuladas.
5. Se entrega resumen de pago neto.

## Principios
SRP para separar responsabilidades y DIP para desacoplar lógica de negocio de la interfaz.
