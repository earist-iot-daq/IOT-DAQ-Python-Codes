import time
import xlsxwriter
import pyrebase
import datetime
import tkinter as tk
from datetime import date
import threading
from PIL import ImageTk, Image

today = date.today
dataArray = []
dataArray_b = []

now = datetime.datetime.now()
run = True
c = 0

def start_extract():
    global worksheet
    global worksheet_b
    global workbook
    global run
    now = datetime.datetime.now()
    button1.configure(state="disabled")
    button2.configure(state="normal")
    time_started2 = tk.Label(root, text=now.strftime('%H:%M:%S'), font="times 11 italic", bg="white")
    time_started2.place(relx=.2, rely=.09, relheight=.04, relwidth=.17)
    print("STARTED!!!")
    threading.Thread(target=count_loop).start()
    worksheet.write("B3", now.strftime("%B %d, %Y"), left)
    worksheet.write("B4", now.strftime("%H:%M:%S"), left)
    worksheet_b.write("B3", now.strftime("%B %d, %Y"), left)
    worksheet_b.write("B4", now.strftime("%H:%M:%S"), left)
    run = True

def stop():
    global worksheet
    global worksheet_b
    global workbook
    global c
    global run
    print("STOPPED!!!")
    now = datetime.datetime.now()
    worksheet.write("B5", now.strftime("%H:%M:%S"), left)
    worksheet.write("G4", c, left)
    worksheet_b.write("B5", now.strftime("%H:%M:%S"), left)
    worksheet_b.write("G4", c, left)
    workbook.close()
    now = datetime.datetime.now()
    #time_ended3 = tk.Label(root, text=now.strftime('%H:%M:%S'), font="times 11 italic", bg="white")
    #time_ended3.place(relx=.2, rely=.15, relheight=.04, relwidth=.17)
    button1.configure(state="normal")
    button2.configure(state="disabled")
    run = False

def quit():
    root.destroy()

root = tk.Tk()
root.geometry("560x400")
root.title("IOT-DAQ")

#excel
excelName = now.strftime('%H-%M-%S')
workbook = xlsxwriter.Workbook(str(excelName) + ".xlsx")
worksheet = workbook.add_worksheet('Device A')
worksheet_b = workbook.add_worksheet('Device B')

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
right.set_bg_color("#AEB6BF")
right1 = workbook.add_format()
right1.set_align("right")
left = workbook.add_format()
left.set_align("left")
left.set_bg_color("#AEB6BF")
center = workbook.add_format()
center.set_center_across()
title = workbook.add_format({"font": "Times", "font_size": 15, "bold": True})
title.set_center_across()

worksheet.merge_range('B1:N1',
                      'MICROCONTROLLER BASED INTERNET OF THINGS DATA ACQUISITION FOR MONITORING AND CONTROL SYSTEM USING CLOUD PLATFORM',
                      title)
worksheet.write("A4", "Time Started:", right)
worksheet.write("A5", "Time Ended:", right)
worksheet.write("A3", "Date:", right)
worksheet.write("A7", "Time", bold_and_center)
worksheet.write("F4", "Samples:", right)
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

#B
worksheet_b.merge_range('B1:N1',
                      'MICROCONTROLLER BASED INTERNET OF THINGS DATA ACQUISITION FOR MONITORING AND CONTROL SYSTEM USING CLOUD PLATFORM',
                      title)
