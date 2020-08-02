########################
# Importando bibliotecas

import os
from os import path
import xml.etree.ElementTree as ET
import pandas as pd


# Função auxiliar
from pandas import DataFrame


def printAllChildrens(element):
    print(f'\nElementos de {element.tag}')
    print('-'*10)
    for item in list(element):
        print(item.tag)
    print('-'*10)
    print()


#######################################################
# Carregando diretório atual para chamada de dados xml

dirAtual = os.getcwd()


dirPrincipal = path.abspath(path.join(dirAtual, ".."))


######################################################
# Carregando os dados xml em objetos tipo ElementTree

busesPascoa = ET.parse(f'{dirPrincipal}/dados/2017-04-13-pascoa/buses_quinta.xml')
busesDomingo = ET.parse(f'{dirPrincipal}/dados/2017-10-22-domingo/buses_20171022.xml')
busesSegunda = ET.parse(f'{dirPrincipal}/dados/2017-10-23-segunda/buses_20171023.xml')
busesTerca = ET.parse(f'{dirPrincipal}/dados/2017-10-24-terca/buses_20171024.xml')
busesQuarta = ET.parse(f'{dirPrincipal}/dados/2017-10-25-quarta/buses_20171025.xml')
busesQuinta = ET.parse(f'{dirPrincipal}/dados/2017-10-26-quinta/buses_20171026.xml')
busesSexta = ET.parse(f'{dirPrincipal}/dados/2017-10-27-sexta/buses_20171027.xml')
busesSabado = ET.parse(f'{dirPrincipal}/dados/2017-10-28-sabado/buses_20171028.xml')

#####################################
# Pegando a raiz dos objetos criados

raizBusesPascoa = busesPascoa.getroot()
raizBusesDomingo = busesDomingo.getroot()
raizBusesSegunda = busesSegunda.getroot()
raizBusesTerca = busesTerca.getroot()
raizBusesQuarta = busesQuarta.getroot()
raizBusesQuinta = busesQuinta.getroot()
raizBusesSexta = busesSexta.getroot()
raizBusesSabado = busesSabado.getroot()


#################################################################################
# Criação de listas para cada atributo de cada elemento bus a cada dia da semana

listIDbusPascoa = [ID.attrib['id'] for ID in list(raizBusesPascoa)]
listINTERVALbusPascoa = [INTERVAL.attrib['interval'] for INTERVAL in list(raizBusesPascoa)]
listSTART_TIMEbusPascoa = [START_TIME.attrib['start_time'] for START_TIME in list(raizBusesPascoa)]
listSTOPSbusPascoa = [STOPS.attrib['stops'] for STOPS in list(raizBusesPascoa)]

dicionarioNodesBusesPascoa = {'id': listIDbusPascoa,
                              'interval': listINTERVALbusPascoa,
                              'start_time': listSTART_TIMEbusPascoa,
                              'stops': listSTOPSbusPascoa}


listIDbusDomingo = [ID.attrib['id'] for ID in list(raizBusesDomingo)]
listINTERVALbusDomingo = [INTERVAL.attrib['interval'] for INTERVAL in list(raizBusesDomingo)]
listSTART_TIMEbusDomingo = [START_TIME.attrib['start_time'] for START_TIME in list(raizBusesDomingo)]
listSTOPSbusDomingo = [STOPS.attrib['stops'] for STOPS in list(raizBusesDomingo)]

dicionarioNodesBusesDomingo = {'id': listIDbusDomingo,
                               'interval': listINTERVALbusDomingo,
                               'start_time': listSTART_TIMEbusDomingo,
                               'stops': listSTOPSbusDomingo}


listIDbusSegunda = [ID.attrib['id'] for ID in list(raizBusesSegunda)]
listINTERVALbusSegunda = [INTERVAL.attrib['interval'] for INTERVAL in list(raizBusesSegunda)]
listSTART_TIMEbusSegunda = [START_TIME.attrib['start_time'] for START_TIME in list(raizBusesSegunda)]
listSTOPSbusSegunda = [STOPS.attrib['stops'] for STOPS in list(raizBusesSegunda)]

