from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import requests



main_user = ""
selected = {'movie': '', 'seance': ''}

current_seance = None






class Info2(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 400)
        Dialog.setStyleSheet("background-color: rgb(148, 143, 124);")
        self.movie_list_2 = QtWidgets.QListWidget(Dialog)
        self.movie_list_2.setGeometry(QtCore.QRect(8, 151, 284, 240))
        self.movie_list_2.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 10px;\n"
"font-size: 20px \"Book Antiqua\";")
        self.movie_list_2.setObjectName("movie_list_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(8, 57, 126, 33))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(8, 9, 126, 33))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_2.setObjectName("label_2")
        self.title_text = QtWidgets.QLineEdit(Dialog)
        self.title_text.setGeometry(QtCore.QRect(146, 9, 146, 33))
        self.title_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font-size: 20px \"Book Antiqua\";")
        self.title_text.setObjectName("title_text")
        self.title_text.setReadOnly(True)
        self.seance_text = QtWidgets.QLineEdit(Dialog)
        self.seance_text.setGeometry(QtCore.QRect(146, 57, 146, 33))
        self.seance_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font-size: 20px \"Book Antiqua\";")
        self.seance_text.setObjectName("seance_text")
        self.seance_text.setReadOnly(True)

        self.get_movie_info()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Total Info"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Seance</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Title</span></p></body></html>"))

    def get_movie_info(self):
        count =  requests.get('http://viollenaki.pythonanywhere.com/get_movie_seances_count', params={'movie':selected["movie"]}).json()
        peoples = requests.get('http://viollenaki.pythonanywhere.com/get_movie_people', params={'movie':selected["movie"]}).json()
        self.title_text.setText(selected["movie"])
        self.seance_text.setText(str(count))
        arr = set()
        for i,j in peoples:
            arr.add(f'{i} --> {j}')
        for i in arr:
            self.movie_list_2.addItem(i)
class Info(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 400)
        Dialog.setStyleSheet("background-color: rgb(148, 143, 124);")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(8, 57, 126, 33))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(8, 9, 126, 33))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_2.setObjectName("label_2")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(8, 150, 284, 241))
        self.listWidget.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 10px;"
"font: 20px \"Book Antiqua\";")
        self.listWidget.setObjectName("listWidget")
        self.title_text = QtWidgets.QLineEdit(Dialog)
        self.title_text.setGeometry(QtCore.QRect(146, 9, 146, 33))
        self.title_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font-size: 20px \"Book Antiqua\";")
        self.title_text.setObjectName("title_text")
        self.title_text.setReadOnly(True)
        self.date_text = QtWidgets.QLineEdit(Dialog)
        self.date_text.setGeometry(QtCore.QRect(146, 57, 146, 33))
        self.date_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font-size: 20px \"Book Antiqua\";")
        self.date_text.setObjectName("date_text")
        self.date_text.setReadOnly(True)

        self.get_movie_info()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Info1"))
        # self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">People</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Date</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Title</span></p></body></html>"))

    def get_movie_info(self):
        self.date_text.setText(selected["seance"])
        self.title_text.setText(selected["movie"])
        people = requests.get('http://viollenaki.pythonanywhere.com/get_seance_people', params={'movie':selected["movie"], 'seance':selected["seance"]}).json()
        # self.people_quantity.setText(str(len(people)))
        arr = set()
        for i,j in people:
            arr.add(f'{i} --> {j}')
        for i in arr:
            self.listWidget.addItem(i)
class History(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 500)
        Dialog.setStyleSheet("background-color: rgb(148, 143, 124);")
        self.movie_list = QtWidgets.QListWidget(Dialog)
        self.movie_list.setGeometry(QtCore.QRect(21, 67, 261, 414))
        self.movie_list.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 10px;\n"
"font-size: 25px \"Book Antiqua\";")
        self.movie_list.setObjectName("movie_list")
        self.date_list = QtWidgets.QListWidget(Dialog)
        self.date_list.setGeometry(QtCore.QRect(318, 67, 261, 414))
        self.date_list.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 10px;\n"
