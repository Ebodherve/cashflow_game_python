# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MAINWINDOWS.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1037, 691)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-20, -30, 16777215, 16777215))
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.dashboard = QtWidgets.QFrame(self.frame)
        self.dashboard.setGeometry(QtCore.QRect(30, 80, 551, 621))
        self.dashboard.setStyleSheet("#dashboard{\n"
"\n"
"background : rgba(196, 209, 97, 0.9);\n"
"border-top-right-radius: 20px ;\n"
"border-top-left-radius: 20px ;\n"
"border-bottom-right-radius: 20px ;\n"
"border-bottom-left-radius: 20px ;\n"
"}")
        self.dashboard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dashboard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dashboard.setObjectName("dashboard")
        self.label_2 = QtWidgets.QLabel(self.dashboard)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 281, 31))
        self.label_2.setStyleSheet("background : rgb(92, 53, 102);\n"
"color: white;")
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.dashboard)
        self.label_6.setGeometry(QtCore.QRect(0, 230, 281, 31))
        self.label_6.setStyleSheet("background : rgb(92, 53, 102);\n"
"color: white;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.dashboard)
        self.label_7.setGeometry(QtCore.QRect(0, 430, 281, 31))
        self.label_7.setStyleSheet("background : rgb(92, 53, 102);\n"
"color: white;\n"
"text-align: center;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.dashboard)
        self.label_8.setGeometry(QtCore.QRect(290, 430, 251, 31))
        self.label_8.setStyleSheet("background : rgb(92, 53, 102);\n"
"color: white;\n"
"text-align: center;")
        self.label_8.setObjectName("label_8")
        self.progressBar = QtWidgets.QProgressBar(self.dashboard)
        self.progressBar.setGeometry(QtCore.QRect(300, 90, 251, 23))
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 50)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.label_3 = QtWidgets.QLabel(self.dashboard)
        self.label_3.setGeometry(QtCore.QRect(330, 20, 161, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.dashboard)
        self.label_4.setGeometry(QtCore.QRect(310, 40, 191, 17))
        self.label_4.setObjectName("label_4")
        self.text_depenses = QtWidgets.QLabel(self.dashboard)
        self.text_depenses.setGeometry(QtCore.QRect(300, 70, 141, 20))
        self.text_depenses.setObjectName("text_depenses")
        self.somm_depenses = QtWidgets.QLabel(self.dashboard)
        self.somm_depenses.setGeometry(QtCore.QRect(440, 70, 131, 17))
        self.somm_depenses.setObjectName("somm_depenses")
        self.text_revnu_passif = QtWidgets.QLabel(self.dashboard)
        self.text_revnu_passif.setGeometry(QtCore.QRect(300, 120, 111, 17))
        self.text_revnu_passif.setObjectName("text_revnu_passif")
        self.somme_revenu_passif = QtWidgets.QLabel(self.dashboard)
        self.somme_revenu_passif.setGeometry(QtCore.QRect(310, 140, 61, 16))
        self.somme_revenu_passif.setObjectName("somme_revenu_passif")
        self.label_5 = QtWidgets.QLabel(self.dashboard)
        self.label_5.setGeometry(QtCore.QRect(300, 270, 91, 31))
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(self.dashboard)
        self.label_9.setGeometry(QtCore.QRect(310, 320, 101, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.dashboard)
        self.label_10.setGeometry(QtCore.QRect(390, 270, 111, 31))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.dashboard)
        self.label_11.setGeometry(QtCore.QRect(310, 340, 111, 17))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.dashboard)
        self.label_12.setGeometry(QtCore.QRect(310, 390, 111, 17))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.dashboard)
        self.label_13.setGeometry(QtCore.QRect(420, 390, 81, 20))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.dashboard)
        self.label_14.setGeometry(QtCore.QRect(420, 320, 81, 20))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.dashboard)
        self.label_15.setGeometry(QtCore.QRect(420, 340, 91, 20))
        self.label_15.setObjectName("label_15")
        self.lineEdit = QtWidgets.QLineEdit(self.dashboard)
        self.lineEdit.setGeometry(QtCore.QRect(300, 370, 231, 12))
        self.lineEdit.setMaximumSize(QtCore.QSize(167772, 12))
        self.lineEdit.setStyleSheet("background : rgb(92, 53, 102)")
        self.lineEdit.setObjectName("lineEdit")
        self.listWidget_entrees = QtWidgets.QListWidget(self.dashboard)
        self.listWidget_entrees.setGeometry(QtCore.QRect(10, 40, 271, 171))
        self.listWidget_entrees.setStyleSheet("border:none;\n"
"border-bottom: solid  10px red;\n"
"background : rgba(196, 209, 97, 0.9);\n"
"border-bottom-right-radius: 20px ;\n"
"")
        self.listWidget_entrees.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget_entrees.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget_entrees.setObjectName("listWidget_entrees")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_entrees.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_entrees.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_entrees.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_entrees.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_entrees.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_entrees.addItem(item)
        self.listWidget_depenses = QtWidgets.QListWidget(self.dashboard)
        self.listWidget_depenses.setGeometry(QtCore.QRect(10, 260, 271, 151))
        self.listWidget_depenses.setStyleSheet("border : none;\n"
"border-bottom-right-radius: 20px ;\n"
"background : rgba(196, 209, 97, 0.9);")
        self.listWidget_depenses.setObjectName("listWidget_depenses")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_depenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_depenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_depenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_depenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_depenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_depenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_depenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_depenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_depenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_depenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_depenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_depenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_depenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_depenses.addItem(item)
        self.listWidget_investissements = QtWidgets.QListWidget(self.dashboard)
        self.listWidget_investissements.setGeometry(QtCore.QRect(10, 460, 271, 151))
        self.listWidget_investissements.setStyleSheet("border-bottom-right-radius: 20px ;\n"
"background : rgba(196, 209, 97, 0.9);\n"
"border:none;")
        self.listWidget_investissements.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget_investissements.setObjectName("listWidget_investissements")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_investissements.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_investissements.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_investissements.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_investissements.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_investissements.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_investissements.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_investissements.addItem(item)
        self.label_16 = QtWidgets.QLabel(self.dashboard)
        self.label_16.setGeometry(QtCore.QRect(380, 140, 47, 13))
        self.label_16.setObjectName("label_16")
        self.listWidget_responsabilites = QtWidgets.QListWidget(self.dashboard)
        self.listWidget_responsabilites.setGeometry(QtCore.QRect(290, 460, 251, 151))
        self.listWidget_responsabilites.setStyleSheet("border-bottom-right-radius: 20px ; \n"
"background-color : rgba(196, 209, 97, 0.9);")
        self.listWidget_responsabilites.setObjectName("listWidget_responsabilites")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.listWidget_responsabilites.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_responsabilites.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_responsabilites.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_responsabilites.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_responsabilites.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_responsabilites.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_responsabilites.addItem(item)
        self.label_17 = QtWidgets.QLabel(self.dashboard)
        self.label_17.setGeometry(QtCore.QRect(490, 270, 71, 31))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.dashboard)
        self.label_18.setGeometry(QtCore.QRect(500, 320, 71, 21))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.dashboard)
        self.label_19.setGeometry(QtCore.QRect(500, 340, 47, 13))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.dashboard)
        self.label_20.setGeometry(QtCore.QRect(500, 390, 47, 13))
        self.label_20.setObjectName("label_20")
        self.pushButton_dashboard = QtWidgets.QPushButton(self.frame)
        self.pushButton_dashboard.setGeometry(QtCore.QRect(60, 50, 75, 23))
        self.pushButton_dashboard.setStyleSheet("QPushButton#pushButton_dashboard{\n"
"    background-color: rgb(23,100,19);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#pushButton_dashboard:hover{\n"
"background-color: rgb(27, 27, 27);\n"
"}\n"
"")
        self.pushButton_dashboard.setObjectName("pushButton_dashboard")
        self.background = QtWidgets.QFrame(self.frame)
        self.background.setGeometry(QtCore.QRect(0, -10, 1111, 731))
        self.background.setStyleSheet("background-image: url(BACK.png);")
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.commandLinkButton_quitter = QtWidgets.QCommandLinkButton(self.background)
        self.commandLinkButton_quitter.setGeometry(QtCore.QRect(900, 50, 91, 41))
        self.commandLinkButton_quitter.setStyleSheet("#commandLinkButton_quitter{\n"
"background: inherit;\n"
"    background-color: rgb(23,100,19);\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"")
        self.commandLinkButton_quitter.setObjectName("commandLinkButton_quitter")
        self.label = QtWidgets.QLabel(self.background)
        self.label.setGeometry(QtCore.QRect(100, 130, 691, 441))
        self.label.setStyleSheet("background-image: url(plateau.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.carte = QtWidgets.QFrame(self.background)
        self.carte.setGeometry(QtCore.QRect(800, 140, 241, 401))
        self.carte.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.carte.setFrameShadow(QtWidgets.QFrame.Raised)
        self.carte.setObjectName("carte")
        self.background.raise_()
        self.dashboard.raise_()
        self.pushButton_dashboard.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1037, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">entrees</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">d??penses</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px;text-align:center;  margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">investissements</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">resonsabilit??s</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">augmenter vos revenus passif</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">et sortez de Rate Race </span></p></body></html>"))
        self.text_depenses.setText(_translate("MainWindow", "Total des d??penses"))
        self.somm_depenses.setText(_translate("MainWindow", "10000FCFA"))
        self.text_revnu_passif.setText(_translate("MainWindow", "revenus passifs :"))
        self.somme_revenu_passif.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">CASH :</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Total entr??es :</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">100000 </span></p><p><br/></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Total d??penses :</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "Cheque de paie :"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p>12000</p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">80000</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">10000</span></p></body></html>"))
        __sortingEnabled = self.listWidget_entrees.isSortingEnabled()
        self.listWidget_entrees.setSortingEnabled(False)
        item = self.listWidget_entrees.item(0)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_entrees.item(1)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_entrees.item(2)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_entrees.item(3)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_entrees.item(4)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_entrees.item(5)
        item.setText(_translate("MainWindow", "New Item"))
        self.listWidget_entrees.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_depenses.isSortingEnabled()
        self.listWidget_depenses.setSortingEnabled(False)
        item = self.listWidget_depenses.item(0)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_depenses.item(1)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_depenses.item(2)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_depenses.item(3)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_depenses.item(4)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_depenses.item(5)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_depenses.item(6)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_depenses.item(7)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_depenses.item(8)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_depenses.item(9)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_depenses.item(10)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_depenses.item(11)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_depenses.item(12)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_depenses.item(13)
        item.setText(_translate("MainWindow", "New Item"))
        self.listWidget_depenses.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_investissements.isSortingEnabled()
        self.listWidget_investissements.setSortingEnabled(False)
        item = self.listWidget_investissements.item(0)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_investissements.item(1)
        item.setText(_translate("MainWindow", "JGCFFYUFHKG"))
        item = self.listWidget_investissements.item(2)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_investissements.item(3)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_investissements.item(4)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_investissements.item(5)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget_investissements.item(6)
        item.setText(_translate("MainWindow", "New Item"))
        self.listWidget_investissements.setSortingEnabled(__sortingEnabled)
        self.label_16.setText(_translate("MainWindow", "FCFA"))
        __sortingEnabled = self.listWidget_responsabilites.isSortingEnabled()
        self.listWidget_responsabilites.setSortingEnabled(False)
        self.listWidget_responsabilites.setSortingEnabled(__sortingEnabled)
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">FCFA</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">FCFA</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">FCFA</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">FCFA</span></p></body></html>"))
        self.pushButton_dashboard.setText(_translate("MainWindow", "DASHBOARD"))
        self.commandLinkButton_quitter.setText(_translate("MainWindow", "quitter"))
import backgroundimage


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
