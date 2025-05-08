from PyQt6.QtWidgets import *
from gui import *

class Television(QMainWindow, Ui_MainWindow):

    MIN_VOLUME = 0
    MAX_VOLUME = 5
    MIN_CHANNEL = 0
    MAX_CHANNEL = 6

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.power_status = False
        self.muted_status = False
        self.volume_status = Television.MIN_VOLUME
        self.channel_status = Television.MIN_CHANNEL
        self.channel_image.setPixmap(QtGui.QPixmap("images/black.png"))

        self.power_button.clicked.connect(self.power)
        self.mute_button.clicked.connect(self.mute)
        self.volume_up_button.clicked.connect(self.volume_up)
        self.volume_down_button.clicked.connect(self.volume_down)
        self.channel_up_button.clicked.connect(self.channel_up)
        self.channel_down_button.clicked.connect(self.channel_down)

    def power(self) -> None:
        """
        Method to turn on the tv.
        """
        if self.power_status:
            self.power_status = False
            self.set_channel_image()
        else:
            self.power_status = True
            self.set_channel_image()

    def mute(self) -> None:
        """
        Method to mute the tv volume.
        """
        if self.power_status:
            if self.muted_status:
                self.muted_status = False
                self.volume_slider.setValue(self.volume_status)
            else:
                self.muted_status = True
                # self.volume_status = 0
                self.volume_slider.setValue(0)

    def channel_up(self) -> None:
        """
        Method to increase the tv channel.
        """
        if self.power_status:
            if self.channel_status < Television.MAX_CHANNEL:
                self.channel_status += 1
                self.set_channel_image()
            else:
                self.channel_status = Television.MIN_CHANNEL
                self.set_channel_image()

    def channel_down(self) -> None:
        """
        Method to decrease the tv channel.
        """
        if self.power_status:
            if self.channel_status > Television.MIN_CHANNEL:
                self.channel_status -= 1
                self.set_channel_image()
            else:
                self.channel_status = Television.MAX_CHANNEL
                self.set_channel_image()

    def volume_up(self) -> None:
        """
        Method to increase the tv volume.
        """
        if self.power_status:
            self.muted_status = False
            if self.volume_status < Television.MAX_VOLUME:
                self.volume_status += 1
                self.volume_slider.setValue(self.volume_status)

    def volume_down(self) -> None:
        """
        Method to decrease the tv volume.
        """
        if self.power_status:
            self.muted_status = False
            if self.volume_status > Television.MIN_VOLUME:
                self.volume_status -= 1
                self.volume_slider.setValue(self.volume_status)

    def set_channel_image(self) -> None:
        if self.power_status:
            if self.channel_status == 0:
                self.channel_image.setPixmap(QtGui.QPixmap("images/gray.png"))
            elif self.channel_status == 1:
                self.channel_image.setPixmap(QtGui.QPixmap("images/abc.png"))
            elif self.channel_status == 2:
                self.channel_image.setPixmap(QtGui.QPixmap("images/cnn.png"))
            elif self.channel_status == 3:
                self.channel_image.setPixmap(QtGui.QPixmap("images/nbc.png"))
            elif self.channel_status == 4:
                self.channel_image.setPixmap(QtGui.QPixmap("images/weather.png"))
            elif self.channel_status == 5:
                self.channel_image.setPixmap(QtGui.QPixmap("images/cbs.png"))
            elif self.channel_status == 6:
                self.channel_image.setPixmap(QtGui.QPixmap("images/espn.png"))
        else:
            self.channel_image.setPixmap(QtGui.QPixmap("images/black.png"))


    def __str__(self):
        pass
