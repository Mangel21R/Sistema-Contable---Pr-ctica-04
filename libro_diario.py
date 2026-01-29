"""
Módulo contable para gestionar un libro diario.
Permite registrar transacciones y calcular resúmenes.
"""
from typing import List, Dict, Union


class LibroDiario:
    """Clase para gestionar transacciones financieras."""

    def __init__(self) -> None:
        """Inicializa la lista de transacciones vacía."""
        self.transacciones: List[Dict[str, Union[str, float]]] = []

    def agregar_transaccion(
        self, fecha: str, descripcion: str, monto: float, tipo: str
    ) -> None:
        """
        Agrega una nueva transacción al libro diario.

        Args:
            fecha (str): Fecha de la transacción.
            descripcion (str): Detalle.
            monto (float): Valor (>0).
            tipo (str): 'ingreso' o 'egreso'.

        Raises:
            ValueError: Si monto <= 0 o tipo inválido.
        """
        if monto <= 0:
            raise ValueError("El monto debe ser positivo.")

        if tipo not in ["ingreso", "egreso"]:
            raise ValueError("Tipo debe ser 'ingreso' o 'egreso'.")

        self.transacciones.append({
            "fecha": fecha,
            "descripcion": descripcion,
            "monto": monto,
            "tipo": tipo
        })

    def obtener_resumen(self) -> Dict[str, float]:
        """
        Calcula el total de ingresos y egresos.

        Returns:
            Dict[str, float]: Totales de 'ingresos' y 'egresos'.
        """
        total_ingresos = 0.0
        total_egresos = 0.0

        for transaccion in self.transacciones:
            if transaccion["tipo"] == "ingreso":
                total_ingresos += transaccion["monto"]
            else:
                total_egresos += transaccion["monto"]

        return {
            "total_ingresos": total_ingresos,
            "total_egresos": total_egresos
        }
        # --- CÓDIGO DE PRUEBA (Para ver que funciona) ---
if __name__ == "__main__":
    libro = LibroDiario()
    
    # Registramos algunas transacciones
    print("Registrando transacciones...")
    libro.agregar_transaccion("2025-01-28", "Venta de servicios", 500.0, "ingreso")
    libro.agregar_transaccion("2025-01-29", "Pago de luz", 50.0, "egreso")
    libro.agregar_transaccion("2025-01-30", "Compra de suministros", 100.0, "egreso")

    # Pedimos el resumen
    resultado = libro.obtener_resumen()
    
    # Mostramos el resultado
    print("-" * 30)
    print(f"Total Ingresos: ${resultado['total_ingresos']}")
    print(f"Total Egresos:  ${resultado['total_egresos']}")
    print(f"Saldo Final:    ${resultado['total_ingresos'] - resultado['total_egresos']}")
    print("-" * 30)