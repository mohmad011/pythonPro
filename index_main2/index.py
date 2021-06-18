##PyQT5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
## from PyQt5.uic import loadUiType
import os
from os import path
import sys
import pafy
import youtube_dl
import urllib.request
import humanize
##### import UI File

from main import Ui_MainWindow

## FORM_CLASS,_= loadUiType(path.join(path.dirname(__file__),'main.ui'))


########## Intiate UO File

##class MainApp(QMainWindow , FORM_CLASS):

class MainApp(QMainWindow , Ui_MainWindow):
    
    def __init__(self , parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI()
        self.Handel_buttons()
    def Handel_UI(self):
        self.setWindowTitle('MoDownloader')
        self.setFixedSize(651 , 361 )
    def Handel_buttons(self):
        self.pushButton.clicked.connect(self.Handel_download)
        self.pushButton_2.clicked.connect(self.Handel_brows)
        self.pushButton_9.clicked.connect(self.Get_Youtube_Vedio)
        self.pushButton_5.clicked.connect(self.Download_Youtube_Vedio)
        self.pushButton_6.clicked.connect(self.Save_Brows)
        self.pushButton_8.clicked.connect(self.Save_Brows_Playlist)
        self.pushButton_7.clicked.connect(self.Playlist_Vedio_Download)
        self.pushButton_11.clicked.connect(self.Playlist_Audio_Download)
        ## self.pushButton_10.clicked.connect(self.Get_Playlist_Vedio)

#####################################################################################################################  Download Any File

    def Handel_brows(self):
        save_place = QFileDialog.getSaveFileName(self , caption="Save As" , directory='.' , filter='All Files (*.*)')
        text = str(save_place)
        x = text
        for r in (("(", ''), ("'", '') , (", All Files *.*))" , '')):
            x = x.replace(*r)
        print(x)
        self.lineEdit_2.setText(x)
    def Handel_progres(self , blocknum , blocksize , totalsize):
        read = blocknum * blocksize

        if totalsize > 0 :
            percent = read * 100 / totalsize
            self.progressBar.setValue(percent)
            QApplication.processEvents()

    def Handel_download(self):
        # url - save location - progress

        url = self.lineEdit.text()
        save_location = self.lineEdit_2.text()
        try:
            urllib.request.urlretrieve(url , save_location , self.Handel_progres)
        except Exception:
            QMessageBox.warning(self, 'Download Error', 'The Download Faild')
            return
        QMessageBox.information(self , 'Download Completed' , 'The Download Finished')
        self.progressBar.setValue(0)
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        
#####################################################################################################################  Downloader_Youtube_Vedio
        
    def Save_Brows(self):
        try:
            save = QFileDialog.getExistingDirectory(self , 'Select Download Directory')
            self.lineEdit_6.setText(save)
        except Exception:
            QMessageBox.warning(self, 'Save Error', 'Please select folder')

    def Get_Youtube_Vedio(self):
        video_link = self.lineEdit_5.text()
        v = pafy.new(video_link)
        st = v.allstreams
        for s in st:
            size = humanize.naturalsize(s.get_filesize()) ## for return to Mgbyte
            data = '{} {} {} {}'.format(s.mediatype , s.extension , s.quality  , size )
            self.comboBox_3.addItem(data)
        QApplication.processEvents()


    def Download_Youtube_Vedio(self):
        video_link = self.lineEdit_5.text()
        save_location = self.lineEdit_6.text()
        v = pafy.new(video_link)
        st = v.allstreams
        quality = self.comboBox_3.currentIndex()
        down = st[quality].download(filepath=save_location)
        QMessageBox.information(self, 'Download Completed', 'The Download Finished')
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.comboBox_3.clear()
        QApplication.processEvents()
        
#####################################################################################################################  Playlist_Downloader
        
    def Save_Brows_Playlist(self):
        try:
            save = QFileDialog.getExistingDirectory(self , 'Select Download Directory')
            self.lineEdit_8.setText(save)
        except Exception:
            QMessageBox.warning(self, 'Save Error', 'Please select folder')

    '''
    
    def Get_Playlist_Vedio(self):
        playlist_link = self.lineEdit_7.text()
        v = pafy.new(playlist_link)
        data = '{} \n \n {}'.format(v.getbestaudio(preftype='any') , v.getbestvideo(preftype='any') )
        self.comboBox_2.addItem(data)
        QApplication.processEvents()

    '''
    
    def Playlist_Vedio_Download(self):
        playlist_link = self.lineEdit_7.text()
        save_location = self.lineEdit_8.text()
        playlist = pafy.get_playlist(playlist_link)
        vedios = playlist['items']

        os.chdir(save_location)
        if os.path.exists(str(playlist['title'])):
            os.chdir(str(playlist['title']))
        else:
            os.mkdir(str(playlist['title']))
            os.chdir(str(playlist['title']))

        for vedio in vedios:
            p = vedio['pafy']
            best = p.getbest(preftype='mp4')
            best.download()
        QMessageBox.information(self, 'Download Completed', 'The Download Finished')

                
    def Playlist_Audio_Download(self): ## pushButton_11
        playlist_link = self.lineEdit_7.text()
        save_location = self.lineEdit_8.text()
        playlist = pafy.get_playlist(playlist_link)
        vedios = playlist['items']

        os.chdir(save_location)
        if os.path.exists(str(playlist['title'])):
            os.chdir(str(playlist['title']))
        else:
            os.mkdir(str(playlist['title']))
            os.chdir(str(playlist['title']))

        for vedio in vedios:
            p = vedio['pafy']
            try:
                best = p.getbestaudio(preftype='mp3')
                best.download()
            except Exception:
                best = p.getbestaudio(preftype='any')
                best.download()
        QMessageBox.information(self, 'Download Completed', 'The Download Finished')



def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_() #infinte loop

if __name__ == '__main__':
    main()


