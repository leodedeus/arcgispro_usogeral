#-*- coding: utf-8 -*-

#Script é destinado a fazer uma cópia de uma feature class de um gdb
#para um novo gdb em outro endereço
#As feature class de interesse não estão dentro de datasets
#Este script foi escrito com base no ArcGIS PRO, utiliza vertão python 3

import arcpy

#definição do endereço do arquivo a ser copiado (base) e do endereço de saída (saida)
base = "E:\\LEONARDO\\Demandas\\ATIVIDADES_GERAIS_TEMPORARIAS\\SDE_28.sde"
saida = "E:\\LEONARDO\\Demandas\\ATIVIDADES_GERAIS_TEMPORARIAS\\MIGRACAO.gdb\\SDE_28"

arcpy.env.workspace = base #define a workspace em execução

features = arcpy.ListFeatureClasses()  #cria uma lista com as camadas que existem dentro do dataset
for feature in features: #para cada camada identificada no dataset em questão
    desc2 = arcpy.Describe(feature) #descreve as características da camada
    nomefeature = str(desc2.name) #salva o nome da camada em uma variável
    for c in ".":
        nomefeature = nomefeature.replace(c,'_') #substitui caracter ponto (.) por underlyne (_) - operação usada no caso específico do trabalho
    print("Feature em cópia: " + nomefeature)
    arcpy.management.CopyFeatures(feature, saida + "\\" + nomefeature + "_28") #copia a camada para o banco local, com o mesmo nome de camada e dataset que existe na workspace