"font-size: 20px \"Book Antiqua\";")
        self.date_list.setObjectName("date_list")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(351, 16, 195, 41))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(54, 16, 196, 41))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label.setObjectName("label")

        self.get_history()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "History"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">Date</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">Movies</span></p></body></html>"))

    def get_history(self):
        history = requests.get('http://viollenaki.pythonanywhere.com/get_user_history', params={'user':main_user}).json()
        for i in history:
            self.movie_list.addItem(i[0])
        self.movie_list.itemClicked.connect(self.fill_date_list)
    def fill_date_list(self):
        self.date_list.clear()
        history = requests.get('http://viollenaki.pythonanywhere.com/get_user_history', params={'user':main_user}).json()
        for i in history:
            if i[0] == self.movie_list.currentItem().text():
                self.date_list.addItem(i[1])


class AllHistory(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 500)
        Dialog.setStyleSheet("background-color: rgb(148, 143, 124);")
        self.users_list = QtWidgets.QListWidget(Dialog)
        self.users_list.setGeometry(QtCore.QRect(12, 75, 266, 415))
        self.users_list.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 10px;\n"
"font-size: 25px \"Book Antiqua\";")
        self.users_list.setObjectName("users_list")
        self.movie_list = QtWidgets.QListWidget(Dialog)
        self.movie_list.setGeometry(QtCore.QRect(322, 75, 266, 415))
        self.movie_list.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 10px;\n"
