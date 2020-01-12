# https://drive.google.com/drive/folders/1gsbCrJFuTuq95ocOz82e2GOUL0xU3TmR


import os
import sys
import time
import zipfile
from _datetime import datetime
import numpy as np
import pandas as pd
import matplotlib as plt
#import pyplot
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import PyQt5
from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QComboBox, QDialog, QVBoxLayout ,  QToolBox, QMenu, QMainWindow, QMenuBar)


#dirname = os.path.dirname(PyQt5.__file__)
#dn = os.path.join('C:,''ProgramData','Anaconda3','Lib','site-packages', 'PyQt5')
#plugin_path = os.path.join(dirname, 'Qt','plugins', 'platforms')
#os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Automate:

    def automate(self, url, emails, passwords, d, c, t, s):
        #Folder Calling

        nwd = self.folder(d, c, t, s)
       # print(nwd)
        try:
            chromeOptions = Options()
            chromeOptions.add_experimental_option("prefs", {"download.default_directory": "{}".format(nwd)})

            #UI Automation
            driverLoc = "D:/Chrome/76/chromedriver.exe"
            browser = webdriver.Chrome(driverLoc, options=chromeOptions)
            browser.maximize_window()

            browser.get(url)
            browser.find_elements_by_xpath('//*[@id="drive_hist_frame"]')
            print("Frame Switched...")

            time.sleep(3)
            signinutton = browser.find_element_by_xpath('//*[@id="gb"]/div[2]/div[3]/div[1]/a')
            signinutton.click()

            time.sleep(5)
            email = browser.find_element_by_xpath('//*[@id="identifierId"]')
            email.send_keys(emails)
            nextbtn = browser.find_element_by_xpath('//*[@id="identifierNext"]')
            nextbtn.click()

            time.sleep(2)
            password = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
            password.send_keys(passwords)

            submit = browser.find_element_by_xpath('//*[@id="passwordNext"]')
            submit.click()

            print("Login Done")

            print("Finding Assignments........")

            browser.implicitly_wait(15)
            dwnarrow = browser.find_element_by_xpath('//*[@id="drive_main_page"]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/nav/div[2]/div[2]/div')
            time.sleep(1)
            dwnarrow.click()
            # //*[@id="drive_main_page"]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/nav/div[2]/div[2]/div
            time.sleep(5)

            print("Assignment Found")
            # downloadbtn = browser.find_element_by_xpath('/html/body/div[19]/div/div[10]/div/span[2]/span/div')
            # downloadbtn.click()

            for i in range(0, 8):
                robohandling = dwnarrow.send_keys(Keys.ARROW_DOWN)

            download = dwnarrow.send_keys(Keys.ENTER)


        except Exception as e:
            print('Unexpected Browser Closure')
            print(e.msg)

        # urllib.urlretrieve("http://www.google.com", fullfilename)

        # download = browser.find_elements_by_xpath('//*[@id="drive_main_page"]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]')
        print("Done With download")

    def folder(self, drive, course, trim, sub):
        # dir = r"C:\Users\DELL\Desktop\proj\bda\python"
        dir = drive+':\\'
        dir = dir + os.path.join(course, trim, sub)
        today = datetime.now()
        tod = '{:%d-%m-%Y}'.format(today)
            # todaystr = tod.isoformat()
            # nwd = dir + '\\' + todaystr
        nwd = os.path.join(dir, tod)
        try:
            os.makedirs(nwd)
            print("directory created")
            return nwd
        except FileExistsError:
            print("directory already exists")
        finally:
            self.directory = nwd
        return nwd


    def makeCsv(self,drive,couse,trim,sub):
        for i in range(0, 1):
            time.sleep(1)
            if (i % 60 == 0):
                print(i)

        try:
            print('makeCsv function in')
            files = os.listdir(self.directory)
            print(files)

            data = {'names': []}
            zip = zipfile.ZipFile(self.directory+'/'+str(files[0]), 'r')
            print('I m a zip file: ' +str(zip))
            for name in zip.namelist():
                # print(name.split('/')[1])
                data['names'].append(name.split('/')[1])

            df = pd.DataFrame(data)
            df.to_csv(self.directory+'/DSBDA.csv', index=False)
        except Exception as e:
            print('CSV File Creation Error')
    
        # Shivam
        # file_dir = "E:/Python/Trimester 1/Assignment"
        # ass_dir = [os.path.join(file_dir, folname) for folname in os.listdir(file_dir)]

        # print("downloaded folders:", ass_dir)
        # on_time = []
        # off_time = []
        # ontime_lis_dir = []

        # for ass in ass_dir:
        #     #ass = 'E:/Python/Trimester 1/Assignment\\aadesh'
        #     if os.listdir(ass) == []:
        #         off_time = off_time + [ass]
        #     else:
        #         on_time = on_time + [ndir for ndir in os.listdir(ass)]
        #         ontime_lis_dir = ontime_lis_dir + [ass]
        #         #print(ndir)

        # print("on time file list:", on_time)
        # print("off time list:", off_time)
        # print("on time directory list:", ontime_lis_dir)

        # folder_dir = []

        # for dirr in ontime_lis_dir:
        #     path, folder = os.path.split(dirr)
        #     folder_dir = folder_dir + [folder]
        # #print("path:", path)
        # print("submit_folders:", folder_dir)


        # with open("E:/Python/Trimester 1/student.csv", "r") as f:
        #     lis = [a for a in f]
        # print("csv list:", lis)

        # total = []
        # for a in lis:
        #     name1, extension1 = a.split('\n')
        #     total = total + [name1]

        # defaulters = []
        # for element in total:
        #     if element not in folder_dir:
        #         defaulters.append(element)

        # print("Total Students:", total)
        # print("Students submitted on time:", folder_dir)
        # print("Students not Submitted:", defaulters)
        # submitted=pd.DataFrame(folder_dir)
        # print(submitted)
        # submitted.to_csv("E:/Python/Trimester 1/Assignment/submitted.csv")

    def visualize(self):
        # Aadesh
        fig = plt.figure()
        data1 = pd.read_csv("DSBDA.csv",names=['Name'])

        data2 = pd.read_csv(self.directory+"/DSBDA.csv",names=['Name'])


        df = pd.merge(data1, data2,how='left', indicator='Submitted')
        df['Submitted'] = np.where(df.Submitted == 'both', True, False)
        # print (df)

        y = []

        for i in range(df.index.min(), df.index.max()+1):
            if(df['Submitted'][i] == True):
                y.append(1)
            elif(df['Submitted'][i] == False):
                y.append(0)

        x=[]
        x=list(df.index+1)

        barWidth = 0.85
        # Create green Bars
        plt.bar(x, y, color='green', edgecolor='white', width=barWidth, label='On Time')
        plt.savefig(self.directory+"/assigenmet1.pdf")
        print('Showing Plot')
        plt.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.app = QtWidgets.QApplication(sys.argv)
        self.Window = QtWidgets.QMainWindow()

        self.imagePath = (r"D:/RPA Project/MITLOGO.png")

        self.initGUI()
        self.Window.setWindowTitle("R P A")
        # self.Window.setStyleSheet("background-color:#6e6e6e")
        self.Window.setGeometry(500, 100, 300, 700)
        self.Window.show()
        sys.exit(self.app.exec())

    def initGUI(self):
        # Creating Label
        self.image = QtGui.QImage(self.imagePath)
        self.label = QtWidgets.QLabel(self.Window)
        self.label.setGeometry(50, 1, 200, 130)

        # self.label.setStyleSheet("background-color:#6e6e6e")
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)

        # Creating a Link Field
        self.link = QtWidgets.QLineEdit(self.Window)
        self.link.setGeometry(25, 120, 250, 40)
        self.link.setPlaceholderText("Link")
        # self.link.setStyleSheet("background-color:#f7f7f7; color:#8e8e8e; padding-top:5px; padding-left:10px")

        # Link == Google Drive Link

        # Creating Email Field
        self.email = QtWidgets.QLineEdit(self.Window)
        self.email.setGeometry(25, 180, 250, 40)
        self.email.setPlaceholderText("Email")

        # Creating Password Field
        self.password = QtWidgets.QLineEdit(self.Window)
        self.password.setEchoMode(self.password.Password)
        self.password.setGeometry(25, 240, 250, 40)
        self.password.setPlaceholderText("Password")

        # Creating Login Button
        self.createBtn = QtWidgets.QPushButton(self.Window)
        self.createBtn.setText("Login")
        self.createBtn.clicked.connect(self.check_password)
        self.createBtn.setGeometry(25, 600, 250, 40)
        self.createBtn.setMouseTracking(True)
        self.createBtn.setToolTip('This will automate further process')

        ## Creating Trimester DropDown ComboBox
        self.lbl = QtWidgets.QLabel(self.Window)
        self.combo = QtWidgets.QComboBox(self.Window)
        self.combo.addItem("<Select Trimester>")
        self.combo.addItem("Trimester I")
        self.combo.addItem("Trimester II")
        self.combo.addItem("Trimester III")
        self.combo.addItem("Trimester IV")
        self.combo.addItem("Trimester V")
        self.combo.addItem("Trimester VI")
        self.lbl = QLabel("Please Select Trimester : ", self.Window)
        self.lbl.setGeometry(25, 295, 250, 40)
        self.combo.setGeometry(25, 325, 250, 40)
        self.combo.activated[str].connect(self.onActivated1)

        ## Creating Cource Field
        self.cource = QtWidgets.QLineEdit(self.Window)
        self.cource.setGeometry(25, 385, 250, 40)
        self.cource.setPlaceholderText("Course")


        ## Creating Subject Fieldcheck_password
        self.subject = QtWidgets.QLineEdit(self.Window)
        self.subject.setGeometry(25, 445, 250, 40)
        self.subject.setPlaceholderText("Subject")
        self.createBtn.clicked.connect(self.check_password)

        # creating a DropDown ComboBox
        self.Dlbl = QtWidgets.QLabel(self.Window)
        self.Dcombo = QtWidgets.QComboBox(self.Window)
        self.Dcombo.addItem("<Select Drive>")
        self.Dcombo.addItem("C")
        self.Dcombo.addItem("D")
        self.Dcombo.addItem("E")
        self.Dcombo.addItem("F")
        self.Dlbl = QLabel("Please Select Download Location : ", self.Window)
        self.Dlbl.setGeometry(25, 488, 250, 40)
        self.Dcombo.setGeometry(25, 520, 250, 40)

        # Combo Box On Chnage
        self.Dcombo.activated[str].connect(self.onActivated)

    #Password Validation
    def check_password(self):
        msg = QMessageBox()

        drive = self.drive
        course = self.cource.text()
        trim = self.trimester
        sub = self.subject.text()

        link = self.link.text()
        email = self.email.text()
        password = self.password.text()

        automate = Automate()
        automate.automate(link,email,password, drive, course, trim, sub)

        automate.makeCsv(drive, course, trim, sub)
        
        automate.visualize()
        #msg.setText('Success')
        print('Success')
        msg.exec_()

    # Drive
    def onActivated(self, text):
        self.drive = text
        print(self.drive)

    # Trimester
    def onActivated1(self, text):
        self.trimester = text
        print(self.trimester)

    #Course
    def check_course(self):
        cource = self.cource
        print(cource)

    # Subject
    def onActivated1(self, text):
        self.trimester = text
        print(self.trimester)

if __name__ == '__main__':
        app = QApplication(sys.argv)
        form = MainWindow()
        form.show()
        sys.exit(app.exec_())