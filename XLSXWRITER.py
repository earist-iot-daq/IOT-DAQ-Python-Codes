from threading import Thread
import time
import xlsxwriter
import pyrebase
import datetime
from tkinter import *

dataArray = []

Height = 400
Width = 500

root = Tk()
root.title("Data Acquisition")

canvas = Canvas(root, height=Height, width=Width,)
canvas.pack()

workbook = xlsxwriter.Workbook("MCU-Based-Data-Acquisition.xlsx")
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': True})
bold_and_italic = workbook.add_format({'bold': True, 'italic': True})
bold_and_italic.set_center_across()
bold_and_center = workbook.add_format()
bold_and_center.set_bold()
bold_and_center.set_center_across()

filename = xlsxwriter.Workbook("DATA-ACQUISITION.xlsx")
filesheet = filename.add_worksheet()
worksheet.write("A2", "Time", bold_and_center)
worksheet.write("B2", " ADC CH1 Cloud", bold_and_center)
worksheet.write("C2", " ADC CH2 Cloud", bold_and_center)
worksheet.write("D2", " ADC CH3 Cloud", bold_and_center)
worksheet.write("E2", " ADC CH4 Cloud", bold_and_center)
worksheet.write("F2", " ADC CH1 Local", bold_and_center)
worksheet.write("G2", "ADC CH2 Local", bold_and_center)
worksheet.write("H2", "ADC CH3 Local", bold_and_center)
worksheet.write("I2", "ADC CH4 Local", bold_and_center)
worksheet.write("J2", "GPIO CH1 Cloud", bold_and_center)
worksheet.write("K2", "GPIO CH2 Cloud", bold_and_center)
worksheet.write("L2", "GPIO CH3 Cloud", bold_and_center)
worksheet.write("M2", "GPIO CH4 Cloud", bold_and_center)
worksheet.write("N2", "GPIO CH1 Local", bold_and_center)
worksheet.write("O2", "GPIO CH2 Local", bold_and_center)
worksheet.write("P2", "GPIO CH3 Local", bold_and_center)
worksheet.write("Q2", "GPIO CH4 Local", bold_and_center)
worksheet.write("R2", "Relay CH1 Cloud", bold_and_center)
worksheet.write("S2", "Relay CH2 Cloud", bold_and_center)
worksheet.write("T2", "MOSFET CH1 Cloud", bold_and_center)
worksheet.write("U2", "MOSFET CH2 Cloud", bold_and_center)
worksheet.write("V2", "Relay CH1 Local", bold_and_center)
worksheet.write("W2", "Relay CH2 Local", bold_and_center)
worksheet.write("X2", "MOSFET CH1 Local", bold_and_center)
worksheet.write("Y2", "MOSFET CH2 Local", bold_and_center)
worksheet.write("Z2", "Digital Input Monitor DI-A Local", bold_and_center)
worksheet.write("AA2", "Digital Input Monitor DI-B Local", bold_and_center)
worksheet.write("AB2", "Digital Output Monitor DO-A Local", bold_and_center)
worksheet.write("AC2", "Digital Output Monitor DO-B Local", bold_and_center)
worksheet.write("AD2", "Counter CH1", bold_and_center)
worksheet.write("AE2", "Counter CH2", bold_and_center)
worksheet.write("AF2", "Counter CH3", bold_and_center)
worksheet.write("AG2", "Counter CH4", bold_and_center)
worksheet.write("AH2", "Counter CH5", bold_and_center)
worksheet.write("AI2", "Counter CH6", bold_and_center)
worksheet.write("AJ2", "Internal Access Register Address", bold_and_center)
worksheet.write("AK2", "Internal Access Register Info", bold_and_center)

worksheet.set_column('B:B', 15)
worksheet.set_column('C:C', 15)
worksheet.set_column('D:D', 15)
worksheet.set_column('E:E', 15)
worksheet.set_column('F:F', 15)
worksheet.set_column('G:G', 15)
worksheet.set_column('H:H', 14)
worksheet.set_column('I:I', 16)
worksheet.set_column('J:J', 16)
worksheet.set_column('K:K', 16)
worksheet.set_column('L:L', 16)
worksheet.set_column('M:M', 16)
worksheet.set_column('N:N', 16)
worksheet.set_column('O:O', 15)
worksheet.set_column('P:P', 15)
worksheet.set_column('Q:Q', 15)
worksheet.set_column('R:R', 17)
worksheet.set_column('S:S', 17)
worksheet.set_column('T:T', 19)
worksheet.set_column('U:U', 19)
worksheet.set_column('V:V', 19)
worksheet.set_column('W:W', 19)
worksheet.set_column('X:X', 20)
worksheet.set_column('Y:Y', 20)
worksheet.set_column('Z:Z', 30)
worksheet.set_column('AA:AA', 30)
worksheet.set_column('AB:AB', 32)
worksheet.set_column('AC:AC', 32)
worksheet.set_column('AD:AD', 15)
worksheet.set_column('AE:AE', 13)
worksheet.set_column('AF:AF', 13)
worksheet.set_column('AG:AG', 13)
worksheet.set_column('AH:AH', 13)
worksheet.set_column('AI:AI', 13)
worksheet.set_column('AJ:AJ', 30)
worksheet.set_column('AK:AK', 27)

