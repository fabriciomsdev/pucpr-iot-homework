def registrar_temperatura_e_umidade(temperatura, umidade):
    import urequests
    url = 'https://api.thingspeak.com/update?api_key=8WPHREERYGG54J14'
    param = f'&field1={temperatura}&field2={umidade}'

    r = urequests.get(url + param)