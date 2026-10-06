import sys
from Pyside6.QtWidgets import QApplication, QMainWindow, QLabel

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minha primeira janela")
        self.resize(400, 250)

        rotulo = QLabel("Olá, Pyside6!", parent=self)
        self.setCentralWidget(rotulo)
        rotulo.setAlignment(from Pyside6.QtCore import Qt)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.show()
    sys.exit(app.exec())