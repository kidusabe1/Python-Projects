from tkinter import *
root = Tk()


#here is the function to open and close the window
def create_window():
    window1 = Toplevel()
    #destroy
    btn = Button(window1, text="destroy main page", command=root.withdraw)
    btn.pack()
    #open
    btn2 = Button(window1, text="open main page", command=root.deiconify)
    btn2.pack()
    window1.mainloop()


b1 = Button(root, text="create window 2", command=create_window)
b1.pack()
root.mainloop()