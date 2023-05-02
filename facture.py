# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'facture.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(784, 541)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-10, -10, 811, 561))
        self.label.setStyleSheet("background-image: url(:/newPrefix/v.jpg.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(300, 20, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"color:white;\n"
"text-align:center;\n"
"background-color: rgb(255, 124, 10);\n"
"padding:5px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 130, 121, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 71, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(190, 360, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 12pt \"Showcard Gothic\";")
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(660, 460, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 199, 121);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(490, 490, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font: 87 12pt \"Segoe UI Black\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(30, 280, 71, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(430, 40, 31, 31))
        self.label_3.setStyleSheet("background-image: url(:/newPrefix/facture.JPG);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 470, 171, 41))
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(156, 157, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"text-align:center;\n"
"padding:5px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(350, 370, 161, 16))
        self.label_10.setStyleSheet("font: 10pt \"Segoe Print\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(170, 130, 141, 16))
        self.label_11.setStyleSheet("font: 10pt \"Segoe Print\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(160, 280, 141, 16))
        self.label_12.setStyleSheet("font: 10pt \"Segoe Print\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(160, 200, 141, 16))
        self.label_13.setStyleSheet("font: 8pt \"Segoe Print\";")
        self.label_13.setObjectName("label_13")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(270, 470, 171, 41))
        self.pushButton_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(156, 157, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"text-align:center;\n"
"padding:5px;")
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "FACTURE"))
        self.label_4.setText(_translate("Form", "Nom&Prénom:"))
        self.label_5.setText(_translate("Form", "Cin:"))
        self.label_7.setText(_translate("Form", "Montant à payer:"))
        self.label_8.setText(_translate("Form", "VOTRE SIGNATURE:"))
        self.label_9.setText(_translate("Form", "Matricule:"))
        self.pushButton_4.setText(_translate("Form", "ENREGISTRER"))
        self.label_10.setText(_translate("Form", "-----------(DINARS)"))
        self.label_11.setText(_translate("Form", "Mr X"))
        self.label_12.setText(_translate("Form", "XXX TN XXXX"))
        self.label_13.setText(_translate("Form", "XXXXXXXX"))
        self.pushButton_5.setText(_translate("Form", "ANNULER"))
import fse_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())