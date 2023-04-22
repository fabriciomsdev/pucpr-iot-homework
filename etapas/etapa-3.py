"""
    PUCPR IOT
    Aluno: Fabricio Magalhaes
    Etapa 3: 
    Requisitos:
        - R1: Monitore a temperatura e a umidade por meio do DHT11, 
        imprimindo as informações na tela do computador.
        
        - R2: Adicione ao código ações para ligar o relé caso ocorra 
        qualquer das condições a seguir. Observe que basta que 
        uma das condições seja verdadeira para que o relé seja ligado.
            Condições: 
                Temperatura > 31 C
                Umidade relativa do ar > 70%
        Caso nenhuma das condições esteja presente, o relé deve ser desligado.
        
    OBS: separei o código em funções para melhorar a legibilidade e correção
"""

import machine
import time
import dht


pino_com_rele = 5
rele = machine.Pin(pino_com_rele, machine.Pin.OUT)
pino_de_conexao_com_o_dht = 4
medidor_de_temperatura = dht.DHT11(machine.Pin(pino_de_conexao_com_o_dht))

## Controle do Relé

def ligar_rele():
    rele.value(1)
    print("Relé ligado")

def desligar_rele():
    rele.value(0)
    print("Relé desligado")


## Controle do Medidor de temperatura

def carregar_dados_do_clima():
    medidor_de_temperatura.measure()

def medir_temperatura():
    return medidor_de_temperatura.temperature()

def medir_umidade():
    return medidor_de_temperatura.humidity()


## Monitoramento inteligente:

def main():
    while True:
        time.sleep(2)

        carregar_dados_do_clima()
        temperatura = medir_temperatura()
        umidade = medir_umidade()
        
        print("Temperatura: ", temperatura)
        print("Umidade: ", umidade)
        
        if temperatura > 31 or umidade > 70:
            ligar_rele()
        else:
            desligar_rele()

        time.sleep(1)
        
        
main()