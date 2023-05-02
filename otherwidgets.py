from PyQt5.QtWidgets import QMessageBox
def showDialog(self,str):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(str)
        msgBox.setWindowTitle("Message Error")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()
    
def showSuccess(self,str):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(str)
        msgBox.setWindowTitle("Success")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()