########################
# Impotando bibliotecas

import os
import xml.etree.ElementTree as ET
import pandas as pd

#######################################################
# Carregando diretório atual para chamada de dados xml

from os import path
dirAtual = os.getcwd()
dirPrincipal = path.abspath(path.join(dirAtual, ".."))

#########################################
# Carregando arquivos texto para análise

textoLatLongPascoa = open(f'{dirPrincipal}/dados/2017-04-13-pascoa/maps_20170413_id_x_y-latlong', 'r')
textoLatLongDomingo = open(f'{dirPrincipal}/dados/2017-10-22-domingo/map_20171022_id_x_y-latlong', 'r')
textoLatLongSegunda = open(f'{dirPrincipal}/dados/2017-10-23-segunda/map_20171023_id_x_y-latlong', 'r')
textoLatLongTerca = open(f'{dirPrincipal}/dados/2017-10-24-terca/map_20171024_id_x_y-latlong', 'r')
textoLatLongQuarta = open(f'{dirPrincipal}/dados/2017-10-25-quarta/map_20171025_id_x_y-latlong', 'r')
textoLatLongQuinta = open(f'{dirPrincipal}/dados/2017-10-26-quinta/map_20171026_id_x_y-latlong', 'r')
textoLatLongSexta = open(f'{dirPrincipal}/dados/2017-10-27-sexta/map_20171027_id_x_y-latlong', 'r')
textoLatLongSabado = open(f'{dirPrincipal}/dados/2017-10-28-sabado/map_20171028_id_x_y-latlong', 'r')


##########################
# Função de escalonamento

xOldMin = float(-23.3894)
xOldMax = float(-23.7686)

yOldMin = float(-46.804501)
yOldMax = float(-46.364498)

oldMax = 0
oldMin = 0
newMax = 1000
newMin = 0

entrada = 0

def scale(entrada, oldMax, oldMin, newMax, newMin):
    return((((entrada - oldMin) * (newMax - newMin)) / (oldMax - oldMin)) + newMin)

##########################
#   Programa Principal   #
##########################

arquivo = open(f'{dirPrincipal}/dados_pd/coordenadas_pascoa', 'w')
with textoLatLongPascoa as texto:
    for linha in texto:
        l = linha.split()
        id = l[0]
        id = id.replace(',', 'id ')
        x = float(l[1])
        x = round(scale(x, xOldMax, xOldMin, newMax, newMin), 2)
        y = l[2]
        y = float(y.replace(';', ''))
        y = round(scale(y, yOldMax, yOldMin, newMax, newMin), 2)
        arquivo.writelines(f'{id}{x} {y} zonaUrbana;\n')


arquivo = open(f'{dirPrincipal}/dados_pd/coordenadas_dom', 'w')
with textoLatLongDomingo as texto:
    for linha in texto:
        l = linha.split()
        id = l[0]
        id = id.replace(',', 'id ')
        x = float(l[1])
        x = round(scale(x, xOldMax, xOldMin, newMax, newMin), 2)
        y = l[2]
        y = float(y.replace(';', ''))
        y = round(scale(y, yOldMax, yOldMin, newMax, newMin), 2)
        arquivo.writelines(f'{id}{x} {y} zonaUrbana;\n')


arquivo = open(f'{dirPrincipal}/dados_pd/coordenadas_seg', 'w')
with textoLatLongSegunda as texto:
    for linha in texto:
        l = linha.split()
        id = l[0]
        id = id.replace(',', 'id ')
        x = float(l[1])
        x = round(scale(x, xOldMax, xOldMin, newMax, newMin), 2)
        y = l[2]
        y = float(y.replace(';', ''))
        y = round(scale(y, yOldMax, yOldMin, newMax, newMin), 2)
        arquivo.writelines(f'{id}{x} {y} zonaUrbana;\n')


arquivo = open(f'{dirPrincipal}/dados_pd/coordenadas_ter', 'w')
with textoLatLongTerca as texto:
    for linha in texto:
        l = linha.split()
        id = l[0]
        id = id.replace(',', 'id ')
        x = float(l[1])
        x = round(scale(x, xOldMax, xOldMin, newMax, newMin), 2)
        y = l[2]
        y = float(y.replace(';', ''))
        y = round(scale(y, yOldMax, yOldMin, newMax, newMin), 2)
        arquivo.writelines(f'{id}{x} {y} zonaUrbana;\n')


arquivo = open(f'{dirPrincipal}/dados_pd/coordenadas_qua', 'w')
with textoLatLongQuarta as texto:
    for linha in texto:
        l = linha.split()
        id = l[0]
        id = id.replace(',', 'id ')
        x = float(l[1])
        x = round(scale(x, xOldMax, xOldMin, newMax, newMin), 2)
        y = l[2]
        y = float(y.replace(';', ''))
        y = round(scale(y, yOldMax, yOldMin, newMax, newMin), 2)
        arquivo.writelines(f'{id}{x} {y} zonaUrbana;\n')


arquivo = open(f'{dirPrincipal}/dados_pd/coordenadas_qui', 'w')
with textoLatLongQuinta as texto:
    for linha in texto:
        l = linha.split()
        id = l[0]
        id = id.replace(',', 'id ')
        x = float(l[1])
        x = round(scale(x, xOldMax, xOldMin, newMax, newMin), 2)
        y = l[2]
        y = float(y.replace(';', ''))
        y = round(scale(y, yOldMax, yOldMin, newMax, newMin), 2)
        arquivo.writelines(f'{id}{x} {y} zonaUrbana;\n')


arquivo = open(f'{dirPrincipal}/dados_pd/coordenadas_sex', 'w')
with textoLatLongSexta as texto:
    for linha in texto:
        l = linha.split()
        id = l[0]
        id = id.replace(',', 'id ')
        x = float(l[1])
        x = round(scale(x, xOldMax, xOldMin, newMax, newMin), 2)
        y = l[2]
        y = float(y.replace(';', ''))
        y = round(scale(y, yOldMax, yOldMin, newMax, newMin), 2)
        arquivo.writelines(f'{id}{x} {y} zonaUrbana;\n')


arquivo = open(f'{dirPrincipal}/dados_pd/coordenadas_sab', 'w')
with textoLatLongSabado as texto:
    for linha in texto:
        l = linha.split()
        id = l[0]
        id = id.replace(',', 'id ')
        x = float(l[1])
        x = round(scale(x, xOldMax, xOldMin, newMax, newMin), 2)
        y = l[2]
        y = float(y.replace(';', ''))
        y = round(scale(y, yOldMax, yOldMin, newMax, newMin), 2)
        arquivo.writelines(f'{id}{x} {y} zonaUrbana;\n')

