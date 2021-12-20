import tkinter as tk
from tkinter import ttk,constants
import random
import time
import sys

root = tk.Tk()
root.title("Algo Visualizer")
root.maxsize(1920,1080)
root.config(bg='#303030')

selected = tk.StringVar()
dt = []
color_data = []
height = 880
width = 1900
off = 0
sp = 10
green  = '#1EDC53'
blue = '#03DAC6'
purple = '#BB86FC'
delay = None



def data():
    global dt,color_data
    x_width = width / (len(dt) )
    ndata = [i/max(dt) for i in dt]
    cv.delete('all')
    for i, h in enumerate(ndata):
        x0 = i * x_width + sp
        y0 = height - h * 840
        x1 = (i+1) * x_width
        y1 = height
        cv.create_rectangle(x0,y0,x1,y1,fill=color_data[i],outline=color_data[i])
        cv.create_text(x0+2,y0,anchor=constants.SW, text = str(dt[i]), fill='#FFFFFF')
    root.update_idletasks()

def data1():
    global dt,color_data
    x_width = width / (len(dt) )
    ndata = [i/max(dt) for i in dt]
    cv.delete('all')
    for i, h in enumerate(ndata):
        x0 = i * x_width + sp
        y0 = height - h * 840
        x1 = (i+1) * x_width
        y1 = height
        cv.create_rectangle(x0,y0,x1,y1,fill=blue,outline=blue)
        cv.create_text(x0+2,y0,anchor=constants.SW, text = str(dt[i]), fill='#FFFFFF')
    root.update_idletasks()


def algpick():
    global dt,color_data
    if menu.get() == 'Selection Sort':
        selsort()
    elif menu.get() == 'Bubble Sort':
        bubblesort()
    elif menu.get() == 'Insertion Sort':
        insort()
    elif menu.get() == 'Merge Sort':
        merge_sort()



def bubblesort():
    global dt,color_data
    for i in range(len(dt) - 1):
        for j in range(0, len(dt) - i - 1):
            color_data[j] = green
            color_data[j+1] = purple

            if dt[j] > dt[j + 1]:
                dt[j], dt[j + 1] = dt[j + 1], dt[j]
                #color_data[]
            time.sleep(delay/5)
            data()
            color_data[j], color_data[j+1] = blue,blue
    u = color_data
    color_data = [blue for i in u]
    data()



def selsort():
    global dt,color_data
    print(delay)
    for i in range(0,len(dt)):
        small = i
        color_data[i] = green
        for j in range(i+1,len(dt)):
            if dt[j] < dt[small]:
                if small != i:
                    color_data[small] = blue
                small = j
                color_data[small] = purple
                data()

        dt[i],dt[small] = dt[small],dt[i]
        time.sleep(delay /5)
        color_data[i] = blue
        color_data[small] = blue
        data()
    u =  color_data
    color_data = [blue for i in u]
    data()



def insort():
    global dt,color_data
    for i in range(1, len(dt)):
        key = dt[i]
        color_data[i] = green
        j = i - 1
        while j >= 0 and key < dt[j]:
            dt[j + 1] = dt[j]
            color_data[j] = blue
            j -= 1
        dt[j + 1] = key
        time.sleep(delay)
        data()
    u = color_data
    color_data = [blue for i in u]
    data()


def merge_sort():
    global dt, color_data,delay
    merge_sort_alg(dt, 0, len(dt) - 1)
    u = color_data
    color_data = [blue for _ in u]
    data1()


def merge_sort_alg(da, left, right):
    if left < right:
        middle = (left + right) // 2
        print('middle',middle)
        merge_sort_alg(da, left, middle)
        merge_sort_alg(da, middle + 1, right)
        merge(da, left, middle, right)



def merge(da, left, middle, right):
    global color_data
    color_data = getColorArray(da, left, right, middle)
    data1()
    time.sleep(delay/10)

    leftp = da[left:middle + 1]
    rightp = da[middle + 1: right + 1]
    print("left",leftp)
    print("right",rightp)

    l = r = 0

    for d in range(left, right + 1):
        if l < len(leftp) and r < len(rightp):
            data1()
            if leftp[l] <= rightp[r]:
                da[d] = leftp[l]
                l += 1
            else:
                da[d] = rightp[r]
                r += 1

        elif l < len(leftp):
            da[d] = leftp[l]
            l += 1
        else:
            da[d] = rightp[r]
            r += 1

    color_data = getColorArray(da, left, right, middle)
    data1()
    time.sleep(delay/10)



