# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rechercheclients.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(790, 506)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-60, 0, 881, 511))
        self.label.setStyleSheet("background-image: url(:/newPrefix/v.jpg.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(240, 60, 321, 61))
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
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 210, 171, 41))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 212, 138);\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"text-align:center;\n"
"padding:5px;")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_7.setText(_translate("Form", "RECHERCHE DES CLIENTS"))
        self.pushButton_2.setText(_translate("Form", "PAR CIN"))
import trr_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())