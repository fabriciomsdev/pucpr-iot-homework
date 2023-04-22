"""
    PUCPR IOT
    Aluno: Fabricio Magalhaes
    Etapa 4: 
    Requisitos:
        PT-1: Aprendendo a usar o network
            - Instalar o driver do ESP32
            - Intalar o Micropython no ESP32
            - Instalar o THONY IDE
            - Chamar o network e conectar na rede wifi utilizando o modulo network            
            - testar conexao a internet
            - separar o codigo para que fique limpo e organizado
        PT-2:
            consta na pasta ./app ele vai ser meu projeto final =)
"""
import time

minha_senha_de_wifi = "12345678"
nome_do_wifi = "Fabricio-AP617"

def conectar_ao_wifi(rede, senha):
    import network

    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.scan()

    for tentativa in range(100):
        print("Tentativa de conexão: ", tentativa)
        station.connect(nome_do_wifi, minha_senha_de_wifi)

        if station.isconnected():
            print("Conectado com sucesso!")
            print(station.ifconfig())
            break
        time.sleep(2)
    
    return station

def testar_se_tem_internet():
    import socket
    try:
        socket.getaddrinfo("google.com", 80)
        print("Conectado na internet")
    except OSError:
        print("Sem conexão com a internet")
        
def exibir_temperatura_da_cidade():
    import urequests

    url_com_dados_do_clima = "http://api.openweathermap.org/data/2.5/weather?q=Curitiba&appid=4f4b3b0b0b0b0b0b0b0b0b0b0b0b0b0b"

    response = urequests.get(url_com_dados_do_clima)

    print(response.text)
    


def main():
    conexao_a_internet = conectar_ao_wifi(nome_do_wifi, minha_senha_de_wifi)

    if conexao_a_internet.isconnected():
        testar_se_tem_internet()
        exibir_temperatura_da_cidade()
    else:
        print("Sem conexão com a internet")
        
    conexao_a_internet.disconnect()
    
main()