worksheet_b.write("A4", "Time Started:", right)
worksheet_b.write("A5", "Time Ended:", right)
worksheet_b.write("A3", "Date:", right)
worksheet_b.write("A7", "Time", bold_and_center)
worksheet_b.write("F4", "Samples:", right)
worksheet_b.write("B7", " ADC CH1 Cloud", bold_and_center)
worksheet_b.write("C7", " ADC CH2 Cloud", bold_and_center)
worksheet_b.write("D7", " ADC CH3 Cloud", bold_and_center)
worksheet_b.write("E7", " ADC CH4 Cloud", bold_and_center)
worksheet_b.write("F7", " ADC CH1 Local", bold_and_center)
worksheet_b.write("G7", "ADC CH2 Local", bold_and_center)
worksheet_b.write("H7", "ADC CH3 Local", bold_and_center)
worksheet_b.write("I7", "ADC CH4 Local", bold_and_center)
worksheet_b.write("J7", "GPIO CH1 Cloud", bold_and_center)
worksheet_b.write("K7", "GPIO CH2 Cloud", bold_and_center)
worksheet_b.write("L7", "GPIO CH3 Cloud", bold_and_center)
worksheet_b.write("M7", "GPIO CH4 Cloud", bold_and_center)
worksheet_b.write("N7", "GPIO CH1 Local", bold_and_center)
worksheet_b.write("O7", "GPIO CH2 Local", bold_and_center)
worksheet_b.write("P7", "GPIO CH3 Local", bold_and_center)
worksheet_b.write("Q7", "GPIO CH4 Local", bold_and_center)
worksheet_b.write("R7", "Relay CH1 Cloud", bold_and_center)
worksheet_b.write("S7", "Relay CH2 Cloud", bold_and_center)
worksheet_b.write("T7", "MOSFET CH1 Cloud", bold_and_center)
worksheet_b.write("U7", "MOSFET CH2 Cloud", bold_and_center)
worksheet_b.write("V7", "Relay CH1 Local", bold_and_center)
worksheet_b.write("W7", "Relay CH2 Local", bold_and_center)
worksheet_b.write("X7", "MOSFET CH1 Local", bold_and_center)
worksheet_b.write("Y7", "MOSFET CH2 Local", bold_and_center)
worksheet_b.write("Z7", "Digital Input Monitor DI-A Local", bold_and_center)
worksheet_b.write("AA7", "Digital Input Monitor DI-B Local", bold_and_center)
worksheet_b.write("AB7", "Digital Output Monitor DO-A Local", bold_and_center)
worksheet_b.write("AC7", "Digital Output Monitor DO-B Local", bold_and_center)
worksheet_b.write("AD7", "Counter CH1", bold_and_center)
worksheet_b.write("AE7", "Counter CH2", bold_and_center)
worksheet_b.write("AF7", "Counter CH3", bold_and_center)
worksheet_b.write("AG7", "Counter CH4", bold_and_center)
worksheet_b.write("AH7", "Counter CH5", bold_and_center)
worksheet_b.write("AI7", "Counter CH6", bold_and_center)
worksheet_b.write("AJ7", "Internal Access Register Address", bold_and_center)
worksheet_b.write("AK7", "Internal Access Register Info", bold_and_center)

worksheet_b.set_column('A:A', 15)
worksheet_b.set_column('B:B', 15)
worksheet_b.set_column('C:C', 15)
worksheet_b.set_column('D:D', 15)
worksheet_b.set_column('E:E', 15)
worksheet_b.set_column('F:F', 15)
worksheet_b.set_column('G:G', 15)
worksheet_b.set_column('H:H', 14)
worksheet_b.set_column('I:I', 16)
worksheet_b.set_column('J:J', 16)
worksheet_b.set_column('K:K', 16)
worksheet_b.set_column('L:L', 16)
worksheet_b.set_column('M:M', 16)
worksheet_b.set_column('N:N', 16)
worksheet_b.set_column('O:O', 15)
worksheet_b.set_column('P:P', 15)
worksheet_b.set_column('Q:Q', 15)
worksheet_b.set_column('R:R', 17)
worksheet_b.set_column('S:S', 17)
worksheet_b.set_column('T:T', 19)
worksheet_b.set_column('U:U', 19)
worksheet_b.set_column('V:V', 19)
worksheet_b.set_column('W:W', 19)
worksheet_b.set_column('X:X', 20)
worksheet_b.set_column('Y:Y', 20)
worksheet_b.set_column('Z:Z', 30)
worksheet_b.set_column('AA:AA', 30)
worksheet_b.set_column('AB:AB', 32)
worksheet_b.set_column('AC:AC', 32)
worksheet_b.set_column('AD:AD', 15)
worksheet_b.set_column('AE:AE', 13)
worksheet_b.set_column('AF:AF', 13)
worksheet_b.set_column('AG:AG', 13)
worksheet_b.set_column('AH:AH', 13)
worksheet_b.set_column('AI:AI', 13)
worksheet_b.set_column('AJ:AJ', 30)
worksheet_b.set_column('AK:AK', 27)

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
    global dataArray
    count = 0
    previousCount = 0
    for x in extract:
        count = count + 1
        if (x == ','):
            dataArray.append(extract[previousCount:count - 1])
            previousCount = count

        if (count == len(extract)):
            dataArray.append(extract[previousCount:len(extract)])
            