dicionarioNodesBusesSegunda = {'id': listIDbusSegunda,
                               'interval': listINTERVALbusSegunda,
                               'start_time': listSTART_TIMEbusSegunda,
                               'stops': listSTOPSbusSegunda}


listIDbusTerca = [ID.attrib['id'] for ID in list(raizBusesTerca)]
listINTERVALbusTerca = [INTERVAL.attrib['interval'] for INTERVAL in list(raizBusesTerca)]
listSTART_TIMEbusTerca = [START_TIME.attrib['start_time'] for START_TIME in list(raizBusesTerca)]
listSTOPSbusTerca = [STOPS.attrib['stops'] for STOPS in list(raizBusesTerca)]

dicionarioNodesBusesTerca = {'id': listIDbusTerca,
                             'interval': listINTERVALbusTerca,
                             'start_time': listSTART_TIMEbusTerca,
                             'stops': listSTOPSbusTerca}


listIDbusQuarta = [ID.attrib['id'] for ID in list(raizBusesQuarta)]
listINTERVALbusQuarta = [INTERVAL.attrib['interval'] for INTERVAL in list(raizBusesQuarta)]
listSTART_TIMEbusQuarta = [START_TIME.attrib['start_time'] for START_TIME in list(raizBusesQuarta)]
listSTOPSbusQuarta = [STOPS.attrib['stops'] for STOPS in list(raizBusesQuarta)]

dicionarioNodesBusesQuarta = {'id': listIDbusQuarta,
                              'interval': listINTERVALbusQuarta,
                              'start_time': listSTART_TIMEbusQuarta,
                              'stops': listSTOPSbusQuarta}


listIDbusQuinta = [ID.attrib['id'] for ID in list(raizBusesQuinta)]
listINTERVALbusQuinta = [INTERVAL.attrib['interval'] for INTERVAL in list(raizBusesQuinta)]
listSTART_TIMEbusQuinta = [START_TIME.attrib['start_time'] for START_TIME in list(raizBusesQuinta)]
listSTOPSbusQuinta = [STOPS.attrib['stops'] for STOPS in list(raizBusesQuinta)]

dicionarioNodesBusesQuinta = {'id': listIDbusQuinta,
                              'interval': listINTERVALbusQuinta,
                              'start_time': listSTART_TIMEbusQuinta,
                              'stops': listSTOPSbusQuinta}


listIDbusSexta = [ID.attrib['id'] for ID in list(raizBusesSexta)]
listINTERVALbusSexta = [INTERVAL.attrib['interval'] for INTERVAL in list(raizBusesSexta)]
listSTART_TIMEbusSexta = [START_TIME.attrib['start_time'] for START_TIME in list(raizBusesSexta)]
listSTOPSbusSexta = [STOPS.attrib['stops'] for STOPS in list(raizBusesSexta)]

dicionarioNodesBusesSexta = {'id': listIDbusSexta,
                             'interval': listINTERVALbusSexta,
                             'start_time': listSTART_TIMEbusSexta,
                             'stops': listSTOPSbusSexta}


listIDbusSabado = [ID.attrib['id'] for ID in list(raizBusesSabado)]
listINTERVALbusSabado = [INTERVAL.attrib['interval'] for INTERVAL in list(raizBusesSabado)]
listSTART_TIMEbusSabado = [START_TIME.attrib['start_time'] for START_TIME in list(raizBusesSabado)]
listSTOPSbusSabado = [STOPS.attrib['stops'] for STOPS in list(raizBusesSabado)]

dicionarioNodesBusesSabado = {'id': listIDbusSabado,
                              'interval': listINTERVALbusSabado,
                              'start_time': listSTART_TIMEbusSabado,
                              'stops': listSTOPSbusSabado}
###############################
# Gerando DataFrames em Pandas

