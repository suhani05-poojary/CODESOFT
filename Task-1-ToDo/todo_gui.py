import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"

def load_task():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME,"r")as file:
        return json.load(file)

def save_task():
    with open(FILE_NAME,"w")as file:
        json.dump(tasks,file,indent=4)

def add_task():
    task_text=entry.get().strip()
    if task_text=="":
        messagebox.showwarning("Warning","Task cannot be empty!!")
        return
    tasks.append({"task":task_text,"done":False})
    save_task()
    update_list()
    entry.delete(0,tk.END)

def delete_task():
    try:
        selected=listbox.curselection()[0]
        tasks.pop(selected)
        save_task()
        update_list()
    except:
        messagebox.showwarning("Warning","Select a task first!!")

def mark_done():
    try:
        selected=listbox.curselection()[0]
        tasks[selected]["done"]=True
        save_task()
        update_list()
    except:
        messagebox.showwarning("Warning","Select a task first!!")    

def clear_all():
    global tasks
    confirm=messagebox.askyesno("Confirm","Delete all tasks??")
    if confirm:
        tasks=[]
        save_task()
        update_list()

def update_list():
    listbox.delete(0,tk.END)
    for task in tasks:
        status="✔️"if task["done"]else "❌"
        listbox.insert(tk.END,f"{status}{task['task']}")

#GUI WINDOW

root=tk.Tk()
root.title("Suhani's Task Manager")
root.geometry("400x450")
root.configure(bg="#f0f8ff")

tasks=load_task()

entry=tk.Entry(root,width=30,font=("Arial",14))
entry.pack(pady=10)
btn_frame=tk.Frame(root,bg="#f0f8ff")
btn_frame.pack()

tk.Button(btn_frame,text="ADD TASK",bg="lightgreen",width=12,
command=add_task).grid(row=0,column=0,padx=5)

tk.Button(btn_frame,text="DELETE TASK",bg="lightcoral",width=12,
command=delete_task).grid(row=0,column=1,padx=5)

tk.Button(btn_frame,text="MARK DONE",bg="lightblue",width=12,
command=mark_done).grid(row=0,column=2,padx=5)

listbox=tk.Listbox(root,width=45,height=15,font=("Arial",12),bg="white")
listbox.pack(pady=20)

tk.Button(root,text="CLEAR ALL",bg="orange",command=clear_all).pack(pady=5)

update_list()
root.mainloop()



