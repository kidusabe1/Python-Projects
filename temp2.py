import tkinter
#from asyncio.streams import _ClientConnectedCallback
from email import message
from ssl import Options
import tkinter
import tkinter.messagebox
import pickle
from turtle import left, title
from unittest import result
updated_task=[]
i,j,count,flag=0,0,0,0

# The following 2 lines are variables that count different tasks, although I could use a list to do that too
task_counter=0
searched=""
entered=""
new_task=[]
location=()

def add_new_task():
    new_win=tkinter.Toplevel(root)
    new_win.configure(bg="#151A30")
    new_win.geometry("500x600")
    new_win.resizable(False,False)
    frame_all=tkinter.Frame(new_win,bg="#151A30")
    frame_all.configure(width=500,height=600)
    frame_all.grid(row=0,column=0)
    frame_all.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    head_title= tkinter.Label(frame_all,text="Add New Task", fg="white",bg="#151A30",font = ("Helvetica", 18, "bold"),justify=tkinter.LEFT)
    head_title.grid(row=0,column=0)
    task_entry=tkinter.Entry(frame_all,width=20)
    task_entry.grid(row=0,column=1)
    entered=task_entry.get()
    title_1= tkinter.Label(frame_all, height=3,text="Category", fg="white",bg="#151A30",font = ("Helvetica", 18, "bold"))
    title_1.grid(row=1,column=0,padx=0)

    # DROP DOWN BOX 1
    options_1 =(
        "Study",
        "Leisure",
        "Exercise",
        "Girlfriend"
    )

    ##################################
    #category_list=
    ##################################

    # This variable gets varying selected text from dropdown box 1
    clicked= tkinter.StringVar()
    clicked.set(options_1[0])
    
    drop_down_menu1= tkinter.OptionMenu(frame_all, clicked, *options_1)
    drop_down_menu1.grid(row=1,column=1,padx=0)

    #DROP DOWN 2
    title_2= tkinter.Label(frame_all, height=3,text="Priority", fg="white",bg="#151A30",font = ("Helvetica", 18, "bold"))
    title_2.grid(row=2,column=0)
    options_2 =(
        "Today",
        "Tomorrow",
        "In the Weekend",
        "When you have free time"
    )

    # This variable gets varying selected text from dropdown box 2
    clicked_2= tkinter.StringVar()
    clicked_2.set(options_2[0])
    
    drop_down_menu2= tkinter.OptionMenu(frame_all, clicked_2, *options_2)
    drop_down_menu2.grid(row=2,column=1)
    
    #dumping the retrieved data in to a text file
    def save_task():
 # Everytime we save a task, we increment task_counter by 1
        if(task_entry.get()!=""):
            global task_counter
            task_counter=task_counter+1
            temp_task=[task_entry.get(),clicked.get(),clicked_2.get()]
            new_task.append(temp_task)
            print(new_task)

            #Dumping the fetched data into tasks.txt file
            #pickle.dump(new_task,open("tasks.txt","wb"))
            #print(new_task)

            # creating a new screen to show the details of the added task 
            success_wind=tkinter.Toplevel(new_win)
            success_wind.configure(bg="#151A30")
            success_wind.geometry("500x600")
            success_wind.resizable(False,False)

            frame_success=tkinter.Frame(success_wind,bg="#151A30")
            frame_success.configure(width=500, height=600)
            frame_success.grid(row=0,column=0,sticky=tkinter.NSEW)
            success_header= tkinter.Label(frame_success,text="Task Details", fg="white",bg="#151A30",font = ("Helvetica", 25, "bold"))
            success_header.grid(row=0,column=0,pady=(200,10),padx=(130,0))
            task_name= tkinter.Label(frame_success,text=f"Task Name: {task_entry.get()}", fg="white",bg="#151A30",font = ("Helvetica", 15, "bold"))
            task_name.grid(row=1,column=0,pady=(0,8),padx=(130,0))

            task_category= tkinter.Label(frame_success,text=f"Category: {clicked.get()}", fg="white",bg="#151A30",font = ("Helvetica", 15, "bold"))
            task_category.grid(row=2,column=0,pady=(0,8),padx=(130,0))
        
            task_priority= tkinter.Label(frame_success,text=f"Task Priority: {clicked_2.get()}", fg="White",bg="#151A30",font = ("Helvetica", 15, "bold"))
            task_priority.grid(row=3,column=0,pady=(0,8),padx=(130,0))

            exit_button= tkinter.Button(frame_success,text="Close Window",width="20", bg="#4660EF",fg="White",font = ("Helvetica", 15, "bold"),command=success_wind.destroy)
            exit_button.grid(row=4,column=0,pady=(10,8),padx=(130,0))
        else:
            tkinter.messagebox.showerror(title="Task failure",message="Add task before saving")

    save_task_button= tkinter.Button(frame_all,text="Add Task", width=30, font=("Arial",12,"bold") , bg="#F27B2C",fg="white",command=save_task)
    save_task_button.grid(row=3,column=0,columnspan=2)
    save_task_button= tkinter.Button(frame_all,text="Go to Main Page", width=30, font=("Arial",12,"bold") , bg="#2F80CF",fg="white",command=save_task)
    save_task_button.grid(row=4,column=0,columnspan=2,pady=(10,0))


root= tkinter.Tk()
root.title("My To Do List")
root.resizable(False, False)
root.geometry("500x600")
root.configure(bg = "#151A30")

head_title= tkinter.Label(root, height=3,width=40,text="My Todo List", fg="white",bg="#151A30",font = ("Helvetica", 36, "bold"))
head_title.pack(pady=(100,0))

add_new_task_button= tkinter.Button(root, text="Add New task", width=40,height=2,font = ("Helvetica", 12,"bold") ,command= lambda:[root.destroy(),add_new_task()], bg="#12A6FE",fg="white")
add_new_task_button.pack(pady=(5,5))

view_tasks_button= tkinter.Button(root, text="View tasks", width=40,height=2,font = ("Helvetica", 12,"bold"), command= view_tasks, bg="#4900FE",fg="white")
view_tasks_button.pack(pady=(5,15))

root.mainloop()