import getopt
import re
import sys
import time
import subprocess
from PyQt5.QtGui import QBitmap, QPainter, QPixmap
from PyQt5.QtNetwork import QLocalServer, QLocalSocket
from ui_update import Ui_Form
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, QBasicTimer
from downloadThread import downloadThread


class MainWindow(QMainWindow, Ui_Form):
    def __init__(self, now_version=None, new_version=None, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        self.setWindowFlags(
            Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)  # 窗口无边框
        # self.setAttribute(Qt.WA_TranslucentBackground)  # 窗框透明
        self.label.setAttribute(Qt.WA_TranslucentBackground)
        self.label_speed.setAttribute(Qt.WA_TranslucentBackground)
        self.label_cont.setAttribute(Qt.WA_TranslucentBackground)
        self.pushButton_close.setAttribute(Qt.WA_TranslucentBackground)

        self.now_version = now_version
        self.new_version = new_version
        self.count = new_version - now_version
        self.filesize = 0
        self.offset = 0
        self.old_time = time.time()
        self.timer = QBasicTimer()

        self.label_cont.setText('更新包：0/' + str(self.count))

        self.downloadThread = downloadThread(self.now_version, self.count, 10240)
        self.downloadThread.signal_download_proess.connect(self.changeprogressBar)
        self.downloadThread.signal_download_end.connect(self.end)
        self.downloadThread.start()
        self.timer.start(500, self)

        self.pushButton_close.clicked.connect(self.close)
        self.pushButton_remove.clicked.connect(self.showMinimized)

    #     self.pix = QBitmap('./img/100.png')
    #     self.resize(self.pix.size())
    #     self.setMask(self.pix.mask())
    #
    # def paintEvent(self, event):
    #     painter = QPainter(self)
    #     painter.drawPixmap(0,0,self.pix.width(),self.pix.height(),QPixmap('./img/100.png'))

    def end(self):
        sss = "DigWord.exe"
        subprocess.Popen(sss)
        self.close()

    def changeprogressBar(self, proess, count, offset, filesize):
        try:
            self.filesize = filesize
            self.offset = offset
            self.label_cont.setText('更新包：' + str(count) + '/' + str(self.count))
            self.progressBar.setValue(proess)
        except Exception as e:
            print(e)

    def timerEvent(self, e):
        t = time.time() - self.old_time
        offset = self.offset / t
        self.label_speed.setText(str(format(round(offset / 1024, 2), ',')) + ' KB/s  ' + str(
            format(round(self.filesize / 1024000, 2), ',')) + 'MB')

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False


def main(now_version, new_version):
    try:
        app = QApplication(sys.argv)
        serverName = 'dig_word_update_Server'
        socket = QLocalSocket()
        socket.connectToServer(serverName)
        # 如果连接成功，表明server已经存在，当前已有实例在运行
        if socket.waitForConnected(500):
            app.quit()
        else:
            localServer = QLocalServer()  # 没有实例运行，创建服务器
            localServer.listen(serverName)
            # 处理其他
            win = MainWindow(now_version, new_version)
            win.show()
            sys.exit(app.exec_())
    except Exception as e:
        app.quit()


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "p:")
        result = re.search('now_version=(.*?),new_version=(.*?);',opts[0][1])
        now_version = result[1].replace('.','')
        new_version = result[2].replace('.','')
        main(int(now_version),int(new_version))
    except Exception as e:
        print(e)