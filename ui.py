from PyQt5 import QtWidgets, uic, QtCore, QtGui
import PyQt5
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(466, 301)
        Dialog.setStyleSheet("background-color:#827a7a;")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(290, 250, 71, 31))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("""
        QPushButton{
        background-color:#241e1e;\n
        color:gold;\n
        border-radius:5px;\n
        \n
        }
        QPushButton:hover {
        background-color:#3d3d3d
        }""")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 250, 271, 31))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:#000000;\n"
"color:#ffe500;\n"
"border:none;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(20, 50, 421, 51))
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("background-color:grey;\n"
"color:#c3cc;\n"
"border-radius:15px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 421, 51))
        self.label_2.setStyleSheet("background-color:lightgrey;\n"
"color:#c3cc;\n"
"border:solid;\n"
"border-radius:15px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 491, 301))
        self.textBrowser.setStyleSheet("background-color:#5e5e5e\n"
"\n"
"\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 491, 301))
        self.label_3.setStyleSheet("background-color:#5e5d52;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.textBrowser.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.label_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "James v 0.1 betatest"))
        self.pushButton.setText(_translate("Dialog", "Отправить"))
        self.label.setText(_translate("Dialog", "Вы"))
        self.label_2.setText(_translate("Dialog", "Джеймс"))