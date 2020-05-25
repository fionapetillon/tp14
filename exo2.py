from PySide2.QtWidgets import *
class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("IHM")

        self.layout = QGridLayout()

        self.label = QLabel("Laisser un commentaire:")
        self.text = QTextEdit()
        self.button = QPushButton("Success")
        self.button2 = QPushButton("Exit")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button2)


        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication([])
    win = Window()
    win.show()
    app.exec_()