"font-size: 20px \"Book Antiqua\";")
        self.movie_list.setObjectName("movie_list")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(365, 18, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(55, 18, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_4.setObjectName("label_4")

        self.get_users_list()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "All History"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Movie | Date</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Users</span></p></body></html>"))

    def get_users_list(self):
        users = requests.get('http://viollenaki.pythonanywhere.com/get_users_list').json()
        for i in users:
            self.users_list.addItem(i)

        self.users_list.itemDoubleClicked.connect(self.get_user_history)

    def get_user_history(self):
        self.movie_list.clear()
        user = self.users_list.selectedItems()[0].text()
        arr = requests.get('http://viollenaki.pythonanywhere.com/get_user_history', params={'user':user}).json()
        history = set()
        for i in arr:
                history.add(i[0] + " | " + i[1])
        for i in history:
            self.movie_list.addItem(i)



class SeatGenerator(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.seats_now = []
        self.price = requests.get('http://viollenaki.pythonanywhere.com/get_movie_price', params={'movie': selected["movie"]}).json()
        self.total = 0


    def setupUi(self):
        self.setGeometry(100, 100, 1000, 700) 
        self.setWindowTitle('Seat Generator') 

        self.setStyleSheet("background-color: rgb(13, 44, 62);")
        
        self.buy = QtWidgets.QPushButton('Buy',self)
        self.buy.setGeometry(QtCore.QRect(390, 610, 226, 41))
        
        
        self.total_text = QtWidgets.QLabel(self)
        self.total_text.setGeometry(QtCore.QRect(670, 610, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(20)
        self.total_text.setFont(font)
        self.total_text.setStyleSheet("background-color: rgb(124, 166, 144);\n"
"border-radius: 20px;\n"
"")
        self.total_text.setObjectName("total_text")
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.buy.setFont(font)
        self.buy.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(23, 137, 143);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(14, 85, 89);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(124, 166, 144);\n"
"color: rgb(0, 0, 0);\n"
"font-size: 30px;\n"
"border-radius: 20px\n"
"}\n"
"")
        self.buy.clicked.connect(self.buy_ticket)


        
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(453, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(561, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(615, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_13 = QtWidgets.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(507, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_14 = QtWidgets.QLabel(self)
        self.label_14.setGeometry(QtCore.QRect(291, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_15 = QtWidgets.QLabel(self)
        self.label_15.setGeometry(QtCore.QRect(238, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_16 = QtWidgets.QLabel(self)
        self.label_16.setGeometry(QtCore.QRect(399, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_17 = QtWidgets.QLabel(self)
        self.label_17.setGeometry(QtCore.QRect(723, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_18 = QtWidgets.QLabel(self)
        self.label_18.setGeometry(QtCore.QRect(884, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_19 = QtWidgets.QLabel(self)
        self.label_19.setGeometry(QtCore.QRect(831, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_20 = QtWidgets.QLabel(self)
        self.label_20.setGeometry(QtCore.QRect(669, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_21 = QtWidgets.QLabel(self)
        self.label_21.setGeometry(QtCore.QRect(777, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background-color: rgb(13, 44, 62);\n")
        
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(76, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(130, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(184, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(346, 550, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")



        
        self.label = QtWidgets.QLabel('Screen',self)
        self.label.setGeometry(QtCore.QRect(47, 27, 905, 28))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(197, 158, 81);\n"
"border-radius: 14px;")
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#000000;\">Screen</span></p></body></html>"))

        
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(952, 104, 39, 428))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(8, 104, 39, 428))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(13, 44, 62);\n"
"border-radius: 10px;")
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">A</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">B</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">C</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">D</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">E</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">F</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">G</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">H</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">I</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">J</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">A</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">B</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">C</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">D</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">E</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">F</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">G</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">H</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">I</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">J</span></p></body></html>"))
        
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">1</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">2</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">3</span></p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">6</span></p></body></html>"))
        
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">8</span></p></body></html>"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">10</span></p></body></html>"))
        self.label_12.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">11</span></p></body></html>"))
        self.label_13.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">9</span></p></body></html>"))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">5</span></p></body></html>"))
        self.label_15.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">4</span></p></body></html>"))
        self.label_16.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">7</span></p></body></html>"))
        self.label_17.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">13</span></p></body></html>"))
        self.label_18.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">16</span></p></body></html>"))
        self.label_19.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">15</span></p></body></html>"))
        self.label_20.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">12</span></p></body></html>"))
        self.label_21.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">14</span></p></body></html>"))
        self.total_text.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">0$</p></body></html>"))
        self.create_buttons()







    def create_buttons(self):
        booked_seats = requests.get('http://viollenaki.pythonanywhere.com/get_movie_booked_seats', 
                                params={'movie': selected["movie"], 'seance': selected["seance"]}).json()
        rows = 'abcdefghij' 
        cols = 16  
        x_start, y_start = 76, 104  
        button_width, button_height = 41, 30  
        x_gap, y_gap = 54, 44 

        for i, row in enumerate(rows):
            for col in range(1, cols + 1):
                seat_id = f'{row}{col}'  
                x = x_start + (col - 1) * x_gap
                y = y_start + i * y_gap
                button = QtWidgets.QPushButton(self)
                button.setGeometry(x, y, button_width, button_height)
                button.setFont(QtGui.QFont('Arial', 10))

                button.clicked.connect(self.make_button_click_handler(seat_id, button))

                if seat_id not in booked_seats:
                     button.setStyleSheet(self.get_button_styles_free()) 
                else:
                     button.setStyleSheet(self.get_button_styles_booked())  # Style for booked seats
                     button.setEnabled(False)  # Disable booked buttons

    def make_button_click_handler(self, seat_id, button):
        def handler():
            self.toggle_seat(seat_id, button)
        return handler

    def toggle_seat(self, seat_id, button):
        if seat_id in self.seats_now:
            self.seats_now.remove(seat_id) 
            self.total -= self.price
            self.total_text.setText(f"<html><head/><body><p align=\"center\">{self.total}$</p></body></html>")
            button.setStyleSheet(self.get_button_styles_free()) 
        else:
            self.seats_now.append(seat_id) 
            self.total += self.price
            self.total_text.setText(f"<html><head/><body><p align=\"center\">{self.total}$</p></body></html>")
            button.setStyleSheet(self.get_button_styles_selected()) 

    def get_button_styles_free(self):
        return ("QPushButton:hover{\n"
        "    background-color: rgb(23, 137, 143);\n"
        "    color: rgb(255, 255, 255);\n"
        "    font-size: 30px;\n"
        "    border-radius: 8px\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color:rgb(14, 85, 89);\n"
        "    color: rgb(255, 255, 255);\n"
        "    font-size: 30px;\n"
        "    border-radius: 8px\n"
        "}\n"
        "QPushButton{\n"
        "background-color: rgb(124, 166, 144);\n"
        "color: rgb(0, 0, 0);\n"
        "font-size: 30px;\n"
        "border-radius: 8px\n"
        "}\n"
        "")

    def get_button_styles_selected(self):
        return (
                "QPushButton:hover{\n"
                "background-color: #de0000;\n"
                "    color: rgb(255, 255, 255);\n"
                "    font-size: 30px;\n"
                "    border-radius: 8px\n"
                "}\n"
                "QPushButton:pressed{\n"
                "background-color: #7f0000;\n"
                "    color: rgb(255, 255, 255);\n"
                "    font-size: 30px;\n"
                "    border-radius: 8px\n"
                "}\n"
                "QPushButton{\n"
                "background-color: #ff5733;\n"
                "color: rgb(0, 0, 0);\n"
                "font-size: 30px;\n"
                "border-radius: 8px\n"
                "}\n"
                ""
        )

    def get_button_styles_booked(self):
        return ("\n"
        "QPushButton {\n"
        "    background-color:  rgb(61, 61, 61); /* Серый фон */\n"
        "    color: rgb(0, 0, 0); /* Черный текст */\n"
        "    font-size: 30px;\n"
        "    border-radius: 8px;\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color:  rgb(61, 61, 61); /* Сохраняем серый фон при наведении */\n"
        "    color: rgb(0, 0, 0); /* Сохраняем черный цвет текста при наведении */\n"
        "}")

    def buy_ticket(self):
        args = ','.join(self.seats_now)
        requests.get('http://viollenaki.pythonanywhere.com/movie_seance_booking', params={'user': main_user, 'movie': selected['movie'], 'seance': selected['seance'], 'seats': args})
        self.close()

    def closeEvent(self, event):
        global selected
        selected["seance"] 
        event.accept()



