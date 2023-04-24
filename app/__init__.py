"""
    PUCPR IOT
    Aluno: Fabricio Magalhaes
    Etapa 4:
        Requisitos:
            - R1: Monitore umidade e temperatura
            - R2: Envie para um servidor thinkspead
"""

from app.medidor import carregar_dados_do_clima, medir_temperatura, medir_umidade
from app.network import conectar_ao_wifi, testar_se_tem_internet
from app.server import registrar_temperatura_e_umidade
from app.rele import ligar_rele, desligar_rele

minha_senha_de_wifi = "wifi01231"
nome_do_wifi = "fasd2-22444"

def main():
    conexao_a_internet = conectar_ao_wifi(nome_do_wifi, minha_senha_de_wifi)

    while True:
        if conexao_a_internet.isconnected():
            testar_se_tem_internet()
            
            ## R1: Monitore umidade e temperatura
            carregar_dados_do_clima()
            temperatura = medir_temperatura()
            umidade = medir_umidade()
            
            print("Temperatura: ", temperatura)
            print("Umidade: ", umidade)

            registrar_temperatura_e_umidade(temperatura, umidade)
            
            if temperatura > 31 or umidade > 70:
                ligar_rele()
            else:
                desligar_rele()     
        else:
            print("Sem conexão com a internet")
            
        conexao_a_internet.disconnect()
    
main()