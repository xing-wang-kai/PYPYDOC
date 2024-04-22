import ast
import datetime
import os

def extract_docstrings(filename):
    """
    Extrai todas as docstrings de um arquivo Python e as armazena em um dicionário.

    Args:
        filename (str): O caminho do arquivo Python.

    Returns:
        dict: Um dicionário contendo as docstrings, onde as chaves são os nomes das funções e os valores são as docstrings.
        
    Author: [ Deusnir Portela]
    """
    docstrings_dict = {}

    with open(filename, 'r') as file:
        tree = ast.parse(file.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.body:
                docstring_node = node.body[0]
                if isinstance(docstring_node, ast.Expr) and isinstance(docstring_node.value, ast.Str):
                    docstrings_dict[node.name] = docstring_node.value.s
                else:
                    docstrings_dict[node.name] = None  # Se não houver docstring, armazena None

    return docstrings_dict

def take_values_from_doctring(docstrings_dict, func_name):
    """
    Esta função recebe o valor de um dicionário e então extrai os dados do dicionário 
    para converter em descrição e retorno da função, nome dos parametros em uma tupla, 
    typo dos parametros e também a descrição dos parametros
    Args:
        docstrings_dict (str) : recebe os values do dicionário no formato string.
        func_name (str) : retorna o nome da função coletada na função extract_docstring
        
    Returns:
        retorna um novo dicionário contendo todos dados necessário para documentação.
        
    Author: [ Deusnir Portela ]
    """
    

    fun_description = ''
    args_description = ''
    parameter_name = []
    parameter_type = []
    parameter_description = []
    fun_return = ''
    fun_author = ''
    
    docstring = str(docstrings_dict)
    
    

    parameters = []
    if 'Args:' in docstring:
        args_description = docstring.split('Args:')[1].split('Returns:')[0]
        parameters = args_description.split('\n')[1:-1]
        
        fun_description = docstring.split('Args:')[0].strip()
    else:
        fun_description = docstring.split('Returns:')[0].strip()
        
    if 'Returns:' in docstring:
        fun_return = docstring.split('Returns:')[1].split('Author:')[0].strip()
        
    if 'Author:' in docstring:    
        fun_author = docstring.split('Author:')[1].strip()

    if len(parameters) > 0:
    
        for args in parameters:
            args.strip()
            
            if args not in '':
                name = args.strip().split('(')[0]
                if name not in '':
                    parameter_name.append(args.strip().split('(')[0])
                    n_type = args.strip().split(r'(')[1].split(r")")[0]
                    parameter_type.append(args.strip().split(r'(')[1].split(r")")[0])
                    parameter_description.append(args.strip().split(':')[1]) 
    print('RODOU ATE O FINAL')
    return {
        "func_name": func_name,
        "fun_description": fun_description,
        "fun_parameters": {
            "parameter_name": parameter_name,
            "parameter_type": parameter_type,
            "parameter_description": parameter_description,    
        },
        "fun_return": fun_return,
        "fun_author" :fun_author
        
    }


def find_imports(file_path):
    """
    Identifica os imports presentes em um arquivo Python.

    Args:
        file_path (str): O caminho do arquivo Python.

    Returns:
        list: Uma lista contendo todos os imports encontrados no arquivo.
    """
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read())

    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            module = node.module
            for alias in node.names:
                imports.append(f"{module}.{alias.name}")

    return imports

