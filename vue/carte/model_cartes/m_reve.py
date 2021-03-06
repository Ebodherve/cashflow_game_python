# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reve.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(361, 356)
        Frame.setStyleSheet("#Frame{\n"
"background-color: rgba(196, 209, 97, 1);\n"
"border-top-right-radius: 20px ;\n"
"border-top-left-radius: 20px ;\n"
"border-bottom-right-radius: 20px ;\n"
"border-bottom-left-radius: 20px ;\n"
"}\n"
"")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(120, 20, 101, 31))
        self.label.setStyleSheet("color : rgb(45, 111, 47);\n"
"font-weight: bold;\n"
"")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Frame)
        self.frame.setGeometry(QtCore.QRect(-10, 270, 371, 51))
        self.frame.setStyleSheet("background-color:rgba(34, 255, 23, 0.5);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_achetez_reve = QtWidgets.QPushButton(self.frame)
        self.pushButton_achetez_reve.setGeometry(QtCore.QRect(50, 10, 75, 23))
        self.pushButton_achetez_reve.setStyleSheet("QPushButton#pushButton_achetez_reve{\n"
"    background-color: rgb(23,100,19);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#pushButton_achetez_reve:hover{\n"
"background-color: rgb(27, 27, 27);\n"
"}")
        self.pushButton_achetez_reve.setObjectName("pushButton_achetez_reve")
        self.pushButton_passer_reve = QtWidgets.QPushButton(self.frame)
        self.pushButton_passer_reve.setGeometry(QtCore.QRect(250, 10, 75, 23))
        self.pushButton_passer_reve.setStyleSheet("QPushButton#pushButton_passer_reve{\n"
"    background-color: rgb(23,100,19);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#pushButton_passer_reve:hover{\n"
"background-color: rgb(27, 27, 27);\n"
"}")
        self.pushButton_passer_reve.setObjectName("pushButton_passer_reve")
        self.label_reve = QtWidgets.QLabel(Frame)
        self.label_reve.setGeometry(QtCore.QRect(50, 110, 251, 111))
        self.label_reve.setWordWrap(True)
        self.label_reve.setObjectName("label_reve")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 271, 171))
        self.label_2.setStyleSheet("border-radius: 40px;\n"
"background-color:rgba(34, 255, 23, 0.5);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.frame.raise_()
        self.label_reve.raise_()

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:22pt;\">REVES</span></p></body></html>"))
        self.pushButton_achetez_reve.setText(_translate("Frame", "Achetez"))
        self.pushButton_passer_reve.setText(_translate("Frame", "Passer"))
        self.label_reve.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">achetez votre reve si vous </span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">avez assez d\'argent</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
