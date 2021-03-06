# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rolldice.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(381, 376)
        Frame.setStyleSheet("#Frame{\n"
"background-color: rgba(196, 209, 97, 1);\n"
"border-top-right-radius: 20px ;\n"
"border-top-left-radius: 20px ;\n"
"border-bottom-right-radius: 20px ;\n"
"border-bottom-left-radius: 20px ;\n"
"}")
        self.frame = QtWidgets.QFrame(Frame)
        self.frame.setGeometry(QtCore.QRect(-10, 300, 461, 51))
        self.frame.setStyleSheet("background-color:rgba(34, 255, 23, 0.5);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_rolldice = QtWidgets.QPushButton(self.frame)
        self.pushButton_rolldice.setGeometry(QtCore.QRect(50, 10, 81, 21))
        self.pushButton_rolldice.setStyleSheet("QPushButton#pushButton_rolldice{\n"
"    background-color: rgb(23,100,19);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#pushButton_rolldice:hover{\n"
"background-color: rgb(27, 27, 27);\n"
"}")
        self.pushButton_rolldice.setObjectName("pushButton_rolldice")
        self.pushButton_payer_rolldice = QtWidgets.QPushButton(Frame)
        self.pushButton_payer_rolldice.setGeometry(QtCore.QRect(40, 260, 81, 21))
        self.pushButton_payer_rolldice.setStyleSheet("QPushButton#pushButton_payer_rolldice{\n"
"    background-color: rgb(23,100,19);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#pushButton_payer_rolldice:hover{\n"
"border-color: red; \n"
"background-color: rgb(27, 27, 27);\n"
"}")
        self.pushButton_payer_rolldice.setObjectName("pushButton_payer_rolldice")
        self.pushButton_emprunter_rolldice = QtWidgets.QPushButton(Frame)
        self.pushButton_emprunter_rolldice.setGeometry(QtCore.QRect(240, 260, 101, 21))
        self.pushButton_emprunter_rolldice.setStyleSheet("QPushButton#pushButton_emprunter_rolldice{\n"
"    background-color: rgb(23,100,19);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#pushButton_emprunter_rolldice:hover{\n"
"background-color: rgb(27, 27, 27);\n"
"width : 60px;\n"
"height : 60px;\n"
"}")
        self.pushButton_emprunter_rolldice.setObjectName("pushButton_emprunter_rolldice")
        self.label_rolldice = QtWidgets.QLabel(Frame)
        self.label_rolldice.setGeometry(QtCore.QRect(50, 90, 291, 141))
        self.label_rolldice.setObjectName("label_rolldice")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(120, 20, 191, 31))
        self.label.setStyleSheet("color : rgb(45, 111, 47);\n"
"font-weight: bold;\n"
"")
        self.label.setObjectName("label")
        self.label_marche = QtWidgets.QLabel(Frame)
        self.label_marche.setGeometry(QtCore.QRect(40, 70, 301, 181))
        self.label_marche.setStyleSheet("border-radius: 40px;\n"
"background-color:rgba(34, 255, 23, 0.5);\n"
"\n"
"QLabel#label_marche:hover{\n"
"border-color: red; \n"
"background-color: rgb(27, 27, 27);\n"
"}\n"
"")
        self.label_marche.setText("")
        self.label_marche.setObjectName("label_marche")
        self.label_marche.raise_()
        self.frame.raise_()
        self.pushButton_payer_rolldice.raise_()
        self.pushButton_emprunter_rolldice.raise_()
        self.label_rolldice.raise_()
        self.label.raise_()

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton_rolldice.setText(_translate("Frame", "ROLL"))
        self.pushButton_payer_rolldice.setText(_translate("Frame", "PAYER"))
        self.pushButton_emprunter_rolldice.setText(_translate("Frame", "empreinter"))
        self.label_rolldice.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">c\'est votre tour, ?? vous de jouez,</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">entre temps vous pouvez</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">emprunter ou rembourser vos dettes</span></p></body></html>"))
        self.label.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:22pt;\">ROLL DICE</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
