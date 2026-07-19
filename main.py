import sys
from PyQt6 import QtWidgets,QtWebEngineWidgets,QtCore
app =QtWidgets.QApplication(sys.argv)

window=QtWidgets.QWidget()
window.setWindowTitle("retumilo")
#label = QtWidgets.QLabel("Hello World!",parent=window)
#label.setWindowTitle("retumilo")
#label.show()
index="https://www.google.com"
browser=QtWebEngineWidgets.QWebEngineView(parent=window)
browser.load(QtCore.QUrl(index))
back_page_button=QtWidgets.QPushButton("back")
#back_page_button.setGeometry(0,0,100,50)
forward_page_button=QtWidgets.QPushButton("forward")
reload_page_button=QtWidgets.QPushButton("reload")
enter_page_button=QtWidgets.QPushButton("enter")
search_input_line=QtWidgets.QLineEdit()
search_input_line.setPlaceholderText("search")
#url_input_line=QtWidgets.QLineEdit()
#input_line.setText("a")


back_page_button.clicked.connect(browser.back)
forward_page_button.clicked.connect(browser.forward)
reload_page_button.clicked.connect(browser.reload)
google="https://www.google.com/search?q="
duckduckgo="https://duckduckgo.com/?q="
bing="https://www.bing.com/search?q="
def load_page(engine,q):
    browser.load(QtCore.QUrl(engine+q))
enter_page_button.clicked.connect(lambda:load_page(google,search_input_line.displayText()))
search_input_line.returnPressed.connect(lambda:load_page(google,search_input_line.displayText()))
#url_input_line.returnPressed.connect(lambda:load_page(google,input_line.displayText()))

back_page_button.setFixedSize(50,20)
forward_page_button.setFixedSize(50,20)
reload_page_button.setFixedSize(50,20)
enter_page_button.setFixedSize(50,20)
search_input_line.setFixedSize(300,20)

bar_layout=QtWidgets.QVBoxLayout()
page_button_layout=QtWidgets.QHBoxLayout()
search_line_layout=QtWidgets.QHBoxLayout()
#b_layout.addWidget(back_page_button,alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
page_button_layout.addWidget(back_page_button)
page_button_layout.addWidget(forward_page_button)
page_button_layout.addWidget(reload_page_button)
page_button_layout.addStretch()
bar_layout.addLayout(page_button_layout)
search_line_layout.addWidget(search_input_line)
search_line_layout.addWidget(enter_page_button)
search_line_layout.addStretch()
bar_layout.addLayout(search_line_layout)
main_layout=QtWidgets.QVBoxLayout()
main_layout.addLayout(bar_layout)
#layout.addWidget(back_page_button)
#layout.addWidget(forward_page_button)
main_layout.addWidget(browser)
window.setLayout(main_layout)
window.move(0,0)
#window.resize(800,600)
window.show()
sys.exit(app.exec())
