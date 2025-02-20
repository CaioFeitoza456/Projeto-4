# O usuáruo deve poder converter
# unidades de medida, como quilômetros 
# para metro, Celsius para Fahrenheit, 
# etc.

"""
As conversões serão:

~~ Distância ~~
Metro para centímetro
Metro para quilômetro
Metro para milímetro
Centímetro para metro
Centímetro para milímetro
Centímetro para quilômetro
Quilômetro para metro
Quilômetro para centímetro
Quilômetro para milímetro
Milímetro para metro
Milímetro para centímetro
Milímetro para quilômetro


~~ Temperatura ~~
Celsius para Fahrenheit
Celsius para Kelvin
Fahrenheit para Kelvin
Fahrenheit para Celsius
Kelvin para Fahrenheit
Kelvin para Celsius
"""


from conversor_temperaturas import *
from conversor_medidas import *
from time import sleep


def tenta_mudar_para_float(valor):
    try:
        # Tenta transformar o valor passado
        # como argumento em um número
        # de ponto flutuante
        return float(valor)
       
    except ValueError:
        # Se der erro de valor(o usuário passar
        # um texto, por exemplo) ele cai aqui
        # na exceção
        return None


while True:
    print("""
    
~~~ Conversor de medidas ~~~
    
Escolha o que deseja fazer:
    
1. Converter distâncias
2. Converter temperaturas
3. Sair
    """)
    
    # Leitura da forma de conversão
    opcao_conversor = input("Digite aqui: ")

    # 3 -> Sair
    if opcao_conversor == "3":
        break
    
    
    # 1 -> Conversor de distâncias
    elif opcao_conversor == "1":
        print("""
Qual a medida que você tem ?

1 - Metro
2 - Centímetro
3 - Quilômetro
4 - Milímetro
            """)
        
        # Leitura da opção de medida inicial
        opcao = input("Digite aqui: ").upper()
        
        while True:
            # Leitura da medida em números
            medida = input("Digite a medida em número: ")
            
            # Chame a função que tenta trocar o tipo
            # de dado para float
            medida = tenta_mudar_para_float(medida)
            
            # Se a mudança NÃO ocorrer, venha aqui
            if medida is None:
                print("Por favor, digite apenas números.")
                continue
            
            break
            
        
        if opcao == "1":
            # METRO
            
            while True:
                print("""
Para qual medida você quer converter ?

1 - Centímetro
2 - Quilômetro
3 - Milímetro
                """)
                
                # Leitura da opção de conversão da medida
                converta_para = input("Digite aqui: ").upper()
                
                if converta_para == "1":
                    # DE METRO PARA CENTÍMETRO
                    
                    # Chame a função que converte de metro para centímetro
                    # e armazene o retorno na variável nova_medida
                    nova_medida = metro_para_centimetro(medida)
                    
                    # Imprima o resultado da nova_medida e volte do início
                    print(f"{medida}m em centímetros fica {nova_medida}cm")
                    
                    # Espere 5 segundos antes de terminar
                    sleep(5)
                    break
                
                
                elif converta_para == "2":
                    # DE METRO PARA QUILÔMETRO
                    
                    # Chame a função que converte de metro para quilômetro
                    # e armazene o retorno na variável nova_medida
                    nova_medida = metro_para_quilometro(medida)
                    
                    # Imprima o resultado da nova_medida e volte do início
                    print(f"{medida}m em quilômetro fica {nova_medida}km")
                    
                    # Espere 5 segundos antes de terminar
                    sleep(5)
                    break
                
                
                elif converta_para == "3":
                    # DE METRO PARA MILÍMETRO
                    
                    # Chame a função que converte de metro para milímetro
                    # e armazene o retorno na variável nova_medida
                    nova_medida = metro_para_milimetro(medida)
                    
                    # Imprima o resultado da nova_medida e volte do início
                    print(f"{medida}m em milímetros fica {nova_medida}mm")
                    
                    # Espere 5 segundos antes de terminar
                    sleep(5)
                    break
                
                # Caso o usuário não digite uma opção do menu
                # ele vem pra cá
                print("Digite uma opção válida.")
                sleep(1.5)  
        
        
        elif opcao == "2":
            # CENTÍMETRO
            while True:
                print("""
Para qual temperatura você quer converter ?

1 - Metro
2 - Quilômetro
3 - Milímetro
                """)
                
                # Leitura da opção de conversão da temperatura
                converta_para = input("Digite aqui: ").upper()
                
                if converta_para == "1":
                    # DE CENTÍMETRO PARA METRO
                    
                    # Chame a função que converte de centímetro para metro
                    # e armazene o retorno na variável nova_medida
                    nova_medida = centimetros_para_metro(medida)
                    
                    # Imprima o resultado da nova_medida e volte do início
                    print(f"{medida}cm em metros fica {nova_medida}m")
                    
                    # Espere 5 segundos antes de terminar
                    sleep(5)
                    break
                
                
                elif converta_para == "2":
                    # DE CENTÍMETRO PARA QUILÔMETRO
                    
                    # Chame a função que converte de centímetro para quilômetro
                    # e armazene o retorno na variável nova_medida
                    nova_medida = centimetros_para_quilometro(medida)
                    
                    # Imprima o resultado da nova_medida e volte do início
                    print(f"{medida}cm em quilômetro fica {nova_medida}km")
                    
                    # Espere 5 segundos antes de terminar
                    sleep(5)
                    break
                
                
                elif converta_para == "3":
                    # DE CENTÍMETRO PARA MILÍMETRO
                    
                    # Chame a função que converte de centímetro para milímetro
                    # e armazene o retorno na variável nova_medida
                    nova_medida = centimetros_para_milimetro(medida)
                    
                    # Imprima o resultado da nova_medida e volte do início
                    print(f"{medida}cm em milímetros fica {nova_medida}mm")
                    
                    # Espere 5 segundos antes de terminar
                    sleep(5)
                    break
                
                # Caso o usuário não digite uma opção do menu
                # ele vem pra cá
                print("Digite uma opção válida.")
                sleep(1.5)
        
        
        elif opcao == "3":
            # QUILÔMETRO
            
            while True:
                print("""
Para qual temperatura você quer converter ?

1 - Metro
2 - Centímetro
3 - Milímetro
                """)
                
                # Leitura da opção de conversão da temperatura
                converta_para = input("Digite aqui: ").upper()
                
                if converta_para == "1":
                    # DE QUILÔMETRO PARA METRO
                    
                    # Chame a função que converte de quilômetro para metro
                    # e armazene o retorno na variável nova_medida
                    nova_medida = quilometro_para_metro(medida)
                    
                    # Imprima o resultado da nova_medida e volte do início
                    print(f"{medida}km em metros fica {nova_medida}m")
                    
                    # Espere 5 segundos antes de terminar
                    sleep(5)
                    break
                
                
                elif converta_para == "2":
                    # DE QUILÔMETRO PARA CENTÍMETRO
                    
                    # Chame a função que converte de quilômetro para quilômetro
                    # e armazene o retorno na variável nova_medida
                    nova_medida = quilometro_para_centimetro(medida)
                    
                    # Imprima o resultado da nova_medida e volte do início
                    print(f"{medida}km em centímetro fica {nova_medida}cm")
                    
                    # Espere 5 segundos antes de terminar
                    sleep(5)
                    break
                
                
                elif converta_para == "3":
                    # DE QUILÔMETRO PARA MILÍMETRO
                    
                    # Chame a função que converte de quilômetro para milímetro
                    # e armazene o retorno na variável nova_medida
                    nova_medida = quilometro_para_milimetro(medida)
                    
                    # Imprima o resultado da nova_medida e volte do início
                    print(f"{medida}km em milímetros fica {nova_medida}mm")
                    
                    # Espere 5 segundos antes de terminar
                    sleep(5)
                    break
                
                # Caso o usuário não digite uma opção do menu
                # ele vem pra cá
                print("Digite uma opção válida.")
                sleep(1.5)
        
        
        elif opcao == "4":
            # MILÍMETRO
            
            while True:
                print("""
Para qual temperatura você quer converter ?

1 - Metro
2 - Centímetro
3 - Quilômetro
                """)
                
                # Leitura da opção de conversão da temperatura
                converta_para = input("Digite aqui: ").upper()
                
                if converta_para == "1":
                    # DE MILÍMETRO PARA METRO
                    
                    # Chame a função que converte de milímetro para metro
                    # e armazene o retorno na variável nova_medida
                    nova_medida = milimetro_para_metro(medida)
                    
                    # Imprima o resultado da nova_medida e volte do início
                    print(f"{medida}mm em metros fica {nova_medida}m")
                    
                    # Espere 5 segundos antes de terminar
                    sleep(5)
                    break
                
                
                elif converta_para == "2":
                    # DE MILÍMETRO PARA CENTÍMETRO
                    
                    # Chame a função que converte de milímetro para centímetro
                    # e armazene o retorno na variável nova_medida
                    nova_medida = milimetro_para_centimetro(medida)
                    
                    # Imprima o resultado da nova_medida e volte do início
                    print(f"{medida}mm em centímetro fica {nova_medida}cm")
                    
                    # Espere 5 segundos antes de terminar
                    sleep(5)
                    break
                
                
                elif converta_para == "3":
                    # DE MILÍMETRO PARA QUILÔMETRO
                    
                    # Chame a função que converte de milímetro para quilômetro
                    # e armazene o retorno na variável nova_medida
                    nova_medida = milimetro_para_quilometro(medida)
                    
                    # Imprima o resultado da nova_medida e volte do início
                    print(f"{medida}mm em quilômetro fica {nova_medida}km")
                    
                    # Espere 5 segundos antes de terminar
                    sleep(5)
                    break
                
                # Caso o usuário não digite uma opção do menu
                # ele vem pra cá
                print("Digite uma opção válida.")
                sleep(1.5)
        
        
        else:
            print("Digite uma opção válida.")
    
    
    # 2 -> Conversor de temperaturas
    elif opcao_conversor == "2":
        
        print("""
Qual temperatura você tem ?
        
C - Celsius
F - Fahrenheit
K - Kelvin
        """)
        
        # Leitura da opção de temperatura que o 
        # usuário tem(°C, °F, K)
        opcao = input("Digite aqui: ").upper()
        
        while True:
            # Leitura da temperatura em número(em str)
            temperatura = input("Digite a temperatura: ")
            
            
            # Tente trocar o tipo de dado da temperatura de
            # str para float, e para isso use a função chamada
            temperatura = tenta_mudar_para_float(temperatura)
            
            
            # Caso a alteração NÃO OCORRA entre aqui
            if temperatura is None:
                
                # Imprima o tratamento de erro e volte
                # do início
                print("Por favor, digite apenas números.")
                continue
            
            break
            
        
        # Se o usuário tiver uma temperatura em 
        # Celsius, ele entra aqui
        if opcao == "C" or opcao == "CELSIUS":
        
            # Se o usuário tem uma temperatura em Celsius,
            # ele quer tansformar ou para Fahrenheit ou
            # para Kelvin, por isso só há essas duas opções
        
            while True:
                print("""
Para qual temperatura você quer converter ?

F - Fahrenheit
K - Kelvin
                """)
                
                # Leitura da opção de conversão da temperatura
                converta_para = input("Digite aqui: ").upper()
                
                # Se for F ou Fahrenheit entre aqui
                if converta_para == "F" or converta_para == "FAHRENHEIT":
                    
                    # Chame a função que converte de Celsius para Fahrenheit
                    # e armazene o retorno na variável nova_temperatura
                    nova_temperatura = celsius_para_fahrenheit(temperatura)
                    
                    # Imprima o resultado da nova_temperatura e volte do início
                    print(f"{temperatura}°C em Fahrenheit fica: {nova_temperatura}°F")
                    
                    # Espere 5 segundos antes de terminar
                    sleep(5)
                    break
                
                # Se for K ou Kelvin entre aqui
                elif converta_para == "K" or converta_para == "KELVIN":
                    
                    # Chame a função que converte de Celsius para Kelvin
                    # e armazene o retorno na variável nova_temperatura
                    nova_temperatura = celsius_para_kelvin(temperatura)
                    
                    # Imprima o resultado da nova_temperatura e volte do início
                    print(f"{temperatura}°C em Kelvin fica: {nova_temperatura}K")
                    
                    # Espere 5 segundos antes de terminar
                    sleep(5)
                    break
                
                
                # Caso o usuário não digite nem F nem K,
                # entre aqui
                else:
                    print("Digite uma opção válida.")
                    
                    # Espere 2 segundos
                    sleep(2)
                    continue
        
        
        # Se o usuário tiver uma temperatura em 
        # Fahrenheit, ele entra aqui
        elif opcao == "F" or opcao == "FAHRENHEIT":
            
            while True:
                print("""
Para qual temperatura você quer converter ?

C - Celsius
K - Kelvin
                """)
                
                # Leitura da opção de conversão da temperatura
                converta_para = input("Digite aqui: ").upper()
                
                if converta_para == "C" or converta_para == "Celsius":
                    
                    # Chame a função que converte de Fahrenheit para Celsius
                    # e armazene o retorno na variável nova_temperatura
                    nova_temperatura = fahrenheit_para_celsius(temperatura)
                    print(f"{temperatura}°F em Celsius fica: {nova_temperatura}°C")
                    
                    # Espere 5 segundos antes de terminar
                    sleep(5)
                    break
                
                
                elif converta_para == "K" or converta_para == "Kelvin":
                    
                    # Chame a função que converte de Fahrenheit para Kelvin
                    # e armazene o retorno na variável nova_temperatura
                    nova_temperatura = fahrenheit_para_kelvin(temperatura)
                    print(f"{temperatura}°F em Kelvin fica: {nova_temperatura}K")
                    
                    # Espere 5 segundos antes de terminar
                    sleep(5)
                    break
                
                else:
                    print("Digite uma opção válida.")
                    
                    # Espere 2 segundos
                    sleep(2)
                    continue
        
        
        
        # Se o usuário tiver uma temperatura em 
        # Kelvin, ele entra aqui
        elif opcao == "K" or opcao == "KELVIN":
            
            while True:
                print("""
Para qual temperatura você quer converter ?

C - Celsius
F - Fahrenheit
                """)
                
                # Leitura da opção de conversão da temperatura
                converta_para = input("Digite aqui: ").upper()
                
                if converta_para == "C" or converta_para == "CELSIUS":
                    
                    # Chame a função que converte de Kelvin para Celsius
                    # e armazene o retorno na variável nova_temperatura
                    nova_temperatura = kelvin_para_celsius(temperatura)
                    print(f"{temperatura}K em Celsius fica: {nova_temperatura}°C")
                    
                    # Espere 5 segundos antes de terminar
                    sleep(5)
                    break
                
                elif converta_para == "F" or converta_para == "FAHRENHEIT":
                    
                    # Chame a função que converte de Kelvin para Fahrenheit
                    # e armazene o retorno na variável nova_temperatura
                    nova_temperatura = kelvin_para_fahrenheit(temperatura)
                    print(f"{temperatura}K em Fahrenheit fica: {nova_temperatura}°F")
                    
                    # Espere 5 segundos antes de terminar
                    sleep(5)
                    break
                
                else:
                    print("Digite uma opção válida.")
                    
                    # Espere 2 segundos
                    sleep(2)
                    continue
                    
        else:
            print("Digite uma opção válida.")
            
    else:
        print("Digite a opção apenas em números.")