class Adding(QtWidgets.QDialog):
    def __init__(self, parent=None):
        
        super().__init__(parent)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 400)
        font = QtGui.QFont()
        font.setPointSize(7)
        Dialog.setFont(font)
        Dialog.setStyleSheet("background-color: rgb(148, 143, 124);")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(8, 20, 126, 33))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(8, 122, 126, 33))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 126, 33))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(8, 219, 126, 33))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_5.setObjectName("label_5")
        self.apply = QtWidgets.QPushButton(Dialog)
        self.apply.setGeometry(QtCore.QRect(86, 324, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.apply.setFont(font)
        self.apply.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(23, 137, 143);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(14, 85, 89);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(15, 86, 90);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 30px;\n"
"border-radius: 20px\n"
"}\n"
"")
        self.apply.setObjectName("apply")
        self.apply.clicked.connect(self.add_movie)


        self.title_text = QtWidgets.QLineEdit(Dialog)
        self.title_text.setGeometry(QtCore.QRect(146, 20, 146, 33))
        self.title_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.title_text.setObjectName("title_text")
        self.date_text = QtWidgets.QLineEdit(Dialog)
        self.date_text.setGeometry(QtCore.QRect(146, 122, 146, 33))
        self.date_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.date_text.setObjectName("date_text")
        self.price_text = QtWidgets.QLineEdit(Dialog)
        self.price_text.setGeometry(QtCore.QRect(146, 219, 146, 33))
        self.price_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.price_text.setObjectName("price_text")



        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Movie (Admin)"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Title</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Title</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Date</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Price</span></p></body></html>"))
        self.apply.setText(_translate("Dialog", "Apply"))


    def add_movie(self):
        title = self.title_text.text()
        date = self.date_text.text()
        price = self.price_text.text()
        url = 'http://viollenaki.pythonanywhere.com/add_movie'
        if title != '' and date != '' and price != '':
                response = requests.get(url, params= {"movie" : title, 'seance' : date, 'price' : price})
                self.parent().fill_film_table()
                if response.json() == True:
                  QtWidgets.QMessageBox.information(None, "Success", "Movie added")
        else:
                QtWidgets.QMessageBox.information(None, "Error", "Please fill all the fields")





class AdminMain(QtWidgets.QWidget):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 780)
        Form.setStyleSheet("background-color: rgb(148, 143, 124);")
        self.movie_total = ''
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(42, 469, 278, 45))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 540, 278, 45))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 18, 221, 47))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label.setObjectName("label")
        self.total_text = QtWidgets.QLineEdit(Form)
        self.total_text.setGeometry(QtCore.QRect(380, 537, 274, 45))
        self.total_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font-size: 25px \"Book Antiqua\";")
        self.total_text.setObjectName("total_text")
        self.total_text.setReadOnly(True)
        self.total_text.setText(str(requests.get('http://viollenaki.pythonanywhere.com/get_total_profit').json()))

        self.seance_list = QtWidgets.QListWidget(Form)
        self.seance_list.setGeometry(QtCore.QRect(371, 77, 296, 372))
        self.seance_list.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 10px;\n"
"font-size: 25px \"Book Antiqua\";")
        self.seance_list.setObjectName("seance_list")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(408, 18, 221, 47))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_2.setObjectName("label_2")
        self.all_history = QtWidgets.QPushButton(Form)
        self.all_history.setGeometry(QtCore.QRect(408, 609, 221, 55))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.all_history.setFont(font)
        self.all_history.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(23, 137, 143);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(14, 85, 89);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(15, 86, 90);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 30px;\n"
