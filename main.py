
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QPropertyAnimation,QEasingCurve
from login_1 import *
import sys,res_rc
#from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QMainWindow, QHeaderView

class MiApp(QtWidgets.QMainWindow):
  
     def __init__(self):
          ##DAMOS LAS CONFIGURACIONES PARA INTERACTUAR CON EL GUI.ui
          super().__init__()
          self.ui = Ui_Form()
          self.ui.setupUi(self)
          #loadUi('main.ui', self)

          #ELIMINAR BARRA TITULO - OPACIDAD
          self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
          self.setWindowOpacity(10)
          
          self.setAttribute(QtCore.Qt.WA_TranslucentBackground)#atributo para que el fondo del widget sea translúcido. 
          self.ui.pushButton_3.clicked.connect(lambda: self.close())

          #aplicar un efecto de sombra a un QLabel en una interfaz gráfica de usuario (GUI)
          self.ui.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0))
          self.ui.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=50, xOffset=0, yOffset=0))
          self.ui.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0))

          #SizeGrip CENTRO DE TODA PANTALLA
          self.gripSize = 10
          self.grip = QtWidgets.QSizeGrip(self)
          self.grip.resize(self.gripSize, self.gripSize)


         

if __name__=='__main__':
   app= QtWidgets.QApplication(sys.argv)
   mi_app = MiApp()
   mi_app.show()
   sys.exit(app.exec_())