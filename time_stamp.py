from tkinter import *
from tkinter import messagebox 
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
    deco2_start.insert(0, time.strftime('%H:%M'))
    
def stop_time2():
    deco2_stop.delete(0, END)
    deco2_stop.insert(0, time.strftime('%H:%M'))
    
def start_time1():
    deco1_start.delete(0, END)
    deco1_start.insert(0, time.strftime('%H:%M'))
    
def stop_time1():
    deco1_stop.delete(0, END)
    deco1_stop.insert(0, time.strftime('%H:%M'))

count = 1

def save_time():
    global count
    if deco2_start.get() <= time.strftime('%H:%M') and deco2_stop.get() <= time.strftime('%H:%M'):
        lable_save_time['text'] += f"{count}.  ПМ2 : {deco2_start.get()} - {deco2_stop.get()}\n"
        lable_save_time['text'] += f"    ПМ1 : {deco1_start.get()} - {deco1_stop.get()}\n"
        file = open('file.txt', 'a', encoding='UTF-8')
        file.write(f"{count}.  ПМ2 : {deco2_start.get()} - {deco2_stop.get()}\n")
        file.write(f"    ПМ1 : {deco1_start.get()} - {deco1_stop.get()}\n")
        file.close()
        count += 1
    else:
        messagebox.showwarning('Важно!', 'Укажите время')


# Widgets

frame_top = Frame(root, bg='green', width=500, height=150)
frame_time = Frame(frame_top, bg='blue')
label_start = Label(frame_time, text='Start')
label_stop = Label(frame_time, text='Stop')

deco2_frame = Frame(frame_top, bg='blue', width=300, height=35)
label_deco2 = Label(deco2_frame, bg='grey', text='ПМ 2 :')
deco2_start = Entry(deco2_frame, width=5)
btn_start2 = Button(deco2_frame, text='\u2713', activebackground='darkgrey', command=start_time2)
deco2_stop = Entry(deco2_frame, width=5)
btn_stop2 = Button(deco2_frame, text='\u2713', activebackground='darkgrey', command=stop_time2)

deco1_frame = Frame(frame_top, bg='blue', width=300, height=35)
label_deco1 = Label(deco1_frame, bg='grey', text='ПМ 1 :')
deco1_start = Entry(deco1_frame, width=5)
btn_start1 = Button(deco1_frame, text='\u2713', activebackground='darkgrey', command=start_time1)
deco1_stop = Entry(deco1_frame, width=5)
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
btn_start2.place(x=115, y=2)
deco2_stop.place(x=170, y=3)
btn_stop2.place(x=230, y=2)

deco1_frame.place(x=50, y=90)
label_deco1.place(x=2, y=6)
deco1_start.place(x=55, y=3)
btn_start1.place(x=115, y=2)
deco1_stop.place(x=170, y=3)
btn_stop1.place(x=230, y=2)

btn_save.place(x=370, y=93)

frame_bottom.pack()
lable_save_time.place(x=2, y=2)


def foo2(e):
    deco2_start.delete ('4', END)

deco2_start.bind('<KeyPress>',foo2)




root.mainloop()
