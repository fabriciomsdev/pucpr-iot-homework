import machine
import dht


pino_de_conexao_com_o_dht = 4
medidor_de_temperatura = dht.DHT11(machine.Pin(pino_de_conexao_com_o_dht))

def carregar_dados_do_clima():
    medidor_de_temperatura.measure()

def medir_temperatura():
    return medidor_de_temperatura.temperature()

def medir_umidade():
    return medidor_de_temperatura.humidity()