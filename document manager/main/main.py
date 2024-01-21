'''
Created by Ishan Pathak, for learning purpose
'''
#################
#importing modules
from tkinter import *
import time
import os

#declaring variables
HEIGHT = 600
WIDTH = 1153

USERNAME = "username"
PASSWORD = "password"

emplst = []

#just some variable which will be used in naming file
timenow = time.time()
print(time)

#getting current directory
crdir = os.getcwd()

#Tk object
win = Tk()

img = PhotoImage(file= "C:\\Users\\ishan\\OneDrive\\Pictures\\1.png")

#declaring Tkinter variables
username_val = StringVar()
password_val = StringVar()

name_val = StringVar()
age_val = StringVar()
exp_val = StringVar()
designation_val = StringVar()
dateofjoining_val = StringVar()
more_val = StringVar()

statusvar = StringVar()
statusvar.set("ready")

#file mechanism
#creating location for directory
storage_dir = crdir+"\\data"
#if directory already exists then just create the file whith qppend+, else create directory, get current directory and then create filename as 
#as 'filepath' 
if os.path.isdir(storage_dir):
    print("directory exists")
    statusvar.set("directory exists")
    os.chdir(storage_dir)
    filepath=os.getcwd() + "\\" + "file__" +str(timenow)
    print(filepath)
    file_ = open(filepath, "a+")
    time.sleep(.6)
    statusvar.set("ready")

else:
    os.mkdir(storage_dir)
    os.chdir(storage_dir)
    filepath=os.getcwd() + str(timenow)

#making a class object to oop each entered data for sake of simplicty, i could hav done more but i am justa beginner in oop and GUI, so that's about
#it for now
class employee():
    count = 0

    def __init__(self, name, age, designation, exp, dateofjoining, more) -> None:
        self.name = name
        self.age = age
        self.exp = exp
        self.designation = designation
        self.dateofjoining = dateofjoining
        self.more = more
        
        employee.count += 1
    
    def add(self):
        s = employee.count
        newdict = {}
        newdict[0] = s
        newdict[1] = self.name
        newdict[2] = self.age
        newdict[3] = self.designation
        newdict[4] = self.exp
        newdict[5] = self.dateofjoining
        newdict[6] = self.more
        
        #with the help for loop creating labels to show added data into table grid in tkinter window GUI
        for i in newdict:
            Label(contentframe2, text=newdict[i], pady=2, padx=2, bg="white", font=("Noto Serif", 15)).grid(row=s+1, column=i)

def clear_values():
    name_val.set("")
    age_val.set("")
    exp_val.set("")
    designation_val.set("")
    more_val.set("")
    dateofjoining_val.set("")

def check():
    username = username_val.get()
    password = password_val.get()

    if password==PASSWORD and username==USERNAME:
        print("verified")
        greetframe.pack_forget()
        mainframe.pack(fill=BOTH, expand=1, side=TOP)
    else:
        statusvar.set("Wrong credentials. Try again.")
        statuslabel.update()
        time.sleep(1)
        statusvar.set("ready")
        password_val.set("")
        username_val.set("")

def button2addfunction():
    name = name_val.get()
    age = age_val.get()
    designation = designation_val.get()
    exp = exp_val.get()
    dateofjoining = dateofjoining_val.get()
    more = more_val.get()

    lst = [name, age, designation, exp, dateofjoining, more]
    var = 0

    for i in lst:
        if i == "":
            var +=1

    if var == 0:

        emplst.append({name:"name", "age":age, "designation":designation, "exp": exp, "date of joining":dateofjoining, "more":more})

        emp1 = employee(name, age, designation, exp, dateofjoining, more)
        emp1.add()
        clear_values()

    else:
        print("ERROR")
        statusvar.set(f"please fill all the details...You have not filled {var} details")
        statuslabel.update()
        time.sleep(0.6)
        statusvar.set("ready")

def save():

    statusvar.set("initializing....")
    statuslabel.update()
    time.sleep(0.7)

    statusvar.set("saving....")
    statuslabel.update()
    time.sleep(0.6)

    file = open(filepath, "a+")

    for i in emplst:        
        file.write(str(i) + "\n")

    file.close()
    statusvar.set("saved!")
    statuslabel.update()
    time.sleep(0.2)

    statusvar.set("Ready")
    statuslabel.update()

def changecolor(event, button, color1 = "black", color2 = "white"):
    button.configure(background=color1, fg=color2, border=5)

win.geometry(f"{WIDTH}x{HEIGHT}")
win.minsize(WIDTH,HEIGHT)
win.title("Employee Index")

bgimage = Label(win, image=img)
bgimage.place(x=0, y=0)


winwidth = win.winfo_width()
winheight = win.winfo_height()
screenwidth = win.winfo_screenwidth()
screenheight = win.winfo_screenheight()

greetframe = Frame(win, bg="white")
mainframe = Frame(win, bg="white")
contentframe1 = Frame(greetframe, bg = "white")
contentframe2 = Frame(mainframe, bg = "white")
statusFrame = Frame(win, bg = "black")

statuslabel = Label(statusFrame,textvariable=statusvar, bg="black", fg="white", font=("Ubuntu", 11))
statuslabel.pack(anchor=W)

welcome = Label(greetframe, text="Welcome", pady=10, bg="white", font=("Bungee Spice", 16, "bold"))
heading1 = Label(greetframe, text="Employee Index", pady =10, bg="white", font=("Bungee Spice", 60, "bold"), fg="#342dc2")

usernamelabel = Label(contentframe1, text="username: ", bg="white", pady=2, font=("Noto Sans", 19))
passwordlabel = Label(contentframe1, text="password: ", bg = "white", pady=2, font=("Noto Sans", 19))

