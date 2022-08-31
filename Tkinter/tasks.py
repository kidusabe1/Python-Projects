import tkinter
import tkinter .messagebox
import pickle

root = tkinter.Tk() 
root.title("To Do list")
root.resizable(False,False)
def add_task():
    task= entry_task.get()
    if(task!=""):
        listboxes_tasks.insert(tkinter.END,task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="WARNING!", message="You Must Enter a Task")

def remove_task():
    try:
        task_index= listboxes_tasks.curselection()[0]
        listboxes_tasks.delete(task_index)
    except:
        tkinter.messagebox.showerror(title="Indexing Error", message="You Must Select a task")
    
def load_tasks():
    try:
        tasks=pickle.load(open("tasks.dat","rb"))
        listboxes_tasks.delete(0,tkinter.END)
        for task in tasks:
            listboxes_tasks.insert(tkinter.END,task)
    except:
        tkinter.messagebox.showerror(title="No added tasks", message="You must save tasks")
def save_task():
    tasks= listboxes_tasks.get(0,listboxes_tasks.size())
    pickle.dump(tasks,open("tasks.dat","wb"))

## CREATING THE GUI

frame_tasks= tkinter.Frame(root)
frame_tasks.pack()

tasks_scroll= tkinter.Scrollbar(frame_tasks)
tasks_scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listboxes_tasks=tkinter.Listbox(frame_tasks,height=15,width=50)
listboxes_tasks.pack()

listboxes_tasks.config(yscrollcommand=tasks_scroll.set)
tasks_scroll.config(command=listboxes_tasks.yview)

entry_task=tkinter.Entry(root,width=50)
entry_task.pack()

button_addtask= tkinter.Button(root, text="Add Task",width=48,command=add_task)
button_addtask.pack()

button_remove_task=tkinter.Button(root, text="Remove Task", width=48, command=remove_task)
button_remove_task.pack()

button_load_tasks= tkinter.Button(root, text="load_Tasks",width=48,command=load_tasks)
button_load_tasks.pack()

button_save_task= tkinter.Button(root, text="Save Task",width=48,command=save_task)
button_save_task.pack()


root.mainloop()