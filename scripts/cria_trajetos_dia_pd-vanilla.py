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

linksPascoa = raizMapsPascoa.find("links")
linksDomingo = raizMapsDomingo.find("links")
linksSegunda = raizMapsSegunda.find("links")
linksTerca = raizMapsTerca.find("links")
linksQuarta = raizMapsQuarta.find("links")
linksQuinta = raizMapsQuinta.find("links")
linksSexta = raizMapsSexta.find("links")
linksSabado = raizMapsSabado.find("links")


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


listIDlinksMapsPascoa = [ID.attrib['id'] for ID in list(linksPascoa)]
listAVGSPEEDlinksMapsPascoa = [AVGSPEED.attrib['avgspeed'] for AVGSPEED in list(linksPascoa)]
dicionarioLinksMapsPascoa = {'id': listIDlinksMapsPascoa,
                             'avgspeed': listAVGSPEEDlinksMapsPascoa}


listIDlinksMapsDomingo = [ID.attrib['id'] for ID in list(linksDomingo)]
listAVGSPEEDlinksMapsDomingo = [AVGSPEED.attrib['avgspeed'] for AVGSPEED in list(linksDomingo)]
dicionarioLinksMapsDomingo = {'id': listIDlinksMapsDomingo,
                              'avgspeed': listAVGSPEEDlinksMapsDomingo}


listIDlinksMapsSegunda = [ID.attrib['id'] for ID in list(linksSegunda)]
listAVGSPEEDlinksMapsSegunda = [AVGSPEED.attrib['avgspeed'] for AVGSPEED in list(linksSegunda)]
dicionarioLinksMapsSegunda = {'id': listIDlinksMapsSegunda,
                              'avgspeed': listAVGSPEEDlinksMapsSegunda}


listIDlinksMapsTerca = [ID.attrib['id'] for ID in list(linksTerca)]
listAVGSPEEDlinksMapsTerca = [AVGSPEED.attrib['avgspeed'] for AVGSPEED in list(linksTerca)]
dicionarioLinksMapsTerca = {'id': listIDlinksMapsTerca,
                            'avgspeed': listAVGSPEEDlinksMapsTerca}


listIDlinksMapsQuarta = [ID.attrib['id'] for ID in list(linksQuarta)]
listAVGSPEEDlinksMapsQuarta = [AVGSPEED.attrib['avgspeed'] for AVGSPEED in list(linksQuarta)]
dicionarioLinksMapsQuarta = {'id': listIDlinksMapsQuarta,
                             'avgspeed': listAVGSPEEDlinksMapsQuarta}


listIDlinksMapsQuinta = [ID.attrib['id'] for ID in list(linksQuinta)]
listAVGSPEEDlinksMapsQuinta = [AVGSPEED.attrib['avgspeed'] for AVGSPEED in list(linksQuinta)]
dicionarioLinksMapsQuinta = {'id': listIDlinksMapsQuinta,
                             'avgspeed': listAVGSPEEDlinksMapsQuinta}


listIDlinksMapsSexta = [ID.attrib['id'] for ID in list(linksSexta)]
listAVGSPEEDlinksMapsSexta = [AVGSPEED.attrib['avgspeed'] for AVGSPEED in list(linksSexta)]
dicionarioLinksMapsSexta = {'id': listIDlinksMapsSexta,
                            'avgspeed': listAVGSPEEDlinksMapsSexta}


listIDlinksMapsSabado = [ID.attrib['id'] for ID in list(linksSabado)]
listAVGSPEEDlinksMapsSabado = [AVGSPEED.attrib['avgspeed'] for AVGSPEED in list(linksSabado)]
dicionarioLinksMapsSabado = {'id': listIDlinksMapsSabado,
                             'avgspeed': listAVGSPEEDlinksMapsSabado}


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

dfLinksMapsPascoa = pd.DataFrame(dicionarioLinksMapsPascoa, columns=['id', 'avgspeed'])
dfLinksMapsDomingo = pd.DataFrame(dicionarioLinksMapsDomingo, columns=['id', 'avgspeed'])
dfLinksMapsSegunda = pd.DataFrame(dicionarioLinksMapsSegunda, columns=['id', 'avgspeed'])
dfLinksMapsTerca = pd.DataFrame(dicionarioLinksMapsTerca, columns=['id', 'avgspeed'])
dfLinksMapsQuarta = pd.DataFrame(dicionarioLinksMapsQuarta, columns=['id', 'avgspeed'])
dfLinksMapsQuinta = pd.DataFrame(dicionarioLinksMapsQuinta, columns=['id', 'avgspeed'])
dfLinksMapsSexta = pd.DataFrame(dicionarioLinksMapsSexta, columns=['id', 'avgspeed'])
dfLinksMapsSabado = pd.DataFrame(dicionarioLinksMapsSabado, columns=['id', 'avgspeed'])


