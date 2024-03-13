import sqlite3


def create_db(bd_name):
    try:
        connection = sqlite3.connect(f'db/{bd_name}.db')
        cursor = connection.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Requisites (
        id INTEGER PRIMARY KEY,
        object_of_building TEXT,
        city_for_testing TEXT,
        name_of_developer TEXT,
        requisites_of_developer TEXT,
        entity_builder TEXT,
        requisites_of_entity TEXT,
        project_preparer TEXT,
        requisites_of_project_preparer TEXT,
        project_inspection TEXT,
        requisites_of_project_inspection TEXT, 
        project_infrastructureOps TEXT,
        requisites_of_infrastructureOps TEXT
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS People (
        id INTEGER PRIMARY KEY,
        construction_supervisor_job TEXT,
        construction_supervisor_name TEXT,
        construction_supervisor_id_and_date TEXT,
        construction_supervisor_requisites_of_doc TEXT,
        construction_supervisor_company TEXT,
        builder_representative_job TEXT,
        builder_representative_name TEXT,
        builder_representative_requisites TEXT,
        builder_representative_company TEXT,
        construction_control_job TEXT,
        construction_control_name TEXT,
        construction_control_id_and_data TEXT,
        construction_control_requisites TEXT,
        construction_control_company TEXT,
        project_documentation_rep_job TEXT,
        project_documentation_rep_name TEXT,
        project_documentation_rep_requisites TEXT,
        project_documentation_rep_company TEXT,
        project_documentation_rep_full_company TEXT,
        completed_work_representative_job TEXT,
        completed_work_representative_name TEXT,
        completed_work_representative_requisites TEXT,
        completed_work_representative_company TEXT,
        completed_work_representative_AOUSITO_job TEXT,
        completed_work_representative_AOUSITO_name TEXT,
        other_entity_1_job TEXT,
        other_entity_1_name TEXT,
        other_entity_1_requisites TEXT,
        other_entity_2_job TEXT,
        other_entity_2_name TEXT,
        other_entity_2_requisites TEXT,
        other_entity_3_job TEXT,
        other_entity_3_name TEXT,
        other_entity_3_requisites TEXT         
        )''')
    
        connection.commit()
    except sqlite3.Error as e:
        output = f"SQLite error: {e}"
        print(output)
    finally:
        connection.close()

def connect_db(file_name):
    try:
        connection = sqlite3.connect(file_name)
        cursor = connection.cursor()
        print('success')
        connection.close()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
