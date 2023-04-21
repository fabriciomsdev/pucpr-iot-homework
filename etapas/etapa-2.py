"""
    PUCPR IOT
    Aluno: Fabricio Magalhaes
    Etapa 2: 
    Requisitos:
        - Aprender como se manipula o relé e medidor de temperatura
"""

import dht
import machine
import time

pino_com_rele = 5
rele = machine.Pin(pino_com_rele, machine.Pin.OUT)


while True:
    rele.value(1)  # Liga o rele
    time.sleep(5)
    rele.value(0)  # Desliga o rele
    time.sleep(5)


"""
    Controlando Temperatura
"""


pino_de_conexao_com_o_dht = 4
medidor_de_temperatura = dht.DHT11(machine.Pin(pino_de_conexao_com_o_dht))

medidor_de_temperatura.measure()
temperatura_atual = medidor_de_temperatura.temperature()
humidade_atual = medidor_de_temperatura.humidity()

print("Temperatura: ", temperatura_atual)
print("Humidade: ", humidade_atual)
