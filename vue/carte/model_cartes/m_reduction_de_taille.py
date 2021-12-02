# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reduction_de_taille.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(333, 354)
        Frame.setStyleSheet("#Frame{\n"
"background-color: rgba(196, 209, 97, 1);\n"
"border-top-right-radius: 20px ;\n"
"border-top-left-radius: 20px ;\n"
"border-bottom-right-radius: 20px ;\n"
"border-bottom-left-radius: 20px ;\n"
"}")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(60, 10, 201, 41))
        self.label.setStyleSheet("color : rgb(45, 111, 47);\n"
"font-weight: bold;\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 281, 191))
        self.label_2.setStyleSheet("border-radius: 40;\n"
"background-color:rgba(34, 255, 23, 0.5);")
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(Frame)
        self.frame.setGeometry(QtCore.QRect(-20, 270, 371, 61))
        self.frame.setStyleSheet("background-color:rgba(34, 255, 23, 0.5);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_reduction_taille = QtWidgets.QPushButton(self.frame)
        self.pushButton_reduction_taille.setGeometry(QtCore.QRect(50, 20, 75, 23))
        self.pushButton_reduction_taille.setStyleSheet("QPushButton#pushButton_reduction_taille{\n"
"    background-color: rgb(23,100,19);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#pushButton_reduction_taille:hover{\n"
"background-color: rgb(27, 27, 27);\n"
"}\n"
"")
        self.pushButton_reduction_taille.setObjectName("pushButton_reduction_taille")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:14pt;\">REDUCTION TAILLE</span></p></body></html>"))
        self.label_2.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Vous avez perdu </span></p><p align=\"center\"><span style=\" font-weight:600;\">temporairement votre emploi ! </span></p><p align=\"center\"><span style=\" font-weight:600;\">vous devez payer le </span></p><p align=\"center\"><span style=\" font-weight:600;\">montant des dépenses totales </span></p><p align=\"center\"><span style=\" font-weight:600;\">et perdre 2 tours. </span></p><p align=\"center\"><span style=\" font-weight:600;\">(Cela met fin à la effet de la charité.)</span></p></body></html>"))
        self.pushButton_reduction_taille.setText(_translate("Frame", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
