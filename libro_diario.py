"""
Módulo contable para gestionar un libro diario.
Permite registrar transacciones y calcular resúmenes de ingresos y egresos.
"""
from typing import List, Dict, Union


class LibroDiario:
    """
    Clase para gestionar transacciones financieras.
    Permite agregar movimientos y obtener un balance general.
    """

    def __init__(self) -> None:
        """Inicializa la lista de transacciones vacía."""
        self.transacciones: List[Dict[str, Union[str, float]]] = []

    def agregar_transaccion(
            self,
            fecha: str,
            descripcion: str,
            monto: float,
            tipo_movimiento: str
    ) -> None:
        """
        Agrega una nueva transacción al libro diario.

        Args:
            fecha (str): Fecha de la transacción.
            descripcion (str): Detalle de la transacción.
            monto (float): Valor monetario (debe ser positivo).
            tipo_movimiento (str): Tipo ('ingreso' o 'egreso').

        Raises:
            ValueError: Si el monto es negativo o el tipo no es válido.
        """
        if monto <= 0:
            raise ValueError("El monto debe ser un número positivo.")

        if tipo_movimiento not in ["ingreso", "egreso"]:
            raise ValueError("El tipo debe ser 'ingreso' o 'egreso'.")

        self.transacciones.append({
            "fecha": fecha,
            "descripcion": descripcion,
            "monto": monto,
            "tipo": tipo_movimiento
        })

    def obtener_resumen(self) -> Dict[str, float]:
        """
        Calcula el total de ingresos y egresos.

        Returns:
            Dict[str, float]: Diccionario con total de 'ingresos' y 'egresos'.
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
        