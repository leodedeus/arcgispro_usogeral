#-*- coding: utf-8 -*-

#Script é destinado a fazer uma cópia de uma feature class de um gdb
#para um novo gdb em outro endereço
#As feature class de interesse estão dentro de datasets
#Este script foi escrito com base no ArcGIS PRO, utiliza vertão python 3

import arcpy

base = "E:\\LEONARDO\\Demandas\\ATIVIDADES_GERAIS_TEMPORARIAS\\SDE_28.sde"
saida = "E:\\LEONARDO\\Demandas\\ATIVIDADES_GERAIS_TEMPORARIAS\\MIGRACAO.gdb\\SDE_28"

#definição do endereço do arquivo a ser copiado (base) e do endereço de saída (saida)
arcpy.env.workspace = base #define a workspace em execução
datasets = arcpy.ListDatasets() #cria uma lista dos datasets na workspace
for dataset in datasets: #para cada dataset identificado na workspace
    print("Dataset em análise: " + dataset)
    features = arcpy.ListFeatureClasses(feature_dataset=dataset)  #cria uma lista com as camadas que existem dentro do dataset
    for feature in features: #para cada camada identificada no dataset em questão
        desc2 = arcpy.Describe(feature) #descreve as características da camada
        nomefeature = str(desc2.name) #salva o nome da camada em uma variável
        for c in ".":
            nomefeature = nomefeature.replace(c,'_') #substitui caracter ponto (.) por underlyne (_) - operação usada no caso específico do trabalho
        print("Feature em cópia: " + nomefeature)
        arcpy.management.CopyFeatures(feature, saida + "\\" + nomefeature) #copia a camada para o banco local, com o mesmo nome de camada e dataset que existe na workspace