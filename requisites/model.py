from PyQt5.QtCore import QObject
from PyQt5.QtSql import QSqlQueryModel
import sqlite3
import settings


INSERT = '''
    insert into Requisites ( object_of_building, city_for_testing, name_of_developer, requisites_of_developer, entity_builder, requisites_of_entity, project_preparer, requisites_of_project_preparer, project_inspection, requisites_of_project_inspection, project_infrastructureOps, requisites_of_infrastructureOps )
    values ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ) ;    
'''

class Model(QSqlQueryModel):

    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)

    def obnovit(self):
        sql = '''
        select object_of_building, city_for_testing, name_of_developer, requisites_of_developer, entity_builder, requisites_of_entity, project_preparer, requisites_of_project_preparer, project_inspection, requisites_of_project_inspection, project_infrastructureOps, requisites_of_project_infrastructureOps
        from Requisites ;
    '''
        self.setQuery(sql)
    
    def add(self, data):
        connection = sqlite3.connect(settings.bd_name)
        cursor = connection.cursor()
        cursor.execute(INSERT, data)
        connection.commit()
        connection.close()
