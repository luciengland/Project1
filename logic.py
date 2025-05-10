from PyQt6.QtWidgets import *
from gui import *

class Television(QMainWindow, Ui_MainWindow):
    """
    Class representing a TV.
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 5
    MIN_CHANNEL = 0
    MAX_CHANNEL = 6

    def __init__(self) -> None:
        """
        Method to initialize the TV GUI.
        """
        super().__init__()
        self.setupUi(self)

        self.__power_status = False
        self.__muted_status = False
        self.__volume_status = Television.MIN_VOLUME
        self.__channel_status = Television.MIN_CHANNEL
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
        if self.__power_status:
            self.__power_status = False
            self.set_channel_image()
        else:
            self.__power_status = True
            self.set_channel_image()

    def mute(self) -> None:
        """
        Method to mute the tv volume.
        """
        if self.__power_status:
            if self.__muted_status:
                self.__muted_status = False
                self.volume_slider.setValue(self.__volume_status)
            else:
                self.__muted_status = True
                self.volume_slider.setValue(0)

    def channel_up(self) -> None:
        """
        Method to increase the tv channel.
        """
        if self.__power_status:
            if self.__channel_status < Television.MAX_CHANNEL:
                self.__channel_status += 1
                self.set_channel_image()
            else:
                self.__channel_status = Television.MIN_CHANNEL
                self.set_channel_image()

    def channel_down(self) -> None:
        """
        Method to decrease the tv channel.
        """
        if self.__power_status:
            if self.__channel_status > Television.MIN_CHANNEL:
                self.__channel_status -= 1
                self.set_channel_image()
            else:
                self.__channel_status = Television.MAX_CHANNEL
                self.set_channel_image()

    def volume_up(self) -> None:
        """
        Method to increase the tv volume.
        """
        if self.__power_status:
            self.__muted_status = False
            if self.__volume_status < Television.MAX_VOLUME:
                self.__volume_status += 1
                self.volume_slider.setValue(self.__volume_status)

    def volume_down(self) -> None:
        """
        Method to decrease the tv volume.
        """
        if self.__power_status:
            self.__muted_status = False
            if self.__volume_status > Television.MIN_VOLUME:
                self.__volume_status -= 1
                self.volume_slider.setValue(self.__volume_status)

    def set_channel_image(self) -> None:
        if self.__power_status:
            if self.__channel_status == 0:
                self.channel_image.setPixmap(QtGui.QPixmap("images/gray.png"))
            elif self.__channel_status == 1:
                self.channel_image.setPixmap(QtGui.QPixmap("images/abc.png"))
            elif self.__channel_status == 2:
                self.channel_image.setPixmap(QtGui.QPixmap("images/cnn.png"))
            elif self.__channel_status == 3:
                self.channel_image.setPixmap(QtGui.QPixmap("images/nbc.png"))
            elif self.__channel_status == 4:
                self.channel_image.setPixmap(QtGui.QPixmap("images/weather.png"))
            elif self.__channel_status == 5:
                self.channel_image.setPixmap(QtGui.QPixmap("images/cbs.png"))
            elif self.__channel_status == 6:
                self.channel_image.setPixmap(QtGui.QPixmap("images/espn.png"))
        else:
            self.channel_image.setPixmap(QtGui.QPixmap("images/black.png"))
