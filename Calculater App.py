import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image


#############################Creating the main window for our application##################

root = Tk()
root.geometry("600x700")
root.title("Arithmetic Calculator")
root.config(bg="olivedrab")
root.resizable(False,False)

#################################creating functions##################################

def enterNumber(x):
    if entry_box.get()=="o":
        entry_box.delete(0,'end')
        entry_box.insert(0,str(x))
    else:
        length=len(entry_box.get())
        entry_box.insert(length,str(x))


def enterOperator(x):
    if entry_box.get() != "o":
        length = len(entry_box.get())
        entry_box.insert(length,button_operator[x]["text"])


def funClear():
    entry_box.delete(0,END)
    entry_box.insert(0,"o")
result=0
result_list=[]

def funEqual():
    problem=entry_box.get()
    print(problem)
    print(type(problem))
    result = eval(problem)
    print(result)
    entry_box.delete(0,END)
    entry_box.insert(0,str(result))

    result_list.append(problem)
    result_list.reverse()
    status_Bar.configure(text='History :'+'|'.join(result_list[:5]))

def funDelete():
    length =len(entry_box.get())
    entry_box.delete(length-1,END)
    if length==1:
        entry_box.insert(0,"o")


###################################Creating an Entry Box#####################################

entry_box =Entry(root,font ='Helvetica 18 bold',width = 30,bd = 10,justify=RIGHT,relief=SUNKEN)
entry_box.place(x=40,y=20)
entry_box.config(bg="grey")
entry_box.insert(0,"o") #Creating the default value to be displayed in the entry box

###################################Creating number buttons ###################################

button_numbers=[]
for i in range (10):
    button_numbers.append(Button(width=6,height= 2,text=str(i),font=('times 15 bold'),bd = 10,bg="purple4",fg="white",
                                 command=lambda x=i:enterNumber(x)))

button_text= 1
for i in range(0,3):
    for j in range(0,3):
       button_numbers[button_text].place(x=55+j*110,y=100+i*80)
       print(j,i)
       button_text+=1


######################################Creating operator buttons###############################

button_operator=[]
for i in range(4):
    button_operator.append(Button(width=2,height =0,font = 'Times 30 bold',bd =10,bg ="black",fg ="white",command=lambda x=i: enterOperator(x)))

button_operator[0]["text"]="+"
button_operator[1]["text"]="-"
button_operator[2]["text"]="*"
button_operator[3]["text"]="/"

for i in range(4):
    button_operator[i].place(x=395,y=100+i*90)


##########################################Creating other buttons#############################################33

button_zero =Button(width =8,height =1,text="0",font ='times 30 bold',bd =10,bg ="purple",fg="white",command=lambda x=0: enterNumber(x))
button_clear =Button(width =4,text="CLR",font ='times 25 bold',bd =10,bg ="blue2",fg="white",command=funClear)
button_dot = Button(width = 2,text=".",font ='times 40 bold',bd =10,bg = "purple",fg="white",command = lambda x=".":enterNumber(x))
button_equal = Button(width =6,text="=",font ='times 25 bold',bd =10,bg ="darkgreen",fg="white",command = funEqual)
button_delete =Button(width =6,text="del",font ='times 25 bold',bd =10,bg ="red3",fg="white",command=funDelete)

button_zero.place(x=55,y=373)
button_clear.place(x=55,y=480)
button_dot.place(x=280,y=350)
button_equal.place(x=175,y=480)
button_delete.place(x=330,y=480)

#######################################Creating the status bar##################################################

status_Bar=Label(root,text="History :",relief=SUNKEN,anchor=W,font='verdana 20 italic',bg="pink3",bd=10)
status_Bar.pack(side=BOTTOM,fill=X)

root.mainloop()
