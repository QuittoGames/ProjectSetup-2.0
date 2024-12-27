from dataclasses import dataclass

@dataclass
class config:
    FILES_PROGETS = ["index","data","tool"]

    FILES_PROGETS_WEB = {
        "index": ".html",
        "style": ".css",
        "js": ".js"
    }

    DIRETORIO = r"C:\Users\Gustavo Quitto\Downloads\Projects"

    DIRETORIO_WEB = r"C:\Users\Gustavo Quitto\Downloads\Projects"

    MESAGE_SCRIPT = "#Project created successfully!"

    MODULES = ["PyQt6"]

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
            <p>&copy; 2024 - Desenvolvido por Quitto</p>
        </footer>

    </body>
    </html>
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
