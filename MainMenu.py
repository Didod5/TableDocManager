from PyQt5.QtWidgets import QMenuBar


class MainMenu(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        help_menu = self.addMenu('&Справка')

        self.__about = help_menu.addAction('О программе...')
        self.about_qt = help_menu.addAction('About Qt')

        db_menu = self.addMenu('&База данных')
        self.create_db = db_menu.addAction('Создание')
        self.connect_db = db_menu.addAction('Подключение')
        self.delete_db = db_menu.addAction('Удаление')
    
    @property
    def about(self):
        return self.__about
    