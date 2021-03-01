from tkinter import *
from tkinter import messagebox
import pyrebase
import datetime
import requests

Height = 400
Width = 500

    
root = Tk()
root.title("Data Acquisition")


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
#.push(),.set()
def data():
    now = datetime.datetime.now()
    C1 = channel1.get() +" V "
    #display.insert(END,C1)
    C2 = channel2.get() +" V "
    #txt2.insert(END,C2)
    C3 =channel3.get() +" V "
    #txt3.insert(END,C3)
    data1 = {"Values": C1} 
    data2 = {"Values": C2}
    data3 = {"Values": C3}
    messagebox.showinfo("DATA ACQUSITION","Data Added")
    db.child("ADC").child("Channel-1").child("Date: "+now.strftime("%y-%m-%d")).child("Time= "+now.strftime("%H:%M:%S")).set(data1)
    db.child("ADC").child("Channel-2").child("Date: "+now.strftime("%y-%m-%d")).child("Time= "+now.strftime("%H:%M:%S")).set(data2)
    db.child("ADC").child("Channel-3").child("Date: "+now.strftime("%y-%m-%d")).child("Time= "+now.strftime("%H:%M:%S")).set(data3)
    channel1.delete(0,END)
    channel2.delete(0,END)
    channel3.delete(0,END)  
    display.delete(1.0,END)
    txt2.delete(0,END)
    txt3.delete(0,END)
        
def info():
    ADC = db.child("ADC").get() 
    time = txt3.get()
    information = ADC.val()
    channel_list = choose.get()
    date = txt2.get()
    #display.insert(END,information)
    try:    
        inf = information[channel_list]["Date: "+date]["Time= "+time]["Values"]
        display.insert(END,"  "+channel_list+"        "+date+"        "+time+"         "+inf+"\n")
        txt3.delete(0,END)
    except:
        messagebox.showinfo("database","NO DATA FOUND!")
        txt3.delete(0,END)

def clear():
    display.delete(1.0,END)
 
canvas = Canvas(root, height=Height, width=Width,)
canvas.pack()

upper = Frame(root, bg="#17202A")
upper.place(relheight=.5 , relwidth=2)

lower = Frame(root, bg="#F1948A")
lower.place(rely=0.5, relheight=.5, relwidth=2)

#BUTTONS

info = Button(root, text="Info", bg="#F1948A", font=60, command=info )
info.place(relx=0.52 , rely=0.38 , relheight=.1 ,relwidth=0.15 )

infoclr = Button(root, text="Clear Info", bg="#F1948A", font=60, command=clear )
infoclr.place(relx=0.67 , rely=0.38 , relheight=.1 ,relwidth=0.15 )

submit = Button(root, text="Submit", bg="#F1948A", font=60, command=data )
submit.place(relx=0.15 , rely=0.38 , relheight=.1 ,relwidth=0.15 )
#channel entry
channel1 = Entry()
channel1.place(relx=0.15 , rely=0.15 , relheight=.05 ,relwidth=0.15 )

channel2 = Entry()
channel2.place(relx=0.15 , rely=0.22 , relheight=.05 ,relwidth=0.15 )

channel3 = Entry()
channel3.place(relx=0.15 , rely=0.3 , relheight=.05 ,relwidth=0.15 )

options = [
        "Channel-1",
        "Channel-2",
        "Channel-3",
    ]
#
choose = StringVar()
choose.set(options[0])

opts = OptionMenu(root, choose, *options)#channel list
opts.place(relx=0.65, rely=0.15, relwidth=.215, relheight=.05)

txt2 = Entry(root)#date
txt2.place(relx=0.65, rely=0.22, relwidth=.17, relheight=.05)

txt3 = Entry(root)#time
txt3.place(relx=0.65, rely=0.3, relwidth=.17, relheight=.05)

#channel labels

label = Label(root, text="ADC INPUT",font="aerial 13 bold", bg="#17202A", fg="#F1948A")
label.place(relx=0.01 , rely=0.03 , relheight=.1 ,relwidth=0.4 )

label1 = Label(root, text="CH-1 in",font="aerial 10 ", bg="#17202A", fg="#F1948A")
label1.place(relx=0.03 , rely=0.15 , relheight=.05 ,relwidth=0.1 )

label2 = Label(root, text="CH-2 in",font="aerial 10 ", bg="#17202A", fg="#F1948A")
label2.place(relx=0.03 , rely=0.22 , relheight=.05 ,relwidth=0.1 )

label3 = Label(root, text="CH-3 in",font="aerial 10 ", bg="#17202A", fg="#F1948A")
label3.place(relx=0.03 , rely=0.3 , relheight=.05 ,relwidth=0.1 )

label4 = Label(root, text="EXTRACT DATA",font="aerial 13 bold", bg="#17202A", fg="#F1948A")
label4.place(relx=0.5 , rely=0.03 , relheight=.1 ,relwidth=0.4 )

label5 = Label(root, text="Select Channel",font="aerial 10 ", bg="#17202A", fg="#F1948A")
label5.place(relx=0.45 , rely=0.15 , relheight=.05 ,relwidth=0.2 )

label6 = Label(root, text="DATE(y/m/d)",font="aerial 10 ", bg="#17202A", fg="#F1948A")
label6.place(relx=0.45 , rely=0.22 , relheight=.05 ,relwidth=0.2 )

label7 = Label(root, text="TIME(h:m:s)",font="aerial 10 ", bg="#17202A", fg="#F1948A")
label7.place(relx=0.45 , rely=0.3 , relheight=.05 ,relwidth=0.2 )
#display
display = Text(root)
display.place(relx=0.01, rely=0.6, relwidth=.98, relheight=.39)

parameters = Label(root, text= "Channel",bg="gray")
parameters.place(relx=0.015, rely=0.54, relwidth=.2, relheight=.06)

parameters1 = Label(root, text= "Date",bg="gray")
parameters1.place(relx=0.27, rely=0.54, relwidth=.2, relheight=.06)

parameters2= Label(root, text= "Time", bg="gray")
parameters2.place(relx=0.53, rely=0.54, relwidth=.2, relheight=.06)

parameters3 = Label(root, text= "Values", bg="gray")
parameters3.place(relx=0.78, rely=0.54, relwidth=.2, relheight=.06)
#lower frame details

root.resizable(False,False)
root.mainloop()