def generate_md_documentation(filename, funcs_info, imports, author=None, company='Koder Solutions'):
    """
    Gera um documento Markdown contendo as docstrings, comentários e descrições de parâmetros extraídos do arquivo Python, 
    incluindo o nome do autor, o nome da empresa e a data/hora de criação.

    Args:
        filename (str): O nome do arquivo Python.
        funcs_info (list) : recebe uma lista contendo dicionários com toda documentação extraída das funções documento.
        imports (list) : recebe todos valores dos imports que contidos no arquivo.py
        author (str, optional): O nome do autor do código. Default é None.
        company (str, optional): O nome da empresa. Default é None.
    """
    # Obter a data/hora atual
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(filename.replace('.py', '') + '_documentation.md', 'w') as file:
        
        file.write("# Documentation for " + filename + "\n\n")  # Título principal
        file.write('##### COMPANY: ' + company +'\n')
        file.write('##### SECTOR: Data & Analytics Brasil\n\n')
        file.write("""
>este documento descreve as funcionabilidades de funções e server como auxilio para entendimento técnico,
>qualquer dúvida sujestão de melhorias ou reportar bugs busque pelo autor do código.
                   """)
        file.write("\n") 
        
        if author:
            file.write(f"**Author:** {author}\n\n")  
        
        file.write(f"**Date/Time:** {current_datetime}\n\n")
        file.write(f"----\n\n")
        
        file.write("# Índice\n\n")
        file.write("* [Important Imports:](#important-imports)\n")
        file.write("* [Functions of this code:](#functions-of-this-code)\n")
        for func in funcs_info:
            file.write(f"    + [{func['func_name']}](#{func['func_name']})\n")
        file.write(f"----\n\n") 
            
        file.write('## Important Imports: \n\n')
        file.write('Esses são uns dos recursos de bibliotescas usados para trabalhar com esse arquivo. \n')
        
        for imp in imports:
            file.write(f' * {imp}\n')
        
        file.write(f"----\n\n")
        file.write('## Functions of this code: \n')
        file.write("""
>Abaixo segue lista das funções usadas nesse programa, as função estão descritas conforme sua descrição,
>principais pâramtros, seus respectivos retornos e nome do autor da função.
                   """)
        file.write('\n\n')
        for func in funcs_info:

            file.write(f"### {func['func_name']}\n")
            
            file.write(f"#### Description\n")
            file.write(f"{func['fun_description']}\n\n")
             
            file.write("#### Parameters\n\n") 
            
            if len(func['fun_parameters']['parameter_name']) < 0:
                
                file.write(f"Essa função não recebe parametros\n")
            else:
                file.write("| Argument | Type | Description |\n")
                file.write("| -------- | ---- | ----------- |\n")
                
                for interator in range(0, len(func['fun_parameters']['parameter_name'])):
                    
                    file.write(f"| {func['fun_parameters']['parameter_name'][interator]} | {func['fun_parameters']['parameter_type'][interator]} | {func['fun_parameters']['parameter_description'][interator]} |\n")
            
            file.write("#### Returns\n\n")  
            file.write(f"{func['fun_return']}\n\n")
            
            file.write("#### function author\n\n")  
            file.write(f"{func['fun_author']}\n\n")
            

def execute_script_with_variables():
    """
    Essa função executa o código no console solicitando ao usuário informar as váriaveis necessárias para rodar o código.
    
    Returns: 
        Este código gera um arquivo markdown com documentação do código
    
    Author: Deusnir dos santos Portela
    """
    
    
    var_benvidos = """\033[33m
    
    
                           OLÁ BEM VINDO AO DOCUPY
    
           Essa biblioteca mapeia e documenta códigos em python e retorna 
           todas informaçõescontidas nas docstrings como descrições da
           função, descrição dos parametros, retornos, e autor.
                    
           Para que esse código rode de forma adequada é importante:
    
           Certifique-se que as docstring dentro do código python estejam
           dentro do padrão exigido para essa biblioteca
           1. precisa conter descrição das funções.
           2. precisa ter a palavra 'Args:' antes da explicação dos argumentos
           3. precisa ter os argumentos da no seguinte padrão:
                     nome (tipo) : decrição do argumento.
           4. para informar retorno precisa conter no docstring 'Returns:'
           5. Caso haja autor do código precisa conter 'Author:'
           
    Power By : Deusnir Portela.
    versão: 1.0.0
    
    
    \033[0m
    """
   
    print(var_benvidos)
    file_path = input("Digite o caminho do arquivo Python a ser executado: ")

    # Verificar se o arquivo existe
    if not os.path.isfile(file_path):
        print("Arquivo não encontrado!")
        return

    # Solicitar outras variáveis necessárias ao usuário
    # Por exemplo:
    author = input("Digite o nome do autor: ")
    
    # Executa as função de extrair documentação do arquivo .py e     
    docstrings = extract_docstrings(file_path)            
    all_documentation = []
    for function_name, docstring in docstrings.items():
        
        documentation = take_values_from_doctring(docstring, function_name)
        print('*'*100)
        print(f"""documentation:\n
                
                    "func_name": {documentation['func_name']},
                    "fun_description": {documentation['fun_description']},
                    "fun_parameters": 
                        "parameter_name": {documentation['fun_parameters']['parameter_name']},
                        "parameter_type": {documentation['fun_parameters']['parameter_type']},
                        "parameter_description": {documentation['fun_parameters']['parameter_description']},    
                    ,
                    "fun_return": {documentation['fun_return']},
                    "fun_author":{documentation['fun_author']}
                    
                
              """)
        print('*'*100)
        
        all_documentation.append(documentation)
    
    # coleta os imports da função .py
    imports = find_imports(file_path)
    
    #Gera o arquivo markdow
    generate_md_documentation(file_path, all_documentation,imports, author=author)
            
    print(""""\033[43m
           
               DOCUMENTO GERADO COM SUCESSO
           
          \033[0m""")

# Exemplo de uso:
if __name__ == "__main__":
    execute_script_with_variables()

    
    