username_entry = Entry(contentframe1, textvariable=username_val, font=("Robot", 19), border=.2, bg="#d3d3db", highlightthickness=2 ,relief=FLAT
                       ,highlightcolor="#2d4780")
password_entry = Entry(contentframe1, textvariable=password_val, font=("Robot", 19), border=.2, bg="#d3d3db", highlightthickness=2, show="x",
                        relief=FLAT, highlightcolor="#2d4780")

button = Button(contentframe1, text="submit", command=check, font=("Roboto", 11,"bold"), pady=8, padx=5, bg="white", border=2, relief=GROOVE)

heading1.pack()
welcome.pack()
usernamelabel.grid(row=0, column=0)
passwordlabel.grid(row=1, column=0)
username_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)
button.grid(row=2, column=1)
contentframe1.pack(padx=15, pady=15)


serialnolabel = Label(contentframe2, text="S.no", bg ="white", padx=2, pady=2, font=("Tw Cen MT", 19))
namelabel = Label(contentframe2, text="name", bg="white", padx=2, pady=2, font=("Tw Cen MT", 19))
agelabel = Label(contentframe2, text="age", bg="white", padx=2, pady=2, font=("Tw Cen MT", 19))
designationlabel = Label(contentframe2, text="designation", bg="white", padx=2, pady=2, font=("Tw Cen MT", 19))
experiencelabel = Label(contentframe2, text="experience", bg="white", padx=2, pady=2, font=("Tw Cen MT", 19))
dateofjoininglabel = Label(contentframe2, text="date of joining", bg="white", padx=2, pady=2, font=("Tw Cen MT", 19))
morelabel = Label(contentframe2, text="more", bg="white", padx=2, pady=2, font=("Tw Cen MT", 19))
button2 = Button(contentframe2, text=" add ", command= button2addfunction, font=("Roboto", 11, "bold"), padx=3, pady=6, bg="#c21057", fg="white", border = 1, width=10)
button3 = Button(contentframe2, text="save", command= save, font=("Roboto", 11,"bold"), padx=3, pady=6,  bg="#28de58", fg="white", border = 1, width=10)
button4 = Button(contentframe2, text=" exit ", command= quit, font=("Roboto", 11,"bold"), padx=3, pady=6,  bg="#546658", fg="white", border = 1, width=10)

heading2 = Label(mainframe, text="Employee Index", bg = "white", pady=10, font=("Ubuntu", 36, "bold"))

name_entry = Entry(contentframe2, textvariable=name_val, font=("Roboto", 11), border=.2, bg="#d3d3db", highlightthickness=2 ,relief=FLAT
                       ,highlightcolor="#2d4780")
age_entry = Entry(contentframe2, textvariable=age_val, font=("Robot", 11), border=.2, bg="#d3d3db", highlightthickness=2 ,relief=FLAT
                       ,highlightcolor="#2d4780")
designation_entry = Entry(contentframe2, textvariable=designation_val, font=("Roboto", 11), border=.2, bg="#d3d3db", highlightthickness=2 ,relief=FLAT
                       ,highlightcolor="#2d4780")
exp_entry = Entry(contentframe2, textvariable=exp_val, font=("Roboto", 11), border=.2, bg="#d3d3db", highlightthickness=2 ,relief=FLAT
                       ,highlightcolor="#2d4780")
dateofjoining_entry = Entry(contentframe2, textvariable=dateofjoining_val, font=("Roboto", 11), border=.2, bg="#d3d3db", highlightthickness=2 ,relief=FLAT
                       ,highlightcolor="#2d4780")
more_entry = Entry(contentframe2, textvariable=more_val, font=("Roboto", 11), border=.2, bg="#d3d3db", highlightthickness=2 ,relief=FLAT
                       ,highlightcolor="#2d4780")

heading2.pack()

serialnolabel.grid(row=0, column=0)
namelabel.grid(row=0, column=1)
agelabel.grid(row=0, column=2)
designationlabel.grid(row=0, column=3)
experiencelabel.grid(row=0, column=4)
dateofjoininglabel.grid(row=0, column=5)
morelabel.grid(row=0, column=6)

name_entry.grid(row=1, column=1)
age_entry.grid(row=1, column=2)
designation_entry.grid(row=1, column=3)
exp_entry.grid(row=1, column=4)
dateofjoining_entry.grid(row=1, column=5)
more_entry.grid(row=1, column=6)

button2.grid(row=1, column=7)
button3.grid(row=2, column=7)
button4.grid(row=3, column=7)

contentframe2.pack()

greetframe.pack(fill=BOTH, expand=1, padx=100, pady=100)
statusFrame.pack(fill=X, side=BOTTOM)

button.bind("<Enter>", lambda event: button.configure(bg="black", fg="white", cursor="circle", font=("Gigi", 11, "bold")))
button.bind("<Leave>", lambda event: button.configure(bg="white", fg="black", cursor="arrow", font=("Roboto", 11,"bold")))

button2.bind("<Enter>", lambda event: button2.configure(bg="black", fg="white", cursor="circle", font=("Roboto", 12, "bold")))
button3.bind("<Enter>", lambda event: button3.configure(bg="black", fg="white", cursor="circle", font=("Roboto", 12, "bold")))
button4.bind("<Enter>", lambda event: button4.configure(bg="black", fg="white", cursor="circle", font=("Roboto", 12, "bold")))

button2.bind("<Leave>", lambda event: button2.configure(bg="#c21057", fg="white", cursor="arrow", font=("Roboto", 11, "bold")))
button3.bind("<Leave>", lambda event: button3.configure(bg="#28de58", fg="white", cursor="arrow", font=("Roboto", 11, "bold")))
button4.bind("<Leave>", lambda event: button4.configure(bg="#546658", fg="white", cursor="arrow", font=("Roboto", 11, "bold")))

win.mainloop()


