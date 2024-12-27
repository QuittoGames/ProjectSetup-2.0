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

    Verify_OS = lambda: platform.system()
#Project created successfully!