# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gestmodifclients.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(766, 513)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-180, -50, 1031, 561))
        self.label.setStyleSheet("background-image: url(:/newPrefix/v.jpg.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(70, 40, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("\n"
"color:white;\n"
"text-align:center;\n"
"padding:5px;\n"
"background-color: rgb(151, 164, 253);\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;")
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 160, 281, 41))
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
        self.pushButton_2.setGeometry(QtCore.QRect(190, 400, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 124, 10);\n"
"color:white;\n"
"\n"
"padding:5px;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 280, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 124, 10);\n"
"color:white;\n"
"\n"
"padding:5px;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_7.setText(_translate("Form", "GESTION DE MODIFICATION DES CLIENTS"))
        self.pushButton.setText(_translate("Form", "MODIFICATION D\'ADRESSE"))
        self.pushButton_2.setText(_translate("Form", "MODIFICATION DE MAIL"))
        self.pushButton_3.setText(_translate("Form", "MODIFICATION DE TELEPHONE"))
import zas_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())