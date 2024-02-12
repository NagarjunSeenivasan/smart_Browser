import os
import sys

from PyQt5.QtCore import QSize, Qt, QUrl
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QDialog,
    QDialogButtonBox, 
    QFileDialog,
    QLabel,
    QLineEdit,
    QMainWindow,
    QToolBar,
    QVBoxLayout,
)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)
        
        # tag::navigation1[]
        navtb = QToolBar("Navigation")
        navtb.setIconSize(QSize(16, 16))
        self.addToolBar(navtb)
        
        #bookmark button
        bookmark_btn = QAction(QIcon(os.path.join("icons", "smiley.png")), "Bookmark", self)
        bookmark_btn.setStatusTip("add to bookmark")
        bookmark_btn.triggered.connect(self.add_bookmark)
        navtb.addAction(bookmark_btn)        
        navtb.addSeparator()

        # tag::menuBookmark[]   
        self.bookmark_menu = self.menuBar().addMenu("&Bookmark")        
        bookmark_select_action = QAction("http://google.com",self)
        bookmark_select_action.triggered.connect(self.navigate_bookmark)
        self.bookmark_menu.addAction(bookmark_select_action)
            
        self.show()

    
    # tag::bookmark[]    
    def add_bookmark(self):
        bookmark_title = self.browser.page().title()
        bookmark_url = self.browser.url().toString()
        bookmark_select_action = QAction(bookmark_url,self)
        bookmark_select_action.triggered.connect(self.navigate_bookmark)
        
        self.bookmark_menu.addAction(bookmark_select_action)
            
    
    # tag::navigationBookmark[]   
    def navigate_bookmark(self):
        action = self.sender()
        action_url = '"'+action.text()+'"'
        self.browser.setUrl(QUrl(action_url))  
        print(action_url)
        


app = QApplication(sys.argv)
app.setApplicationName("IIR")
app.setOrganizationName("IIR")
app.setOrganizationDomain("iir.org ")

window = MainWindow()

app.exec_()