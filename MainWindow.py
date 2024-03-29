from PyQt5.QtWidgets import (
    QMainWindow,
    QMessageBox,
    QTabWidget,
    QWidget,
    QVBoxLayout
    )
from MainMenu import MainMenu
from PyQt5.QtCore import pyqtSlot
from requisites import RequisitesWidget
from people import People


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        
        main_menu = MainMenu(parent=self)
        self.setMenuBar(main_menu)

        main_menu.about.triggered.connect(self.about)
        main_menu.about_qt.triggered.connect(self.about_qt)

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
