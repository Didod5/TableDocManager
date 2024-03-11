from PyQt5.QtWidgets import QLabel, QPlainTextEdit, QGridLayout, QWidget, QScrollArea
from PyQt5.QtCore import Qt


class RequisitesWidget(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QGridLayout()
        self.scroll_widget = QWidget()
        self.scroll_widget.setLayout(self.layout)
        self.layout.setContentsMargins(400, 20, 400, 50)

        self.setWidgetResizable(True)
        self.setWidget(self.scroll_widget)


        
        # 0 - 2 rows
        self.general_info = QLabel()
        self.object_of_building_0_label = QLabel()
        self.object_of_building = QPlainTextEdit()
        self.description_0 = QLabel()

        self.add_widget_to_grid(self.general_info, 0, 0, 1, 3,
                                'Общая информация', alignment=Qt.AlignCenter)
        self.add_widget_to_grid(self.object_of_building_0_label, 1, 0, 1, 3, 
                                text='Объект капитального строительства', alignment=Qt.AlignCenter)
        self.add_widget_to_grid(self.object_of_building, 2, 1)
        self.add_widget_to_grid(self.description_0, 2, 2, 
                                text=
'''Наименование проектной 
документации, почтовый или 
строительный адрес объекта
капитального строительства)''', alignment=Qt.AlignCenter)


        # 3nd row
        self.city_for_testing = QPlainTextEdit()
        self.description_1 = QLabel()
        
        self.add_widget_to_grid(self.city_for_testing, 3, 1)
        self.add_widget_to_grid(self.description_1, 3, 2,
                                text='Город для актов гидростатического\nили манометрического испытания\n на герметичность',
                                alignment=Qt.AlignCenter)
        

        # 4th row
        self.developer = QLabel()
        
        self.add_widget_to_grid(self.developer, 4, 0, 1, 3,
                                '\nЗастройщик (технический заказчик, эксплуатирующая организация или региональный оператор)', alignment=Qt.AlignCenter)
   

        # 5th and 6th row
        self.name_of_developer_label = QLabel()
        self.name_of_developer = QPlainTextEdit()
        self.developer_desc = QLabel()
        self.requisites_of_developer_label = QLabel()
        self.requisites_of_developer = QPlainTextEdit()


        self.add_widget_to_grid(self.name_of_developer_label, 5, 0, text='Наименование', alignment=Qt.AlignRight)
        self.add_widget_to_grid(self.name_of_developer, 5, 1, )
        self.add_widget_to_grid(self.developer_desc, 5, 2, 2, text=
'''Фамилия, имя, отчество,
адрес места жительства,
ОРГНИП, ИНН индивидуального
предпринимателя, наименование,
ОГРН, ИНН, место нахождения,
юридического лица, телефон/факс,
наименование, ОГРН, ИНН
саморегулируемой организации,
членом оторой является – для
 индивидуальных предпринимателей
и юридических лиц; фамилия, имя,
отчество, паспортные данные,
адрес места жительства,
телефон/факс - для физических лиц, 
не являющихся индивидуальными
предпринимателями''',
alignment=Qt.AlignRight)
        self.add_widget_to_grid(self.requisites_of_developer_label, 6, 0, text='Реквизиты', alignment=Qt.AlignRight)
        self.add_widget_to_grid(self.requisites_of_developer, 6, 1)


        # 7 - 8 rows
        self.entity = QLabel()
        self.add_widget_to_grid(self.entity, 7, 0, 2, 3, '\nЛицо, осуществляющее строительство',
                                alignment=Qt.AlignCenter)
        

        # 9 - 10 rows
        self.entity_builder_label = QLabel()
        self.entity_builder = QPlainTextEdit()
        self.requisites_of_entity_label = QLabel()
        self.requisites_of_entity = QPlainTextEdit()
        self.entity_builder_desc = QLabel()

        self.add_widget_to_grid(self.entity_builder_label, 9, 0, text='Наименование', alignment=Qt.AlignRight)
        self.add_widget_to_grid(self.entity_builder, 9, 1)
        self.add_widget_to_grid(self.requisites_of_entity_label, 10, 0, text='Реквизиты', alignment=Qt.AlignRight)
        self.add_widget_to_grid(self.requisites_of_entity, 10, 1)
        self.add_widget_to_grid(self.entity_builder_desc, 9, 2, 2, text=
'''Фамилия, имя, отчество, 
адрес места жительства,
ОРГНИП, ИНН индивидуального
предпринимателя, наименование, 
ОГРН, ИНН, место нахождения, 
юридического лица, телефон/факс, 
наименование, ОГРН,
ИНН саморегулируемой организации,
членом которой является''',
alignment=Qt.AlignCenter)


        # 11 - 13
        self.preparer = QLabel()
        self.project_preparer_label = QLabel()
        self.project_preparer = QPlainTextEdit()
        self.requisites_of_project_preparer_label = QLabel()
        self.requisites_of_project_preparer = QPlainTextEdit()
        self.project_preparer_desc = QLabel()

        self.add_widget_to_grid(self.preparer, 11, 0, 1, 3, text='\nЛицо, осуществляющее подготовку проектной документации',
                                alignment=Qt.AlignCenter)
        self.add_widget_to_grid(self.project_preparer_label, 12, 0, text='Наименование', alignment=Qt.AlignRight)
        self.add_widget_to_grid(self.project_preparer, 12, 1)
        self.add_widget_to_grid(self.requisites_of_project_preparer_label, 13, 0, text='Реквизиты', alignment=Qt.AlignRight)
        self.add_widget_to_grid(self.requisites_of_project_preparer, 13, 1)
        self.add_widget_to_grid(self.project_preparer_desc, 12, 2, 2, text=
'''Наименование, ОГРН, ИНН,
номер и дата выдачи свидетельства
 о допуске к видам работ по 
 строительству, реконструкции, 
 капитальному ремонту объектов 
 капитального строительства, 
 которые оказывают влияние на 
 безопасность объектов капитального 
 строительства, с указанием 
 саморегулируемой организации, 
 его выдавшей, почтовые реквизиты, 
 телефон/факс - для юридических лиц 
 и индивидуальных предпринимателей; 
 фамилия, имя, отчество, 
 паспортные данные, место проживания,
 телефон/факс - для физических лиц
''',
alignment=Qt.AlignCenter)

        # 14-16
        self.inspection = QLabel()
        self.project_inspection_label = QLabel()
        self.project_inspection = QPlainTextEdit()
        self.requisites_of_project_inspection_label = QLabel()
        self.requisites_of_project_inspection = QPlainTextEdit()
        self.project_inspection_desc = QLabel()

        self.add_widget_to_grid(self.inspection, 14, 0, 1, 3, text='\nЛицо, выполнившее работы, подлежащие освидетельствованию',
                                alignment=Qt.AlignCenter)
        self.add_widget_to_grid(self.project_inspection_label, 15, 0, text='Наименование', alignment=Qt.AlignRight)
        self.add_widget_to_grid(self.project_inspection, 15, 1)
        self.add_widget_to_grid(self.requisites_of_project_inspection_label, 16, 0, text='Реквизиты', alignment=Qt.AlignRight)
        self.add_widget_to_grid(self.requisites_of_project_inspection, 16, 1)
        self.add_widget_to_grid(self.project_inspection_desc, 15, 2, 2, text=
'''Наименование, ОГРН, ИНН,
номер и дата выдачи свидетельства
 о допуске к видам работ по 
 строительству, реконструкции, 
 капитальному ремонту объектов 
 капитального строительства, 
 которые оказывают влияние на 
 безопасность объектов капитального 
 строительства, с указанием 
 саморегулируемой организации, 
 его выдавшей, почтовые реквизиты, 
 телефон/факс - для юридических лиц 
 и индивидуальных предпринимателей; 
 фамилия, имя, отчество, 
 паспортные данные, место проживания,
 телефон/факс - для физических лиц''')
        
        # 17-19
        self.infrastructureOps = QLabel()
        self.infrastructureOps_label = QLabel()
        self.project_infrastructureOps = QPlainTextEdit()
        self.requisites_of_infrastructureOps_label = QLabel()
        self.requisites_of_infrastructureOps = QPlainTextEdit()
        self.infrastructureOps_desc = QLabel()

        self.add_widget_to_grid(self.infrastructureOps, 17, 0, 1, 3, text='\nОрганизация, осуществляющая эксплуатацию сетей инженерно-технического обеспечения',
                                alignment=Qt.AlignCenter)
        self.add_widget_to_grid(self.infrastructureOps_label, 18, 0, text='                                        Наименование',
                                alignment=Qt.AlignRight)
        self.add_widget_to_grid(self.project_infrastructureOps, 18, 1)
        self.add_widget_to_grid(self.requisites_of_infrastructureOps_label, 19, 0, text='Реквизиты', alignment=Qt.AlignRight)
        self.add_widget_to_grid(self.requisites_of_infrastructureOps, 19, 1)
        self.add_widget_to_grid(self.infrastructureOps_desc, 18, 2, 2, text=
'''Наименование, ОГРН, ИНН, место
нахождения, телефон/факс - для 
юридических лиц; ФИО, адрес места
жительства, ОРГНИП, ИНН 
индивидуального предпринимателя, 
телефон/факс - для индивидуальных
предпринимателей
''')

    def add_widget_to_grid(self, widget, row, column, row_span=1, col_span=1, text='', alignment=None):
        if text:
            widget.setText(text)
        if alignment:
            self.layout.addWidget(widget, row, column, row_span, col_span, alignment)
        else:
            self.layout.addWidget(widget, row, column, row_span, col_span)
