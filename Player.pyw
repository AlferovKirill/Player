from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtGui import QIcon
import sys

class Player(QMainWindow):
    def __init__(self):
        super().__init__()
        self.base()

    def base(self):
        self.setGeometry(300, 300, 640, 480)
        self.setWindowTitle("Player")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.wid = QWidget(self)
        self.player = QMediaPlayer(self)
        self.video = QVideoWidget()
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.time = QSlider(Qt.Horizontal)
        self.volume = QSlider(Qt.Horizontal)
        
        self.icon = QPushButton()
        self.icon.setIcon(self.style().standardIcon(QStyle.SP_MediaVolume))
        self.icon.clicked.connect(self.m)
        
        openAction = QAction(QIcon('open.png'), '&Open', self)        
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open movie')
        openAction.triggered.connect(self.videoChange)

        exitAction = QAction(QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exitCall)

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)
        menuBar.setStyleSheet(" background-color: white;")
        fileMenu.setStyleSheet("background-color: #387bc7;")

        self.playButton = QPushButton()
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        self.playButton.clicked.connect(self.p)
        self.playIndicator = False

        self.back = QPushButton()
        self.back.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipBackward))
        self.back.clicked.connect(self.b)
        self.backIndicator = False

        self.next = QPushButton()
        self.next.setIcon(self.style().standardIcon(QStyle.SP_MediaSeekForward))
        self.next.clicked.connect(self.n)
        self.nextIndicator = False
        
        self.setCentralWidget(self.wid)
        self.layout.addWidget(self.video, 0, 0, 1, 20)
        self.layout.addWidget(self.time, 1, 0, 1, 20)
        self.layout.addWidget(self.back, 2, 5, 1, 3)
        self.layout.addWidget(self.playButton, 2, 8, 1, 4)
        self.layout.addWidget(self.next, 2, 12, 1, 3)
        self.layout.addWidget(self.volume, 2, 1, 1, 4)
        self.layout.addWidget(self.icon, 2, 0, 1, 1)
        self.wid.setLayout(self.layout)
        self.time.setValue(0)
        self.volume.setValue(15)
        self.player.setVolume(15)
        self.volume.setMaximum(100)
        self.volume.setMinimum(0)

        self.time.setStyleSheet(
            """
        QSlider::handle:horizontal {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 #FFFFFF, stop:1 #E3E3E3);
            border: 1px solid #707070;
            width: 10px;
            margin-top: -4px;
            margin-bottom: -4px;
            border-radius: 4px;
        }

        QSlider::handle:horizontal:hover {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 #DEDEDE, stop:1 #C9C9C9);
            border: 1px solid #4F4F4F;
            border-radius: 4px;
        }

        QSlider::sub-page:horizontal {
            background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,
                stop: 0 #BFBFBF, stop: 1 #9E9E9E);
            background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,
                stop: 0 #387bc7, stop: 1 #387bc7);
            border: 1px solid #777;
            height: 10px;
            border-radius: 4px;
        }

        QSlider::add-page:horizontal {
            background: #FCFCFC;
            border: 1px solid #707070;
            height: 10px;
            border-radius: 4px;
        }"""
        )

        self.setStyleSheet("background-color: black;")
        self.next.setStyleSheet("background-color: #FCFCFC;")
        self.back.setStyleSheet("background-color: #FCFCFC;")
        self.playButton.setStyleSheet("background-color: #FCFCFC;")
        self.video.setStyleSheet("background-color: #FCFCFC;")
        self.volume.setStyleSheet("""

        QSlider::handle:horizontal {
            background: white
            border: 1px solid #707070;
            width: 10px;
            margin-top: -4px;
            margin-bottom: -4px;
            border-radius: 4px;
        }
        
        QSlider::sub-page:horizontal {
            background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,
                stop: 0 #BFBFBF, stop: 1 #9E9E9E);
            background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,
                stop: 0 #387bc7, stop: 1 #387bc7);
            border: 1px solid #777;
            height: 10px;
            border-radius: 4px;
        }


        QSlider::add-page:horizontal {
            background: #FCFCFC;
            border: 1px solid #707070;
            height: 10px;
            border-radius: 4px;
        }"""
        )
        self.player.positionChanged.connect(self.positionChanged)
        self.time.sliderMoved.connect(self.changeTime)
        self.volume.sliderMoved.connect(self.changeVolume)
        self.player.durationChanged.connect(self.durationChanged)
        self.player.setVideoOutput(self.video)
        
        
        self.video.show()
        
        self.show()

    def videoChange(self):
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(QFileDialog.getOpenFileName(self, "Open Movie", QDir.homePath())[0])))
        self.player.play()

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                QDir.homePath())

        if fileName != '':
            self.player.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
            
    def exitCall(self):
        sys.exit(app.exec_())
        
    def changeTime(self, value):
        self.player.setPosition(value)

    def positionChanged(self, position):
        self.time.setValue(position)
    
    def durationChanged(self, duration):
        self.time.setRange(0, duration)

    def p(self):
        if self.playIndicator:
            self.playIndicator = False
            self.player.play()
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playIndicator = True
            self.player.pause()
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def n(self):
        try:
            self.player.setPosition(self.player.position() + 10000)
        except:
            pass

    def b(self):
        try:
            self.player.setPosition(self.player.position() - 10000)
        except:
            pass

    def changeVolume(self, value):
        self.player.setVolume(value)
        self.volume.setValue(value)
        
        if value == 0:
            self.icon.setIcon(self.style().standardIcon(QStyle.SP_MediaVolumeMuted))
        else:
            self.icon.setIcon(self.style().standardIcon(QStyle.SP_MediaVolume))
            
    def m(self):
        pass
if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = Player()
    sys.exit(app.exec_())

        
