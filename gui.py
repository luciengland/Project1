# Form implementation generated from reading ui file 'remote.ui'
#
# Created by: PyQt6 UI code generator 6.9.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(353, 605)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("QWidget {\n"
"    background-color: rgb(51, 51, 51)\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.power_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.power_button.setGeometry(QtCore.QRect(140, 10, 80, 80))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 32))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 32))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 32))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 32))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 32))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 32))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 32))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 32))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 32))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        self.power_button.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.power_button.setFont(font)
        self.power_button.setStyleSheet("QPushButton {\n"
"    border-radius: 40px; \n"
"    background-color: rgb(255, 0, 32);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: solid;\n"
"    border-width: 4px;\n"
"    border-color: black;\n"
"}")
        self.power_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/power.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.power_button.setIcon(icon)
        self.power_button.setIconSize(QtCore.QSize(40, 40))
        self.power_button.setAutoDefault(False)
        self.power_button.setObjectName("power_button")
        self.volume_up_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.volume_up_button.setGeometry(QtCore.QRect(60, 340, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(20)
        self.volume_up_button.setFont(font)
        self.volume_up_button.setStyleSheet("QPushButton {\n"
"    border-radius: 35px; \n"
"    background-color: rgb(124, 165, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: solid;\n"
"    border-width: 4px;\n"
"    border-color: black;\n"
"}")
        self.volume_up_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/up.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.volume_up_button.setIcon(icon1)
        self.volume_up_button.setIconSize(QtCore.QSize(40, 40))
        self.volume_up_button.setObjectName("volume_up_button")
        self.volume_buttons = QtWidgets.QButtonGroup(MainWindow)
        self.volume_buttons.setObjectName("volume_buttons")
        self.volume_buttons.addButton(self.volume_up_button)
        self.volume_down_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.volume_down_button.setGeometry(QtCore.QRect(60, 460, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(15)
        self.volume_down_button.setFont(font)
        self.volume_down_button.setStyleSheet("QPushButton {\n"
"    border-radius: 35px; \n"
"    background-color: rgb(124, 165, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: solid;\n"
"    border-width: 4px;\n"
"    border-color: black;\n"
"}")
        self.volume_down_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/down.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.volume_down_button.setIcon(icon2)
        self.volume_down_button.setIconSize(QtCore.QSize(40, 40))
        self.volume_down_button.setObjectName("volume_down_button")
        self.volume_buttons.addButton(self.volume_down_button)
        self.channel_up_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel_up_button.setGeometry(QtCore.QRect(220, 340, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(20)
        self.channel_up_button.setFont(font)
        self.channel_up_button.setAutoFillBackground(False)
        self.channel_up_button.setStyleSheet("QPushButton {\n"
"    border-radius: 35px; \n"
"    background-color: rgb(124, 165, 255)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: solid;\n"
"    border-width: 4px;\n"
"    border-color: black;\n"
"}")
        self.channel_up_button.setText("")
        self.channel_up_button.setIcon(icon1)
        self.channel_up_button.setIconSize(QtCore.QSize(40, 40))
        self.channel_up_button.setObjectName("channel_up_button")
        self.channel_buttons = QtWidgets.QButtonGroup(MainWindow)
        self.channel_buttons.setObjectName("channel_buttons")
        self.channel_buttons.addButton(self.channel_up_button)
        self.channel_down_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel_down_button.setGeometry(QtCore.QRect(220, 460, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.channel_down_button.setFont(font)
        self.channel_down_button.setStyleSheet("QPushButton {\n"
"    border-radius: 35px; \n"
"    background-color: rgb(124, 165, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: solid;\n"
"    border-width: 4px;\n"
"    border-color: black;\n"
"}")
        self.channel_down_button.setText("")
        self.channel_down_button.setIcon(icon2)
        self.channel_down_button.setIconSize(QtCore.QSize(40, 40))
        self.channel_down_button.setObjectName("channel_down_button")
        self.channel_buttons.addButton(self.channel_down_button)
        self.mute_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.mute_button.setGeometry(QtCore.QRect(150, 290, 65, 65))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.mute_button.setFont(font)
        self.mute_button.setStyleSheet("QPushButton {\n"
"    border-radius: 32px; \n"
"    background-color: rgb(230, 230, 230)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: solid;\n"
"    border-width: 4px;\n"
"    border-color: black;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/mute.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.mute_button.setIcon(icon3)
        self.mute_button.setIconSize(QtCore.QSize(40, 40))
        self.mute_button.setObjectName("mute_button")
        self.volume_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.volume_label.setGeometry(QtCore.QRect(50, 420, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(15)
        self.volume_label.setFont(font)
        self.volume_label.setStyleSheet("QLabel {\n"
"    color: rgb(230, 230, 230);\n"
"    background-color: rgb(51, 51, 51);\n"
"}")
        self.volume_label.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.volume_label.setLineWidth(2)
        self.volume_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.volume_label.setObjectName("volume_label")
        self.channel_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.channel_label.setGeometry(QtCore.QRect(210, 420, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(15)
        self.channel_label.setFont(font)
        self.channel_label.setStyleSheet("QLabel {\n"
"    color: rgb(230, 230, 230);\n"
"    background-color: rgb(51, 51, 51);\n"
"}")
        self.channel_label.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.channel_label.setLineWidth(2)
        self.channel_label.setScaledContents(False)
        self.channel_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.channel_label.setWordWrap(False)
        self.channel_label.setObjectName("channel_label")
        self.channel_image = QtWidgets.QLabel(parent=self.centralwidget)
        self.channel_image.setGeometry(QtCore.QRect(80, 100, 211, 150))
        self.channel_image.setAutoFillBackground(False)
        self.channel_image.setStyleSheet("QLabel {\n"
"    background-color: white;\n"
"\n"
"}")
        self.channel_image.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.channel_image.setLineWidth(3)
        self.channel_image.setMidLineWidth(0)
        self.channel_image.setText("")
        self.channel_image.setPixmap(QtGui.QPixmap("black.png"))
        self.channel_image.setScaledContents(False)
        self.channel_image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.channel_image.setObjectName("channel_image")
        self.volume_slider = QtWidgets.QSlider(parent=self.centralwidget)
        self.volume_slider.setGeometry(QtCore.QRect(70, 260, 211, 22))
        self.volume_slider.setMaximum(5)
        self.volume_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.volume_slider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.volume_slider.setTickInterval(1)
        self.volume_slider.setObjectName("volume_slider")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 353, 38))
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Remote"))
        self.volume_label.setText(_translate("MainWindow", "VOLUME"))
        self.channel_label.setText(_translate("MainWindow", "CHANNEL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