dfBusesPascoa: DataFrame = pd.DataFrame(dicionarioNodesBusesPascoa, columns=['id', 'interval', 'start_time', 'stops'])
dfBusesDomingo: DataFrame = pd.DataFrame(dicionarioNodesBusesDomingo, columns=['id', 'interval', 'start_time', 'stops'])
dfBusesSegunda: DataFrame = pd.DataFrame(dicionarioNodesBusesSegunda, columns=['id', 'interval', 'start_time', 'stops'])
dfBusesTerca: DataFrame = pd.DataFrame(dicionarioNodesBusesTerca, columns=['id', 'interval', 'start_time', 'stops'])
dfBusesQuarta: DataFrame = pd.DataFrame(dicionarioNodesBusesQuarta, columns=['id', 'interval', 'start_time', 'stops'])
dfBusesQuinta: DataFrame = pd.DataFrame(dicionarioNodesBusesQuinta, columns=['id', 'interval', 'start_time', 'stops'])
dfBusesSexta: DataFrame = pd.DataFrame(dicionarioNodesBusesSexta, columns=['id', 'interval', 'start_time', 'stops'])
dfBusesSabado: DataFrame = pd.DataFrame(dicionarioNodesBusesSabado, columns=['id', 'interval', 'start_time', 'stops'])


#################################
# Separando DataFrames por coluna

onibusPascoa = dfBusesPascoa['id']
intervalPascoa = dfBusesPascoa['interval']
start_timePascoa = dfBusesPascoa['start_time']
stopsPascoa = dfBusesPascoa['stops']

onibusDomingo = dfBusesDomingo['id']
intervalDomingo = dfBusesDomingo['interval']
start_timeDomingo = dfBusesDomingo['start_time']
stopsDomingo = dfBusesDomingo['stops']

onibusSegunda = dfBusesSegunda['id']
intervalSegunda = dfBusesSegunda['interval']
start_timeSegunda = dfBusesSegunda['start_time']
stopsSegunda = dfBusesSegunda['stops']

onibusTerca = dfBusesTerca['id']
intervalTerca = dfBusesTerca['interval']
start_timeTerca = dfBusesTerca['start_time']
stopsTerca = dfBusesTerca['stops']

onibusQuarta = dfBusesQuarta['id']
intervalQuarta = dfBusesQuarta['interval']
start_timeQuarta = dfBusesQuarta['start_time']
stopsQuarta = dfBusesQuarta['stops']

onibusQuinta = dfBusesQuinta['id']
intervalQuinta = dfBusesQuinta['interval']
start_timeQuinta = dfBusesQuinta['start_time']
stopsQuinta = dfBusesQuinta['stops']

onibusSexta = dfBusesSexta['id']
intervalSexta = dfBusesSexta['interval']
start_timeSexta = dfBusesSexta['start_time']
stopsSexta = dfBusesSexta['stops']

onibusSabado = dfBusesSabado['id']
intervalSabado = dfBusesSabado['interval']
start_timeSabado = dfBusesSabado['start_time']
stopsSabado = dfBusesSabado['stops']


####################################
# Funções para criação dos datasets

def imprime_lista_onibus(df):
    max = len(df)
    linha_de_onibus = df[0]
    arquivo.writelines(f'0, {linha_de_onibus};')
    for i in range(1, max):
        arquivo.writelines('\n')
        linha_de_onibus = df[i]
        arquivo.writelines(f'{i}, {linha_de_onibus};')

def imprime_linha_interval_pascoa(l):
    linhaInterval = intervalPascoa[l]
    linhaInterval = linhaInterval.replace(',', ' ')
    for i in range(0, len(linhaInterval)):
        arquivo.writelines(f'{linhaInterval[i]}')

def imprime_linha_interval_domingo(l):
    linhaInterval = intervalDomingo[l]
    linhaInterval = linhaInterval.replace(',', ' ')
    for i in range(0, len(linhaInterval)):
        arquivo.writelines(f'{linhaInterval[i]}')

def imprime_linha_interval_segunda(l):
    linhaInterval = intervalSegunda[l]
    linhaInterval = linhaInterval.replace(',', ' ')
    for i in range(0, len(linhaInterval)):
        arquivo.writelines(f'{linhaInterval[i]}')

def imprime_linha_interval_terca(l):
    linhaInterval = intervalTerca[l]
    linhaInterval = linhaInterval.replace(',', ' ')
    for i in range(0, len(linhaInterval)):
        arquivo.writelines(f'{linhaInterval[i]}')

