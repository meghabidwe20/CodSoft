import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        self.tasks = []
        
        self.task_frame = tk.Frame(root)
        self.task_frame.pack(pady=10)
        
        self.task_listbox = tk.Listbox(self.task_frame, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.scrollbar = tk.Scrollbar(self.task_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)
        
        self.entry_task = tk.Entry(root, width=50)
        self.entry_task.pack(pady=10)
        
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)
        
        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=10)
        
        self.update_button = tk.Button(self.button_frame, text="Update Task", command=self.update_task)
        self.update_button.grid(row=0, column=1, padx=10)
        
        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=10)
    
    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            new_task = self.entry_task.get()
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.update_listbox()
                self.entry_task.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a new task.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")
    
    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")
    
    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
