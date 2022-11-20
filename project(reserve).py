import os
import sys
import wave

import pyaudio
from PyQt5 import QtCore, QtMultimedia, QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QSound
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w3 = None
        self.w2 = None
        uic.loadUi('project.ui', self)

        self.hat.clicked.connect(QSound(f'drum/hat.wav', self).play)
        self.hat2.clicked.connect(QSound(f'drum/hat2.wav', self).play)
        self.kick.clicked.connect(QSound(f'drum/kick.wav', self).play)
        self.kick2.clicked.connect(QSound(f'drum/kick2.wav', self).play)
        self.clap.clicked.connect(QSound(f'drum/clap.wav', self).play)
        self.open_hat.clicked.connect(QSound(f'drum/open_hat.wav', self).play)

        self.instrument = 'Пианино'

        self.s = QSound('drum', self)

        self.horizontalSlider.valueChanged.connect(self.change_volume)

        self.tool.clicked.connect(self.remember)

        self.openWindow2.clicked.connect(self.show_window_2)  # Октрыть диалоговое окно1
        self.openWindow3.clicked.connect(self.show_window_3)  # Октрыть диалоговое окно1

        # Словарь (ключ - выбранный пользаваетиле инструмент)
        # где элемент - название папки со звуками
        self.instrument_number = {'Пианино': 'pianino',
                                  'Саксофон': 'Alto sax', 'Колокола': 'Ball'}

        # Первая актава
        self.pBtn_C.clicked.connect(self.C)
        self.pBtn_Cd.clicked.connect(self.Cd)
        self.pBtn_D.clicked.connect(self.D)
        self.pBtn_Dd.clicked.connect(self.Dd)
        self.pBtn_E.clicked.connect(self.E)
        self.pBtn_F.clicked.connect(self.F)
        self.pBtn_Fd.clicked.connect(self.Fd)
        self.pBtn_G.clicked.connect(self.G)
        self.pBtn_Gd.clicked.connect(self.Gd)
        self.pBtn_A.clicked.connect(self.A)
        self.pBtn_Ad.clicked.connect(self.Ad)
        self.pBtn_B.clicked.connect(self.B)
        # Вторая актава
        self.pBtn_C2.clicked.connect(self.C2)
        self.pBtn_Cd2.clicked.connect(self.Cd2)
        self.pBtn_D2.clicked.connect(self.D2)
        self.pBtn_Dd2.clicked.connect(self.Dd2)
        self.pBtn_E2.clicked.connect(self.E2)
        self.pBtn_F2.clicked.connect(self.F2)
        self.pBtn_Fd2.clicked.connect(self.Fd2)
        self.pBtn_G2.clicked.connect(self.G2)
        self.pBtn_Gd2.clicked.connect(self.Gd2)
        self.pBtn_A2.clicked.connect(self.A2)
        self.pBtn_Ad2.clicked.connect(self.Ad2)
        self.pBtn_B2.clicked.connect(self.B2)

        self.player = QMediaPlayer()  # Создание плеера

    def keyPressEvent(self, event):
        # Первая актава
        if event.key() == Qt.Key_Q:
            url = QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-do.wav'))
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        if event.key() == Qt.Key_2:
            url = QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-do#.wav'))
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        if event.key() == Qt.Key_W:
            url = QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-re.wav'))
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        if event.key() == Qt.Key_3:
            url = QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-re#.wav'))
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        if event.key() == Qt.Key_E:
            url = QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-mi.wav'))
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        if event.key() == Qt.Key_R:
            url = QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-fa.wav'))
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        if event.key() == Qt.Key_5:
            url = QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-fa#.wav'))
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        if event.key() == Qt.Key_T:
            url = QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-sol.wav'))
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        if event.key() == Qt.Key_6:
            url = QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-sol#.wav'))
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        if event.key() == Qt.Key_Y:
            url = QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-lya.wav'))
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        if event.key() == Qt.Key_7:
            url = QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-lya#.wav'))
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        if event.key() == Qt.Key_U:
            url = QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-si.wav'))
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        # Вторая актава
        if event.key() == Qt.Key_Z:
            url = QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-do2.wav'))
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        if event.key() == Qt.Key_S:
            url = QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-do#2.wav'))
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        if event.key() == Qt.Key_X:
            url = QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-re2.wav'))
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        if event.key() == Qt.Key_D:
            url = QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-re#2.wav'))
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        if event.key() == Qt.Key_C:
            url = QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-mi.wav'))
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        if event.key() == Qt.Key_V:
            url = QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-fa2.wav'))
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        if event.key() == Qt.Key_G:
            url = QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-fa#2.wav'))
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        if event.key() == Qt.Key_B:
            url = QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-sol2.wav'))
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        if event.key() == Qt.Key_H:
            url = QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-sol#2.wav'))
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        if event.key() == Qt.Key_N:
            url = QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-lya2.wav'))
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        if event.key() == Qt.Key_J:
            url = QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-lya#2.wav'))
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        if event.key() == Qt.Key_M:
            url = QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-si2.wav'))
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        # Драм партия
        if event.key() == Qt.Key_8:
            self.s.play(f'drum/hat.wav')
        if event.key() == Qt.Key_9:
            self.s.play(f'drum/hat2.wav')
        if event.key() == Qt.Key_0:
            self.s.play(f'drum/kick.wav')
        if event.key() == Qt.Key_I:
            self.s.play(f'drum/kick2.wav')
        if event.key() == Qt.Key_O:
            self.s.play(f'drum/clap.wav')
        if event.key() == Qt.Key_P:
            self.s.play(f'drum/open_hat.wav')

    # Первая актава
    def C(self):
        url = QUrl.fromLocalFile(
            os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-do.wav'))
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    def Cd(self):
        url = QUrl.fromLocalFile(
            os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-do#.wav'))
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    def D(self):
        url = QUrl.fromLocalFile(
            os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-re.wav'))
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    def Dd(self):
        url = QUrl.fromLocalFile(
            os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-re#.wav'))
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    def E(self):
        url = QUrl.fromLocalFile(
            os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-mi.wav'))
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    def F(self):
        url = QUrl.fromLocalFile(
            os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-fa.wav'))
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    def Fd(self):
        url = QUrl.fromLocalFile(
            os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-fa#.wav'))
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    def G(self):
        url = QUrl.fromLocalFile(
            os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-sol.wav'))
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    def Gd(self):
        url = QUrl.fromLocalFile(
            os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-sol#.wav'))
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    def A(self):
        url = QUrl.fromLocalFile(
            os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-lya.wav'))
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    def Ad(self):
        url = QUrl.fromLocalFile(
            os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-lya#.wav'))
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    def B(self):
        url = QUrl.fromLocalFile(
            os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-si.wav'))
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    # Вторая актава
    def C2(self):
        url = QUrl.fromLocalFile(
            os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-do2.wav'))
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    def Cd2(self):
        url = QUrl.fromLocalFile(
            os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-do#2.wav'))
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    def D2(self):
        url = QUrl.fromLocalFile(
            os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-re2.wav'))
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    def Dd2(self):
        url = QUrl.fromLocalFile(
            os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-re#2.wav'))
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    def E2(self):
        url = QUrl.fromLocalFile(
            os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-mi2.wav'))
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    def F2(self):
        url = QUrl.fromLocalFile(
            os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-fa2.wav'))
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    def Fd2(self):
        url = QUrl.fromLocalFile(
            os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-fa#2.wav'))
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    def G2(self):
        url = QUrl.fromLocalFile(
            os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-sol2.wav'))
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    def Gd2(self):
        url = QUrl.fromLocalFile(
            os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-sol#2.wav'))
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    def A2(self):
        url = QUrl.fromLocalFile(
            os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-lya2.wav'))
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    def Ad2(self):
        url = QUrl.fromLocalFile(
            os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-lya#2.wav'))
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    def B2(self):
        url = QUrl.fromLocalFile(
            os.path.join(os.getcwd(), f'piano sounds/{self.instrument_number[self.instrument]}/nots-si2.wav'))
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    def change_volume(self):  # Функция изменения громкости звука
        self.player.setVolume(self.horizontalSlider.value())
        self.label.setText(str(self.horizontalSlider.value()))

    def show_window_2(self):
        self.w2 = Window2()
        self.w2.show()

    def show_window_3(self):
        self.w3 = Window3()
        self.w3.show()

    def remember(self):
        self.instrument = self.buttonGroup_2.checkedButton().text()  # Выбор инструмента
        self.label_2.setText(f'Выбран {self.buttonGroup_2.checkedButton().text()}')


class Window2(QMainWindow):
    def __init__(self):
        super(Window2, self).__init__()
        uic.loadUi('window2.ui', self)
        self.number = []
        self.p = pyaudio.PyAudio()
        # Цикл находящий все устройсва ввода звука
        for i in range(self.p.get_device_count()):
            if self.p.get_device_info_by_index(i)['name'].encode('cp1251').decode('utf-8')[0:8] == 'Микрофон':
                self.number.append(i)
                a = i, self.p.get_device_info_by_index(i)['name'].encode('cp1251').decode('utf-8')
                self.listWidget.addItem(str(a)[1:len(str(a)) - 1])

        self.Play.clicked.connect(self.recording)

    def recording(self):  # Функция записи звука с выьраного устройства
        self.label_4.setText("")
        n = int(self.spinBox_3.text())
        time = int(self.spinBox_2.text())
        if n not in self.number:
            self.label_2.setText("Такого индекса нет")
            self.label_2.setStyleSheet('''QLabel {
           background-color: rgb(255, 115, 115);
           color: rgb(191, 79, 255);
           border-style: outset;
           border-width: 5px;
           border-radius: 10px;
           border-color: rgb(255, 53, 53)
        }''')
        else:
            self.label_2.setText("Все верно")
            self.label_2.setStyleSheet('''QLabel {
           background-color: rgb(0, 255, 127);
           color: rgb(0, 121, 56);
           border-style: outset;
           border-width: 5px;
           border-radius: 10px;
           border-color: rgb(0, 255, 127)
        }''')
            CHUNK = 1024
            FORMAT = pyaudio.paInt16
            CHANNELS = 2
            RATE = 44100
            RECORD_SECONDS = time + 1
            WAVE_OUTPUT_FILENAME = "voice/voice.wav"
            p = pyaudio.PyAudio()
            stream = p.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            input_device_index=n,
                            frames_per_buffer=CHUNK)

            frames = []
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)

            stream.stop_stream()
            stream.close()
            p.terminate()

            # Запись в wav формат
            wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()
            self.label_4.setText("Запись завершина")


class Window3(QMainWindow):
    def __init__(self):
        super(Window3, self).__init__()
        self.player = None
        uic.loadUi('window3.ui', self)
        # Диалоговое окно для выбора файла
        self.wb_patch = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Файл (*.mp3);;Файл(*.wav)')[0]

        self.load_mp3(self.wb_patch)

        self.playBtn.clicked.connect(self.player.play)
        self.pauseBtn.clicked.connect(self.player.pause)
        self.stopBtn.clicked.connect(self.player.stop)

        self.horizontalSlider.valueChanged.connect(self.change_volume)

    def load_mp3(self, filename):  # Функция открывает файл в медио плеере
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)

    def change_volume(self):  # Функция регулировки громкости
        self.player.setVolume(self.horizontalSlider.value())
        self.label.setText(str(self.horizontalSlider.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
