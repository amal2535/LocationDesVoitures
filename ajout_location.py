# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ajout_location.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from otherwidgets import *
from ctrl_cli import *
from location import *


class Ui_Form(object):
    def effacer(self):

        self.lineEdit_2.clear()
        self.lineEdit_7.clear()
        self.lineEdit_3.clear()
        self.lineEdit_5.clear()
        self.lineEdit_4.clear()
        self.lineEdit_6.clear()
    def remplir(self):
        age='0'
        cin='00000000'
        tel='00000000'
        L=[]
        cp=0
        Num_loc='-1'
        Num_loc = self.lineEdit_7.text()
        cin = self.lineEdit_10.text()
        nom = self.lineEdit_9.text()
        matricule = self.lineEdit_13.text()
        duree = self.lineEdit_8.text()
        tel = self.lineEdit_11.text()
        dat = self.lineEdit_12.text()
        prix = self.lineEdit_14.text()
        
        if(int(Num_loc)<0):
            showDialog(self,"NUM loc Invalide")
        elif(lecture(Num_loc)):
             showDialog(self,"NUM loc Invalide")
        else:
            cp+=1
        
        if (cin.isdigit()) and (cin[0]=='1' or cin[0]=='0') and len(cin)==8:
            cp+=1
        else:
            showDialog(self,"CIN Invalide")
        
        if np(nom):
            cp+=1
        else:
            showDialog(self,"Nom Invalide")
                    
        if (tel.isdigit()and (len(tel)==8) and ((orange(tel)) or (Telec(tel)) or (ooredoo(tel)) or (ellisa(tel)))):
            cp+=1
        else:
            showDialog(self,"Numero de Telephone Invalide")
        
        if (date(dat)):
            cp+=1
        else:
            showDialog(self,"Date Invalide")
            
        if(int(prix)>60):
            cp+=1
        else:
            showDialog(self,"Prix Invalide")
        
        if(cp>=6):
                ecrire(cin)
                L=[Num_loc,cin,nom,matricule,duree,tel,dat,prix]
                remplir_csl(L)
                showSuccess(self,"Successful")
        else:
                showDialog(self,"Restart")
        
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(598, 554)
        Form.setStyleSheet("background-color: rgb(214, 250, 222);")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 10, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;\n"
"text-align:center;\n"
"background-color: rgb(255, 124, 10);\n"
"padding:5px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(310, 100, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(310, 150, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(290, 200, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(100, 100, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 199, 121);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(390, 100, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("background-color: rgb(255, 199, 121);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(100, 200, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setStyleSheet("background-color: rgb(255, 199, 121);")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(Form)
        self.lineEdit_10.setGeometry(QtCore.QRect(100, 150, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setStyleSheet("background-color: rgb(255, 199, 121);")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(Form)
        self.lineEdit_11.setGeometry(QtCore.QRect(390, 150, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setStyleSheet("background-color: rgb(255, 199, 121);")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(Form)
        self.lineEdit_12.setGeometry(QtCore.QRect(390, 200, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setStyleSheet("background-color: rgb(255, 199, 121);")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 250, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(310, 250, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_13 = QtWidgets.QLineEdit(Form)
        self.lineEdit_13.setGeometry(QtCore.QRect(100, 250, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setStyleSheet("background-color: rgb(255, 199, 121);")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(Form)
        self.lineEdit_14.setGeometry(QtCore.QRect(390, 250, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setStyleSheet("background-color: rgb(255, 199, 121);")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 350, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 124, 10);\n"
"color:white;\n"
"\n"
"padding:5px;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 350, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color:white;\n"
"background-color: rgb(255, 124, 10);\n"
"padding:5px;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(190, 310, 211, 171))
        self.label_10.setStyleSheet("image: url(:/newPrefix/loca.jpg);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "CIN:"))
        self.label_4.setText(_translate("Form", "Nom:"))
        self.label.setText(_translate("Form", "Ajouter Location"))
        self.label_3.setText(_translate("Form", "Numéro:"))
        self.label_6.setText(_translate("Form", "Durée:"))
        self.label_7.setText(_translate("Form", "Numéro:"))
        self.label_8.setText(_translate("Form", "Date prevue:"))
        self.label_5.setText(_translate("Form", "Matricule:"))
        self.label_9.setText(_translate("Form", "Montant:"))
        self.pushButton.setText(_translate("Form", "Enregistrer"))
        self.pushButton.clicked.connect(self.remplir)
        self.pushButton_2.setText(_translate("Form", "Annuler"))
        self.pushButton_2.clicked.connect(self.effacer)
import loca_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