def getColorArray(data, left, middle, right):
    colorArray = []

    return colorArray



def des():
    root.destroy()
    sys.exit(0)



def gen():
    global delay
    cv.delete('all')
    print('Alg Selected: ' + selected.get())
    try:
        minVal = int(min_entry.get())
    except:
        minVal = 1
    try:
        maxVal = int(max_entry.get())
    except:
        maxVal = 10
    try:
        size = int(size_entry.get())
    except:
        size = 10
    delay = (1/delay_slider.get())
    print(delay)
    if minVal < 0: minVal = 0
    if maxVal > 300: maxVal = 300
    if size > 80 or size < 3: size = 80
    if minVal > maxVal: minVal, maxVal = maxVal, minVal
    dt.clear()
    color_data.clear()
    for u in range(size):
        dt.append(random.randrange(minVal, maxVal + 1))
        color_data.append(blue)
    data()




f = tk.Frame(root,width = 1900, height = 200, bg = '#303030')
f.grid(row=0,column=0,padx=10,pady=10)

cv = tk.Canvas(root, width=1900, height = 880,bg = '#303030',bd=-2)
cv.grid(row=1,column=0,padx=10,pady=10)


#UI Row 1
alg_name = tk.Label(f, text = "Algorithm: ",bg = '#303030',fg='#BB86FC')
alg_name.grid(row=0,column=0,padx=10,pady=10,sticky=constants.W)

menu = ttk.Combobox(f,textvariable=selected, values=['Selection Sort','Bubble Sort','Insertion Sort','Merge Sort'])
menu.grid(row=0,column=1,padx=10,pady=10)
menu.current(0)

generate_button = tk.Button(f,text='Generate', command = gen,bg='#BB86FC',fg='#FFFFFF',relief='flat')
generate_button.grid(row=0,column=2,padx=10,pady=10)

run_button = tk.Button(f,text='Run', command = algpick,bg='#BB86FC',fg='#FFFFFF',relief='flat')
run_button.grid(row=0,column=3,padx=10,pady=10)

delay_name = tk.Label(f, text = "Algorithm Speed: ",bg = '#303030',fg='#BB86FC')
delay_name.grid(row=0,column=4,padx=10,pady=10,sticky=constants.W)

delay_slider = ttk.Scale(f, from_=0.05,to=10,length = 300,orient=constants.HORIZONTAL)
delay_slider.grid(row=0,column=5,padx = 10,pady = 10)
delay_slider.set(3)
style = ttk.Style()
style.configure("TScale", background="#BB86FC")

close_button = tk.Button(f, text='Exit', command=des, bg='#D03B56', fg='#FFFFFF', relief='flat')
close_button.grid(row=0, column=6, padx=10, pady=10,sticky=constants.NE)


#UI Row 2
size_label= tk.Label(f,text='Size: ',bg='#303030',fg='#BB86FC')
size_label.grid(row=1,column=0,padx=10,pady=10,sticky=constants.W)
size_entry = tk.Entry(f)
size_entry.grid(row=1,column=1,padx=10,pady=10,sticky=constants.W)

min_label= tk.Label(f,text='Min Value: ',bg='#303030',fg='#BB86FC')
min_label.grid(row=1,column=2,padx=10,pady=10,sticky=constants.W)
min_entry = tk.Entry(f)
min_entry.grid(row=1,column=3,padx=10,pady=10,sticky=constants.W)

max_label= tk.Label(f,text='Max Value: ',bg='#303030',fg='#BB86FC')
max_label.grid(row=1,column=4,padx=10,pady=10,sticky=constants.W)
max_entry = tk.Entry(f)
max_entry.grid(row=1,column=5,padx=10,pady=10,sticky=constants.W)


root.mainloop()
