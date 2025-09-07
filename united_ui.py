import sys, os
import untitled_ui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QDialog
from qfluentwidgets import setTheme, Theme, setThemeColor

class Form(QDialog, untitled_ui.Ui_Form):
    def __init__(self, parent=None, title=""):
        super(Form, self).__init__(parent)
        self.setupUi(self)
        if title: self.TitleLabel.setText(title)
        
QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling)
QApplication.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)
app = QApplication(sys.argv)
setTheme(Theme.LIGHT)
setThemeColor(app.palette().highlight().color())
title = sys.argv[1] if len(sys.argv) > 1 else "正在烧烤"
ui = Form(title=title)
if title: ui.setWindowTitle(title)
ui.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "spinner.png")))
ui.show()
sys.exit(app.exec_())