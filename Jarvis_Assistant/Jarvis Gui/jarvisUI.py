# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jarvisUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Jarvis_Ai_Assistant(object):
    def setupUi(self, Jarvis_Ai_Assistant):
        Jarvis_Ai_Assistant.setObjectName("Jarvis_Ai_Assistant")
        Jarvis_Ai_Assistant.setWindowModality(QtCore.Qt.ApplicationModal)
        Jarvis_Ai_Assistant.resize(687, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Jarvis_Ai_Assistant.sizePolicy().hasHeightForWidth())
        Jarvis_Ai_Assistant.setSizePolicy(sizePolicy)
        Jarvis_Ai_Assistant.setMinimumSize(QtCore.QSize(687, 400))
        Jarvis_Ai_Assistant.setMaximumSize(QtCore.QSize(687, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imageedit_91_6635454523.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Jarvis_Ai_Assistant.setWindowIcon(icon)
        Jarvis_Ai_Assistant.setIconSize(QtCore.QSize(36, 36))
        self.centralwidget = QtWidgets.QWidget(Jarvis_Ai_Assistant)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(687, 400))
        self.centralwidget.setObjectName("centralwidget")
        self.background_gif = QtWidgets.QLabel(self.centralwidget)
        self.background_gif.setGeometry(QtCore.QRect(-10, 0, 711, 401))
        self.background_gif.setStatusTip("")
        self.background_gif.setStyleSheet("")
        self.background_gif.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_gif.setText("")
        self.background_gif.setPixmap(QtGui.QPixmap("../../../Downloads/ezgif-3-5c1cdc1da873.gif"))
        self.background_gif.setObjectName("background_gif")
        self.run_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_button.setGeometry(QtCore.QRect(590, 320, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.run_button.setFont(font)
        self.run_button.setAutoFillBackground(False)
        self.run_button.setStyleSheet("background-color: rgb(21, 50, 50);\n"
"background-color: rgb(43, 104, 154);\n"
"border-radius:none;")
        self.run_button.setObjectName("run_button")
        self.cmd_border = QtWidgets.QLabel(self.centralwidget)
        self.cmd_border.setGeometry(QtCore.QRect(510, 170, 171, 131))
        self.cmd_border.setText("")
        self.cmd_border.setPixmap(QtGui.QPixmap("../../../Downloads/imageedit_76_8230725375.png"))
        self.cmd_border.setScaledContents(True)
        self.cmd_border.setObjectName("cmd_border")
        self.footer = QtWidgets.QLabel(self.centralwidget)
        self.footer.setGeometry(QtCore.QRect(0, 360, 701, 41))
        self.footer.setText("")
        self.footer.setPixmap(QtGui.QPixmap("../../../Downloads/imageedit_68_4334097749.png"))
        self.footer.setScaledContents(True)
        self.footer.setObjectName("footer")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 691, 41))
        self.header.setText("")
        self.header.setPixmap(QtGui.QPixmap("../../../Downloads/imageedit_74_7199871132.png"))
        self.header.setScaledContents(True)
        self.header.setObjectName("header")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(530, 200, 131, 91))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background:transparent;border:none;")
        self.textEdit.setObjectName("textEdit")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setEnabled(True)
        self.listWidget.setGeometry(QtCore.QRect(20, 80, 180, 270))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMaximumSize(QtCore.QSize(180, 270))
        self.listWidget.setSizeIncrement(QtCore.QSize(180, 0))
        self.listWidget.setBaseSize(QtCore.QSize(180, 0))
        self.listWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.listWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.listWidget.setAcceptDrops(False)
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setStyleSheet("background:transparent;border:none;\n"
"gridline-color: transparent;\n"
"selection-background-color:transparent;\n"
"color: rgb(1, 182, 179);\n"
"\n"
"QScrollBar::handle:vertical{\n"
"    background:pink;\n"
"}")
        self.listWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.listWidget.setAutoScroll(True)
        self.listWidget.setAutoScrollMargin(100)
        self.listWidget.setTabKeyNavigation(True)
        self.listWidget.setProperty("showDropIndicator", True)
        self.listWidget.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.listWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.listWidget.setMovement(QtWidgets.QListView.Free)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setWordWrap(False)
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 60, 151, 101))
        self.label.setMaximumSize(QtCore.QSize(151, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("I_made_a_copy_of_5.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        Jarvis_Ai_Assistant.setCentralWidget(self.centralwidget)

        self.retranslateUi(Jarvis_Ai_Assistant)
        self.listWidget.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(Jarvis_Ai_Assistant)

    def retranslateUi(self, Jarvis_Ai_Assistant):
        _translate = QtCore.QCoreApplication.translate
        Jarvis_Ai_Assistant.setWindowTitle(_translate("Jarvis_Ai_Assistant", "Jarvis_Ai_Assistant"))
        self.run_button.setText(_translate("Jarvis_Ai_Assistant", "Run"))
        self.textEdit.setHtml(_translate("Jarvis_Ai_Assistant", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Yu Gothic Light\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-weight:600; color:#01b6b3;\">Hello sir,</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-weight:600; color:#01b6b3;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-weight:600; color:#01b6b3;\">How can I help you ?</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-weight:600; color:#01b6b3;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-weight:600; color:#01b6b3;\">Ask me what can I do</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Jarvis_Ai_Assistant = QtWidgets.QMainWindow()
    ui = Ui_Jarvis_Ai_Assistant()
    ui.setupUi(Jarvis_Ai_Assistant)
    Jarvis_Ai_Assistant.show()
    sys.exit(app.exec_())