Config = {
    "apiKey": "AIzaSyACMOlcva5DuubIiIAByOYJihdKlLP0-gM",
    "authDomain": "data-acquisition-eb65d.firebaseapp.com",
    "databaseURL": "https://data-acquisition-eb65d-default-rtdb.firebaseio.com",
    "projectId": "data-acquisition-eb65d",
    "storageBucket": "data-acquisition-eb65d.appspot.com",
    "messagingSenderId": "572653975883",
    "appId": "1:572653975883:web:6a5b51cf45f19fd50f50ce",
    "measurementId": "G-DW3VMZ4TSS"
}
firebase = pyrebase.initialize_app(Config)
db = firebase.database()

def extractData(extract):
    count = 0
    previousCount = 0
    for x in extract:
        count = count + 1
        if (x == ','):
            dataArray.append(extract[previousCount:count - 1])
            previousCount = count

        if (count == len(extract)):
            dataArray.append(extract[previousCount:len(extract)])

class PrintA(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = True

    def run(self):
        c = 0
        row = 0
        column = 0
        while self.running:
            c += 1
            now = datetime.datetime.now()
            ADC = db.child("A").get()
            info = ADC.val()
            extractData(info)
            now = datetime.datetime.now()
            worksheet.write(row+3, column, now.strftime("%H:%M:%S") )
            worksheet.write(row+3, column+1, dataArray[0])
            worksheet.write(row+3, column+2, dataArray[1])
            worksheet.write(row+3, column+3, dataArray[2])
            worksheet.write(row+3, column+4, dataArray[3])
            worksheet.write(row+3, column+5, dataArray[4])
            worksheet.write(row+3, column+6, dataArray[5])
            worksheet.write(row+3, column+7, dataArray[6])
            worksheet.write(row+3, column+8, dataArray[7])
            worksheet.write(row+3, column+9, dataArray[8])
            worksheet.write(row+3, column+10, dataArray[9])
            worksheet.write(row+3, column+11, dataArray[10])
            worksheet.write(row+3, column+12, dataArray[11])
            worksheet.write(row+3, column+13, dataArray[12])
            worksheet.write(row+3, column+14, dataArray[13])
            worksheet.write(row+3, column+15, dataArray[14])
            worksheet.write(row+3, column+16, dataArray[15])
            worksheet.write(row+3, column+17, dataArray[16])
            worksheet.write(row+3, column+18, dataArray[17])
            worksheet.write(row+3, column+19, dataArray[18])
            worksheet.write(row+3, column+20, dataArray[19])
            worksheet.write(row+3, column+21, dataArray[20])
            worksheet.write(row+3, column+22, dataArray[21])
            worksheet.write(row+3, column+23, dataArray[22])
            worksheet.write(row+3, column+24, dataArray[23])
            worksheet.write(row+3, column+25, dataArray[24])
            worksheet.write(row+3, column+26, dataArray[25])
            worksheet.write(row+3, column+27, dataArray[26])
            worksheet.write(row+3, column+28, dataArray[27])
            worksheet.write(row+3, column+29, dataArray[28])
            worksheet.write(row+3, column+30, dataArray[29])
            worksheet.write(row+3, column+31, dataArray[30])
            worksheet.write(row+3, column+32, dataArray[31])
            worksheet.write(row+3, column+33, dataArray[32])
            worksheet.write(row+3, column+34, dataArray[33])
            worksheet.write(row+3, column+35, dataArray[34])
            worksheet.write(row+3, column+36, dataArray[35])
           
            time.sleep(1)
            row += 1
            dataArray.clear()
            

    def stop(self):
        workbook.close()
        self.running = False

a = PrintA()

print("START!!!")
a.start()
time.sleep(100)
print("DONE EXTRACTING!!!!!!")
a.stop()

root.mainloop()


