# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bebe.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(396, 373)
        Frame.setStyleSheet("\n"
"#Frame{\n"
"\n"
"background-color: rgba(196, 209, 97, 1);\n"
"border-radius: 30px ;\n"
"}")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(150, 10, 91, 41))
        self.label.setStyleSheet("color : rgb(45, 111, 47);\n"
"font-weight: bold;\n"
"")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Frame)
        self.frame.setGeometry(QtCore.QRect(-30, 280, 441, 51))
        self.frame.setStyleSheet("background-color:rgba(34, 255, 23, 0.5);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_ok_bebe = QtWidgets.QPushButton(self.frame)
        self.pushButton_ok_bebe.setGeometry(QtCore.QRect(180, 10, 91, 31))
        self.pushButton_ok_bebe.setStyleSheet("QPushButton#pushButton_ok_bebe{\n"
"    background-color: rgb(23,100,19);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#pushButton_ok_bebe:hover{\n"
"background-color: rgb(27, 27, 27);\n"
"}\n"
"")
        self.pushButton_ok_bebe.setObjectName("pushButton_ok_bebe")
        self.label_bebe = QtWidgets.QLabel(Frame)
        self.label_bebe.setGeometry(QtCore.QRect(110, 110, 171, 121))
        self.label_bebe.setObjectName("label_bebe")
        self.label_marche = QtWidgets.QLabel(Frame)
        self.label_marche.setGeometry(QtCore.QRect(30, 80, 321, 171))
        self.label_marche.setStyleSheet("border-radius: 40px;\n"
"background-color:rgba(34, 255, 23, 0.5);")
        self.label_marche.setText("")
        self.label_marche.setObjectName("label_marche")
        self.frame.raise_()
        self.label_marche.raise_()
        self.label.raise_()
        self.label_bebe.raise_()

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:26pt;\">BEBE</span></p></body></html>"))
        self.pushButton_ok_bebe.setText(_translate("Frame", "OK"))
        self.label_bebe.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">VOUS AVEZ UN</span></p><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">NOUVEAU BEBE</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