def imprime_linha_interval_quarta(l):
    linhaInterval = intervalQuarta[l]
    linhaInterval = linhaInterval.replace(',', ' ')
    for i in range(0, len(linhaInterval)):
        arquivo.writelines(f'{linhaInterval[i]}')

def imprime_linha_interval_quinta(l):
    linhaInterval = intervalQuinta[l]
    linhaInterval = linhaInterval.replace(',', ' ')
    for i in range(0, len(linhaInterval)):
        arquivo.writelines(f'{linhaInterval[i]}')

def imprime_linha_interval_sexta(l):
    linhaInterval = intervalSexta[l]
    linhaInterval = linhaInterval.replace(',', ' ')
    for i in range(0, len(linhaInterval)):
        arquivo.writelines(f'{linhaInterval[i]}')

def imprime_linha_interval_sabado(l):
    linhaInterval = intervalSabado[l]
    linhaInterval = linhaInterval.replace(',', ' ')
    for i in range(0, len(linhaInterval)):
        arquivo.writelines(f'{linhaInterval[i]}')


def imprime_linha_stops_pascoa(l):
    linhaStops = stopsPascoa[l]
    linhaStops = linhaStops.replace(',', 'id ')
    for i in range(0, len(linhaStops)):
        arquivo.writelines(f'{linhaStops[i]}')

def imprime_linha_stops_domingo(l):
    linhaStops = stopsDomingo[l]
    linhaStops = linhaStops.replace(',', 'id ')
    for i in range(0, len(linhaStops)):
        arquivo.writelines(f'{linhaStops[i]}')

def imprime_linha_stops_segunda(l):
    linhaStops = stopsSegunda[l]
    linhaStops = linhaStops.replace(',', 'id ')
    for i in range(0, len(linhaStops)):
        arquivo.writelines(f'{linhaStops[i]}')

def imprime_linha_stops_terca(l):
    linhaStops = stopsTerca[l]
    linhaStops = linhaStops.replace(',', 'id ')
    for i in range(0, len(linhaStops)):
        arquivo.writelines(f'{linhaStops[i]}')

def imprime_linha_stops_quarta(l):
    linhaStops = stopsQuarta[l]
    linhaStops = linhaStops.replace(',', 'id ')
    for i in range(0, len(linhaStops)):
        arquivo.writelines(f'{linhaStops[i]}')

def imprime_linha_stops_quinta(l):
    linhaStops = stopsQuinta[l]
    linhaStops = linhaStops.replace(',', 'id ')
    for i in range(0, len(linhaStops)):
        arquivo.writelines(f'{linhaStops[i]}')

def imprime_linha_stops_sexta(l):
    linhaStops = stopsSexta[l]
    linhaStops = linhaStops.replace(',', 'id ')
    for i in range(0, len(linhaStops)):
        arquivo.writelines(f'{linhaStops[i]}')

def imprime_linha_stops_sabado(l):
    linhaStops = stopsSabado[l]
    linhaStops = linhaStops.replace(',', 'id ')
    for i in range(0, len(linhaStops)):
        arquivo.writelines(f'{linhaStops[i]}')


def gerar_dataset_pascoa():
    for l in range(0, len(onibusPascoa)):
        arquivo.writelines(f'{onibusPascoa[l]}, {start_timePascoa[l]} ')
        imprime_linha_interval_pascoa(l)
        arquivo.writelines(' ')
        imprime_linha_stops_pascoa(l)
        arquivo.writelines('id;\n')

def gerar_dataset_domingo():
    for l in range(0, len(onibusDomingo)):
        arquivo.writelines(f'{onibusDomingo[l]}, {start_timeDomingo[l]} ')
        imprime_linha_interval_domingo(l)
        arquivo.writelines(' ')
        imprime_linha_stops_domingo(l)
        arquivo.writelines('id;\n')

def gerar_dataset_segunda():
    for l in range(0, len(onibusSegunda)):
        arquivo.writelines(f'{onibusSegunda[l]}, {start_timeSegunda[l]} ')
        imprime_linha_interval_segunda(l)
        arquivo.writelines(' ')
        imprime_linha_stops_segunda(l)
        arquivo.writelines('id;\n')

