from PyQt5.QtWidgets import (
    QMainWindow,
    QMessageBox,
    QTabWidget,
    QWidget,
    QVBoxLayout,
    QInputDialog
    )
from MainMenu import MainMenu
from PyQt5.QtCore import pyqtSlot
from requisites import RequisitesWidget
from people import People
from db.db import create_db as cb
import os


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        
        main_menu = MainMenu(parent=self)
        self.setMenuBar(main_menu)

        main_menu.about.triggered.connect(self.about)
        main_menu.about_qt.triggered.connect(self.about_qt)

        main_menu.create_db.triggered.connect(self.create_db)


        central_field = QWidget(self)
        tab_widget = QTabWidget(central_field)

        tab_1 = RequisitesWidget()
        tab_widget.addTab(tab_1, 'Реквизиты')


        tab_2 = People()
        tab_widget.addTab(tab_2, 'Люди')

        self.setCentralWidget(central_field)

        main_layout = QVBoxLayout(central_field)
        main_layout.addWidget(tab_widget)
        

    @pyqtSlot()
    def about(self):
        title = 'autogen'
        text = "Менеджер составления исполнительных актов"
        QMessageBox.about(self, title, text)

    @pyqtSlot()
    def about_qt(self):
        QMessageBox.aboutQt(self, 'Автоген')

    @pyqtSlot()
    def create_db(self):
        try:
            msg = QMessageBox()
            status = 1
            while status:
                bd_name, status = QInputDialog.getText(self, '', 'Enter the name:' , text='project')
                if not bd_name:
                    msg.setText('The name is too short')
                    msg.exec_()
                    continue
                elif status:            
                    if os.path.exists(f'db/{bd_name}.db'):
                        msg.setText('File with this name already exists')
                    else:
                        cb(bd_name)
                        msg.setText('Successfully created')
                        status = 0
                    msg.exec_()
            
        except Exception as ex:
            print('MainWindow', ex)
