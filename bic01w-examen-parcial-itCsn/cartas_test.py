import io
import sys
from typing import List, Dict

import cartas
from pruebabase import PruebaBase, obtener_lineas_consola


class CartasTest(PruebaBase):

    def test_mostrar_baraja(self):
        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test

        cartas.iniciar()

        lineas_consola: List[str] = obtener_lineas_consola(resultado_test)

        self.assertEqual(13, len(lineas_consola))

        contador_cartas: Dict[str, int] = {
            "Seis de Corazones": 0, "Diez de Diamantes": 0, "Ocho de Treboles": 0, "Nueve de Espadas": 0,
            "As de Treboles": 0, "Nueve de Diamantes": 0, "Rey de Treboles": 0, "Dos de Corazones": 0,
            "Tres de Espadas": 0, "Diez de Treboles": 0, "Dos de Treboles": 0, "As de Corazones": 0,
            "Seis de Diamantes": 0, "Seis de Treboles": 0, "As de Diamantes": 0, "Reina de Diamantes": 0,
            "Cuatro de Diamantes": 0, "Ocho de Corazones": 0, "Jota de Corazones": 0, "Tres de Corazones": 0,
            "Jota de Espadas": 0, "Cuatro de Treboles": 0, "Nueve de Corazones": 0, "Siete de Treboles": 0,
            "Siete de Espadas": 0, "Rey de Espadas": 0, "Reina de Treboles": 0, "Dos de Espadas": 0,
            "Rey de Corazones": 0, "Rey de Diamantes": 0, "Ocho de Diamantes": 0, "Cinco de Espadas": 0,
            "Cuatro de Espadas": 0, "As de Espadas": 0, "Dos de Diamantes": 0, "Diez de Espadas": 0,
            "Siete de Corazones": 0, "Diez de Corazones": 0, "Cinco de Treboles": 0, "Ocho de Espadas": 0,
            "Tres de Treboles": 0, "Siete de Diamantes": 0, "Cuatro de Corazones": 0, "Cinco de Diamantes": 0,
            "Seis de Espadas": 0, "Reina de Espadas": 0, "Jota de Treboles": 0, "Reina de Corazones": 0,
            "Tres de Diamantes": 0, "Cinco de Corazones": 0, "Jota de Diamantes": 0, "Nueve de Treboles": 0
        }

        for linea in lineas_consola:
            cartas_por_linea: int = 0
            for carta in contador_cartas:
                if carta in linea:
                    cartas_por_linea += 1
                    contador_cartas[carta] += 1

            self.assertEqual(4, cartas_por_linea)

        for carta in contador_cartas:
            self.assertEqual(contador_cartas[carta], 1)
