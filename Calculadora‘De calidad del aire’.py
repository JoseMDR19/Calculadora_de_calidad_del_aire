
print("*************************************************************\n")
print("*                    MENU DE OPCIONES                       *\n")
print("*************************************************************\n")
print("*             1. Calidad de aire en exteriores              *\n")
print("*             2. Calidad de aire en interiores              *\n")
print("*************************************************************")
print("*                        SIGLAS                             *")
print("* ICAp = Indice de calidad del Aire para el contaminante p  *")
print("* Cp = Concentración medida para el contaminante p          *")
print("* PCalto = Punto de corte mayor o igual a Cp                *")
print("* PCbajo = Punto de corte menor o igual a Cp                *")
print("* Ialto = Valor del ICA correspondiente al PCalto           *")
print("* Ibajo = Valor del ICA correspondiente al PCbajo           *")
print("*************************************************************")
print("Este programa esta ligado a la resolución No.2254 de")
print("   noviembre del 2017 en la republica de Colombia\n")
opción=int(input("Digite una opción del menú: "))
if opción == 1 or opción == 2:
    dias = int(input("Digite el numero de dias que tiene el mes a monitorear: "))
    if opción == 1:
        print("Calidad de aire en EXTERIORES")
        dias_totales = 0
        RPM10 = 0
        RCO = 0
        ROZONO = 0
        RNO2 = 0
        RSO2 = 0
        print("PM10: partículas en suspensión atmosférica con diámetro igual o inferior a 10um")
        print("CO: monóxido de carbono")
        print("OZONO: gas incoloro")
        print("NO2: dióxido de nitrógeno")
        print("SO2: dióxido de azufre")
        for dias_totales in range(dias):
            PM10 = float(input("Ingrese medida de PM10: "))
            CO  = float(input("Ingrese medida de CO: "))
            OZONO = float(input("Ingrese medida de OZONO: "))
            NO2 = float(input("Ingrese medida de NO2: "))
            SO2 = float(input("Ingrese medida de SO2: "))

            if PM10 >= 0 and PM10 <= 50:
                RPM10=PM10*0.5-0
                print("El valor de ICA del PM10 es: \n",RPM10)
                print("La calidad de aire es BUENA")
                print("Color: verde")
                print("Categoría: Buena\n")
            if PM10 >= 51 and PM10 <= 75:
                RPM10=PM10*1-25
                print("El valor de ICA del PM10 es: ",RPM10)
                print("La calidad de aire es ACEPTABLE")
                print("Color: amarillo")
                print("Categoría: aceptable\n")
            if PM10 >= 76 and PM10 <= 100:
                RPM10=PM10*2-100
                print("El valor de ICA del PM10 es: ",RPM10)
                print("La calidad de aire es LEVEMENTE DAÑINA")
                print("Color: naranja")
                print("Categoría: dañina a la salud de los grupos sensibles\n")
            if PM10 >= 101 and PM10 <= 150:
                RPM10=PM10*2-100
                print("El valor de ICA del PM10 es: ",RPM10)
                print("La calidad de aire es DAÑINA")
                print("Color: rojo")
                print("Categoría: dañina a la salud\n")
            if PM10 >= 151 and PM10 <= 225:
                RPM10=PM10*1.3-0
                print("El valor de ICA del PM10 es: ",RPM10)
                print("La calidad de aire es MUY DAÑINA")
                print("Color: púrpura")
                print("Categoría: muy dañina a la salud\n")
            if PM10 >= 226 and PM10 <= 340:
                RPM10=PM10*0.9+104
                print("El valor de ICA del PM10 es: ",RPM10)
                print("La calidad de aire es MORTAL ")
                print("Color: marrón")
                print("Categoría: peligrosa\n")


            if CO >= 0 and CO <= 4.5:
                RCO=CO*5.6-0
                print("El valor de ICA del CO es: \n",RCO)
                print("La calidad de aire es BUENA")
                print("Color: verde")
                print("Categoría: Buena\n")
            if CO >= 4.6 and CO <= 7:
                RCO=CO*10-20
                print("El valor de ICA del CO es: ",RCO)
                print("La calidad de aire es ACEPTABLE")
                print("Color: amarillo")
                print("Categoría: aceptable\n")
            if CO >= 8 and CO <= 10:
                RCO=CO*16.7-67
                print("El valor de ICA del CO es: ",RCO)
                print("La calidad de aire es LEVEMENTE DAÑINA")
                print("Color: naranja")
                print("Categoría: dañina a la salud de los grupos sensibles\n")
            if CO >= 11 and CO <= 15:
                RCO=CO*20-100
                print("El valor de ICA del CO es: ",RCO)
                print("La calidad de aire es DAÑINA")
                print("Color: rojo")
                print("Categoría: dañina a la salud\n")
            if CO >= 16 and CO <= 22:
                RCO=CO*14.3-14
                print("El valor de ICA del CO es: ",RCO)
                print("La calidad de aire es MUY DAÑINA")
                print("Color: púrpura")
                print("Categoría: muy dañina a la salud\n")
            if CO >= 23 and CO <= 33:
                RCO=CO*9.1+100
                print("El valor de ICA del CO es: ",RCO)
                print("La calidad de aire es MORTAL ")
                print("Color: marrón")
                print("Categoría: peligrosa\n")


            if OZONO >= 0 and OZONO <= 80:
                ROZONO=OZONO*0.3-0
                print("El valor de ICA del O3 es: \n",ROZONO)
                print("La calidad de aire es BUENA ")
                print("Color: verde")
                print("Categoría: Buena\n")
            if OZONO >= 81 and OZONO <= 100 :
                ROZONO=OZONO*1.3-75
                print("El valor de ICA del O3 es: ",ROZONO)
                print("La calidad de aire es ACEPTABLE ")
                print("Color: amarillo")
                print("Categoría: aceptable\n")
            if OZONO >= 101 and OZONO <= 160:
                ROZONO=OZONO*0.8-33
                print("El valor de ICA del O3 es: ",ROZONO)
                print("La calidad de aire es LEVEMENTE DAÑINA ")
                print("Color: naranja")
                print("Categoría: dañina a la salud de los grupos sensibles\n")
            if OZONO >= 161 and OZONO <= 240:
                ROZONO=OZONO*1.3-100
                print("El valor de ICA del O3 es: ",ROZONO)
                print("La calidad de aire es DAÑINA ")
                print("Color: rojo")
                print("Categoría: dañina a la salud\n")
            if OZONO >= 241 and OZONO <= 360:
                ROZONO=OZONO*0.8-0
                print("El valor de ICA del O3 es: ",ROZONO)
                print("La calidad de aire es MUY DAÑINA ")
                print("Color: púrpura")
                print("Categoría: muy dañina a la salud\n")
            if OZONO >= 361 and OZONO <= 540:
                ROZONO=OZONO*0.6+100
                print("El valor de ICA del O3 es: ",ROZONO)
                print("La calidad de aire es MORTAL ")
                print("Color: marrón")
                print("Categoría: peligrosa\n")


            if NO2 >= 0 and NO2 <= 40:
                RNO2=NO2*0.6-0
                print("El valor de ICA del NO2 es: \n",RNO2)
                print("La calidad de aire es BUENA ")
                print("Color: verde")
                print("Categoría: Buena\n")
            if NO2 >= 41 and NO2 <= 75:
                RNO2=NO2*0.7-4
                print("El valor de ICA del NO2 es: ",RNO2)
                print("La calidad de aire es ACEPTABLE ")
                print("Color: amarillo")
                print("Categoría: aceptable\n")
            if NO2 >= 76 and NO2 <= 200:
                RNO2=NO2*0.4+20
                print("El valor de ICA del NO2 es: ",RNO2)
                print("La calidad de aire es LEVEMENTE DAÑINA")
                print("Color: naranja")
                print("Categoría: dañina a la salud de los grupos sensibles\n")
            if NO2 >= 201 and NO2 <= 500:
                RNO2=NO2*0.3+33
                print("El valor de ICA del NO2 es: ",RNO2)
                print("La calidad de aire es DAÑINA ")
                print("Color: rojo")
                print("Categoría: dañina a la salud\n")
            if NO2 >= 501 and NO2 <= 1130:
                RNO2=NO2*0.2+121
                print("El valor de ICA del NO2 es: ",RNO2)
                print("La calidad de aire es MUY DAÑINA ")
                print("Color: púrpura")
                print("Categoría: muy dañina a la salud\n")
            if NO2 >= 1131 and NO2 <= 2260:
                RNO2=NO2*0.1-200
                print("El valor de ICA del NO2 es: ",RNO2)
                print("La calidad de aire es MORTAL ")
                print("Color: marrón")
                print("Categoría: peligrosa\n")


            if SO2 >= 0 and SO2 <= 20:
                RSO2=SO2*1.3+0
                print("El valor de ICA del SO2 es: \n",RSO2)
                print("La calidad de aire es BUENA ")
                print("Color: verde")
                print("Categoría: buena\n")
            if SO2 >= 21 and SO2 <= 50:
                RSO2=SO2*0.8+8
                print("El valor de ICA del SO2 es: ",RSO2)
                print("La calidad de aire es ACEPTABLE ")
                print("Color: amarillo")
                print("Categoría: aceptable\n")
            if SO2 >= 51 and SO2 <= 125:
                RSO2=SO2*0.7+17
                print("El valor de ICA del SO2 es: ",RSO2)
                print("La calidad de aire es LEVEMENTE DAÑINA ")
                print("Color: naranja")
                print("Categoría: dañina a la salud de los grupos sensibles\n")
            if SO2 >= 126 and SO2 <= 365:
                RSO2=SO2*0.4+48
                print("El valor de ICA del SO2 es: ",RSO2)
                print("La calidad de aire es DAÑINA ")
                print("Color: rojo")
                print("Categoría: dañina a la salud\n")
            if SO2 >= 366 and SO2 <= 550:
                RSO2=SO2*0.5+3
                print("El valor de ICA del SO2 es: ",RSO2)
                print("La calidad de aire es MUY DAÑINA ")
                print("Color: púrpura")
                print("Categoría: muy dañina a la salud\n")
            if SO2 >= 551 and SO2 <= 825:
                RSO2=SO2*0.4+100
                print("El valor de ICA del SO2 es: ",RSO2)
                print("La calidad de aire es MORTAL ")
                print("Color: marrón")
                print("Categoría: peligrosa\n")


    if opción == 2:
        print("Calidad de aire en INTERIORES\n")
        print("*              SIGLAS                      *")
        print("* CO2 = Dioxido de Carbono                 *")
        print("* PM 10 = Partículas < 10 um de diámetro   *")
        print("* PM 2.5 = Partículas < 2.5 um de diámetro *")
        print("* COVs = Compuestos Orgánicos Volátiles    *")
        print("********************************************")
        dias_totales = 0
        RPM10 = 0
        RCO = 0
        ROZONO = 0
        RNO2 = 0
        RSO2 = 0
        for dias_totales in range(dias):
            PM10 = float(input("Ingrese medida de PM10 en ug/m^3: "))
            PM25 = float(input("Ingrese medida de PM 2.5 en ug/m^3: "))
            CO2  = float(input("Ingrese medida de CO2 en ppm: "))
            COVs = float(input("Ingrese medida de COVs en mg/m^3: "))
            Temp = float(input("Ingrese medida de Temperatura en °C: "))
            Hume = float(input("Ingrese medida de Humedad en %: "))

            if PM10 <= 150:
                print ("PM10: RANGO IDEAL")
                print ("(exposición durante 24h)\n")
            if PM10 > 150:
                print ("PM10 riesgo de exposición")
                print ("PELIGROSO")
                print ("*      Efectos secundarios:    *\n")
                print (" Enfermedades respiratorias y cardiovasculares, asma  ")
                print (" e infecciones respiratorias            \n")
            if PM25 <= 35:
                print ("PM 2.5: RANGO IDEAL")
                print ("(exposición durante 24h)\n")
            if PM25 > 35:
                print ("PM 2.5 riesgo de exposición")
                print ("PELIGROSO")
                print ("*      Efectos secundarios:    *\n")
                print (" Debido a su tamaño, atraviesan la barrera pulmonar      ")
                print (" y entran al torrente sanguíneo, son practicamente invisibles")
                print (" y las defensas del organismo no son efectivas para detenerlas\n")
            if CO2 >= 300 and CO2 <= 800:
                print ("CO2: RANGO IDEAL\n")
            if CO2 < 300 or CO2 > 800:
                print ("CO2 riesgo de exposición")
                print ("PELIGROSO")
                print ("*      Efectos secundarios:    *\n")
                print (" Somnolencia, dolores de cabeza, perdida de atención \n")
            if COVs <= 0:
                print ("COVs depende del compuesto ")
                print ("*      Efectos secundarios:    *\n")
                print (" Corto plazo: dolores de cabeza, tos, inflamación de los ojos")
                print (" A largo plazo: ansiedad, asma\n")
            if Temp >= 19 and Temp <= 21 or Temp >= 24 and Temp <= 26:
                print("TEMPERATURA")
                print (" * La temperatura está en el rango ideal                 *\n")
            elif Temp < 19 or Temp > 21 or Temp < 24 or Temp > 26:
                print("TEMPERATURA")
                print (" * Efectos:                                              *\n")
                print (" las personas entran en la zona de incomodidad. ")
                print (" Pérdida de concentración, quejas, frío, etc.\n")
            if Hume >= 40 and Hume <= 60:
                print ("HUMEDAD")
                print ("* La humedad está en el rango ideal                      *\n")
            if Hume < 40 or Hume > 60:
                print ("HUMEDAD")
                print ("* Efectos:                                                *\n")
                print (" La humedad ayuda a la supervivencia ")
                print (" de virus, bacterias, hongos y ácaros \n")

    RPM10 += RPM10
    PPM10 = RPM10/dias
    RCO += RCO
    PRCO = RCO/dias
    ROZONO += ROZONO
    PROZONO = ROZONO/dias
    RNO2 += RNO2
    PRNO2 = RNO2/dias
    RSO2 += RSO2
    PRSO2 = RSO2/dias

    print("El promedio de PM10 es de: ",PPM10)
    print("El promedio de CO es de: ", PRCO)
    print("El promedio de O3 es de: ", PROZONO)
    print("El promedio de NO2 es de: ", PRNO2)
    print("El promedio de SO2 es de: ", PRSO2)

    from matplotlib import pyplot as plt
    for i,j in zip((PPM10, PRCO, PROZONO, PRNO2, PRSO2),(PM10, CO, OZONO, NO2, SO2)):
      print(i,":",j)
    plt.bar(("PM10","CO","OZONO","NO2","SO2"),(PPM10, PRCO, PROZONO, PRNO2, PRSO2))
    plt.ylabel("Promedio")
    plt.xlabel("Contaminantes")
    plt.title("GRAFICA DEL ICA EN EL MES")
    plt.show()

    if RPM10 <= 101 or RCO <= 119 or ROZONO <= 108 or  RNO2 <= 92 or RSO2 <= 97:

        print("PRECAUCIONES")
        print("SIGUIENDO LOS SIGUIENTES PASOS PUEDES AYUDAR A PRESERVAR EL NIVEL DE AIRE EN LA ZONA")
        print("1) Usa transporte público o alternativas sostenibles")
        print("2) Evita el uso de carbón o leña")
        print("3) No quemes llantas ni basuras")
        print("4) Aplica la ley de las tres R")
        print("5) Ahorro de energía")
        print("6) Plantar árboles")
        print("7) Uso de productos ecológicos")
        print("8) Educación y concienciación")
        print("9) Reportar actividades contaminantes")
        print("10) Siga las actualizaciones del ICA en su zona\n")
        print("ESTA EN TUS MANOS PRESERVAR NUESTRA CALIDAD DE VIDA")

    if RPM10 >= 102 or RCO >= 120 or ROZONO >= 109 or  RNO2 >= 93 or RSO2 >= 98:
        print("RECOMENDACIONES")
        print("SIGUIENDO LOS SIGUIENTES PASOS PUEDES AYUDAR A MEJORAR EL NIVEL DE AIRE EN LA ZONA\n")
        print("1) Reforzamiento de los programas de seguimiento al cumplimiento de la normativa para fuentes fijas y móviles.")
        print("2) Mejoramiento y modernización de la infraestructura de monitoreo de los contaminantes del aire (emisión - inmisión)")
        print("3) Adopción de planes de movilidad.")
        print("4) Definición de Programas de estímulos para el uso y la adquisición de vehículos eléctricos")
        print("5) Definición de Programas de mantenimiento preventivo vehicular.")
        print("6) Mejoramiento o implementación de sistemas de control de emisiones en proyectos, obras o actividades.")
        print("7) Control de la resuspensión de particulas.")
        print("8) Incorporación de tecnologías más limpias en las industrias.")
        print("9) Mantenimiento y mejoramiento de vías.")
        print("10) Definición de Programas de mejoramiento del espacio público.")
        print("11) Integración de políticas de desarrollo urbano, transporte y calidad del aire.")
        print("12) Establecimiento de directrices y determinantes ambientales para la planeación del territorio,")
        print("teniendo en cuenta el comportamiento y dispersión de los contaminantes del aire\n")
        print("ESTA EN TUS MANOS MEJORAR NUESTRA CALIDAD DE VIDA")

else:
    print("opcion no valida")