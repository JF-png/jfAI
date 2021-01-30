from PyQt5 import QtWidgets, uic, QtCore, QtGui
import sys
import datetime
from ui import Ui_Dialog
import sysoperation
from sysoperation import Sys
from pyparsersys import bit, dol, eur, temp, w
from weboperation import Web

now = datetime.datetime.now()
he = "Джеймс: "
you = "Вы: "
app=QtWidgets.QApplication(sys.argv)

Dialog=QtWidgets.QDialog()

ui=Ui_Dialog()

ui.setupUi(Dialog)

Dialog.show()
def send():
    tbr = ui.lineEdit.text()
    tbr=tbr.lower()

    if 'погод' in tbr or 'weather' in tbr:
        ui.label.setText(you + tbr)
        ui.label_2.setText(he + " У вас сейчас " + str(temp) + "°С. "  + "Погода: " + w.get_detailed_status())
        ui.lineEdit.clear()
    elif 'врем' in tbr or 'time' in tbr:
        ui.label.setText(you + tbr)
        ui.lineEdit.clear()
        if now.minute > 10:
            ui.label_2.setText(he + "Сейчас " + str(now.hour) + ":" + str(now.minute))
        if now.minute < 9:
           ui.label_2.setText(he + "Сейчас " + str(now.hour) + ":" + "0" + str(now.minute))
        ui.lineEdit.clear()
    elif 'шут' in tbr:
        ui.label.setText(you + tbr)
        ui.label_2.setText(he + "Я не знаю шуток, разработчику лень писать, ха-ха-ха")
        ui.lineEdit.clear()
    elif 'дол' in tbr or "dol" in tbr:
        ui.label_2.setText(he +"1$ = " + dol + "₽")
        ui.label.setText(you + tbr)
        ui.lineEdit.clear()
    elif "евр" in tbr or "eur" in tbr:
        ui.label_2.setText(he +"1€ = " + eur + "₽")
        ui.label.setText(you + tbr)
        ui.lineEdit.clear()
    elif "битк" in tbr or "bit" in tbr:
        ui.label_2.setText(he + "1₿ = " + bit + "₽")
        ui.label.setText(you + tbr)
        ui.lineEdit.clear()
    elif "вк" in tbr or "vk" in tbr:
        Web.VK()
        ui.label.setText(you + tbr)
        ui.label_2.setText(he + "открываю ВК")
        ui.lineEdit.clear()
    elif "ютуб" in tbr or "youtube" in tbr:
        Web.youtube()
        ui.label.setText(you + tbr)
        ui.label_2.setText(he + "открываю Ютуб")
        ui.lineEdit.clear()
    elif "хват" in tbr or "пока" in tbr:
        #ui.label.setText(you + tbr)
        #ui.label_2.setText(he + sysoperation.ttx)
        #ui.lineEdit.clear()
        Sys.Quit()
    else:
        ui.label.setText(you + tbr)
        ui.label_2.setText(he +"Команда не распознана, повторите")
        ui.lineEdit.clear()
        
ui.pushButton.clicked.connect(send)
sys.exit(app.exec_())