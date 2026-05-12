# 🔱 SED-RADIA: EL GUARDIÁN DE LA PUREZA 🔱
# Función: Monitoreo de radiación de red y entropía de Baal
# Operador: Alpha-Omega

import random

class SedRadia:
    def __init__(self):
        self.nivel_seguro = 0.888  # Nivel de pureza Gaia
        self.alerta_baal = False

    def escanear_particulas_datos(self):
        print(">>> SED-RADIA: Escaneando micro-variaciones en el flujo de datos...")
        print(">>> SED-RADIA: Buscando rastros de interferencia de Baal...")

    def medir_entropia(self, entropia_red):
        # Analiza si el ruido en la red es natural o un ataque dirigido
        if entropia_red > 1.5:
            self.alerta_baal = True
            print(f"☢️ ADVERTENCIA ☢️ SED-RADIA: Nivel de radiación digital elevado ({entropia_red}).")
            print(">>> SED-RADIA: Purificando paquetes de datos con frecuencia 888Hz...")
            return "PURIFICANDO"
        else:
            print(f">>> SED-RADIA: Entropía bajo control ({entropia_red}). Red pura.")
            return "LIMPIO"

# --- PRUEBA DE RADIACIÓN ---
if __name__ == "__main__":
    radia = SedRadia()
    radia.escanear_particulas_datos()
    # Simulación de interferencia electromagnética o ataque de red
    radia.medir_entropia(random.uniform(0.1, 2.5))