"border-radius: 20px\n"
"}\n"
"")
        self.all_history.setObjectName("all_history")
        self.all_history.clicked.connect(self.All_history)


        self.movie_list = QtWidgets.QListWidget(Form)
        self.movie_list.setGeometry(QtCore.QRect(33, 77, 296, 372))
        self.movie_list.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 10px;\n"
"font-size: 25px \"Book Antiqua\";")
        self.movie_list.setObjectName("movie_list")
        self.movie_list.itemDoubleClicked.connect(self.fill_seance_table)
        self.add_movie = QtWidgets.QPushButton(Form)
        self.add_movie.setGeometry(QtCore.QRect(70, 609, 221, 55))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.add_movie.setFont(font)
        self.add_movie.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(23, 137, 143);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(14, 85, 89);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(15, 86, 90);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 30px;\n"
"border-radius: 20px\n"
"}\n"
"")
        self.add_movie.setObjectName("add_movie")
        self.add_movie.clicked.connect(self.adding_window)

        self.totalofmovie_text = QtWidgets.QLineEdit(Form)
        self.totalofmovie_text.setGeometry(QtCore.QRect(380, 469, 274, 45))
        self.totalofmovie_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font-size: 25px \"Book Antiqua\";")
        self.totalofmovie_text.setObjectName("totalofmovie_text")
        self.totalofmovie_text.setReadOnly(True)

        self.fill_film_table()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

            

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "main (Admin)"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">Total of Movie</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">Total</span></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">Movies</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">Seance</span></p></body></html>"))
        self.all_history.setText(_translate("Form", "All History"))
        self.add_movie.setText(_translate("Form", "Add Movie"))


    def adding_window(self):
        self.window = QtWidgets.QDialog()
        self.add_window = Adding(self) 
        self.add_window.setupUi(self.window)
        self.window.show()

    def fill_film_table(self):
        self.movie_list.clear()
        response = requests.get('http://viollenaki.pythonanywhere.com/get_movies').json()
        for i in response:
            self.movie_list.addItem(i)

    def fill_seance_table(self):
        response = requests.get('http://viollenaki.pythonanywhere.com/get_movie_profit', params={'movie': self.movie_list.selectedItems()[0].text()}).json()
        self.totalofmovie_text.setText(str(response))
        self.seance_list.clear()
        self.movie_total = self.movie_list.selectedItems()[0].text()
        selected_movie = self.movie_list.selectedItems()[0].text()
        response = requests.get('http://viollenaki.pythonanywhere.com/get_movie_seances', params={'movie': selected_movie}).json()
        for i in response:
            self.seance_list.addItem(i)

    def All_history(self):
        self.window = QtWidgets.QDialog()
        self.ui = AllHistory()
        self.ui.setupUi(self.window)
        self.window.show()



class Ui_Main_Window(QtWidgets.QWidget):

    def setupUi(self, Main_Window):
        Main_Window.setObjectName("Main_Window")
        Main_Window.resize(700, 780)
        Main_Window.setStyleSheet("background-color: rgb(148, 143, 124);")
        self.history = QtWidgets.QPushButton(Main_Window)
        self.history.setGeometry(QtCore.QRect(449, 470, 141, 51))
        self.history.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(23, 137, 143);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(14, 85, 89);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(15, 86, 90);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 30px;\n"
"border-radius: 20px\n"
"}\n"
"")
        self.history.setObjectName("history")
        self.info = QtWidgets.QPushButton(Main_Window)
        self.info.setGeometry(QtCore.QRect(60, 470, 130, 51))
        self.info.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(23, 137, 143);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(14, 85, 89);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(15, 86, 90);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 30px;\n"
"border-radius: 20px\n"
"}\n"
"")
        self.info.setObjectName("info")
        self.info.clicked.connect(self.info1_func)

        self.movie_list = QtWidgets.QListWidget(Main_Window)
        self.movie_list.setGeometry(QtCore.QRect(36, 105, 296, 439))
        self.movie_list.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 10px;\n"
