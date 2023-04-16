from tkinter import *
root = Tk()


# Config
root.title("Список задач")
root.geometry('400x520+410+150')
root.resizable(False, False)
root.config(bg='#B186B9')


# Logic
def addbd(t):
      files = open('bd.txt', "a+")
      files.write(t + '\n')
      files.close()

def readbd():
    files1 = open('bd.txt', "r+")
    res = files1.readlines()
    files1.close()
    return res

def delete(d1):
    res12=readbd()
    counter = 0
    s=open("bd.txt", "w+")
    for i in range(len(res12)):
        if i==d1:
            res12.pop(counter)
            print(counter)
        counter+=1
        print(counter)
    s.writelines(res12)
    s.close()

listing = readbd()
listing_var = StringVar(value=listing) 

def addtask():
    task = en.get()
    if task !="":
        addbd(task)    
        listbox.insert(END, task) # добавление задач
        en.delete(0, END)  # очистка инпута
        

def deltask():
    select = listbox.curselection()
    if select:
        get_dels = listbox.get(select)
        listbox.delete(select) # удаление задач из списка
        delete(get_dels) # удаление задач из базы данных


# Content
Title = Label(root,
                  text='Список задач',
                  bg='#B186B9',
                  font=('Arial',20, 'bold'),
                  foreground='white',
                  )
listbox = Listbox(root, height=20, width=34, listvariable=(listing_var))
en = Entry(root)
addButton = Button(root, text='Добавить', justify='center', command= addtask)
delButton = Button(root, text='Удалить',  justify='center', command= deltask)


# Position content
Title.grid(row=0, column=0, ipadx=60, padx=50)
listbox.grid(row=1, column=0)
en.grid(row=2, column=0, ipadx=40, ipady=6, padx=5, pady=5, columnspan=2)
addButton.grid(row=3, column=0, columnspan=2, ipadx=70, ipady=6, padx=5, pady=5)
delButton.grid(row=4, column=0, columnspan=2, ipadx=74, ipady=6, padx=5, pady=5)


# Run
root.mainloop()