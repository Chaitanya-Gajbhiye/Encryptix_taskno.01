# TASK01 --- GUI BASED TO-DO-LIST APPLICATION 

# IMPORTING MODULES -
from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle

# INTERFACE SECTION -
interface = Tk()
interface.title("Python To-Do List")
interface.geometry('400x600')
interface["bg"] = "lightblue"

# WRITTEN SECTION -
Label1 = Label(text="Welcome to Python To-Do List", font=("Calibri",15,"bold"),bg="orange")
Label2 = Label(text="", font=("Calibri",15,"bold"),bg="lightblue")
Label3 = Label(text="Your To-Do List ↓", font=("Calibri",15,"bold"),bg="gold",justify="left")
Label1.pack(fill="x"),Label2.pack(),Label3.pack()

# CUSTOMIZATION SECTION -

#1 Defining our Font
My_Font = Font(family="Comic Sans MS",size=15,weight="bold")

#2 Create Frame
My_Frame = Frame(interface)
My_Frame.pack(pady=10)

#3 Create Listbox
My_List = Listbox(My_Frame,font=My_Font,bg="SystemButtonFace",bd=0,fg="#464646",highlightthickness=0,selectbackground="#a6a6a6",activestyle="none",width=25)
My_List.pack(side=LEFT,fill=BOTH)

#4.1 Create Dummy List
Stuff = ["Your task will appear here","eg- Rule the World","eg- Take a Nap","eg- Read a book..."]
#4.2  Add Dummy List
for item in Stuff:
    My_List.insert(END, item)

#5.1 Create Scrollbar
My_Scrollbar = Scrollbar(My_Frame)
My_Scrollbar.pack(side=RIGHT,fill=BOTH)
#5.2 Add Scrollbar
My_List.config(yscrollcommand=My_Scrollbar.set)
My_Scrollbar.config(command=My_List.yview)

#6 Create Entry Box to Add Items to the List
Label2 = Label(text="", font=("Calibri",15,"bold"),bg="lightblue")
Label4 = Label(text="Enter your Task ↓", font=("Calibri",15,"bold"),bg="gold",justify="left")
Label2.pack(),Label4.pack()

My_Entry = Entry(interface, font=("Helvetica",12,"bold"),width=30)
My_Entry.pack(pady=10)



# DEFINING TASK RELATED FUNCTIONS -  

def Delete_task():
    My_List.delete(ANCHOR)

def Add_task():
    My_List.insert(END,My_Entry.get())
    My_Entry.delete(0,END)

def Cross_Task():
    # Cross the Task Completed
    My_List.itemconfig(My_List.curselection(),fg="#dedede")
    # Get Rid of Selection Bar
    My_List.selection_clear(0,END)

def Uncross_Task():
    # Uncross the Task Mistakenly Clicked
    My_List.itemconfig(My_List.curselection(),fg="#464646")
    # Get Rid of Selection Bar
    My_List.selection_clear(0,END)

def delete_crossed():
    count = 0
    while count < My_List.size():
        if My_List.itemcget(count, "fg") =="#dedede":
            My_List.delete(My_List.index(count))
        else:    
            count += 1  

def Clear_Task():
    My_List.delete(0,END)
          

# DEFINING S TO-DO-LIST MENU FUNCTIONS - 

def save_list():
    file_name = filedialog.asksaveasfilename(initialdir="D:\GUI\Dat File Folder",title="Save File",filetypes=(("Dat Files","*.dat"),("All Files","*.*")))
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'

        # Delete crossed off items before saving
        count = 0
        while count < My_List.size():
            if My_List.itemcget(count, "fg") =="#dedede":
                My_List.delete(My_List.index(count))
            else:    
                count += 1  

        # Grab all the stuff from the list
        stuff = My_List.get(0,END)

        # Open the file
        output_file = open(file_name, 'wb')

        #Actual add the stuff to the file
        pickle.dump(stuff,output_file)


def open_list():
    file_name = filedialog.askopenfilename(initialdir="D:\GUI\Dat File Folder",title="Open File",filetypes=(("Dat Files","*.dat"),("All Files","*.*")))

    if file_name:
        # Delete currently open list 
        My_List.delete(0,END)

        # Open the file
        input_file = open(file_name,'rb')

        # Load the data from file
        stuff = pickle.load(input_file)

        # Output stuff to the screen
        for item in stuff:
            My_List.insert(END,item)

def clear_list():
    pass

# MENU SECTION -

#1 Create Menu
My_Menu = Menu(interface)              
interface.config(menu=My_Menu)
#2 Add Items to the Menu
File_Menu = Menu(My_Menu, tearoff=False)
My_Menu.add_cascade(label="File",menu=File_Menu)
#3 Add Dropdown Items
File_Menu.add_command(label="Save List",command=save_list)
File_Menu.add_command(label="Open List",command=open_list)
File_Menu.add_separator()
File_Menu.add_command(label="Clear List",command=clear_list)

# BUTTON SECTION -

#1 Create a Button Frame
button_frame = Frame(interface,bg="lightblue")
button_frame.pack(pady=15)

#2 Different Task Button 
delete_button = Button(button_frame,text="Delete Task",command=Delete_task)
add_button = Button(button_frame,text="Add Task",command=Add_task)
cross_off_button = Button(button_frame,text="Cross Task",command=Cross_Task)
uncross_off_button = Button(button_frame,text="Uncross Task",command=Uncross_Task)
Delete_Crossed_button = Button(button_frame,text="Delete Crossed",command=delete_crossed)
Clear_Task_Button = Button(button_frame,text="Clr All Task",command=Clear_Task)

delete_button.grid(row=0,column=0)
add_button.grid(row=0,column=1,padx=20)
cross_off_button.grid(row=0,column=2)
uncross_off_button.grid(row=1,column=0,padx=20)
Clear_Task_Button.grid(row=1,column=1)
Delete_Crossed_button.grid(row=1,column=2)

# RUNNING THE INTERFACE- 
interface.mainloop()