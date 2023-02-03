# setar campo com valor default Null

import arcpy

#ler a variável de interesse
camada = "np_upar" 
# se estiver utilizando o terminal python do próprio arcgis, basta colocar o nome da camada como esta aqui
# se estiver utilizando alguma ide para escrever o código é preciso descrever o patch de onde o arquivo esta

#criar uma lista dos campos da camada de interesse
campos = arcpy.ListFields(camada)

#criar um laço de repetição para ler cada campo do arquivo
for campo in campos:
        #utiliza a ferramenta AssignDefaultToField com os argumentos: AssignDefaultToField(nome da camada, nome do campo, valor default)
        #como o valor default desejado é que o campo seja nulo, então basta escrever None, sem aspas, assim como é feito na calculadora de campo do arcgis
        arcpy.management.AssignDefaultToField(camada, campo.name, None)

#se a camada for vetorial é preciso desconsiderar os campos object id e shape
for campo in campos:
    if campo.type != 'OID' and campo.type != 'Geometry':
        arcpy.management.AssignDefaultToField(camada, campo.name, None)
        
#criar um laço de repetição para ler cada campo do arquivo
for campo in campos:
    #restringindo os campos de interesse aos que são do tipo texto
    if campo.type == 'String':
