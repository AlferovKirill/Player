from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtGui import *
import sys

class AudioPlayer(QWidget):
    
    i = 0
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 220)
        self.setWindowTitle("AudioPlayer")

        self.playlist = QMediaPlaylist()
        self.path = QMediaContent(QUrl("T.mp3"))
        self.playlist.addMedia(QMediaContent(self.path))
        
        #self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        
        self.player = QMediaPlayer()
        self.player.setPlaylist(self.playlist)
        self.player.setVolume(0)
        self.player.play()
        self.player.pause()
        

        self.volume = QSlider(Qt.Horizontal, self)
        self.volume.setValue(0)
        self.volume.setFocusPolicy(Qt.NoFocus)
        self.volume.valueChanged[int].connect(self.changeValue)
        self.volume.setMaximum(100)
        self.volume.setMinimum(0)
        self.volume.show()
        self.volume.setGeometry(60, 190, 135, 15)

        self.lbl = QLabel(self)
        self.lbl.setGeometry(10, 160, 50, 70)
        self.lbl.setPixmap(QPixmap('min.png'))

        self.pause = QPushButton(self)
        self.pause.setIcon(QIcon('play.png'))
        self.pause.setGeometry(230, 170, 40, 40)
        self.pause.clicked.connect(self.pa)

        self.rewind = QSlider(Qt.Horizontal, self)
        self.rewind.setValue(0)
        self.rewind.setFocusPolicy(Qt.NoFocus)
        self.rewind.valueChanged[int].connect(self.changeRewind)
        self.rewind.show()
        self.rewind.setGeometry(50, 130, 400, 40)
        
        self.show()
        
    def changeValue(self, value):
        self.player.setVolume(value)
        self.volume.setValue(value)
        if value > 50:
            self.lbl.setPixmap(QPixmap('max.png'))
        elif value > 0 and value < 51:
            self.lbl.setPixmap(QPixmap('min.png'))
        else:
            self.lbl.setPixmap(QPixmap('mute.png'))
            
    def pa(self):
        if self.i == 0:
            self.player.play()
            self.pause.setIcon(QIcon('pause.png'))
            self.i = 1
        else:
            self.player.pause()
            self.pause.setIcon(QIcon('play.png'))
            self.i = 0

    def changeRewind(self, value):
        self.player.setPosition(value*1000)


            
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = AudioPlayer()
    
    sys.exit(app.exec_())
    
