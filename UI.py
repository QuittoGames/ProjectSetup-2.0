from dataclasses import dataclass
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel,QLineEdit
from PyQt6.QtGui import QPixmap, QIcon, QFont
from PyQt6.QtCore import Qt

@dataclass
class dataUI:
    Font: str = "Segoe UI"


class UI:
    def create_btn(screm, txt, X, Y, A, L):
        BTN = QPushButton(txt, screm)
        BTN.setGeometry(X, Y, L, A)
        BTN.setStyleSheet("""
            QPushButton {
                background-color: #1E1E1E;          /* Fundo preto moderno */
                color: white;                       /* Texto branco */
                border-radius: 8px;                 /* Bordas arredondadas */
                font-size: 16px;                    /* Tamanho da fonte */
                font-family: Segoe UI, Arial, sans-serif;
                font-weight: 500;                   /* Fonte levemente destacada */
                border: 2px solid #3C3C3C;          /* Bordas cinzas escuras */
            }
            QPushButton:hover {
                background-color: #333333;          /* Fundo cinza mais claro */
                border: 2px solid #0078D4;          /* Azul sutil ao passar o mouse */
            }
            QPushButton:pressed {
                background-color: #292929;          /* Fundo cinza mais escuro ao clicar */
                border: 2px solid #005A9E;          /* Azul mais forte ao pressionar */
            }
        """)
        return BTN

    @staticmethod
    def create_text(screm, txt, x, y, font_size=20):
        Title = QLabel(txt, screm)
        Title.move(x, y)
        Title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        Title.setStyleSheet(f"""
            QLabel {{
                color: white;                      /* Texto branco */
                font-size: {font_size}px;          /* Tamanho da fonte */
                font-family: Segoe UI, Arial, sans-serif;
                font-weight: 600;                 /* Texto em negrito suave */
                border: none;                     /* Sem bordas */
                background-color: transparent;    /* Fundo transparente */
            }}
        """)
        return Title

    @staticmethod
    def create_window(resX, resY, Logo_path,Title):
        Window = QWidget()
        Window.resize(resX, resY)
        Window.setWindowTitle(Title)
        Window.setWindowIcon(QIcon(Logo_path))
        Window.setStyleSheet("""
            QWidget {
                background-color: #121212;          /* Fundo preto elegante */
                border-radius: 12px;                /* Bordas arredondadas modernas */
            }
        """)
        return Window

    def create_input(Txt,Screm):
        input = QLineEdit(Screm)
        input.setPlaceholderText(Txt)
        return input.text()
