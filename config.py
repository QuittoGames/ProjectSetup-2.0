from dataclasses import dataclass

@dataclass
class config:
    FILES_PROGETS = ["index","data","tool"]

    FILES_PROGETS_WEB = {
        "index": ".html",
        "style": ".css",
        "js": ".js"
    }

    DIRETORIO = r"D:\Projects\Python"

    DIRETORIO_WEB = r"D:\Projects\Web"
    
    MESAGE_SCRIPT = "#Project created successfully!"

    MODULES = ["PyQt6"]

    DATA_DIR = r"data\data_diretory.txt"

    TOOLS_CODE_BASE = """
import os
import platform
from dataclasses import dataclass

@dataclass
class tool:
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
    """
    DATA_CODE_BASE = """
from dataclasses import dataclass

@dataclass
class data:
    pass
    """

    HTML_CODE_BASE = """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
    <link rel="stylesheet" href="style.css"> <!-- Referência ao CSS -->
    <script src="js.js"></script> <!-- Referência ao JavaScript -->
</head>
<body>
    <footer>
        <p>&copy; 2025 - Desenvolvido por Quitto</p>
    </footer>

</body>
</html>
    """

    CODE_BASE_JAVA_MAIN = """import data.data;
    import  tool.tool;

    public class Main {
        tool tool_class = new tool();

        public static void main(String[] args) {
            System.out.println("Hello, World!");
        }
    }"""

    CODE_BASE_JAVA_TOOL = """package tool;

    public class tool {
    }
    """

    CODE_BASE_JAVA_DATA = """package data;

    public class data {
    }
    """

    CODE_BASE_CSS_STYLE = """:root {
    /* Tons de azul base modernos */
    --color-primary: #1e40af;     /* Azul escuro */
    --color-secondary: #3b82f6;   /* Azul médio (moderno) */
    --color-accent: #60a5fa;      /* Azul claro para destaque */
    
    /* Tons neutros e de fundo */
    --color-bg: #f9fafb;
    --color-surface: #ffffff;
    --color-text: #1f2937;        /* Quase preto */
    --color-muted: #6b7280;       /* Cinza para texto secundário */
  }
  
  body {
    margin: 0;
    padding: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  """

    FILE_EXTENSIONS = [
        ".py",   # Python
        ".java", # Java
        ".jar"
        ".c",    # C
        ".cpp",  # C++
        ".cs",   # C#
        ".rb",   # Ruby
        ".js",   # JavaScript
        ".ts",   # TypeScript
        ".php",  # PHP
        ".html", # HTML
        ".css",  # CSS
        ".swift",# Swift
        ".go",   # Go
        ".rs",   # Rust
        ".lua",  # Lua
        ".kt",   # Kotlin
        ".m",    # Objective-C
        ".h",    # Header files (C, C++)
        ".r",    # R
        ".pl",   # Perl
        ".vb",   # Visual Basic
        ".scala",# Scala
        ".sh",   # Shell Script
        ".sql",  # SQL
        ".dart", # Dart
        ".hs",   # Haskell
        ".erl",  # Erlang
        ".ex",   # Elixir
        ".clj",  # Clojure
        ".f",    # Fortran
        ".ml",   # OCaml
        ".bat",  # Batch File
        ".asm",  # Assembly
        ".v",    # Verilog
        ".vhd",  # VHDL
        ".groovy",# Groovy
        ".coffee",# CoffeeScript
        ".ps1",  # PowerShell
        ".rkt",  # Racket
        ".nim",  # Nim
        ".cr",   # Crystal
        ".fs",   # F#
        ".hx",   # Haxe
        ".tsx",  # TypeScript React (TSX)
        ".jsx",  # JavaScript React (JSX)
        ".ada",  # Ada
        ".lisp", # Lisp
        ".d",    # D
        ".julia",# Julia
        ".tcl",  # Tcl
        ".pro",  # Prolog
        ".bas",  # BASIC
        ".mjs",  # ES Module (JavaScript)
        ".cmake",# CMake
        ".nix",  # Nix
        ".rbi",  # Ruby Interface
        ".elm",  # Elm
        ".raku", # Raku (formerly Perl 6)
        ".m4",   # M4
        ".nimble", # Nimble (Nim Package)
        ".yang", # YANG
        ".xq",   # XQuery
        ".sml",  # Standard ML
        ".sbt",  # Scala Build Tool
        ".pm",   # Perl Module
        ".gd",   # GDScript (Godot Engine)
        ".glsl", # OpenGL Shading Language
        ".pig",  # Apache Pig
        ".oz",   # Oz
        ".matlab", # MATLAB
        ".maxmsp", # Max/MSP
        ".dsp",  # Digital Signal Processing
        ".site",
        ".dj",
    ]

    def Config_Diretorio(config_local,tool):
        tool.clear_screen()
        print("Configurações de Diretório:")
        print(f"Diretorio Padrao: {config_local.DIRETORIO}")
        print(f"Diretorio Web: {config_local.DIRETORIO_WEB}")
        print("1. Configurar Diretório Default")
        print("2. Configurar Diretório Web")
        print("3. Voltar")
        c =input("Digite Sua Opiçao: ")
        if c == "1":
            tool.Diretorio_Default(config_local=config_local)
            return
        elif c == "2":
            tool.Diretorio_Web(config_local=config_local)
            return
        elif c == "3":
            return
        
        
    def Config_Files(config_local,tool):
        tool.clear_screen()
        print("Configurações de Arquivos:")
        print(f"Files: {config_local.FILES_PROGETS}")
        print("1. Adicionar Arquivos")
        print("2. Remover Arquivos")
        print("3. Voltar")
        c =input("Digite Sua Opiçao: ")
        if c == "1":
            tool.Add_File(config_local=config_local)
            return
        elif c == "2":
            tool.Remove_File(config_local=config_local)
            return
        elif c == "3":
            return