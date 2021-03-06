# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'poursuite.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(340, 352)
        Frame.setStyleSheet("#Frame{\n"
"background-color: rgba(196, 209, 97, 1);\n"
"border-top-right-radius: 20px ;\n"
"border-top-left-radius: 20px ;\n"
"border-bottom-right-radius: 20px ;\n"
"border-bottom-left-radius: 20px ;\n"
"}\n"
"")
        self.frame = QtWidgets.QFrame(Frame)
        self.frame.setGeometry(QtCore.QRect(-10, 270, 371, 51))
        self.frame.setStyleSheet("background-color:rgba(34, 255, 23, 0.5);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_ok_poursuite = QtWidgets.QPushButton(self.frame)
        self.pushButton_ok_poursuite.setGeometry(QtCore.QRect(130, 10, 75, 23))
        self.pushButton_ok_poursuite.setStyleSheet("QPushButton#pushButton_ok_poursuite{\n"
"    background-color: rgb(23,100,19);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#pushButton_ok_poursuite:hover{\n"
"background-color: rgb(27, 27, 27);\n"
"}")
        self.pushButton_ok_poursuite.setObjectName("pushButton_ok_poursuite")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(80, 20, 181, 31))
        self.label.setStyleSheet("color : rgb(45, 111, 47);\n"
"font-weight: bold;\n"
"")
        self.label.setObjectName("label")
        self.label_poursuite = QtWidgets.QLabel(Frame)
        self.label_poursuite.setGeometry(QtCore.QRect(100, 90, 151, 131))
        self.label_poursuite.setObjectName("label_poursuite")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 271, 161))
        self.label_2.setStyleSheet("border-radius: 40px;\n"
"background-color:rgba(34, 255, 23, 0.5);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.frame.raise_()
        self.label.raise_()
        self.label_poursuite.raise_()

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton_ok_poursuite.setText(_translate("Frame", "OK"))
        self.label.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:22pt;\">POURSUITE</span></p></body></html>"))
        self.label_poursuite.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Vous etes poursuivis </span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">en justice donc </span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">vous allez perdre </span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">la moiti?? de votre cash</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
