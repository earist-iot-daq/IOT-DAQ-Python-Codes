from threading import Thread
import time
import xlsxwriter
import pyrebase
import datetime
from tkinter import *
from datetime import date

today = date.today()

def start():
    a = PrintA()
    now = datetime.datetime.now()
    worksheet.write("B3", now.strftime("%B %d, %Y"),  left)
    worksheet.write("B4", now.strftime("%H:%M:%S"),  left)
    print("STARTED!!!")
    a.start()
    time.sleep(60)
    print("DONE EXTRACTING!!!!!!")
    a.stop()
  
def stop():   
    a = PrintA()
    a.stop()

dataArray = []

Height = 400
Width = 500

root = Tk()
root.title("Data Acquisition")

canvas = Canvas(root, height=Height, width=Width,)
canvas.pack()

start = Button(root, text="START", bg="#F1948A", font=60, command=start  )
start.place(relx=0.15 , rely=0.38 , relheight=.1 ,relwidth=0.15 )

stop = Button(root, text="STOP", bg="#F1948A", font=60, command=stop )
stop.place(relx=0.67 , rely=0.38 , relheight=.1 ,relwidth=0.15 )


workbook = xlsxwriter.Workbook("MCU-Based-Data-Acquisition.xlsx")
worksheet = workbook.add_worksheet()


bold = workbook.add_format({'bold': True})
bold_and_italic = workbook.add_format({'bold': True, 'italic': True})
bold_and_italic.set_center_across()
bold_and_center = workbook.add_format()
bold_and_center.set_bold()
bold_and_center.set_center_across()
bold_and_center.set_bg_color("#F1948A")  
bold_and_center.set_border_color("black")

right = workbook.add_format()
right.set_align("right")
right.set_bold()
right1 = workbook.add_format()
right1.set_align("right")
left = workbook.add_format()
left.set_align("left")
center = workbook.add_format()
center.set_center_across()
title = workbook.add_format({"font":"Times", "font_size":15, "bold":True}) 
title.set_center_across() 



worksheet.merge_range('B1:N1', 'MICROCONTROLLER BASED INTERNET OF THINGS DATA ACQUISITION FOR MONITORING AND CONTROL SYSTEM USING CLOUD PLATFORM', title)
worksheet.write("A4", "Time Started:" , right)
worksheet.write("A5", "Time Ended:" , right)
worksheet.write("A3", "Date:" , right)
worksheet.write("A7", "Time", bold_and_center)
worksheet.write("B7", " ADC CH1 Cloud", bold_and_center)
worksheet.write("C7", " ADC CH2 Cloud", bold_and_center)
worksheet.write("D7", " ADC CH3 Cloud", bold_and_center)
worksheet.write("E7", " ADC CH4 Cloud", bold_and_center)
worksheet.write("F7", " ADC CH1 Local", bold_and_center)
worksheet.write("G7", "ADC CH2 Local", bold_and_center)
worksheet.write("H7", "ADC CH3 Local", bold_and_center)
worksheet.write("I7", "ADC CH4 Local", bold_and_center)
worksheet.write("J7", "GPIO CH1 Cloud", bold_and_center)
worksheet.write("K7", "GPIO CH2 Cloud", bold_and_center)
worksheet.write("L7", "GPIO CH3 Cloud", bold_and_center)
worksheet.write("M7", "GPIO CH4 Cloud", bold_and_center)
worksheet.write("N7", "GPIO CH1 Local", bold_and_center)
worksheet.write("O7", "GPIO CH2 Local", bold_and_center)
worksheet.write("P7", "GPIO CH3 Local", bold_and_center)
worksheet.write("Q7", "GPIO CH4 Local", bold_and_center)
worksheet.write("R7", "Relay CH1 Cloud", bold_and_center)
worksheet.write("S7", "Relay CH2 Cloud", bold_and_center)
worksheet.write("T7", "MOSFET CH1 Cloud", bold_and_center)
worksheet.write("U7", "MOSFET CH2 Cloud", bold_and_center)
worksheet.write("V7", "Relay CH1 Local", bold_and_center)
worksheet.write("W7", "Relay CH2 Local", bold_and_center)
worksheet.write("X7", "MOSFET CH1 Local", bold_and_center)
worksheet.write("Y7", "MOSFET CH2 Local", bold_and_center)
worksheet.write("Z7", "Digital Input Monitor DI-A Local", bold_and_center)
worksheet.write("AA7", "Digital Input Monitor DI-B Local", bold_and_center)
worksheet.write("AB7", "Digital Output Monitor DO-A Local", bold_and_center)
worksheet.write("AC7", "Digital Output Monitor DO-B Local", bold_and_center)
worksheet.write("AD7", "Counter CH1", bold_and_center)
worksheet.write("AE7", "Counter CH2", bold_and_center)
worksheet.write("AF7", "Counter CH3", bold_and_center)
worksheet.write("AG7", "Counter CH4", bold_and_center)
worksheet.write("AH7", "Counter CH5", bold_and_center)
worksheet.write("AI7", "Counter CH6", bold_and_center)
worksheet.write("AJ7", "Internal Access Register Address", bold_and_center)
worksheet.write("AK7", "Internal Access Register Info", bold_and_center)


