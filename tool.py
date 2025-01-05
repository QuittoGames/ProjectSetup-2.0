import os
import platform
from dataclasses import dataclass
from time import sleep
from config import config


@dataclass
class tool:
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    def Install_Django():
        try:
            if platform.system() == "Windows": 
                os.system("py -m pip install Django")
                return True
            else:
                os.system("python -m pip install Django")
                return True
        except:
            print("Nao Foi Possivel Intalar Ou Atalizar O Django")
            sleep(2)
            return False
    
    
    def verify_modules():
        for i in config.MODULES:
            os.system(f"pip3 install {i}")
            tool.clear_screen()

    def Diretorio_Default(config_local):
        try:
            tool.clear_screen()
            New_Dir = input(r"Digite a Diretorio: ")
            if str(New_Dir).lower().strip() == "":
                print("Dir Nao Pode Ser Aceita!")
                sleep(1)
                return
            config_local.DIRETORIO = New_Dir
            print(f"Diretorio Atalizado Com Susseso!, Diretorio Atual: {config_local.DIRETORIO}")
            return
        except Exception as e:
            print(f"Erro ao Dir: {e}")

    def Diretorio_Web(config_local):
        try:
            tool.clear_screen()
            New_Dir = input(r"Digite a Diretorio: ")
            if str(New_Dir).lower().strip() == "":
                print("Diretorio Nao Pode Ser Aceita!")
                sleep(1)
                return
            config_local.DIRETORIO = New_Dir
            print(f"Diretorio Atalizado Com Susseso!, Diretorio Atual: {config_local.DIRETORIO_WEB}")
            return
        except Exception as e:
                print(f"Erro ao adicionar arquivo: {e}")
    
    def Add_File(config_local):
        try:
            tool.clear_screen()
            File_Name = input("Digite o Nome Do Arquivo: ")
            if str(File_Name).lower().strip() == "":
                print("Nome Nao Pode Ser Aceito!")
                sleep(1)
                return
            config_local.FILES_PROGETS.append(File_Name)
            print(f"Arquivo Adicionado Com Susseso!, Arquivo Atual: {config_local.FILES_PROGETS}")
        except Exception as e:
            print(f"Erro ao adicionar arquivo: {e}")
        return
    
    def Remove_File(config_local):
        try:
            tool.clear_screen()
            File_Name = input("Digite o Nome Do Arquivo: ")
            if str(File_Name).lower().strip() == "":
                print("Nome Nao Pode Ser Aceito!")
                sleep(1)
                return
            if str(File_Name) not in config_local.FILES_PROGETS:
                print("Arquivo Nao Encontrado!")
                sleep(1)
                return
            else:
                config_local.FILES_PROGETS.remove(File_Name)
                print(f"Arquivo Removido Com Susseso!, Arquivo Atual: {config_local.FILES_PROGETS}")
        except Exception as e:
            print(f"Erro ao remover arquivo: {e}")
        return

    Verify_OS = lambda: platform.system()
#Project created successfully!