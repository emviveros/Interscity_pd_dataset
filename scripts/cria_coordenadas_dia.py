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
'''
######################################################
# Carregando os dados xml em objetos tipo ElementTree

mapsPascoa = ET.parse(f'{dirPrincipal}/dados/2017-04-13-pascoa/map_20170413.xml')
mapsDomingo = ET.parse(f'{dirPrincipal}/dados/2017-10-22-domingo/map_20171022.xml')
mapsSegunda = ET.parse(f'{dirPrincipal}/dados/2017-10-23-segunda/map_20171023.xml')
mapsTerca = ET.parse(f'{dirPrincipal}/dados/2017-10-24-terca/map_20171024.xml')
mapsQuarta = ET.parse(f'{dirPrincipal}/dados/2017-10-25-quarta/map_20171025.xml')
mapsQuinta = ET.parse(f'{dirPrincipal}/dados/2017-10-26-quinta/map_20171026.xml')
mapsSexta = ET.parse(f'{dirPrincipal}/dados/2017-10-27-sexta/map_20171027.xml')
mapsSabado = ET.parse(f'{dirPrincipal}/dados/2017-10-28-sabado/map_20171028.xml')

#####################################
# Pegando a raiz dos objetos criados

raizMapsPascoa = mapsPascoa.getroot()
raizMapsDomingo = mapsDomingo.getroot()
raizMapsSegunda = mapsSegunda.getroot()
raizMapsTerca = mapsTerca.getroot()
raizMapsQuarta = mapsQuarta.getroot()
raizMapsQuinta = mapsQuinta.getroot()
raizMapsSexta = mapsSexta.getroot()
raizMapsSabado = mapsSabado.getroot()

#####################################################
# Recuperação elemento nodes de cada xml

nodesPascoa = raizMapsPascoa.find("nodes")
nodesDomingo = raizMapsDomingo.find("nodes")
nodesSegunda = raizMapsSegunda.find("nodes")
nodesTerca = raizMapsTerca.find("nodes")
nodesQuarta = raizMapsQuarta.find("nodes")
nodesQuinta = raizMapsQuinta.find("nodes")
nodesSexta = raizMapsSexta.find("nodes")
nodesSabado = raizMapsSabado.find("nodes")


#####################################################
# Formatação para processamento de dados pelo Pandas

listIDnodesMapsPascoa = [ID.attrib['id'] for ID in list(nodesPascoa)]
listXnodesMapsPascoa = [X.attrib['x'] for X in list(nodesPascoa)]
listYnodesMapsPascoa = [Y.attrib['y'] for Y in list(nodesPascoa)]
dicionarioNodesMapsPascoa = {'id': listIDnodesMapsPascoa,
                             'x': listXnodesMapsPascoa,
                             'y': listYnodesMapsPascoa}


listIDnodesMapsDomingo = [ID.attrib['id'] for ID in list(nodesDomingo)]
listXnodesMapsDomingo = [X.attrib['x'] for X in list(nodesDomingo)]
listYnodesMapsDomingo = [Y.attrib['y'] for Y in list(nodesDomingo)]
dicionarioNodesMapsDomingo = {'id': listIDnodesMapsDomingo,
                              'x': listXnodesMapsDomingo,
                              'y': listYnodesMapsDomingo}


listIDnodesMapsSegunda = [ID.attrib['id'] for ID in list(nodesSegunda)]
listXnodesMapsSegunda = [X.attrib['x'] for X in list(nodesSegunda)]
listYnodesMapsSegunda = [Y.attrib['y'] for Y in list(nodesSegunda)]
dicionarioNodesMapsSegunda = {'id': listIDnodesMapsSegunda,
                              'x': listXnodesMapsSegunda,
                              'y': listYnodesMapsSegunda}


listIDnodesMapsTerca = [ID.attrib['id'] for ID in list(nodesTerca)]
listXnodesMapsTerca = [X.attrib['x'] for X in list(nodesTerca)]
listYnodesMapsTerca = [Y.attrib['y'] for Y in list(nodesTerca)]
dicionarioNodesMapsTerca = {'id': listIDnodesMapsTerca,
                            'x': listXnodesMapsTerca,
                            'y': listYnodesMapsTerca}


listIDnodesMapsQuarta = [ID.attrib['id'] for ID in list(nodesQuarta)]
listXnodesMapsQuarta = [X.attrib['x'] for X in list(nodesQuarta)]
listYnodesMapsQuarta = [Y.attrib['y'] for Y in list(nodesQuarta)]
dicionarioNodesMapsQuarta = {'id': listIDnodesMapsQuarta,
                             'x': listXnodesMapsQuarta,
                             'y': listYnodesMapsQuarta}


listIDnodesMapsQuinta = [ID.attrib['id'] for ID in list(nodesQuinta)]
listXnodesMapsQuinta = [X.attrib['x'] for X in list(nodesQuinta)]
listYnodesMapsQuinta = [Y.attrib['y'] for Y in list(nodesQuinta)]
dicionarioNodesMapsQuinta = {'id': listIDnodesMapsQuinta,
                             'x': listXnodesMapsQuinta,
                             'y': listYnodesMapsQuinta}


listIDnodesMapsSexta = [ID.attrib['id'] for ID in list(nodesSexta)]
listXnodesMapsSexta = [X.attrib['x'] for X in list(nodesSexta)]
listYnodesMapsSexta = [Y.attrib['y'] for Y in list(nodesSexta)]
dicionarioNodesMapsSexta = {'id': listIDnodesMapsSexta,
                            'x': listXnodesMapsSexta,
                            'y': listYnodesMapsSexta}


listIDnodesMapsSabado = [ID.attrib['id'] for ID in list(nodesSabado)]
listXnodesMapsSabado = [X.attrib['x'] for X in list(nodesSabado)]
listYnodesMapsSabado = [Y.attrib['y'] for Y in list(nodesSabado)]
dicionarioNodesMapsSabado = {'id': listIDnodesMapsSabado,
                             'x': listXnodesMapsSabado,
                             'y': listYnodesMapsSabado}


###############################
# Gerando DataFrames em Pandas

dfNodesMapsPascoa = pd.DataFrame(dicionarioNodesMapsPascoa, columns=['id', 'x', 'y'])
dfNodesMapsSegunda = pd.DataFrame(dicionarioNodesMapsDomingo, columns=['id', 'x', 'y'])
dfNodesMapsTerca = pd.DataFrame(dicionarioNodesMapsSegunda, columns=['id', 'x', 'y'])
dfNodesMapsQuarta = pd.DataFrame(dicionarioNodesMapsTerca, columns=['id', 'x', 'y'])
dfNodesMapsQuinta = pd.DataFrame(dicionarioNodesMapsQuarta, columns=['id', 'x', 'y'])
dfNodesMapsSexta = pd.DataFrame(dicionarioNodesMapsQuinta, columns=['id', 'x', 'y'])
dfNodesMapsSabado = pd.DataFrame(dicionarioNodesMapsSexta, columns=['id', 'x', 'y'])
dfNodesMapsDomingo = pd.DataFrame(dicionarioNodesMapsSabado, columns=['id', 'x', 'y'])


#################################
# Separando DataFrames por coluna

idCoordenadasPascoa = dfNodesMapsPascoa['id']
#xCoordenadasPascoa = dfNodesMapsPascoa['x']
#yCoordenadasPascoa = dfNodesMapsPascoa['y']
'''
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
        id = id.replace(',', 'id, ')
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
        id = id.replace(',', 'id, ')
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
        id = id.replace(',', 'id, ')
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
        id = id.replace(',', 'id, ')
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
        id = id.replace(',', 'id, ')
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
        id = id.replace(',', 'id, ')
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
        id = id.replace(',', 'id, ')
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
        id = id.replace(',', 'id, ')
        x = float(l[1])
        x = round(scale(x, xOldMax, xOldMin, newMax, newMin), 2)
        y = l[2]
        y = float(y.replace(';', ''))
        y = round(scale(y, yOldMax, yOldMin, newMax, newMin), 2)
        arquivo.writelines(f'{id}{x} {y} zonaUrbana;\n')

