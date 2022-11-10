#-*- coding: utf-8 -*-

#Script é destinado a comparar duas feature class de endereços diferentes
#Se as features são iguais, é criado um novo registro com o nome das features em uma nova tabela no gdb
#A comparação entre as camadas envolve: tipo da feature; retangulo envolvente; número de registros; e a comparação da localização de cada registro
#Este script foi escrito com base no ArcGIS PRO, utiliza vertão python 3


import arcpy

bm = "E:\\LEONARDO\\Demandas\\ATIVIDADES_GERAIS_TEMPORARIAS\\MIGRACAO.gdb"
result = "E:\\LEONARDO\\Demandas\\ATIVIDADES_GERAIS_TEMPORARIAS\\MIGRACAO.gdb\\SDE_38_x_SDE_28"

#define a workspace de trabalho e cria uma lista para cada um dos datasets envolvidos
arcpy.env.workspace = bm #define a workspace em execução
datasetsbm = arcpy.ListDatasets() #cria uma lista dos datasets na workspace
for dataset in datasetsbm: #para cada dataset identificado na workspace
    desc = arcpy.Describe(dataset)  # descreve as características do dataset
    nomedataset = str(desc.name)  # salva o nome do dataset em uma variável, para usar a seguir
    if desc.name == 'SDE_38': #nome do dataset base de interesse
        featuresbase = arcpy.ListFeatureClasses(feature_dataset=dataset)
    elif desc.name == 'SDE_28': #nome do dataset teste de interesse
        featurestestagem = arcpy.ListFeatureClasses(feature_dataset=dataset)

#cria uma lista com o nome das camadas que já foram analisadas
existentes = [] #cria uma lista vazia
with arcpy.da.SearchCursor(result, "base") as cursor: #pesquisa no arquivo 'result', no campo 'base'
    for row in cursor: #em cada linha (o resulado aqui tem saido com paranteses
        for letra in row: #então faz um novo for, que o resultado tem ficado só o texto de interesse
            existentes.append(letra) #escreve o resultado na lista

prafazer = [] #cria uma lista vazia
for feature in featuresbase: #pra cada feature na lista de features do dataset base
    if feature in existentes: #se o nome da feature esta na lista das camadas que já foram analisadas
        print(feature + ": camada já existe no resultado") #escreve que a camada já foi analisada
    else: #se a feature não existe na lista de camadas que foram analisadas
        prafazer.append(feature) #essa feature é adiciona na lista para fazer
        print(feature + ": camada a ser analisada")

for i in prafazer:
    var = 0
    i_name = str(i)
    #print(i_name)
    #print(type(i_name))
    print("Camada em análise: " + i)
    descbase = arcpy.Describe(i)
    #print(descbase.shapeType)
    tipo_base = str(descbase.shapeType)
    extent_base = str(descbase.extent)
    #print(extent_base)
    rowsbase = arcpy.management.GetCount(i)
    for j in featurestestagem:
        print("Camada de teste: " + j)
        j_name = str(j)
        #print(j_name)
        #print(type(j_name))
        descteste = arcpy.Describe(j)
        tipo_teste = str(descteste.shapeType)
        if tipo_teste == tipo_base:
            extent_teste = str(descteste.extent)
            if extent_teste == extent_base:
                rowsteste = arcpy.management.GetCount(j)
                if int(str(rowsteste)) == int(str(rowsbase)):
                    sel = arcpy.management.SelectLayerByLocation(j, "ARE_IDENTICAL_TO", i, "", "NEW_SELECTION")
                    rowssel = arcpy.management.GetCount(sel)
                    arcpy.management.SelectLayerByAttribute(j, 'CLEAR_SELECTION')
                    if int(str(rowssel)) == int(str(rowsbase)):
                        print(descteste.shapeType, descbase.shapeType)
                        print(extent_teste)
                        print(extent_base)
                        print(rowsteste, rowsbase)
                        print(rowssel, rowsbase)
                        var = 1
                        print(i + " ; " + j + " ; camadas iguais")
                        new_linha = [i_name, j_name, "camadas iguais"]
                        campos = ["base", "teste", "situacao"]
                        with arcpy.da.InsertCursor(result, campos) as cursor_ok:
                            cursor_ok.insertRow(new_linha)
                        break
    if var == 0:
        print(i + " ; " + "; Camada sem correspondencia")
        new_linha = [i_name, "-", "camadas sem correspondencia"]
        campos = ["base", "teste", "situacao"]
        with arcpy.da.InsertCursor(result, campos) as cursor_ok:
            cursor_ok.insertRow(new_linha)