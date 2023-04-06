from cgitb import text
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile,asksaveasfile

file_name = NONE

def new_file():
    global file_menu
    file_menu = "без названия"
    text.delete('1.0', END)
    
    def save_as():
        out = asksaveasfile(mode='w', defaultextension='.txt')
        data = text.get('1.0',END)
        try:
            out.write(data.rstrip())
        except Exception:
            messagebox.showerror("ой")
            
    def open_file():
        global file_name
        inp = askopenfile(mode=('r'))
        if inp is None:
            return 
        file_menu = inp.name
        data = inp.read()
        text.delete('1.0',END)
        text.insert('1.0',data)
            

root = Tk()
root.title("Заметки")
root.geometry("400x400")

Text = Text(root,width=400,height=400)
text.pack()

menu_bar = Menu(root)
file_menu = (menu_bar)

file_menu.add_command(Label="новый",command=new_file)
file_menu.add_command(Label="открыть",command=open_file)
file_menu.add_command(Label="сохранить как",command=save as)

menu_bar.add_cascade(label="Файл",menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()


