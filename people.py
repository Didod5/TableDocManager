from PyQt5.QtWidgets import QLabel, QLineEdit, QPlainTextEdit, QGridLayout, QWidget, QScrollArea
from PyQt5.QtCore import Qt


class People(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QGridLayout()
        self.scroll_widget = QWidget()
        self.scroll_widget.setLayout(self.layout)
        self.layout.setContentsMargins(400, 50, 400, 50)
        self.layout.setSpacing(40)


        self.setWidgetResizable(True)
        self.setWidget(self.scroll_widget)

        # 1 column
        self.label_0 = QLabel('Люди')
        self.add_widget_to_grid(self.label_0, 0, 0, 1, 3, alignment=Qt.AlignCenter)

        self.label_1 = QLabel('Представитель застройщика (технического заказчика, эксплуатирующей организации\n или регионального оператора) по вопросам строительного контроля')
        self.label_2 = QLabel('В случае осуществления строительства, реконструкции,\nкапитального ремонта на основании договора строительного подряда')
        self.add_widget_to_grid(self.label_1, 1, 0, 1, 3, alignment=Qt.AlignCenter)
        self.add_widget_to_grid(self.label_2, 2, 0, 1, 3, alignment=Qt.AlignCenter)

        self.layout.addWidget(QLabel('Должность'), 3, 0, alignment=Qt.AlignRight)
        self.layout.addWidget(QLabel('Фамилия И. О.'), 4, 0, alignment=Qt.AlignRight)
        self.layout.addWidget(QLabel('Идентификационный номер \nспециалиста в НРС и дата'), 5, 0, alignment=Qt.AlignRight)
        self.layout.addWidget(QLabel('Реквизиты распорядительного\n документа, подтверждающего\n полномочия'), 6, 0, alignment=Qt.AlignRight)
        self.layout.addWidget(QLabel('Наименование, ОГРН, ИНН, место\n нахождения юридического \nлица (В случае осуществления \nстроительного контроля на основании \nдоговора с застройщиком, техническим \nзаказчиком, эксплуатирующей организацией\n или региональным оператором)'),
                                7, 0, alignment=Qt.AlignRight)
        
        self.label_3 = QLabel('Представитель лица, осуществляющего строительство')
        self.add_widget_to_grid(self.label_3, 8, 0, 2, 3, alignment=Qt.AlignCenter)
        self.layout.addWidget(QLabel('Должность'), 10, 0, alignment=Qt.AlignRight)
        self.layout.addWidget(QLabel('Фамилия И. О.'), 11, 0, alignment=Qt.AlignRight)
        self.layout.addWidget(QLabel('Реквизиты распорядительного\nдокумента, подтверждающего\nполномочия'), 12, 0, alignment=Qt.AlignRight)
        self.layout.addWidget(QLabel('Наименование юридического лица'), 13, 0, alignment=Qt.AlignRight)

        self.label_4 = QLabel('Представитель лица, осуществляющего строительство,\nпо вопросам строительного контроля (специалист по \nорганизации строительства)')
        self.layout.addWidget(self.label_4, 14, 0, 2, 3, alignment=Qt.AlignCenter)
        self.layout.addWidget(QLabel('Должность'), 16, 0, alignment=Qt.AlignRight)
        self.layout.addWidget(QLabel('Фамилия И. О.'), 17, 0, alignment=Qt.AlignRight)
        self.layout.addWidget(QLabel('Идентификационный номер\nспециалиста в НРС и дата'), 18, 0, alignment=Qt.AlignRight)
        self.layout.addWidget(QLabel('Реквизиты распорядительного документа,\nподтверждающего полномочия'), 19, 0, alignment=Qt.AlignRight)
        self.layout.addWidget(QLabel('Наименование юридического лица'), 20, 0, alignment=Qt.AlignRight)
        
        self.label_5 = QLabel('\nПредставитель лица, осуществляющего подготовку проектной документации\n(в случаях когда авторский надзор осуществляется)')
        self.layout.addWidget(self.label_5, 21, 0, 2, 3, alignment=Qt.AlignCenter)
        self.layout.addWidget(QLabel('Должность'), 23, 0, alignment=Qt.AlignRight)
        self.layout.addWidget(QLabel('Фамилия И. О.'), 24, 0, alignment=Qt.AlignRight)
        self.layout.addWidget(QLabel('Реквизиты распорядительного документа,\nподтверждающего полномочия'),
                              25, 0, alignment=Qt.AlignRight)
        self.layout.addWidget(QLabel('Наименование, ОГРН, ИНН, место нахождения\n юридического лица (В случае \nосуществления авторского надзора\nлицом, не являющимся разработчиком \nпроектной документации)'),
                              26, 0, alignment=Qt.AlignRight)
        self.layout.addWidget(QLabel('Наименование, ОГРН, ИНН саморегулируемой \nорганизации, членом которой является\n указанное юридическое лицо \n(За исключением случаев, когда членство в \nсаморегулируемых организациях в области \nархитектурно-строительного проектирования \nне требуется)',),
                              27, 0, alignment=Qt.AlignRight)

        # 2 column
        self.construction_supervisor_job = QLineEdit()
        self.construction_supervisor_name = QLineEdit()
        self.construction_supervisor_id_and_date = QLineEdit()
        self.construction_supervisor_requisites_of_doc = QLineEdit()
        self.construction_supervisor_company = QPlainTextEdit()
        self.layout.addWidget(self.construction_supervisor_job, 3, 1)
        self.layout.addWidget(self.construction_supervisor_name, 4, 1)
        self.layout.addWidget(self.construction_supervisor_id_and_date, 5, 1)
        self.layout.addWidget(self.construction_supervisor_requisites_of_doc, 6, 1)
        self.layout.addWidget(self.construction_supervisor_company, 7, 1)

        self.builder_representative_job = QLineEdit()
        self.builder_representative_name = QLineEdit()
        self.builder_representative_requisites = QLineEdit()
        self.builder_representative_company = QLineEdit()
        self.layout.addWidget(self.builder_representative_job, 10, 1)
        self.layout.addWidget(self.builder_representative_name, 11, 1)
        self.layout.addWidget(self.builder_representative_requisites, 12, 1)
        self.layout.addWidget(self.builder_representative_company, 13, 1)

        self.construction_control_job = QLineEdit()
        self.construction_control_name = QLineEdit()
        self.construction_control_id_and_data = QLineEdit()
        self.construction_control_requisites = QLineEdit()
        self.construction_control_company = QLineEdit()
        self.layout.addWidget(self.construction_control_job, 16, 1)
        self.layout.addWidget(self.construction_control_name, 17, 1)
        self.layout.addWidget(self.construction_control_id_and_data, 18, 1)
        self.layout.addWidget(self.construction_control_requisites, 19, 1)
        self.layout.addWidget(self.construction_control_company, 20, 1)

        self.project_documentation_rep_job = QLineEdit()
        self.project_documentation_rep_name = QLineEdit()
        self.project_documentation_rep_requisites = QLineEdit()
        self.project_documentation_rep_company = QPlainTextEdit()
        self.project_documentation_rep_full_company = QPlainTextEdit()
        self.layout.addWidget(self.project_documentation_rep_job, 23, 1)         
        self.layout.addWidget(self.project_documentation_rep_name, 24, 1) 
        self.layout.addWidget(self.project_documentation_rep_requisites, 25, 1)         
        self.layout.addWidget(self.project_documentation_rep_company, 26, 1) 
        self.layout.addWidget(self.project_documentation_rep_full_company, 27, 1)
        

        # 3 column
        self.layout.addWidget(QLabel('Что получилось:'), 3, 2)

        self.layout.addWidget(QLabel('Что получилось:'), 10, 2)


    def add_widget_to_grid(self, widget, row, column, row_span=1, col_span=1, text='', alignment=None):
        if text:
            widget.setText(text)
        if alignment:
            self.layout.addWidget(widget, row, column, row_span, col_span, alignment)
        else:
            self.layout.addWidget(widget, row, column, row_span, col_span)    