def extractData_b(extract_b):
    global dataArray_b
    count = 0
    previousCount = 0
    for x in extract_b:
        count = count + 1
        if (x == ','):
            dataArray_b.append(extract_b[previousCount:count - 1])
            previousCount = count

        if (count == len(extract_b)):
            dataArray_b.append(extract_b[previousCount:len(extract_b)])

def count_loop():
    global c
    row = 0
    column = 0
    global run
    while True:
        c += 1
        ADC = db.child("A").get()
        info = ADC.val()
        extractData(info)
        now = datetime.datetime.now()
        
        ADC_b = db.child("B").get()
        info_b = ADC_b.val()
        extractData_b(info_b)
        print(info_b)
        
        worksheet.write(row + 7, column, now.strftime("%H:%M:%S"))
        worksheet.write(row + 7, column + 1, dataArray[0], right1)
        worksheet.write(row + 7, column + 2, dataArray[1], right1)
        worksheet.write(row + 7, column + 3, dataArray[2], right1)
        worksheet.write(row + 7, column + 4, dataArray[3], right1)
        worksheet.write(row + 7, column + 5, dataArray[4], right1)
        worksheet.write(row + 7, column + 6, dataArray[5], right1)
        worksheet.write(row + 7, column + 7, dataArray[6], right1)
        worksheet.write(row + 7, column + 8, dataArray[7], right1)
        worksheet.write(row + 7, column + 9, dataArray[8], right1)
        worksheet.write(row + 7, column + 10, dataArray[9], right1)
        worksheet.write(row + 7, column + 11, dataArray[10], right1)
        worksheet.write(row + 7, column + 12, dataArray[11], right1)
        worksheet.write(row + 7, column + 13, dataArray[12], right1)
        worksheet.write(row + 7, column + 14, dataArray[13], right1)
        worksheet.write(row + 7, column + 15, dataArray[14], right1)
        worksheet.write(row + 7, column + 16, dataArray[15], right1)
        worksheet.write(row + 7, column + 17, dataArray[16], right1)
        worksheet.write(row + 7, column + 18, dataArray[17], right1)
        worksheet.write(row + 7, column + 19, dataArray[18], right1)
        worksheet.write(row + 7, column + 20, dataArray[19], right1)
        worksheet.write(row + 7, column + 21, dataArray[20], right1)
        worksheet.write(row + 7, column + 22, dataArray[21], right1)
        worksheet.write(row + 7, column + 23, dataArray[22], right1)
        worksheet.write(row + 7, column + 24, dataArray[23], right1)
        worksheet.write(row + 7, column + 25, dataArray[24], right1)
        worksheet.write(row + 7, column + 26, dataArray[25], right1)
        worksheet.write(row + 7, column + 27, dataArray[26], right1)
        worksheet.write(row + 7, column + 28, dataArray[27], right1)
        worksheet.write(row + 7, column + 29, dataArray[28], right1)
        worksheet.write(row + 7, column + 30, dataArray[29], right1)
        worksheet.write(row + 7, column + 31, dataArray[30], right1)
        worksheet.write(row + 7, column + 32, dataArray[31], right1)
        worksheet.write(row + 7, column + 33, dataArray[32], right1)
        worksheet.write(row + 7, column + 34, dataArray[33], right1)
        worksheet.write(row + 7, column + 35, dataArray[34], right1)
        worksheet.write(row + 7, column + 36, dataArray[35], right1)
        
       
        worksheet_b.write(row + 7, column, now.strftime("%H:%M:%S"))
        worksheet_b.write(row + 7, column + 1, dataArray_b[0], right1)
        worksheet_b.write(row + 7, column + 2, dataArray_b[1], right1)
        worksheet_b.write(row + 7, column + 3, dataArray_b[2], right1)
        worksheet_b.write(row + 7, column + 4, dataArray_b[3], right1)
        worksheet_b.write(row + 7, column + 5, dataArray_b[4], right1)
        worksheet_b.write(row + 7, column + 6, dataArray_b[5], right1)
        worksheet_b.write(row + 7, column + 7, dataArray_b[6], right1)
        worksheet_b.write(row + 7, column + 8, dataArray_b[7], right1)
        worksheet_b.write(row + 7, column + 9, dataArray_b[8], right1)
        worksheet_b.write(row + 7, column + 10, dataArray_b[9], right1)
        worksheet_b.write(row + 7, column + 11, dataArray_b[10], right1)
        worksheet_b.write(row + 7, column + 12, dataArray_b[11], right1)
        worksheet_b.write(row + 7, column + 13, dataArray_b[12], right1)
        worksheet_b.write(row + 7, column + 14, dataArray_b[13], right1)
        worksheet_b.write(row + 7, column + 15, dataArray_b[14], right1)
        worksheet_b.write(row + 7, column + 16, dataArray_b[15], right1)
        worksheet_b.write(row + 7, column + 17, dataArray_b[16], right1)
        worksheet_b.write(row + 7, column + 18, dataArray_b[17], right1)
        worksheet_b.write(row + 7, column + 19, dataArray_b[18], right1)
        worksheet_b.write(row + 7, column + 20, dataArray_b[19], right1)
        worksheet_b.write(row + 7, column + 21, dataArray_b[20], right1)
        worksheet_b.write(row + 7, column + 22, dataArray_b[21], right1)
        worksheet_b.write(row + 7, column + 23, dataArray_b[22], right1)
        worksheet_b.write(row + 7, column + 24, dataArray_b[23], right1)
        worksheet_b.write(row + 7, column + 25, dataArray_b[24], right1)
        worksheet_b.write(row + 7, column + 26, dataArray_b[25], right1)
        worksheet_b.write(row + 7, column + 27, dataArray_b[26], right1)
        worksheet_b.write(row + 7, column + 28, dataArray_b[27], right1)
        worksheet_b.write(row + 7, column + 29, dataArray_b[28], right1)
        worksheet_b.write(row + 7, column + 30, dataArray_b[29], right1)
        worksheet_b.write(row + 7, column + 31, dataArray_b[30], right1)
        worksheet_b.write(row + 7, column + 32, dataArray_b[31], right1)
        worksheet_b.write(row + 7, column + 33, dataArray_b[32], right1)
        worksheet_b.write(row + 7, column + 34, dataArray_b[33], right1)
        worksheet_b.write(row + 7, column + 35, dataArray_b[34], right1)
        worksheet_b.write(row + 7, column + 36, dataArray_b[35], right1)
        
        num_sample1 = tk.Label(root, text=c, font="times 12 italic", bg="white")
        num_sample1.place(relx=.7, rely=.09, relheight=.04, relwidth=.1)
        time_ended3 = tk.Label(root, text=now.strftime('%H:%M:%S'), font="times 11 italic", bg="white")
        time_ended3.place(relx=.2, rely=.15, relheight=.04, relwidth=.17)
        time.sleep(1)
        row += 1
        dataArray.clear()
        dataArray_b.clear()
        if run == False:
            break