worksheet.set_column('A:A', 15)
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
            worksheet.write(row+8, column, now.strftime("%H:%M:%S") )
            worksheet.write(row+8, column+1, dataArray[0],right1)
            worksheet.write(row+8, column+2, dataArray[1],right1)
            worksheet.write(row+8, column+3, dataArray[2],right1)
            worksheet.write(row+8, column+4, dataArray[3],right1)
            worksheet.write(row+8, column+5, dataArray[4],right1)
            worksheet.write(row+8, column+6, dataArray[5],right1)
            worksheet.write(row+8, column+7, dataArray[6],right1)
            worksheet.write(row+8, column+8, dataArray[7],right1)
            worksheet.write(row+8, column+9, dataArray[8],right1)
            worksheet.write(row+8, column+10, dataArray[9],right1)
            worksheet.write(row+8, column+11, dataArray[10],right1)
            worksheet.write(row+8, column+12, dataArray[11],right1)
            worksheet.write(row+8, column+13, dataArray[12],right1)
            worksheet.write(row+8, column+14, dataArray[13],right1)
            worksheet.write(row+8, column+15, dataArray[14],right1)
            worksheet.write(row+8, column+16, dataArray[15],right1)
            worksheet.write(row+8, column+17, dataArray[16],right1)
            worksheet.write(row+8, column+18, dataArray[17],right1)
            worksheet.write(row+8, column+19, dataArray[18],right1)
            worksheet.write(row+8, column+20, dataArray[19],right1)
            worksheet.write(row+8, column+21, dataArray[20],right1)
            worksheet.write(row+8, column+22, dataArray[21],right1)
            worksheet.write(row+8, column+23, dataArray[22],right1)
            worksheet.write(row+8, column+24, dataArray[23],right1)
            worksheet.write(row+8, column+25, dataArray[24],right1)
            worksheet.write(row+8, column+26, dataArray[25],right1)
            worksheet.write(row+8, column+27, dataArray[26],right1)
            worksheet.write(row+8, column+28, dataArray[27],right1)
            worksheet.write(row+8, column+29, dataArray[28],right1)
            worksheet.write(row+8, column+30, dataArray[29],right1)
            worksheet.write(row+8, column+31, dataArray[30],right1)
            worksheet.write(row+8, column+32, dataArray[31],right1)
            worksheet.write(row+8, column+33, dataArray[32],right1)
            worksheet.write(row+8, column+34, dataArray[33],right1)
            worksheet.write(row+8, column+35, dataArray[34],right1)
            worksheet.write(row+8, column+36, dataArray[35],right1)
            print(c)
            #worksheet.write(row, column, c)
            time.sleep(1)
            row += 1
            dataArray.clear()
            

    def stop(self):
        now = datetime.datetime.now()
        worksheet.write("B5", now.strftime("%H:%M:%S"),  left)
        workbook.close()
        self.running = False
        root.quit()
        

root.resizable(False,False)
root.mainloop()


