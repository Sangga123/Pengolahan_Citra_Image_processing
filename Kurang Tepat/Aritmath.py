from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import  QFileDialog, QProgressBar
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt


class Ui_Aritmath(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(940, 478)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 70, 300, 300))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 70, 300, 300))
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(630, 70, 300, 300))
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setText("")
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 40, 111, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 40, 111, 16))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(720, 40, 111, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.progress_bar = QProgressBar(self.centralwidget)
        self.progress_bar.setGeometry(QtCore.QRect(720, 400, 201, 20))
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("loading")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 657, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuPenjumlahan = QtWidgets.QMenu(self.menubar)
        self.menuPenjumlahan.setObjectName("menuPenjumlahan")
        self.menuOperasi_lain = QtWidgets.QMenu(self.menubar)
        self.menuOperasi_lain.setObjectName("menuOperasi_lain")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionInput_Gambar_2 = QtWidgets.QAction(MainWindow)
        self.actionInput_Gambar_2.setObjectName("actionInput_Gambar_2")
        self.actionInput_Gambar_2.triggered.connect(self.open_image1)
        self.actionInput_Gambar_3 = QtWidgets.QAction(MainWindow)
        self.actionInput_Gambar_3.setObjectName("actionInput_Gambar_3")
        self.actionInput_Gambar_3.triggered.connect(self.open_image2)
        self.actionSimpan = QtWidgets.QAction(MainWindow)
        self.actionSimpan.setObjectName("actionSimpan")
        self.actionSimpan.triggered.connect(self.save_image)
        self.actionKeluar = QtWidgets.QAction(MainWindow)
        self.actionKeluar.setObjectName("actionKeluar")
        self.actionKeluar.triggered.connect(self.exit_confirmation)
        self.actionPenjumlahan = QtWidgets.QAction(MainWindow)
        self.actionPenjumlahan.setObjectName("actionPenjumlahan")
        self.actionPenjumlahan.triggered.connect(self.penjumlahan_operation)
        self.actionPengurangan = QtWidgets.QAction(MainWindow)
        self.actionPengurangan.setObjectName("actionPengurangan")
        self.actionPengurangan.triggered.connect(self.pengurangan_operation)
        self.actionPerkalian = QtWidgets.QAction(MainWindow)
        self.actionPerkalian.setObjectName("actionPerkalian")
        self.actionPerkalian.triggered.connect(self.perkalian_operation)
        self.actionPembagian = QtWidgets.QAction(MainWindow)
        self.actionPembagian.setObjectName("actionPembagian")
        self.actionPembagian.triggered.connect(self.pembagian_operation)
        self.actionAnd = QtWidgets.QAction(MainWindow)
        self.actionAnd.setObjectName("actionAnd")
        self.actionAnd.triggered.connect(self.and_operation)
        self.actionOr = QtWidgets.QAction(MainWindow)
        self.actionOr.setObjectName("actionOr")
        self.actionOr.triggered.connect(self.or_operation)
        self.actionNOT = QtWidgets.QAction(MainWindow)
        self.actionNOT.setObjectName("actionNOT")
        self.actionNOT.triggered.connect(self.not_operation)
        self.menuFile.addAction(self.actionInput_Gambar_2)
        self.menuFile.addAction(self.actionInput_Gambar_3)
        self.menuFile.addAction(self.actionSimpan)
        self.menuFile.addAction(self.actionKeluar)
        self.menuPenjumlahan.addAction(self.actionPenjumlahan)
        self.menuPenjumlahan.addAction(self.actionPengurangan)
        self.menuPenjumlahan.addAction(self.actionPerkalian)
        self.menuPenjumlahan.addAction(self.actionPembagian)
        self.menuOperasi_lain.addAction(self.actionAnd)
        self.menuOperasi_lain.addAction(self.actionOr)
        self.menuOperasi_lain.addAction(self.actionNOT)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPenjumlahan.menuAction())
        self.menubar.addAction(self.menuOperasi_lain.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aritmatic Operations"))
        self.label_4.setText(_translate("MainWindow", "Input Image 1"))
        self.label_5.setText(_translate("MainWindow", "Input Image 2"))
        self.label_6.setText(_translate("MainWindow", "Output"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuPenjumlahan.setTitle(_translate("MainWindow", "Operasi"))
        self.menuOperasi_lain.setTitle(_translate("MainWindow", "Operasi lain"))
        self.actionInput_Gambar_2.setText(_translate("MainWindow", "Input Image 1"))
        self.actionInput_Gambar_3.setText(_translate("MainWindow", "Input Image 2"))
        self.actionSimpan.setText(_translate("MainWindow", "Save"))
        self.actionKeluar.setText(_translate("MainWindow", "Exit"))
        self.actionPenjumlahan.setText(_translate("MainWindow", "Penjumlahan"))
        self.actionPengurangan.setText(_translate("MainWindow", "Pengurangan"))
        self.actionPerkalian.setText(_translate("MainWindow", "Perkalian"))
        self.actionPembagian.setText(_translate("MainWindow", "Pembagian"))
        self.actionAnd.setText(_translate("MainWindow", "AND"))
        self.actionOr.setText(_translate("MainWindow", "OR"))
        self.actionNOT.setText(_translate("MainWindow", "NOT"))
        
    def open_image1(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly 
        self.label_2.clear()
        file_name, _ = QFileDialog.getOpenFileName(None, "Open Image File", "", "Images (*.png *.jpg *.bmp *.jpeg);;All Files (*)", options=options)
        if file_name:
            image = QtGui.QImage(file_name)
            if not image.isNull():
                pixmap = QtGui.QPixmap.fromImage(image)
                self.label.setPixmap(pixmap) 
                self.label.setScaledContents(True) 
                self.image1 = image  # Inisialisasi variabel image1

    def open_image2(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly 
        self.label_3.clear()
        file_name, _ = QFileDialog.getOpenFileName(None, "Open Image File", "", "Images (*.png *.jpg *.bmp *.jpeg);;All Files (*)", options=options)
        if file_name:
            image = QtGui.QImage(file_name)
            if not image.isNull():
                pixmap = QtGui.QPixmap.fromImage(image)
                self.label_2.setPixmap(pixmap) 
                self.label_2.setScaledContents(True) 
                self.image2 = image  # Inisialisasi variabel image2
    
    def save_image(self):
        if hasattr(self, 'gambars'):
            # Inisialisasi opsi untuk dialog pemilihan berkas
            options = QFileDialog.Options()
            # Menambahkan opsi mode baca saja ke dalam opsi dialog
            options |= QFileDialog.ReadOnly 
            # menampung file path dari dialog open file dan difilter hanya format png , jpg , bmp
            file_name, _ = QFileDialog.getSaveFileName(None, "Save Image File", "", "Images (*.png *.jpg *.bmp *.jpeg);;All Files (*)", options=options)
            # check apakah terdapat path file
            if file_name:
                #Simpan gambar yang telah diformat
                self.gambars.save(file_name)  
                
    def and_operation(self):
        if self.image1 is not None and self.image2 is not None:
            width = min(self.image1.width(), self.image2.width())
            height = min(self.image1.height(), self.image2.height())
            result_and = QImage(width, height, QImage.Format_RGB888)

            for x in range(width):
                for y in range(height):
                    color1 = QtGui.QColor(self.image1.pixelColor(x, y))
                    color2 = QtGui.QColor(self.image2.pixelColor(x, y))
                        
                    r_result = color1.red() & color2.red()
                    g_result = color1.green() & color2.green()
                    b_result = color1.blue() & color2.blue()

                    result_pixel = QtGui.qRgb(r_result, g_result, b_result)
                    result_and.setPixel(x, y, result_pixel)

            result_pixmap = QPixmap.fromImage(result_and)
            self.label_3.setPixmap(result_pixmap)
            self.label_3.setScaledContents(True)
            self.gambars = result_and
                    # Perbarui ProgressBar setelah operasi selesai
            self.progress_bar.setProperty("value", 100)
            
        else:
            # Tampilkan notifikasi jika citra tidak ada
            QMessageBox.warning(None, 'Peringatan', 'Citra belum dipilih. Pilih citra terlebih dahulu untuk diolah.')
            
    def perkalian_operation(self):
        if self.image1 is not None and self.image2 is not None:
            width = min(self.image1.width(), self.image2.width())
            height = min(self.image1.height(), self.image2.height())
            result_kali = QImage(width, height, QImage.Format_RGB888)

            for x in range(width):
                for y in range(height):
                    color1 = QtGui.QColor(self.image1.pixelColor(x, y))
                    color2 = QtGui.QColor(self.image2.pixelColor(x, y))

                    r_result = min(color1.red() * color2.red(), 255)  # Batasan nilai maksimum
                    g_result = min(color1.green() * color2.green(), 255)  # Batasan nilai maksimum
                    b_result = min(color1.blue() * color2.blue(), 255)  # Batasan nilai maksimum

                    result_pixel = QtGui.qRgb(r_result, g_result, b_result)
                    result_kali.setPixel(x, y, result_pixel)

            result_pixmap = QPixmap.fromImage(result_kali)
            self.label_3.setPixmap(result_pixmap)
            self.label_3.setScaledContents(True)
            self.gambars = result_kali
            self.progress_bar.setProperty("value", 100)
            
        else:
            # Tampilkan notifikasi jika citra tidak ada
            QMessageBox.warning(None, 'Peringatan', 'Citra belum dipilih. Pilih citra terlebih dahulu untuk diolah.')
            
    def pembagian_operation(self):
        if self.image1 is not None and self.image2 is not None:
            width = min(self.image1.width(), self.image2.width())
            height = min(self.image1.height(), self.image2.height())
            result_bagi = QImage(width, height, QImage.Format_RGB888)

            for x in range(width):
                for y in range(height):
                    color1 = QtGui.QColor(self.image1.pixelColor(x, y))
                    color2 = QtGui.QColor(self.image2.pixelColor(x, y))

                    # Hindari pembagian oleh nol atau nilai yang sangat kecil
                    divisorRed = max(color2.red(), 1)
                    divisorgreen = max(color2.green(),1)
                    divisorBlue = max(color2.blue(),1)
                    
                    r_result = max(round(color1.red() / divisorRed), 0)  # Batasan nilai maksimum
                    g_result = max(round(color1.green() / divisorgreen), 0)  # Batasan nilai maksimum
                    b_result = max(round(color1.blue() / divisorBlue), 0)  # Batasan nilai maksimum

                    result_pixel = QtGui.qRgb(r_result, g_result, b_result)
                    result_bagi.setPixel(x, y, result_pixel)

            result_pixmap = QPixmap.fromImage(result_bagi)
            self.label_3.setPixmap(result_pixmap)
            self.label_3.setScaledContents(True)
            self.gambars = result_bagi 
            self.progress_bar.setProperty("value", 100)
            
        else:
            # Tampilkan notifikasi jika citra tidak ada
            QMessageBox.warning(None, 'Peringatan', 'Citra belum dipilih. Pilih citra terlebih dahulu untuk diolah.')
                           
    def pengurangan_operation(self):
        if self.image1 is not None and self.image2 is not None:
            width = min(self.image1.width(), self.image2.width())
            height = min(self.image1.height(), self.image2.height())
            result_min = QImage(width, height, QImage.Format_RGB888)

            for x in range(width):
                for y in range(height):
                    color1 = QtGui.QColor(self.image1.pixelColor(x, y))
                    color2 = QtGui.QColor(self.image2.pixelColor(x, y))

                    r_result = max(color1.red() - color2.red(), 0)  # Batasan nilai minimum
                    g_result = max(color1.green() - color2.green(), 0)  # Batasan nilai minimum
                    b_result = max(color1.blue() - color2.blue(), 0)  # Batasan nilai minimum

                    result_pixel = QtGui.qRgb(r_result, g_result, b_result)
                    result_min.setPixel(x, y, result_pixel)

            result_pixmap = QPixmap.fromImage(result_min)
            self.label_3.setPixmap(result_pixmap)
            self.label_3.setScaledContents(True)
            self.gambars = result_min
            self.progress_bar.setProperty("value", 100)
        
        else:
            # Tampilkan notifikasi jika citra tidak ada
            QMessageBox.warning(None, 'Peringatan', 'Citra belum dipilih. Pilih citra terlebih dahulu untuk diolah.')
                    
    def penjumlahan_operation(self):
        if self.image1 is not None and self.image2 is not None:
            width = min(self.image1.width(), self.image2.width())
            height = min(self.image1.height(), self.image2.height())
            result_plus = QImage(width, height, QImage.Format_RGB888)

            for x in range(width):
                for y in range(height):
                    color1 = QtGui.QColor(self.image1.pixelColor(x, y))
                    color2 = QtGui.QColor(self.image2.pixelColor(x, y))

                    r_result = min(color1.red() + color2.red(),255)
                    g_result = min(color1.green() + color2.green(),255)
                    b_result = min(color1.blue() + color2.blue(),255)

                    result_pixel = QtGui.qRgb(r_result, g_result, b_result)
                    result_plus.setPixel(x, y, result_pixel)

            result_pixmap = QPixmap.fromImage(result_plus)
            self.label_3.setPixmap(result_pixmap)
            self.label_3.setScaledContents(True)
            self.gambars = result_plus
            self.progress_bar.setProperty("value", 100)
            
        else:
            # Tampilkan notifikasi jika citra tidak ada
            QMessageBox.warning(None, 'Peringatan', 'Citra belum dipilih. Pilih citra terlebih dahulu untuk diolah.')
                    
    def or_operation(self):
        if self.image1 is not None and self.image2 is not None:
            width = min(self.image1.width(), self.image2.width())
            height = min(self.image1.height(), self.image2.height())
            result_orop = QImage(width, height, QImage.Format_RGB888)

            for x in range(width):
                for y in range(height):
                    color1 = QtGui.QColor(self.image1.pixelColor(x, y))
                    color2 = QtGui.QColor(self.image2.pixelColor(x, y))

                    r_result = color1.red() | color2.red()
                    g_result = color1.green() | color2.green()
                    b_result = color1.blue() | color2.blue()

                    result_pixel = QtGui.qRgb(r_result, g_result, b_result)
                    result_orop.setPixel(x, y, result_pixel)

            result_pixmap = QPixmap.fromImage(result_orop)
            self.label_3.setPixmap(result_pixmap)
            self.label_3.setScaledContents(True)
            self.gambars = result_orop
            self.progress_bar.setProperty("value", 100)
            
        else:
            # Tampilkan notifikasi jika citra tidak ada
            QMessageBox.warning(None, 'Peringatan', 'Citra belum dipilih. Pilih citra terlebih dahulu untuk diolah.')
            
    def not_operation(self):
        if self.image1 is not None and self.image2 is not None:
            width = min(self.image1.width(), self.image2.width())
            height = min(self.image1.height(), self.image2.height())
            result_notop = QImage(width, height, QImage.Format_RGB888)

            for x in range(width):
                for y in range(height):
                    color1 = QtGui.QColor(self.image1.pixelColor(x, y))
                    color2 = QtGui.QColor(self.image2.pixelColor(x, y))

                    r_result = 255 - color2.red()
                    g_result = 255 - color2.green()
                    b_result = 255 - color2.blue()

                    result_pixel = QtGui.qRgb(r_result, g_result, b_result)
                    result_notop.setPixel(x, y, result_pixel)

            result_pixmap = QPixmap.fromImage(result_notop)
            self.label_3.setPixmap(result_pixmap)
            self.label_3.setScaledContents(True)
            self.gambars = result_notop
            self.progress_bar.setProperty("value", 100)
            
        else:
        # Tampilkan notifikasi jika citra tidak ada
            QMessageBox.warning(None, 'Peringatan', 'Citra belum dipilih. Pilih citra terlebih dahulu untuk diolah.')
               
    def save_image(self):
        if hasattr(self, 'gambars'):
            # Inisialisasi opsi untuk dialog pemilihan berkas
            options = QFileDialog.Options()
            # Menambahkan opsi mode baca saja ke dalam opsi dialog
            options |= QFileDialog.ReadOnly 
            # menampung file path dari dialog open file dan difilter hanya format png , jpg , bmp
            file_name, _ = QFileDialog.getSaveFileName(None, "Save Image File", "", "Images (*.png *.jpg *.bmp *.jpeg);;All Files (*)", options=options)
            # check apakah terdapat path file
            if file_name:
                #Simpan gambar yang telah diformat
                self.gambars.save(file_name)  
    
    def exit_confirmation(self):
        reply = QMessageBox.question(None, 'Konfirmasi Keluar', 'Apakah Anda yakin ingin keluar?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.exit_application()
            
    def exit_application(self):
        QtWidgets.qApp.quit()
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Aritmath()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
