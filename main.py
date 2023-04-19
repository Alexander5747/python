from tkinter import *
root = Tk()


# Config
root.title("Список задач")
root.geometry('400x520+410+150')
root.resizable(False, False)
root.config(bg='#4682B4')
	
# Logic
tasks = []


def addtask():
    task = en.get()
    if task !="":  
        listbox.insert(END, task) # добавление задач
        tasks.append(task)
        en.delete(0, END)  # очистка инпута
        save_task()
        
def deltask():
    select = listbox.curselection()
    if select:
        task_index = int(select[0])
        del tasks[task_index]
        listbox.delete(select) # удаление задач из списка
        save_task()

def save_task():
    f=open("bd.txt", "w")
    for t in tasks:
        f.write(f"{t}\n")

def load_tasks():
        f1 = open("bd.txt","r")
        tasks1 = f1.readlines()
        for t1 in tasks1:
             t1 = t1.strip()
             if t1:
                  tasks.append(t1)
                  listbox.insert(END,t1) 


# Content
Title = Label(root,
                  text='Список задач',
                  bg='#4682B4',
                  font=('Arial',20, 'bold'),
                  foreground='white',
                  )
listbox = Listbox(root, height=20, width=34, ) 
en = Entry(root)
addButton = Button(root, text='Добавить', justify='center', command= addtask)
delButton = Button(root, text='Удалить',  justify='center', command= deltask)


# Position content
Title.grid(row=0, column=0, ipadx=60, padx=50)
listbox.grid(row=1, column=0)
en.grid(row=2, column=0, ipadx=40, ipady=6, padx=5, pady=5, columnspan=2)
addButton.grid(row=3, column=0, columnspan=2, ipadx=70, ipady=6, padx=5, pady=5)
delButton.grid(row=4, column=0, columnspan=2, ipadx=74, ipady=6, padx=5, pady=5)
load_tasks()

# Run
root.mainloop()