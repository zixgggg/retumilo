import sys
from PyQt6 import QtWidgets,QtWebEngineWidgets,QtCore
app =QtWidgets.QApplication(sys.argv)

window=QtWidgets.QWidget()
window.setWindowTitle("retumilo")
#label = QtWidgets.QLabel("Hello World!",parent=window)
#label.setWindowTitle("retumilo")
#label.show()
browser=QtWebEngineWidgets.QWebEngineView(parent=window)
browser.load(QtCore.QUrl("https://www.google.com"))
layout=QtWidgets.QVBoxLayout()
layout.addWidget(browser)
window.setLayout(layout)
window.move(0,0)
#window.resize(800,600)
window.show()
sys.exit(app.exec())
