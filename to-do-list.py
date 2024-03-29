#import the Tkinter library
import tkinter
from tkinter import *
import tkinter.messagebox

#Create to−do list application window
window = Tk()
#Setting the App title
window.title("Python TO−DO List App")
window.geometry("400x650+400+100")
window.resizable(False,False)

task_list=[]

def enterTask():
    task= task_entry.get()
    task_entry.delete(0,END)
    
    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
            task_list.append(task)
            listbox.insert(END,task)
            
#function to facilitate the delete task from the Listbox
          
def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
                
        listbox.delete(ANCHOR)        
    
#topbar
TopImage = PhotoImage(file="Image/topbar.PNG")
Label(window,image=TopImage).pack()

#Dock icon
DockImage = PhotoImage(file="Image/dock.PNG")
Label(window,image=DockImage,bg="white").place(x=30,y=25)

#note icon
NoteImage = PhotoImage(file="Image/note.png")
Label(window,image=NoteImage,bg="white").place(x=340,y=25)

heading = Label(window,text="All task" ,font="ariai 20 bold",bd=0)
heading.place(x=130,y=20)
 
 #Create the initial window
frame = Frame(window,width="400", height="40", bg="white")
frame.place(x=0,y=180)  

task= StringVar()
task_entry =Entry(frame, width=18, font="arial 15", bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button=Button(frame,text="ADD",font="arial 20 bold",
              width=6, bg="gray",fg="#fff",bd=0,pady=0,command =enterTask)
button.place(x=300,y=0)

#listbox
frame1 = Frame(window,bd=3,width=700,height=180,bg="#600080")
frame1.pack(pady=(160,0))

listbox = Listbox(frame1, font= "arial 20",
                  width=25,height=8,fg="white",bg="#600080", cursor="hand2")
listbox.pack(side= LEFT,fill=BOTH,padx=2)

#Scrolldown in case the total list exceeds the size of the given window
scrollbar = Scrollbar(frame1)
scrollbar.pack(side= RIGHT,fill=BOTH)

listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command=listbox.yview)

#delete icon
Delete_Icon = PhotoImage(file="Image/trash.PNG")
Button(window,image=Delete_Icon,bg="white",bd=0, 
       command=deleteTask).pack(side=BOTTOM,pady=13)

window.mainloop()