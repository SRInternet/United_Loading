import sys, os
from PySide6.QtCore import Qt, QByteArray
from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtGui import QFontDatabase, QIcon
from qfluentwidgets import setTheme, Theme, setThemeColor

app = QApplication(sys.argv)
try:
    with open(os.path.join(os.path.dirname(__file__), "HARMONYOS_SANS_SC_BLACK.TTF"), "rb") as f:
        font_data = QByteArray(f.read())
    QFontDatabase.addApplicationFontFromData(font_data)
except Exception as e:
    print(e)
    
import untitled_ui
class Form(QDialog, untitled_ui.Ui_Form):
    def __init__(self, parent=None, title=""):
        super(Form, self).__init__(parent)
        self.setupUi(self)
        if title: self.TitleLabel.setText(title)
                    
QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling)
QApplication.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)
setTheme(Theme.LIGHT)
setThemeColor(app.palette().highlight().color())
title = sys.argv[1] if len(sys.argv) > 1 else "正在烧烤"
ui = Form(title=title)
if title: ui.setWindowTitle(title)
ui.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "spinner.png")))
ui.show()
sys.exit(app.exec_())