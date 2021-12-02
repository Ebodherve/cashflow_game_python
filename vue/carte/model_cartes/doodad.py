# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doodad.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(362, 367)
        Frame.setStyleSheet("\n"
"#Frame{\n"
"background-color: rgba(196, 209, 97, 1);\n"
"border-top-left-radius: 20px ;\n"
"border-top-right-radius: 20px ;\n"
"border-bottom-left-radius: 20px ;\n"
"border-bottom-right-radius: 20px \n"
"}")
        self.frame = QtWidgets.QFrame(Frame)
        self.frame.setGeometry(QtCore.QRect(-20, 290, 411, 61))
        self.frame.setStyleSheet("background-color:rgba(34, 255, 23, 0.5);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_payer_doodad = QtWidgets.QPushButton(self.frame)
        self.pushButton_payer_doodad.setGeometry(QtCore.QRect(60, 20, 75, 23))
        self.pushButton_payer_doodad.setStyleSheet("QPushButton#pushButton_payer_doodad{\n"
"    background-color: rgb(23,100,19);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#pushButton_payer_doodad:hover{\n"
"background-color: rgb(27, 27, 27);\n"
"}\n"
"")
        self.pushButton_payer_doodad.setObjectName("pushButton_payer_doodad")
        self.label_doodad = QtWidgets.QLabel(Frame)
        self.label_doodad.setGeometry(QtCore.QRect(70, 80, 241, 141))
        self.label_doodad.setWordWrap(True)
        self.label_doodad.setObjectName("label_doodad")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(120, 10, 141, 31))
        self.label.setStyleSheet("color : rgb(45, 111, 47);\n"
"font-weight: bold;\n"
"")
        self.label.setObjectName("label")
        self.label_marche = QtWidgets.QLabel(Frame)
        self.label_marche.setGeometry(QtCore.QRect(40, 60, 291, 201))
        self.label_marche.setStyleSheet("border-radius: 40px;\n"
"background-color:rgba(34, 255, 23, 0.5);")
        self.label_marche.setText("")
        self.label_marche.setObjectName("label_marche")
        self.label_marche.raise_()
        self.frame.raise_()
        self.label_doodad.raise_()
        self.label.raise_()

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton_payer_doodad.setText(_translate("Frame", "PAYER"))
        self.label_doodad.setText(_translate("Frame", "TextLabel"))
        self.label.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:22pt;\">DOODAD</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