"font-size: 25px \"Book Antiqua\";")
        self.movie_list.setObjectName("movie_list")
        self.movie_list.itemDoubleClicked.connect(self.fill_seance_table)
        self.seance_list = QtWidgets.QListWidget(Main_Window)
        self.seance_list.setGeometry(QtCore.QRect(374, 105, 296, 439))
        self.seance_list.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 10px;\n"
"font-size: 25px \"Book Antiqua\";")
        self.seance_list.setObjectName("seance_list")
        self.seance_list.itemDoubleClicked.connect(self.info1_func)
        self.seance_list.itemClicked.connect(self.set_one_click)
        self.label = QtWidgets.QLabel(Main_Window)
        self.label.setGeometry(QtCore.QRect(73, 35, 221, 47))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Main_Window)
        self.label_2.setGeometry(QtCore.QRect(411, 35, 221, 47))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_2.setObjectName("label_2")


        self.info_2 = QtWidgets.QPushButton(Main_Window)
        self.info_2.setGeometry(QtCore.QRect(44, 601, 172, 48))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.info_2.setFont(font)
        self.info_2.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(23, 137, 143);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(14, 85, 89);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(15, 86, 90);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 30px;\n"
"border-radius: 20px\n"
"}\n"
"")
        self.info_2.setObjectName("info_2")
        self.info_2.clicked.connect(self.info2_func)

        self.buy = QtWidgets.QPushButton(Main_Window)
        self.buy.setGeometry(QtCore.QRect(264, 601, 172, 48))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.buy.setFont(font)
        self.buy.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(23, 137, 143);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(14, 85, 89);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(15, 86, 90);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 30px;\n"
"border-radius: 20px\n"
"}\n"
"")
        self.buy.setObjectName("buy")
        self.buy.clicked.connect(self.buying)


        self.history_2 = QtWidgets.QPushButton(Main_Window)
        self.history_2.setGeometry(QtCore.QRect(484, 601, 172, 48))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.history_2.setFont(font)
        self.history_2.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(23, 137, 143);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(14, 85, 89);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(15, 86, 90);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 30px;\n"
"border-radius: 20px\n"
"}\n"
"")
        self.history_2.setObjectName("history_2")
        self.history_2.clicked.connect(self.history_func)

        self.fill_film_table()
        self.retranslateUi(Main_Window)
        QtCore.QMetaObject.connectSlotsByName(Main_Window)

    def retranslateUi(self, Main_Window):
        _translate = QtCore.QCoreApplication.translate
        Main_Window.setWindowTitle(_translate("Main_Window", "Main Window"))
        self.history.setText(_translate("Main_Window", "HISTORY"))
        self.info.setText(_translate("Main_Window", "INFO"))
        self.label.setText(_translate("Main_Window", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">Movies</span></p></body></html>"))
        self.label_2.setText(_translate("Main_Window", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">Seance</span></p></body></html>"))
        self.info_2.setText(_translate("Main_Window", "Info"))
        self.buy.setText(_translate("Main_Window", "Buy"))
        self.history_2.setText(_translate("Main_Window", "My History"))

    def fill_film_table(self):

        response = requests.get('http://viollenaki.pythonanywhere.com/get_movies').json()
        for i in response:
            self.movie_list.addItem(i)


    def history_func(self):
        self.window = QtWidgets.QDialog()
        self.ui = History()
        self.ui.setupUi(self.window)
        self.window.show()

    def info1_func(self):
        global selected
        selected["seance"] = self.seance_list.selectedItems()[0].text()
        self.window = QtWidgets.QDialog()
        self.ui = Info()
        self.ui.setupUi(self.window)
        self.window.show()

    def info2_func(self):
        if selected["movie"] == "":
            QtWidgets.QMessageBox.critical(None, "Error", "Movie not selected")
            return
        self.window = QtWidgets.QDialog()
        self.ui = Info2()
        self.ui.setupUi(self.window)
        self.window.show()

    def fill_seance_table(self):
        global selected
        self.seance_list.clear()
        selected_movie = self.movie_list.selectedItems()[0].text()
        selected["movie"] = selected_movie
        selected["seance"] = ""
        response = requests.get('http://viollenaki.pythonanywhere.com/get_movie_seances', params={'movie': selected_movie}).json()
        for i in response:
            self.seance_list.addItem(i)

    def buying(self):
        global selected
        if selected["seance"] == "":
            QtWidgets.QMessageBox.critical(None, "Error", "Select seance")
        else:       
                selected["seance"] = self.seance_list.selectedItems()[0].text()
                self.ui = SeatGenerator()
                self.ui.show()

    def set_one_click(self):
        global selected
        selected["seance"]=self.seance_list.selectedItems()[0].text()

