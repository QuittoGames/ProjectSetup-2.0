from UI import UI
from tool import tool
from config import config 
import sys
import os
from time import sleep

config_local = config()

def Start():
    tool.clear_screen()
    print("1. Start Project")
    print("2. Create A WebSite")
    print("3. Start Django Project")
    print("4. Config")
    print("5. Exit")
    c = input("Digite Sua Opiçao: ")
    if c == "1":
        Start_Code()
        return
    elif c == "2":
        Web_Progect()
        return
    elif c == "3":
        Django_Project()
        return
    elif c == "4":
        Config_Main()
        return
    elif c == "5":
        return
    else:
        print("Comando Nao Pdoe Ser Idetificado! ")
        sleep(1)
        Start()
        return

def Start_Code():
    try:
        tool.clear_screen()
        Folder_Name = input("Digite o nome da pasta: ").strip()
        extetioin = input("Digite a extensão do seu projeto (por exemplo, .py): ").strip()

        if extetioin not in config.FILE_EXTENSIONS:
            print("Extensão não reconhecida!")
            Start()
            return

        path = os.path.join(config_local.DIRETORIO, Folder_Name)
        
        # Cria o diretório se não existir
        os.makedirs(path, exist_ok=True)
        
        # Cria os arquivos dentro do diretório
        for file in config_local.FILES_PROGETS:
            file_path = os.path.join(path, f"{file}{extetioin}")
            
            with open(file_path, 'w', encoding='utf-8') as arquivo:
                print(f"File: {file, extetioin}")
                if file == "tool":
                    arquivo.write(config_local.TOOLS_CODE_BASE)
                elif file == "data":
                    arquivo.write(config_local.DATA_CODE_BASE)

                arquivo.write(config_local.MESAGE_SCRIPT)
        print(f"Todos os arquivos foram criados com sucesso no diretório '{path}'.")
        sleep(5)
        Start()
        return
    except Exception as E:
        print(f"Erro Al Criar Proejto: {E}")
        return

def Web_Progect():
    try:
        tool.clear_screen()
        Folder_Name = input("Digite o nome da pasta: ").strip()
        path = os.path.join(config_local.DIRETORIO_WEB, Folder_Name)

        os.makedirs(path, exist_ok=True)

        for file, extetioin in config_local.FILES_PROGETS_WEB.items():
            file_path = os.path.join(path, f"{file}{extetioin}")
            
            with open(file_path, 'w', encoding='utf-8') as arquivo:
                print(f"File: {file, extetioin}")
                if file == "index":
                    arquivo.write(config.HTML_CODE_BASE)

        print(f"Todos os arquivos foram criados com sucesso no diretório '{path}'.")
        sleep(5)
        Start()
        return
    except Exception as E:
        print(f"Erro Al Criar Site: {E}")
        return

def Django_Project():
    try:
        if not tool.Install_Django():
            Start()
            return
        tool.clear_screen()
        Folder_Name = input("Digite o nome da pasta: ").strip()

        os.system(f"cd {config_local.DIRETORIO}")
        file_path = os.path.join(config_local.DIRETORIO)
        os.system(f"django-admin startproject {Folder_Name}")

        sleep(1)
        tool.clear_screen()
        print(f"Projeto Criado Com Susseso! Project Name: {Folder_Name}")
        sleep(5)
        Start()
        return
    except:
        print("Erro Al Criar Projeto! ")
        sleep(2)
        Start()
        return

        #test push 

def Config_Main():
    try:
        tool.clear_screen()
        print("1. Configurações de Diretório")
        print("2. Configurações de Arquivos")
        print("4. Voltar")
        c = input("Digite Sua Opiçao: ")
        if c == "1":
            config.Config_Diretorio(config_local,tool=tool)
            Config_Main()
            return
        elif c == "2":
            config.Config_Files(config_local=config_local,tool=tool)
            Config_Main()
            return
        elif c == "4":
            Start()
            return
        else:
            print("Comando Nao Pdoe Ser Idetificado! ")
            sleep(1)
            Config_Main()
            return
    except Exception as E:
        print(f"Erro Al Configurar! {E} ")
        sleep(2)
        Start()
        return


if __name__ == "__main__":
    tool.verify_modules()
    Start()