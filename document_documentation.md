# Documentation for document.py

##### COMPANY: Koder Solutions
##### SECTOR: Data & Analytics Brasil


>este documento descreve as funcionabilidades de funções e server como auxilio para entendimento técnico,
>qualquer dúvida sujestão de melhorias ou reportar bugs busque pelo autor do código.
                   
**Author:** Deusnir Portela
**Date/Time:** 2024-04-22 00:28:04

----

# Índice

* [Important Imports:](#important-imports)
* [Functions of this code:](#functions-of-this-code)
    + [extract_docstrings](#extract_docstrings)
    + [take_values_from_doctring](#take_values_from_doctring)
    + [find_imports](#find_imports)
    + [generate_md_documentation](#generate_md_documentation)
    + [execute_script_with_variables](#execute_script_with_variables)
----

## Important Imports: 

Esses são uns dos recursos de bibliotescas usados para trabalhar com esse arquivo. 
 * ast
 * datetime
 * os
----

## Functions of this code: 

>Abaixo segue lista das funções usadas nesse programa, as função estão descritas conforme sua descrição,
>principais pâramtros, seus respectivos retornos e nome do autor da função.
                   

### extract_docstrings
#### Description
Extrai todas as docstrings de um arquivo Python e as armazena em um dicionário.

#### Parameters

| Argument | Type | Description |
| -------- | ---- | ----------- |
| filename  | str |  O caminho do arquivo Python. |
#### Returns

dict: Um dicionário contendo as docstrings, onde as chaves são os nomes das funções e os valores são as docstrings.

#### function author

[ Deusnir Portela]

### take_values_from_doctring
#### Description
Esta função recebe o valor de um dicionário e então extrai os dados do dicionário 
    para converter em descrição e retorno da função, nome dos parametros em uma tupla, 
    typo dos parametros e também a descrição dos parametros

#### Parameters

| Argument | Type | Description |
| -------- | ---- | ----------- |
| docstrings_dict  | str |  recebe os values do dicionário no formato string. |
| func_name  | str |  retorna o nome da função coletada na função extract_docstring |
#### Returns

retorna um novo dicionário contendo todos dados necessário para documentação.

#### function author

[ Deusnir Portela ]

### find_imports
#### Description
Identifica os imports presentes em um arquivo Python.

#### Parameters

| Argument | Type | Description |
| -------- | ---- | ----------- |
| file_path  | str |  O caminho do arquivo Python. |
#### Returns

list: Uma lista contendo todos os imports encontrados no arquivo.

#### function author



### generate_md_documentation
#### Description
Gera um documento Markdown contendo as docstrings, comentários e descrições de parâmetros extraídos do arquivo Python, 
    incluindo o nome do autor, o nome da empresa e a data/hora de criação.

#### Parameters

| Argument | Type | Description |
| -------- | ---- | ----------- |
| filename  | str |  O nome do arquivo Python. |
| funcs_info  | list |  recebe uma lista contendo dicionários com toda documentação extraída das funções documento. |
| imports  | list |  recebe todos valores dos imports que contidos no arquivo.py |
| author  | str, optional |  O nome do autor do código. Default é None. |
| company  | str, optional |  O nome da empresa. Default é None. |
#### Returns



#### function author



### execute_script_with_variables
#### Description
Essa função executa o código no console solicitando ao usuário informar as váriaveis necessárias para rodar o código.

#### Parameters

| Argument | Type | Description |
| -------- | ---- | ----------- |
#### Returns

Este código gera um arquivo markdown com documentação do código

#### function author

Deusnir dos santos Portela

