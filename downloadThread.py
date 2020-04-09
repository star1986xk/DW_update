#-*-coding: UTF-8 -*-
import os

import requests
from PyQt5.QtCore import QThread, pyqtSignal
import zipfile

class downloadThread(QThread):
    signal_download_proess = pyqtSignal(int,int,int,int)
    signal_download_end = pyqtSignal()

    def __init__(self, now_version, filecount, buffer):
        super(downloadThread, self).__init__()
        self.now_version = now_version
        self.filecount = filecount
        self.buffer = buffer
        self.offset = 0

        self.url_down = 'http://www.bingshanciku.com/update/{}'

    def download(self,url,count):
        try:
            response = requests.get(url, stream=True)
            filesize = int(response.headers['Content-Length'])
            offset = 0
            with open(url.split('/')[-1], 'wb') as f:
                for chunk in response.iter_content(chunk_size=self.buffer):
                    f.write(chunk)
                    offset = offset + len(chunk)
                    proess = offset / filesize * 100
                    self.offset += len(chunk)
                    self.signal_download_proess.emit(int(proess),count,self.offset,filesize)
        except Exception as e:
            print(e)

    def run(self):
        try:
            for i in range(1, self.filecount + 1):
                A = list(str(self.now_version + i))[0]
                B = list(str(self.now_version + i))[1]
                C = list(str(self.now_version + i))[2]
                D = list(str(self.now_version + i))[3]
                zipName = 'dig_word_update{}.{}.{}.{}.zip'.format(A, B, C, D)
                self.download(self.url_down.format(zipName),i)
                zfile = zipfile.ZipFile("./{}".format(zipName), "r")
                zfile.extractall()
                zfile.close()
                if os.path.exists("./{}".format(zipName)):
                        os.remove("./{}".format(zipName))
            self.signal_download_end.emit()
        except Exception as e:
            print(e)
