import machine
import time
import dht


pino_com_rele = 5
rele = machine.Pin(pino_com_rele, machine.Pin.OUT)

def ligar_rele():
    rele.value(1)
    print("Relé ligado")

def desligar_rele():
    rele.value(0)
    print("Relé desligado")