def gerar_dataset_terca():
    for l in range(0, len(onibusTerca)):
        arquivo.writelines(f'{onibusTerca[l]}, {start_timeTerca[l]} ')
        imprime_linha_interval_terca(l)
        arquivo.writelines(' ')
        imprime_linha_stops_terca(l)
        arquivo.writelines('id;\n')

def gerar_dataset_quarta():
    for l in range(0, len(onibusQuarta)):
        arquivo.writelines(f'{onibusQuarta[l]}, {start_timeQuarta[l]} ')
        imprime_linha_interval_quarta(l)
        arquivo.writelines(' ')
        imprime_linha_stops_quarta(l)
        arquivo.writelines('id;\n')

def gerar_dataset_quinta():
    for l in range(0, len(onibusQuinta)):
        arquivo.writelines(f'{onibusQuinta[l]}, {start_timeQuinta[l]} ')
        imprime_linha_interval_quinta(l)
        arquivo.writelines(' ')
        imprime_linha_stops_quinta(l)
        arquivo.writelines('id;\n')

def gerar_dataset_sexta():
    for l in range(0, len(onibusSexta)):
        arquivo.writelines(f'{onibusSexta[l]}, {start_timeSexta[l]} ')
        imprime_linha_interval_sexta(l)
        arquivo.writelines(' ')
        imprime_linha_stops_sexta(l)
        arquivo.writelines('id;\n')

def gerar_dataset_sabado():
    for l in range(0, len(onibusSabado)):
        arquivo.writelines(f'{onibusSabado[l]}, {start_timeSabado[l]} ')
        imprime_linha_interval_sabado(l)
        arquivo.writelines(' ')
        imprime_linha_stops_sabado(l)
        arquivo.writelines('id;\n')


##########################
#   Programa Principal   #
##########################

arquivo = open(f'{dirPrincipal}/dados_pd/onibus_pascoa', 'w')
gerar_dataset_pascoa()
arquivo = open(f'{dirPrincipal}/dados_pd/onibus_dom', 'w')
gerar_dataset_domingo()
arquivo = open(f'{dirPrincipal}/dados_pd/onibus_seg', 'w')
gerar_dataset_segunda()
arquivo = open(f'{dirPrincipal}/dados_pd/onibus_ter', 'w')
gerar_dataset_terca()
arquivo = open(f'{dirPrincipal}/dados_pd/onibus_qua', 'w')
gerar_dataset_quarta()
arquivo = open(f'{dirPrincipal}/dados_pd/onibus_qui', 'w')
gerar_dataset_quinta()
arquivo = open(f'{dirPrincipal}/dados_pd/onibus_sex', 'w')
gerar_dataset_sexta()
arquivo = open(f'{dirPrincipal}/dados_pd/onibus_sab', 'w')
gerar_dataset_sabado()

arquivo = open(f'{dirPrincipal}/dados_pd/lista_onibus_pascoa', 'w')
imprime_lista_onibus(onibusPascoa)
arquivo = open(f'{dirPrincipal}/dados_pd/lista_onibus_dom', 'w')
imprime_lista_onibus(onibusDomingo)
arquivo = open(f'{dirPrincipal}/dados_pd/lista_onibus_seg', 'w')
imprime_lista_onibus(onibusSegunda)
arquivo = open(f'{dirPrincipal}/dados_pd/lista_onibus_ter', 'w')
imprime_lista_onibus(onibusTerca)
arquivo = open(f'{dirPrincipal}/dados_pd/lista_onibus_qua', 'w')
imprime_lista_onibus(onibusQuarta)
arquivo = open(f'{dirPrincipal}/dados_pd/lista_onibus_qui', 'w')
imprime_lista_onibus(onibusQuinta)
arquivo = open(f'{dirPrincipal}/dados_pd/lista_onibus_sex', 'w')
imprime_lista_onibus(onibusSexta)
arquivo = open(f'{dirPrincipal}/dados_pd/lista_onibus_sab', 'w')
imprime_lista_onibus(onibusSabado)