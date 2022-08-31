#from asyncio.streams import _ClientConnectedCallback
from ssl import Options
import tkinter
import tkinter.messagebox
import pickle
from unittest import result
updated_task=[]
i,j,count=0,0,0

# The following 2 lines are variables that count different tasks, although I could use a list to do that too
task_counter=0
searched=""
entered=""
new_task=[]
location=()
# This Function is for adding a new task
def add_new_task():
    new_win=tkinter.Toplevel(root)
    new_win.configure(bg="grey")
    head_title= tkinter.Label(new_win, height=3,text="Add New Task", fg="black",bg="grey",font = ("Arial", 12, "bold"))
    head_title.grid(row=0,column=0,pady=(20,5),padx=(5,10))
    task_entry=tkinter.Entry(new_win,width=40, text="Put in your task")
    task_entry.grid(row=0,column=1,pady=(20),padx=(0,15))
    entered=task_entry.get()
    title_1= tkinter.Label(new_win, height=3,text="Category", fg="black",bg="grey",font = ("Arial", 12, "bold"))
    title_1.grid(row=1,column=0,pady=(20,5),padx=(5,2))

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
    
    drop_down_menu1= tkinter.OptionMenu(new_win, clicked, *options_1)
    drop_down_menu1.grid(row=1,column=1,pady=(20,5),padx=(0,10))

    #DROP DOWN 2
    title_2= tkinter.Label(new_win, height=3,text="Priority", fg="black",bg="grey",font = ("Arial", 12, "bold"))
    title_2.grid(row=2,column=0,pady=(20,5),padx=(5,2))
    options_2 =(
        "Today",
        "Tomorrow",
        "In the Weekend",
        "When you have free time"
    )

    # This variable gets varying selected text from dropdown box 2
    clicked_2= tkinter.StringVar()
    clicked_2.set(options_2[0])
    
    drop_down_menu2= tkinter.OptionMenu(new_win, clicked_2, *options_2)
    drop_down_menu2.grid(row=2,column=1,pady=(20,5),padx=(0,10))
    
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
            success_wind.configure(bg="grey")
            success_wind.geometry("300x300")
            success_wind.resizable(False,False)
            success_header= tkinter.Label(success_wind,text="Task Details", fg="black",bg="grey",font = ("Arial", 12, "bold"))
            success_header.grid(row=0,column=0,pady=(30,5),padx=70)
            task_name= tkinter.Label(success_wind,text=f"Task Name: {task_entry.get()}", fg="black",bg="grey",font = ("Arial", 10, "bold"))
            task_name.grid(row=1,column=0,pady=(20,5),padx=70)

            task_category= tkinter.Label(success_wind,text=f"Category: {clicked.get()}", fg="black",bg="grey",font = ("Arial", 10, "bold"))
            task_category.grid(row=2,column=0,pady=(20,5),padx=70)
        
            task_priority= tkinter.Label(success_wind,text=f"Task Priority: {clicked_2.get()}", fg="black",bg="grey",font = ("Arial", 10, "bold"))
            task_priority.grid(row=3,column=0,pady=(20,5),padx=70)

            exit_button= tkinter.Button(success_wind,text="EXIT",  bg="grey",fg="red",command=success_wind.destroy)
            exit_button.grid(row=4,column=0,pady=(0,20),padx=70)
        else:
            tkinter.messagebox.showerror(title="Task failure",message="Add task before saving")

    save_task_button= tkinter.Button(new_win,text="Add Task", width=30,  bg="black",fg="white",command=save_task)
    save_task_button.grid(row=3,column=0,pady=(5,10))


