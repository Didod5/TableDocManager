from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtSql import QSqlDatabase
import sys
import settings


class Application(QApplication):

    def __init__(self, argv):
        super().__init__(argv)
        db = QSqlDatabase.addDatabase('QSQLITE')
        if not settings.bd_name:
            file_dialog = QFileDialog.getOpenFileName(caption='Choose the file',
                                directory='db/', 
                                filter='DataBases(*.db)')
            bd_name = file_dialog[0]
            db.setDatabaseName(bd_name)
            with open('settings.py', 'w') as st:
                st.write(f'bd_name = "{bd_name}"')
        else:
            db.setDatabaseName(settings.bd_name)
        ok = db.open()
        if ok:
            print('connected to db', file=sys.stderr)
        else:
            print('connection failed', file=sys.stderr)
        