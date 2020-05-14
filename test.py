from PySide2.QtWidgets import *
app = QApplication([])
mainWidget = QWidget()


layout = QVBoxLayout()


label = QLabel("Ceci est un QLabel")
button = QPushButton("Ceci est un QPushButton")
progressbar = QProgressBar()
dial = QDial()


layout.addWidget(label)
layout.addWidget(button)
layout.addWidget(progressbar)
layout.addWidget(dial)


mainWidget.setLayout(layout)


mainWidget.show()
app.exec_()

