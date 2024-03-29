# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\jayma\OneDrive\Documents\GitHub\JugglingGUIV2\JugglingGUIV2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import mysql.connector
import json

with open ('config.json',"r") as info:
    data = json.load(info)
try:
    database = mysql.connector.connect(host = data['host'],user=data['user'],password=data['password'],database = data['database'],auth_plugin=data['auth_plugin'])
except mysql.connector.errors.DatabaseError as e:
    print("Database is not online!")
cursor = database.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(973, 636)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.remove_from_pending = QtWidgets.QPushButton(self.centralwidget)
        self.remove_from_pending.setGeometry(QtCore.QRect(20, 130, 241, 81))
        self.remove_from_pending.setObjectName("remove_from_pending")
        self.add_to_pending = QtWidgets.QPushButton(self.centralwidget)
        self.add_to_pending.setGeometry(QtCore.QRect(20, 40, 241, 81))
        self.add_to_pending.setStyleSheet("")
        self.add_to_pending.setObjectName("add_to_pending")
        self.incomplete_list = QtWidgets.QListWidget(self.centralwidget)
        self.incomplete_list.setGeometry(QtCore.QRect(20, 290, 251, 191))
        self.incomplete_list.setObjectName("incomplete_list")
        self.pending_list = QtWidgets.QListWidget(self.centralwidget)
        self.pending_list.setGeometry(QtCore.QRect(360, 40, 251, 191))
        self.pending_list.setObjectName("pending_list")
        self.completed_list = QtWidgets.QListWidget(self.centralwidget)
        self.completed_list.setGeometry(QtCore.QRect(690, 280, 251, 221))
        self.completed_list.setObjectName("completed_list")
        self.incomplete = QtWidgets.QLabel(self.centralwidget)
        self.incomplete.setGeometry(QtCore.QRect(60, 250, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        self.incomplete.setFont(font)
        self.incomplete.setObjectName("incomplete")
        self.pending = QtWidgets.QLabel(self.centralwidget)
        self.pending.setGeometry(QtCore.QRect(450, 0, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        self.pending.setFont(font)
        self.pending.setObjectName("pending")
        self.completed = QtWidgets.QLabel(self.centralwidget)
        self.completed.setGeometry(QtCore.QRect(730, 240, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        self.completed.setFont(font)
        self.completed.setObjectName("completed")
        self.jugglingGif = QtWidgets.QLabel(self.centralwidget)
        self.jugglingGif.setGeometry(QtCore.QRect(290, 260, 381, 351))
        self.jugglingGif.setFrameShape(QtWidgets.QFrame.Box)
        self.jugglingGif.setText("")
        self.jugglingGif.setObjectName("jugglingGif")
        self.movie = QMovie('JugglingGIF.gif')
        self.jugglingGif.setMovie(self.movie)
        self.movie.start()
        self.add_to_completed = QtWidgets.QPushButton(self.centralwidget)
        self.add_to_completed.setGeometry(QtCore.QRect(700, 40, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.add_to_completed.setFont(font)
        self.add_to_completed.setObjectName("add_to_completed")
        self.remove_from_completed = QtWidgets.QPushButton(self.centralwidget)
        self.remove_from_completed.setGeometry(QtCore.QRect(700, 140, 241, 81))
        self.remove_from_completed.setObjectName("remove_from_completed")
        self.incomplete_search_bar = QtWidgets.QTextBrowser(self.centralwidget)
        self.incomplete_search_bar.setGeometry(QtCore.QRect(20, 470, 251, 16))
        self.incomplete_search_bar.setObjectName("incomplete_search_bar")
        self.pending_search_bar = QtWidgets.QTextBrowser(self.centralwidget)
        self.pending_search_bar.setGeometry(QtCore.QRect(360, 220, 251, 16))
        self.pending_search_bar.setObjectName("pending_search_bar")
        self.completed_search_bar = QtWidgets.QTextBrowser(self.centralwidget)
        self.completed_search_bar.setGeometry(QtCore.QRect(690, 490, 251, 16))
        self.completed_search_bar.setObjectName("completed_search_bar")
        self.browser = QtWidgets.QPushButton(self.centralwidget)
        self.browser.setGeometry(QtCore.QRect(20, 500, 241, 81))
        self.browser.setObjectName("browser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(700, 510, 101, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 973, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_to_pending.clicked.connect(self.add_pending)
    def loadIncomplete(self):
        cursor.execute('''SELECT *
                          FROM trickslist
                          WHERE trick_status = "INCOMPLETE"''')     
        for i in cursor:
            self.incomplete_list.addItem(i[0])
        
    def loadComplete(self):
        cursor.execute('''SELECT *
                          FROM trickslist
                          WHERE trick_status = "COMPLETE"''')     
        for i in cursor:
            self.completed_list.addItem(i[0])
    
    def loadPending(self):
        cursor.execute('''SELECT *
                          FROM trickslist
                          WHERE trick_status = "PENDING"''')     
        for i in cursor:
            self.pending_list.addItem(i[0])

    def add_pending(self):
        trick = self.incomplete_list.currentItem().text()
        cursor.execute('''UPDATE trickslist
                          SET trick_status = "PENDING"
                          WHERE tricks = "%s"''' %trick)
        print(trick)
        database.commit()
        self.loadLists()
    
    def loadLists(self):
        self.pending_list.clear()
        self.incomplete_list.clear()
        self.completed_list.clear()
        self.loadComplete()
        self.loadIncomplete()
        self.loadPending()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.remove_from_pending.setText(_translate("MainWindow", "Remove from Pending"))
        self.add_to_pending.setText(_translate("MainWindow", "Add to Pending"))
        self.incomplete.setText(_translate("MainWindow", "Incomplete"))
        self.pending.setText(_translate("MainWindow", "Pending"))
        self.completed.setText(_translate("MainWindow", "Completed"))
        self.add_to_completed.setText(_translate("MainWindow", "Add to Completed"))
        self.remove_from_completed.setText(_translate("MainWindow", "Remove from Completed"))
        self.browser.setText(_translate("MainWindow", "View Trick in Browser"))
        self.label.setText(_translate("MainWindow", "Gui by Jaden Leake"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.loadLists()
    MainWindow.show()
    sys.exit(app.exec_())