def view_tasks():
    study_counter,leisure_counter,girl_friend_counter,free_time,weekend_counter,today_counter,tomorrow_counter=0,0,0,0,0,0,0
    for task in new_task:
        if("Leisure" in task):
            leisure_counter+=1
        if("Study" in task):
            study_counter+=1
        if("Girlfriend" in task):
            girl_friend_counter+=1 
        if("Today" in task):
            today_counter+=1
        if("Tomorrow" in task):
            tomorrow_counter+=1
        if("In the Weekend" in task):
            weekend_counter+=1
        if("When you have free time" in task):
            free_time+=1
    def edit_task():
        edit_task_label=tkinter.Label(view_page,text="Edit Task",bg="grey",fg="black",width = 20, height = 1,font=("Helvetica",15,"bold"))
        edit_task_label.grid(row=3,column=0,pady=(5,2))
        task_rename_entry=tkinter.Entry(view_page,width=30)
        task_rename_entry.grid(row=4,column=0,pady=(2,3))
        task_rename_entry.insert(0,"Add new task detail")
        options_1 =(
            "Study",
            "Leisure",
            "Exercise",
            "Girlfriend"
        )

    ##################################
    #category_list=
    ##################################
        category_label=tkinter.Label(view_page,text="Category",bg="grey",fg="black",width = 20, height = 1,font=("Helvetica",12))
        category_label.grid(row=5,column=0,pady=(2,2))
        
        clicked= tkinter.StringVar()
        clicked.set(options_1[0])
        drop_down_menu1= tkinter.OptionMenu(view_page, clicked, *options_1)
        drop_down_menu1.grid(row=6,column=0,pady=(2,5))

        priority_label=tkinter.Label(view_page,text="Priority",bg="grey",fg="black",width = 20, height = 1,font=("Helvetica",12))
        priority_label.grid(row=7,column=0,pady=(2,2))
        options_2 =(
            "Today",
            "Tomorrow",
            "In the Weekend",
            "When you have free time"
        )

        # This variable gets varying selected text from dropdown box 2
        clicked_2= tkinter.StringVar()
        clicked_2.set(options_2[0])

        drop_down_menu2= tkinter.OptionMenu(view_page, clicked_2, *options_2)
        drop_down_menu2.grid(row=8,column=0,pady=(2,2))
        def update_task():
            new_task[i]=[task_rename_entry.get(),clicked.get(),clicked_2.get()]
            tkinter.messagebox.showinfo(title="Success",message="Task Updated!")
            view_page.destroy()
            view_tasks()
        def remove_task():
            del new_task[i]
            global task_counter
            task_counter-=1
            view_page.destroy()
            view_tasks()

        #updated_task=[task_rename_entry.get(),clicked.get(),clicked_2.get()]
        #print(updated_task)

        update_task_button=tkinter.Button(view_page,text="Update Task",bg="black",fg="white",width = 20, height = 1,command=update_task)
        update_task_button.grid(row=9,column=0,pady=(2,2))
        
        delete_task_button=tkinter.Button(view_page,text="Delete Task",bg="black",fg="white",width = 20, height = 1,command=remove_task)
        delete_task_button.grid(row=10,column=0,pady=(2,2))

    def search_task():
        def remove_task():
            del new_task[i]
            global task_counter
            task_counter-=1
            view_page.destroy()
            view_tasks()
        searched=search_entry.get()
        if any(searched in e[0] for e in new_task):
            categoryy.destroy()
            total_tasks.destroy()
            leisure_tasks.destroy()
            Study.destroy()
            Girlfriend.destroy()
            Priority.destroy()
            today.destroy()
            tomorrow.destroy()
            weekend.destroy()
            free.destroy()
            
            def find_in_list_of_list(new_task, searched):
                for sub_list in new_task:
                    if searched  in sub_list[0]:
                        return (new_task.index(sub_list), sub_list[0].find(searched))
                    
                raise ValueError("Not in list!")
            
            location=find_in_list_of_list(new_task,searched)
            i=location[0]
            j=location[1]
            result_frame=tkinter.LabelFrame(view_page,bg="grey",bd=1,cursor="heart",labelanchor='nw',relief="flat")
            result_frame.grid(row=2,column=0)
            Result=tkinter.Label(result_frame,
                text=f"{new_task[i][j]}\nCategory: {new_task[i][j+1]}\nPriority: {new_task[i][j+2]}",
                bg="grey",fg="black",
                font = ("Helvetica", 12, "bold"),
                justify="left")
            Result.grid(row=0,column=0,pady=(0,5))
            edit_task_button=tkinter.Button(view_page,text="Edit Task",bg="black",fg="white",width = 20, height = 1,command=lambda: [edit_task_button.destroy(),delete_task_button.destroy(), edit_task()])
            edit_task_button.grid(row=3,column=0,pady=(0,10))
            delete_task_button=tkinter.Button(view_page,text="Delete Task",bg="black",fg="white",width = 20, height = 1,command=remove_task)
            delete_task_button.grid(row=4,column=0)
        else:
            tkinter.messagebox.showerror(title="Empty Search",message="Empty Search Not Allowed")

    
    view_page=tkinter.Toplevel(root)
    view_page.config(bg="grey")
    view_page.geometry("300x400")
    view_page.resizable(False,False)
    search_entry=tkinter.Entry(view_page,width=40, text="Which task?")
    search_entry.grid(row=0,column=0,pady=(10,10),padx=20)
    #searched=search_entry.get()
    
    search_button=tkinter.Button(view_page,text="Search task",bg="black",fg="white",command=search_task)
    search_button.grid(row=1,column=0,pady=(0,5))
    
    categoryy=tkinter.Label(view_page,text="Based On Category", fg="black",bg="grey",font = ("Helvtica", 14, "bold") )
    categoryy.grid(row=2,column=0,pady=(0,10))
    total_tasks=tkinter.Label(view_page,text=f"Total tasks:      {task_counter}", 
        fg="black",bg="grey",
        font = ("Arial", 11, "bold"),
        justify="left"
        )
    total_tasks.grid(row=3,column=0,pady=(0,2),padx=30,sticky="w")
    leisure_tasks=tkinter.Label(view_page,text=f"Leisure:      {leisure_counter}", fg="black",bg="grey",font = ("Arial", 11, "bold"),justify="left")
    leisure_tasks.grid(row=4,column=0,pady=(0,2), sticky="w",padx=30)
    Study=tkinter.Label(view_page,text=f"Study Sessions:      {study_counter}", fg="black",bg="grey",font = ("Arial", 11, "bold"),justify="left")
    Study.grid(row=5,column=0,pady=(0,2), sticky="w",padx=30)
    Girlfriend=tkinter.Label(view_page,text=f"Girl friend:      {girl_friend_counter}", fg="black",bg="grey",font = ("Arial", 11, "bold"),justify="left")
    Girlfriend.grid(row=6,column=0,pady=(0,2), sticky="w",padx=30)

    Priority=tkinter.Label(view_page,text="Based On Priority", fg="black",bg="grey",font = ("Arial", 14, "bold"))
    Priority.grid(row=7,column=0,pady=(4,10))
    today=tkinter.Label(view_page,text=f"Today:      {today_counter}", fg="black",bg="grey",font = ("Arial", 11, "bold"),justify="left")
    today.grid(row=8,column=0,pady=(0,2), sticky="w",padx=30)
    tomorrow=tkinter.Label(view_page,text=f"Tomorrow:      {tomorrow_counter}", fg="black",bg="grey",font = ("Arial", 11, "bold"),justify="left")
    tomorrow.grid(row=9,column=0,pady=(0,2), sticky="w",padx=30)
    weekend=tkinter.Label(view_page,text=f"In the weekend:      {weekend_counter}", fg="black",bg="grey",font = ("Arial", 11, "bold"),justify="left")
    weekend.grid(row=10,column=0,pady=(0,2), sticky="w",padx=30)
    free=tkinter.Label(view_page,text=f"Whenever you are free:      {free_time}", fg="black",bg="grey",font = ("Arial", 11, "bold"),justify="left")
    free.grid(row=11,column=0,pady=(0,2), sticky="w",padx=30)
    

    


# Creating the main window
root= tkinter.Tk()
root.title("My To Do List")
root.resizable(False, False)
root.configure(bg = "grey")

head_title= tkinter.Label(root, height=3,width=40,text="My To DO List", fg="black",bg="grey",font = ("Arial", 12, "bold"))
head_title.pack(pady=(0,0))

add_new_task_button= tkinter.Button(root, text="Add New task", width=30, command= add_new_task, bg="black",fg="white")
add_new_task_button.pack(pady=(10,5))

view_tasks_button= tkinter.Button(root, text="View tasks", width=30, command= view_tasks, bg="black",fg="white")
view_tasks_button.pack(pady=(5,15))

root.mainloop()


######### FIGURE OUT A WAY TO MAKE THE SEARCH BUTTON WORK, and for it to loop through the tasks.txt file