file = "hotdog.gif"
info = Image.open(file)

load = Image.open("qrcode.png")
render = ImageTk.PhotoImage(load)

img = tk.Label(image=render)
img.image = render
img.place(x=1, y=1)

frames = info.n_frames  # gives total number of frames that gif contains
im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None

def animation():
    #lambda: animation()
    global count
    global anim
    im2 = im[count]

    gif_label.configure(image=im2,)
    #gif_label2.configure(image=im2, )
    count += 1
    if count == frames:
        count = 0
    anim = root.after(80,lambda :animation())

frame = tk.Frame(root,bg="#AEB6BF")
frame.place(relheight=1,relwidth=2)

img = ImageTk.PhotoImage(Image.open("qrcode.png"))
label_img = tk.Label(root, image=img)
label_img.place(relx=.01, rely=.855)

img1 = ImageTk.PhotoImage(Image.open("logo12.png"))
label_img1 = tk.Label(root, image=img1)
label_img1.place(relx=.89,rely=.02)


date_started = tk.Label(root, text="Date:" ,font="times 12 italic" , bg= "#AEB6BF")
date_started.place(relx=.11,rely=.03,relheight=.04,relwidth=.07)

time_started = tk.Label(root, text="Time Started:" ,font="times 12 italic" , bg= "#AEB6BF")
time_started.place(relx=.01,rely=.09,relheight=.04,relwidth=.17)

