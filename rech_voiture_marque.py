# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rech_voiture_marque.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from otherwidgets import *
from ctrl_sais import *

class Ui_Form(object):
    def effacer(self):
        self.lineEdit.clear()
        self.textEdit.clear()
    def rech_marq(self):
        wb = load_workbook('test.xlsx')
        ws = wb.active
        n =  ws.max_row
        L1=[]
        row=[]
        m=self.lineEdit.text()
        row=recherche_marque1(m,n)
        if (len(row)==-1):
                showDialog(self,"Marque non existante")
        else:
                print(row)
                for j in row:
                    L1=(recherche_mar1(j))
                    print(L1)
                    s=' || '.join(L1)
                    self.textEdit.append(s)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(583, 500)
        Form.setStyleSheet("background-color: rgb(214, 250, 222);")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 120, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 25, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;\n"
"background-color: rgb(255, 116, 3);\n"
"text-align:center;\n"
"padding:5px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(200, 120, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 199, 121);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 180, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("\n"
"color:white;\n"
"background-color: rgb(255, 124, 10);\n"
"\n"
"padding:5px;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 180, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("\n"
"color:white;\n"
"background-color: rgb(255, 124, 10);\n"
"\n"
"padding:5px;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(500, 60, 71, 61))
        self.label_4.setStyleSheet("image: url(:/newPrefix/reche.jpg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 230, 531, 251))
        self.textEdit.setStyleSheet("background-color: rgb(255, 199, 121);")
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Marque:"))
        self.label.setText(_translate("Form", "Recherche voiture par Marque"))
        self.pushButton.setText(_translate("Form", "Rechercher"))
        self.pushButton.clicked.connect(self.rech_marq)
        self.pushButton_2.setText(_translate("Form", "Annuler"))
        self.pushButton_2.clicked.connect(self.effacer)
import kk_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
