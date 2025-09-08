from PyQt5.QtWidgets import *
from query import MySQL

class User_Window(QWidget):
    def __init__(self, oyna):
        super().__init__()

        self.main_window = oyna
        self.c = MySQL()

        self.v_main_lay = QVBoxLayout()

        self.lst_wdg = QListWidget()
        datalar = self.c.FirstQuery()
        if datalar:
            for i in datalar:
                # self.lst_wdg.addItem(str(i)[1:-1])
                self.lst_wdg.addItem(f"{i[0]} | {i[1]} {i[2]} {i[3]}")

        self.back_btn = QPushButton("BACK", clicked=self.Back)

        self.v_main_lay.addWidget(self.lst_wdg)
        self.v_main_lay.addWidget(self.back_btn)

        self.setLayout(self.v_main_lay)
    
    def Back(self):
        self.hide()
        self.main_window.show()
