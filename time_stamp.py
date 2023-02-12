from tkinter import *
from tkinter import messagebox
import re
import time


# root APP

root = Tk()
root.title('Time_stamp')
root.geometry('600x400+800+300')
root.resizable(width=False, height=False)
count = 1

# Functions

def start_time2():
    deco2_start.delete(0, END)
    deco2_start2.delete(0, END)
    deco2_start.insert(0, time.strftime('%H'))
    deco2_start2.insert(0, time.strftime('%M'))
    
def stop_time2():
    deco2_stop.delete(0, END)
    deco2_stop2.delete(0, END)
    deco2_stop.insert(0, time.strftime('%H'))
    deco2_stop2.insert(0, time.strftime('%M'))
    
def start_time1():
    deco1_start.delete(0, END)
    deco1_start2.delete(0, END)
    deco1_start.insert(0, time.strftime('%H'))
    deco1_start2.insert(0, time.strftime('%M'))
    
def stop_time1():
    deco1_stop.delete(0, END)
    deco1_stop2.delete(0, END)
    deco1_stop.insert(0, time.strftime('%H'))
    deco1_stop2.insert(0, time.strftime('%M'))
    
def is_valid(newval):
    return re.match("^\d{0,2}$", newval) is not None

check = (root.register(is_valid), "%P")
    
def valid_time():
    hour1 = deco2_start.get()
    minutes1 = deco2_start2.get()
    hour2 = deco2_stop.get()
    minutes2 = deco2_stop2.get()
    hour3 = deco1_start.get()
    minutes3 = deco1_start2.get()
    hour4 = deco1_stop.get()
    minutes4 = deco1_stop2.get()
    if 0 <= int(hour1) < 24 and 0 <= int(minutes1) < 60 and 0 <= int(hour2) < 24 and 0 <= int(minutes2) < 60 and 0 <= int(hour3) < 24 and 0 <= int(minutes3) < 60 and 0 <= int(hour4) < 24 and 0 <= int(minutes4) < 60:
        return True
    else:
            messagebox.showwarning('Важно!', 'Время указанно не верно')

count = 1

def save_time():
    global count
    stop_dec2 = deco2_start.get() + ':' + deco2_start2.get()
    start_dec2 = deco2_stop.get() + ':' + deco2_stop2.get()
    stop_dec1 = deco1_start.get() + ':' + deco1_start2.get()
    start_dec1 = deco1_stop.get() + ':' + deco1_stop2.get()
    if deco2_start.get() and deco2_start2.get() and deco1_start.get() and deco1_start2.get() and deco2_stop.get() and deco2_stop2.get() and deco1_stop.get() and deco1_stop2.get() and valid_time():
        lable_save_time['text'] += f"{count}.  ПМ2 : {stop_dec2} - {start_dec2}\n"
        lable_save_time['text'] += f"    ПМ1 : {stop_dec1} - {start_dec1}\n"
        file = open('file.txt', 'a', encoding='UTF-8')
        file.write(f"{count}. {time.strftime('%d-%m-%y')}  ПМ2 : {stop_dec2} - {start_dec2}\n")
        file.write(f"             ПМ1 : {stop_dec1} - {start_dec1}\n")
        file.close()
        count += 1
    else:
        messagebox.showwarning('Важно!', 'Укажите время')


# Widgets

frame_top = Frame(root, width=500, height=150)
frame_time = Frame(frame_top)
label_start = Label(frame_time, text='Start')
label_stop = Label(frame_time, text='Stop')

deco2_frame = Frame(frame_top, width=300, height=35)
label_deco2 = Label(deco2_frame, text='ПМ 2 :')
deco2_start = Entry(deco2_frame, width=2, validate='key', validatecommand=check)
deco2_start2 = Entry(deco2_frame, width=2, validate='key', validatecommand=check)
btn_start2 = Button(deco2_frame, text='\u2713', activebackground='darkgrey', command=start_time2)
deco2_stop = Entry(deco2_frame, width=2, validate='key', validatecommand=check)
deco2_stop2 = Entry(deco2_frame, width=2, validate='key', validatecommand=check)
btn_stop2 = Button(deco2_frame, text='\u2713', activebackground='darkgrey', command=stop_time2)

deco1_frame = Frame(frame_top, width=300, height=35)
label_deco1 = Label(deco1_frame, text='ПМ 1 :')
deco1_start = Entry(deco1_frame, width=2, validate='key', validatecommand=check)
deco1_start2 = Entry(deco1_frame, width=2, validate='key', validatecommand=check)
btn_start1 = Button(deco1_frame, text='\u2713', activebackground='darkgrey', command=start_time1)
deco1_stop = Entry(deco1_frame, width=2, validate='key', validatecommand=check)
deco1_stop2 = Entry(deco1_frame, width=2, validate='key', validatecommand=check)
btn_stop1 = Button(deco1_frame, text='\u2713', activebackground='darkgrey', command=stop_time1)

btn_save = Button(frame_top, text='Save', activebackground='darkgrey', command=save_time)

frame_bottom = Frame(root, width=500, height=200)
lable_save_time = Label(frame_bottom, text='')

# Packages

frame_top.pack(pady=10)
frame_time.place(x=75, y=10)
label_start.pack(side=LEFT, padx=40)
label_stop.pack(side=RIGHT, padx=40)

deco2_frame.place(x=50, y=40)
label_deco2.place(x=2, y=6)
deco2_start.place(x=55, y=3)
deco2_start2.place(x=85, y=3)
btn_start2.place(x=115, y=2)
deco2_stop.place(x=170, y=3)
deco2_stop2.place(x=200, y=3)
btn_stop2.place(x=230, y=2)

deco1_frame.place(x=50, y=90)
label_deco1.place(x=2, y=6)
deco1_start.place(x=55, y=3)
deco1_start2.place(x=85, y=3)
btn_start1.place(x=115, y=2)
deco1_stop.place(x=170, y=3)
deco1_stop2.place(x=200, y=3)
btn_stop1.place(x=230, y=2)

btn_save.place(x=370, y=93)

frame_bottom.pack()
lable_save_time.place(x=2, y=2)


root.mainloop()
