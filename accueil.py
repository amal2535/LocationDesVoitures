# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accueil.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(873, 561)
        MainWindow.setStyleSheet("background-color: rgb(214, 250, 222);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -330, 981, 1091))
        self.label.setWhatsThis("")
        self.label.setStyleSheet("\n"
"image: url(:/newPrefix/image.png);\n"
"background-color: rgb(214, 250, 222);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 251, 41))
        self.pushButton.setStyleSheet("background-color: rgb(255, 160, 80);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"text-align:center;\n"
"padding:5px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 10, 251, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 160, 80);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"text-align:center;\n"
"padding:5px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 10, 251, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 160, 80);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"text-align:center;\n"
"padding:5px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 220, 171, 41))
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(156, 157, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"text-align:center;\n"
"padding:5px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 320, 171, 41))
        self.pushButton_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(156, 157, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"text-align:center;\n"
"padding:5px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(650, 470, 201, 41))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(800, 470, 31, 31))
        self.label_5.setStyleSheet("image: url(:/newPrefix/maj.JPG);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "GESTION DES VOITURES"))
        self.pushButton_2.setText(_translate("MainWindow", "GESTION DES LOCATIONS"))
        self.pushButton_3.setText(_translate("MainWindow", "GESTION DES CLIENTS"))
        self.pushButton_4.setText(_translate("MainWindow", "CONTRAT"))
        self.pushButton_5.setText(_translate("MainWindow", "FACTURE"))
        self.commandLinkButton_3.setText(_translate("MainWindow", "A PROPOS DE NOUS"))
import img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
