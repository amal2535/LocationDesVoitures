# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'suppvage.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(583, 499)
        Dialog.setStyleSheet("background-color: rgb(214, 250, 222);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 40, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"color:white;\n"
"text-align:center;\n"
"background-color: rgb(255, 124, 10);\n"
"padding:5px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 190, 111, 41))
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
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 190, 111, 41))
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
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(210, 300, 141, 111))
        self.label_8.setStyleSheet("image: url(:/newPrefix/suppression.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Supprimer Voiture Agée(plus de 10 ans)"))
        self.pushButton.setText(_translate("Dialog", "Supprimer"))
        self.pushButton_2.setText(_translate("Dialog", "Annuler"))
import ggg_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