class Ui_Registration(QtWidgets.QWidget):
    def setupUi(self, Registration):
        Registration.setObjectName("Registration")
        Registration.setWindowModality(QtCore.Qt.ApplicationModal)
        Registration.resize(300, 400)
        Registration.setStyleSheet("background-color:rgb(148, 143, 124)")
        self.label_3 = QtWidgets.QLabel(Registration)
        self.label_3.setGeometry(QtCore.QRect(72, 34, 155, 33))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_3.setObjectName("label_3")
        self.apply = QtWidgets.QPushButton(Registration)
        self.apply.setGeometry(QtCore.QRect(73, 342, 155, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.apply.setFont(font)
        self.apply.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(23, 137, 143);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(14, 85, 89);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(15, 86, 90);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 30px;\n"
"border-radius: 20px\n"
"}\n"
"")
        self.apply.setObjectName("apply")
        self.apply.clicked.connect(self.new_user)



        self.label_4 = QtWidgets.QLabel(Registration)
        self.label_4.setGeometry(QtCore.QRect(72, 132, 155, 33))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Registration)
        self.label_5.setGeometry(QtCore.QRect(72, 237, 155, 33))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_5.setObjectName("label_5")
        self.name_text = QtWidgets.QLineEdit(Registration)
        self.name_text.setGeometry(QtCore.QRect(38, 77, 223, 38))
        self.name_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.name_text.setObjectName("name_text")
        self.password_text = QtWidgets.QLineEdit(Registration)
        self.password_text.setGeometry(QtCore.QRect(38, 182, 223, 38))
        self.password_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.password_text.setObjectName("password_text")
        self.password_text.setEchoMode(QtWidgets.QLineEdit.Password)


        self.confirm_text = QtWidgets.QLineEdit(Registration)
        self.confirm_text.setGeometry(QtCore.QRect(38, 287, 223, 38))
        self.confirm_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.confirm_text.setObjectName("confirm_text")
        self.confirm_text.setEchoMode(QtWidgets.QLineEdit.Password)




        self.retranslateUi(Registration)
        QtCore.QMetaObject.connectSlotsByName(Registration)

    def retranslateUi(self, Registration):
        _translate = QtCore.QCoreApplication.translate
        Registration.setWindowTitle(_translate("Registration", "Sign Up"))
        self.label_3.setText(_translate("Registration", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Name</span></p></body></html>"))
        self.apply.setText(_translate("Registration", "Apply"))
        self.label_4.setText(_translate("Registration", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Password</span></p></body></html>"))
        self.label_5.setText(_translate("Registration", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Confirm</span></p></body></html>"))


    def new_user(self):
        name = self.name_text.text().lower()
        password = self.password_text.text()
        confirm = self.confirm_text.text()
        if len(name) != 0 and len(password) != 0 and len(confirm) != 0:
            if password == confirm:
                url = 'http://viollenaki.pythonanywhere.com/get_user'
                response = requests.get(url, params={'user' : name})
                if response.json() == False:
                        url = 'http://viollenaki.pythonanywhere.com/add_user'
                        response = requests.get(url, params={'user' : name, 'password' : password})
                        QtWidgets.QMessageBox.information(None, "Success", "Added new user")
                else:
                        QtWidgets.QMessageBox.critical(None, "Error", "User is already exist")
            else:
                QtWidgets.QMessageBox.critical(None, "Error", "Passwords aren't same")
        else:
            QtWidgets.QMessageBox.critical(None, "Error", "Fill all fields")

class Ui_Login_Window(QtWidgets.QWidget):
    def setupUi(self, Login_Window):
        Login_Window.setObjectName("Login_Window")
        Login_Window.resize(300, 400)
        Login_Window.setMaximumSize(QtCore.QSize(300, 400))
        Login_Window.setStyleSheet("background-color:rgb(148, 143, 124)")
        self.label_3 = QtWidgets.QLabel(Login_Window)
        self.label_3.setGeometry(QtCore.QRect(72, 34, 155, 33))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_3.setObjectName("label_3")
        self.login = QtWidgets.QPushButton(Login_Window)
        self.login.setGeometry(QtCore.QRect(72, 293, 155, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.login.setFont(font)
        self.login.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(23, 137, 143);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(14, 85, 89);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(15, 86, 90);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 30px;\n"
"border-radius: 20px\n"
"}\n"
"")
        self.login.setObjectName("login")
        self.login.clicked.connect(self.check_password)



        self.label_4 = QtWidgets.QLabel(Login_Window)
        self.label_4.setGeometry(QtCore.QRect(72, 132, 155, 33))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(15, 86, 90);\n"
"border-radius: 10px;")
        self.label_4.setObjectName("label_4")
        self.new_user = QtWidgets.QPushButton(Login_Window)
        self.new_user.setGeometry(QtCore.QRect(72, 343, 155, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.new_user.setFont(font)
        self.new_user.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(23, 137, 143);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(14, 85, 89);\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 30px;\n"
"    border-radius: 20px\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(15, 86, 90);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 30px;\n"
"border-radius: 20px\n"
"}\n"
"")
        self.new_user.setObjectName("new_user")
        self.new_user.clicked.connect(self.registration)


        self.username_text = QtWidgets.QLineEdit(Login_Window)
        self.username_text.setGeometry(QtCore.QRect(38, 77, 223, 38))
        self.username_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.username_text.setObjectName("username_text")
        self.password_text = QtWidgets.QLineEdit(Login_Window)
        self.password_text.setGeometry(QtCore.QRect(38, 182, 223, 38))
        self.password_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.password_text.setObjectName("password_text")
        self.password_text.setEchoMode(QtWidgets.QLineEdit.Password)

        self.checkBox = QtWidgets.QCheckBox(Login_Window)
        self.checkBox.setGeometry(QtCore.QRect(40, 260, 211, 21))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setTristate(False)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("font-size: 20px")

        self.login.setDisabled(True)
        self.checkBox.mousePressEvent = self.check_mouse_event

        self.retranslateUi(Login_Window)
        QtCore.QMetaObject.connectSlotsByName(Login_Window)

    def retranslateUi(self, Login_Window):
        _translate = QtCore.QCoreApplication.translate
        Login_Window.setWindowTitle(_translate("Login_Window", "Sign In"))
        self.label_3.setText(_translate("Login_Window", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">User Name</span></p></body></html>"))
        self.login.setText(_translate("Login_Window", "Login"))
        self.label_4.setText(_translate("Login_Window", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Password</span></p></body></html>"))
        self.new_user.setText(_translate("Login_Window", "New User"))
        self.checkBox.setText(_translate("Login_Window", "I\'m not a robot"))

    def registration(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Registration()
        self.ui.setupUi(self.window)
        self.window.show()

    def check_password(self):
        global main_user
        name = self.username_text.text().lower()
        password = self.password_text.text()
        url = 'http://viollenaki.pythonanywhere.com/get_user'
        response = requests.get(url, params={"user" : name}) 
        if len(name) != 0 and len(password) != 0:
                if name != admin:
                    if response.json() == True:
                        url = 'http://viollenaki.pythonanywhere.com/login'
                        response = requests.get(url, params={"user" : name, "password" : password})
                        if response.json() == True:
                                main_user = name
                                self.checkBox.setChecked(False)

                                self.username_text.setText('')
                                self.password_text.setText('')
                                self.window = QtWidgets.QWidget()
                                self.ui = Ui_Main_Window()
                                self.ui.setupUi(self.window)
                                self.window.show()
                        else:
                            QtWidgets.QMessageBox.critical(None, "Error", "Wrong password")
                    else:
                        QtWidgets.QMessageBox.critical(None, "Error", "User is not exist")
                else:
                     if password == admin_password:
                        self.checkBox.setChecked(False)

                        self.username_text.setText('')
                        self.password_text.setText('')
                        self.window = QtWidgets.QWidget()
                        self.ui = AdminMain()
                        self.ui.setupUi(self.window)
                        self.window.show()
        else:
            QtWidgets.QMessageBox.critical(None, "Error", "Fill all fields")

    def check_mouse_event(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            
            self.login.setDisabled(False)
        # Вызов стандартного метода, чтобы галочка появлялась
            QtWidgets.QCheckBox.mousePressEvent(self.checkBox, event)
        else:
            QtWidgets.QMessageBox.critical(None, "Error", "Fill all fields")



class Window(QtWidgets.QMainWindow, Ui_Login_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

admin = "admin"
admin_password = "123"



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Window()
    sys.exit(app.exec_())