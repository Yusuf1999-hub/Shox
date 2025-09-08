from PyQt5.QtWidgets import *
from registry_oyna import Registry_Window
from all_user_oyna import User_Window

class Main_Window(QWidget):
    def __init__(self):
        super().__init__()

        self.v_main_lay = QVBoxLayout()
        
        self.registry_btn = QPushButton("REGISTRY", clicked=self.Registry)
        self.all_user_btn = QPushButton("USERS", clicked=self.Users)
        self.exit_btn = QPushButton("EXIT", clicked=exit)


        self.v_main_lay.addWidget(self.registry_btn)
        self.v_main_lay.addWidget(self.all_user_btn)
        self.v_main_lay.addWidget(self.exit_btn)

        self.setLayout(self.v_main_lay)
    
    def Registry(self):
        self.hide()
        self.r_oyna = Registry_Window(self)
        self.r_oyna.show()

    def Users(self):
        self.hide()
        self.u_oyna = User_Window(self)
        self.u_oyna.show()