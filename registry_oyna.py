from PyQt5.QtWidgets import *
from query import MySQL

class Registry_Window(QWidget):
    def __init__(self, oyna):
        super().__init__()

        self.main_oyna = oyna
        self.c = MySQL()

        self.v_main_lay = QVBoxLayout()
        self.h_btn_lay = QHBoxLayout()

        self.ism_edit = QLineEdit()
        self.ism_edit.setPlaceholderText("Ism...")

        self.fam_edit = QLineEdit()
        self.fam_edit.setPlaceholderText("Familiya...")

        self.yosh_edit = QLineEdit()
        self.yosh_edit.setPlaceholderText("Yosh...")

        self.back_btn = QPushButton("BACK", clicked=self.Back)
        self.submit_btn = QPushButton("SUBMIT", clicked=self.Submit)

        self.h_btn_lay.addWidget(self.back_btn)
        self.h_btn_lay.addWidget(self.submit_btn)

        self.v_main_lay.addWidget(self.ism_edit)
        self.v_main_lay.addWidget(self.fam_edit)
        self.v_main_lay.addWidget(self.yosh_edit)
        self.v_main_lay.addLayout(self.h_btn_lay)

        self.setLayout(self.v_main_lay)

    def Back(self):
        self.hide()
        self.main_oyna.show()

    def Submit(self):
        if self.ism_edit.text() and self.fam_edit.text() and self.yosh_edit.text():
            self.c.InsertTB(self.ism_edit.text(), self.fam_edit.text(), int(self.yosh_edit.text()))
            self.ism_edit.clear() 
            self.fam_edit.clear() 
            self.yosh_edit.clear()