#################################
# Separando DataFrames por coluna

idTrajetoPascoa = dfLinksMapsPascoa['id']
avgspeedPascoa = dfLinksMapsPascoa['avgspeed']

idTrajetoDomingo = dfLinksMapsDomingo['id']
avgspeedDomingo = dfLinksMapsDomingo['avgspeed']

idTrajetoSegunda = dfLinksMapsSegunda['id']
avgspeedSegunda = dfLinksMapsSegunda['avgspeed']

idTrajetoTerca = dfLinksMapsTerca['id']
avgspeedTerca = dfLinksMapsTerca['avgspeed']

idTrajetoQuarta = dfLinksMapsQuarta['id']
avgspeedQuarta = dfLinksMapsQuarta['avgspeed']

idTrajetoQuinta = dfLinksMapsQuinta['id']
avgspeedQuinta = dfLinksMapsQuinta['avgspeed']

idTrajetoSexta = dfLinksMapsSexta['id']
avgspeedSexta = dfLinksMapsSexta['avgspeed']

idTrajetoSabado = dfLinksMapsSabado['id']
avgspeedSabado = dfLinksMapsSabado['avgspeed']

####################################
# Funções para criação dos datasets

def imprime_id_pascoa(l):
    linhaIDtrajeto = idTrajetoPascoa[l]
    linhaIDtrajeto = linhaIDtrajeto.replace('-', 'id-')
    for i in range(0, len(linhaIDtrajeto)):
        arquivo.writelines(f'{linhaIDtrajeto[i]}')

def imprime_avgspeed_pascoa(l):
    linhaAvgspeed = avgspeedPascoa[l]
    linhaAvgspeed = linhaAvgspeed.replace(',', '')
    for i in range(0, len(linhaAvgspeed)):
        arquivo.writelines(f'{linhaAvgspeed[i]}')

def gerar_dataset_pascoa():
    for l in range(0, len(idTrajetoPascoa)):
        imprime_id_pascoa(l)
        arquivo.writelines('id ')
        imprime_avgspeed_pascoa(l)
        arquivo.writelines(';\n')


def imprime_id_domingo(l):
    linhaIDtrajeto = idTrajetoDomingo[l]
    linhaIDtrajeto = linhaIDtrajeto.replace('-', 'id-')
    for i in range(0, len(linhaIDtrajeto)):
        arquivo.writelines(f'{linhaIDtrajeto[i]}')

def imprime_avgspeed_domingo(l):
    linhaAvgspeed = avgspeedDomingo[l]
    linhaAvgspeed = linhaAvgspeed.replace(',', '')
    for i in range(0, len(linhaAvgspeed)):
        arquivo.writelines(f'{linhaAvgspeed[i]}')

def gerar_dataset_domingo():
    for l in range(0, len(idTrajetoDomingo)):
        imprime_id_domingo(l)
        arquivo.writelines('id ')
        imprime_avgspeed_domingo(l)
        arquivo.writelines(';\n')


def imprime_id_segunda(l):
    linhaIDtrajeto = idTrajetoSegunda[l]
    linhaIDtrajeto = linhaIDtrajeto.replace('-', 'id-')
    for i in range(0, len(linhaIDtrajeto)):
        arquivo.writelines(f'{linhaIDtrajeto[i]}')

def imprime_avgspeed_segunda(l):
    linhaAvgspeed = avgspeedSegunda[l]
    linhaAvgspeed = linhaAvgspeed.replace(',', '')
    for i in range(0, len(linhaAvgspeed)):
        arquivo.writelines(f'{linhaAvgspeed[i]}')

def gerar_dataset_segunda():
    for l in range(0, len(idTrajetoSegunda)):
        imprime_id_segunda(l)
        arquivo.writelines('id ')
        imprime_avgspeed_segunda(l)
        arquivo.writelines(';\n')


def imprime_id_terca(l):
    linhaIDtrajeto = idTrajetoTerca[l]
    linhaIDtrajeto = linhaIDtrajeto.replace('-', 'id-')
    for i in range(0, len(linhaIDtrajeto)):
        arquivo.writelines(f'{linhaIDtrajeto[i]}')

def imprime_avgspeed_terca(l):
    linhaAvgspeed = avgspeedTerca[l]
    linhaAvgspeed = linhaAvgspeed.replace(',', '')
    for i in range(0, len(linhaAvgspeed)):
        arquivo.writelines(f'{linhaAvgspeed[i]}')