time_ended = tk.Label(root, text="Time Ended:" ,font="times 12 italic" , bg= "#AEB6BF")
time_ended.place(relx=.01,rely=.15,relheight=.04,relwidth=.17)

date_started1 = tk.Label(root, text=now.strftime('%B %d, %Y') ,font="times 11 italic" , bg= "white")
date_started1.place(relx=.2,rely=.03,relheight=.04,relwidth=.25)

time_started2 = tk.Label(root, text="H : M : S" ,font="times 11 italic" , bg= "white")
time_started2.place(relx=.2,rely=.09,relheight=.04,relwidth=.17)

time_ended3 = tk.Label(root, text="H : M : S" ,font="times 11 italic" , bg= "white")
time_ended3.place(relx=.2,rely=.15,relheight=.04,relwidth=.17)

label5 = tk.Label(root,text='visit us @ https//earist-iot-daq.innotechphils.com',font = "times 10 italic",bg="#AEB6BF")
label5.place(relx=.11,rely=.865,relheight=.04,relwidth=.49)#AEB6BF

label6 = tk.Label(root,text='fb page: IOT-DAQ',font = "times 10 italic",bg="#AEB6BF")
label6.place(relx=.11,rely=.92,relheight=.04,relwidth=.19)

num_sample = tk.Label(root, text="Samples:" ,font="times 12 italic" , bg= "#AEB6BF")
num_sample.place(relx=.7,rely=.03,relheight=.04,relwidth=.1)

num_sample1 = tk.Label(root, text="" ,font="times 12 italic" , bg= "white")
num_sample1.place(relx=.7,rely=.09,relheight=.04,relwidth=.1)

gif_label = tk.Label(root,image="")
gif_label.place(relx=.1,rely=.20)

gif_label3 = tk.Label(root,text="hello")
gif_label3.place(relx=1,rely=1,relwidth=.01, relheight=.01)

button1 = tk.Button(root,text="START",bg = "#605EEB",font ="times 16 italic bold",command=start_extract)
button1.place(relx=.13,rely=.27,relheight=.20,relwidth=.20)

button2 = tk.Button(root,text="STOP",bg = "#605EEB",font ="times 16 italic bold",command=stop)
button2.place(relx=.13,rely=.58,relheight=.20,relwidth=.20)
button2.config(state="disabled")

button3 = tk.Button(root,text="Close",bg = "#605EEB",font ="times 13 italic ",command=quit)
button3.place(relx=.80,rely=.865,relheight=.10,relwidth=.10)

animation()

root.resizable(False, False)
root.mainloop()

