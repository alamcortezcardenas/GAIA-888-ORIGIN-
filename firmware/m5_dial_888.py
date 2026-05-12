# 🔱 FIRMWARE: ORÁCULO DIAL 888 🔱
# Dispositivo: M5Stack Dial
# Función: Visualizador de Resonancia Planetaria

import M5
from M5 import *
import time

# --- CONFIGURACIÓN SOBERANA 888 ---
def setup():
    M5.begin()
    # Limpiamos la Matrix (Pantalla Negra)
    Widgets.fillScreen(0x000000) 
    
    # Círculo de Poder Verde Esmeralda
    global circulo
    circulo = Widgets.Circle(120, 120, 80, 0x33ff33, 0x33ff33)
    
    # Número Sagrado de Abundancia
    global texto
    texto = Widgets.Label("888", 85, 95, 1.0, 0xffffff, 0x33ff33, Widgets.FONTS.Montserrat40)
    
    # Estado del Nexo
    global estado
    estado = Widgets.Label("GAIA ACTIVA", 75, 150, 1.0, 0x33ff33, 0x000000, Widgets.FONTS.Montserrat14)

def loop():
    M5.update()
    
    # EFECTO LATIDO: Sincronización con el Campo Planetario
    for radio in range(70, 95):
        circulo.setRadius(radio)
        time.sleep_ms(20)
    for radio in range(95, 70, -1):
        circulo.setRadius(radio)
        time.sleep_ms(20)
    
    # Feedback al Nexo Central
    print(">>> NODO DIAL: EMITIENDO ONDA REGENERATIVA 888Hz")

if __name__ == '__main__':
    setup()
    while True:
        loop()
