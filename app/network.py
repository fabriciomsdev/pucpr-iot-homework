def conectar_ao_wifi(rede, senha):
    import network
    import time 

    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.scan()

    for tentativa in range(100):
        print("Tentativa de conexão: ", tentativa)
        station.connect(rede, senha)

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