import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.simpledialog import askstring

class TaskManager:
    def __init__(self, root):
        self.tasks = []
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("500x600")
        self.root.configure(bg="#34495e")

        # Style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", font=("Helvetica", 14, "bold"), padding=10, background="#e74c3c", foreground="white")
        style.configure("TLabel", font=("Verdana", 12, "bold"), background="#34495e", foreground="white")
        style.configure("TEntry", font=("Verdana", 12), padding=5)

        # Title Label
        title_label = ttk.Label(root, text="Task Manager", font=("Helvetica", 24, "bold"), foreground="#f1c40f", background="#34495e")
        title_label.pack(pady=10)

        # Task Entry
        self.task_entry = self.create_labeled_entry("Enter a task")
        self.add_button = self.create_button("Add Task", self.add_task, "#2ecc71")

        # Task List
        self.task_listbox = tk.Listbox(root, width=50, height=10, font=("Verdana", 12), bg="#ecf0f1", fg="#2c3e50")
        self.task_listbox.pack(pady=10)

        # Buttons
        self.delete_button = self.create_button("Delete Task", self.delete_task, "#e67e22")
        self.complete_button = self.create_button("Complete Task", self.complete_task, "#3498db")
        self.clear_button = self.create_button("Clear All Tasks", self.clear_all_tasks, "#9b59b6")

    def create_labeled_entry(self, label_text):
        label = ttk.Label(self.root, text=label_text)
        label.pack()
        entry = ttk.Entry(self.root, font=("Verdana", 12))
        entry.pack(pady=5)
        return entry

    def create_button(self, text, command, color):
        button = tk.Button(self.root, text=text, command=command, font=("Helvetica", 12, "bold"), bg=color, fg="white", padx=10, pady=5, borderwidth=2, relief="raised")
        button.pack(pady=5, fill="x", padx=20)
        return button

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_tasks()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_tasks()
        else:
            messagebox.showwarning("Warning", "No task selected!")

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks[selected_task_index[0]] += " (Completed)"
            self.update_tasks()
        else:
            messagebox.showwarning("Warning", "No task selected!")

    def clear_all_tasks(self):
        self.tasks.clear()
        self.update_tasks()

    def update_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