def gerar_dataset_terca():
    for l in range(0, len(idTrajetoTerca)):
        imprime_id_terca(l)
        arquivo.writelines('id ')
        imprime_avgspeed_terca(l)
        arquivo.writelines(';\n')


def imprime_id_quarta(l):
    linhaIDtrajeto = idTrajetoQuarta[l]
    linhaIDtrajeto = linhaIDtrajeto.replace('-', 'id-')
    for i in range(0, len(linhaIDtrajeto)):
        arquivo.writelines(f'{linhaIDtrajeto[i]}')

def imprime_avgspeed_quarta(l):
    linhaAvgspeed = avgspeedQuarta[l]
    linhaAvgspeed = linhaAvgspeed.replace(',', '')
    for i in range(0, len(linhaAvgspeed)):
        arquivo.writelines(f'{linhaAvgspeed[i]}')

def gerar_dataset_quarta():
    for l in range(0, len(idTrajetoQuarta)):
        imprime_id_quarta(l)
        arquivo.writelines('id ')
        imprime_avgspeed_quarta(l)
        arquivo.writelines(';\n')


def imprime_id_quinta(l):
    linhaIDtrajeto = idTrajetoQuinta[l]
    linhaIDtrajeto = linhaIDtrajeto.replace('-', 'id-')
    for i in range(0, len(linhaIDtrajeto)):
        arquivo.writelines(f'{linhaIDtrajeto[i]}')

def imprime_avgspeed_quinta(l):
    linhaAvgspeed = avgspeedQuinta[l]
    linhaAvgspeed = linhaAvgspeed.replace(',', '')
    for i in range(0, len(linhaAvgspeed)):
        arquivo.writelines(f'{linhaAvgspeed[i]}')

def gerar_dataset_quinta():
    for l in range(0, len(idTrajetoQuinta)):
        imprime_id_quinta(l)
        arquivo.writelines('id ')
        imprime_avgspeed_quinta(l)
        arquivo.writelines(';\n')


def imprime_id_sexta(l):
    linhaIDtrajeto = idTrajetoSexta[l]
    linhaIDtrajeto = linhaIDtrajeto.replace('-', 'id-')
    for i in range(0, len(linhaIDtrajeto)):
        arquivo.writelines(f'{linhaIDtrajeto[i]}')

def imprime_avgspeed_sexta(l):
    linhaAvgspeed = avgspeedSexta[l]
    linhaAvgspeed = linhaAvgspeed.replace(',', '')
    for i in range(0, len(linhaAvgspeed)):
        arquivo.writelines(f'{linhaAvgspeed[i]}')

def gerar_dataset_sexta():
    for l in range(0, len(idTrajetoSexta)):
        imprime_id_sexta(l)
        arquivo.writelines('id ')
        imprime_avgspeed_sexta(l)
        arquivo.writelines(';\n')


def imprime_id_sabado(l):
    linhaIDtrajeto = idTrajetoSabado[l]
    linhaIDtrajeto = linhaIDtrajeto.replace('-', 'id-')
    for i in range(0, len(linhaIDtrajeto)):
        arquivo.writelines(f'{linhaIDtrajeto[i]}')

def imprime_avgspeed_sabado(l):
    linhaAvgspeed = avgspeedSabado[l]
    linhaAvgspeed = linhaAvgspeed.replace(',', '')
    for i in range(0, len(linhaAvgspeed)):
        arquivo.writelines(f'{linhaAvgspeed[i]}')

def gerar_dataset_sabado():
    for l in range(0, len(idTrajetoSabado)):
        imprime_id_sabado(l)
        arquivo.writelines('id ')
        imprime_avgspeed_sabado(l)
        arquivo.writelines(';\n')


##########################
#   Programa Principal   #
##########################

arquivo = open(f'{dirPrincipal}/dados_pd/trajetos_pascoa', 'w')
gerar_dataset_pascoa()
arquivo = open(f'{dirPrincipal}/dados_pd/trajetos_dom', 'w')
gerar_dataset_domingo()
arquivo = open(f'{dirPrincipal}/dados_pd/trajetos_seg', 'w')
gerar_dataset_segunda()
arquivo = open(f'{dirPrincipal}/dados_pd/trajetos_ter', 'w')
gerar_dataset_terca()
arquivo = open(f'{dirPrincipal}/dados_pd/trajetos_qua', 'w')
gerar_dataset_quarta()
arquivo = open(f'{dirPrincipal}/dados_pd/trajetos_qui', 'w')
gerar_dataset_quinta()
arquivo = open(f'{dirPrincipal}/dados_pd/trajetos_sex', 'w')
gerar_dataset_sexta()
arquivo = open(f'{dirPrincipal}/dados_pd/trajetos_sab', 'w')
gerar_dataset_sabado()
