import tkinter as tk
from tkinter import font as tkfont

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My To-Do List")
        self.root.geometry("460 stopped x680")
        self.root.configure(bg="#f4f6f7") # Light gray background matching the image
        self.root.resizable(False, False)
        
        # Main Card Container (Centered White Box)
        self.card = tk.Frame(root, bg="white", padx=30, pady=30)
        self.card.place(relx=0.5, rely=0.5, anchor="center", width=400, height=620)
        
        # Title
        title_font = tkfont.Font(family="Segoe UI", size=22, weight="bold")
        self.title_label = tk.Label(self.card, text="My To-Do List", font=title_font, bg="white", fg="#2c3e50")
        self.title_label.pack(pady=(0, 25))
        
        # Input Section Frame
        self.input_frame = tk.Frame(self.card, bg="white")
        self.input_frame.pack(fill="x", pady=(0, 20))
        
        # Task Entry Input Box
        self.task_entry = tk.Entry(self.input_frame, font=("Segoe UI", 12), bg="white", fg="#a0a0a0",
                                   bd=1, relief="solid", highlightthickness=0)
        self.task_entry.insert(0, "Add a new task...")
        self.task_entry.bind("<FocusIn>", self.clear_placeholder)
        self.task_entry.bind("<FocusOut>", self.restore_placeholder)
        self.task_entry.pack(side="left", fill="both", expand=True, ipady=8, padx=(0, 10))
        
        # "Add" Button
        self.add_btn = tk.Button(self.input_frame, text="Add", font=("Segoe UI", 12, "bold"),
                                 bg="#27ae60", fg="white", activebackground="#219653",
                                 activeforeground="white", bd=0, cursor="hand2", command=self.add_task)
        self.add_btn.pack(side="right", ipadx=18, ipady=6)
        
        # Tasks Container List
        self.tasks_frame = tk.Frame(self.card, bg="white")
        self.tasks_frame.pack(fill="both", expand=True)
        
        # Populate initial tasks from your image
        initial_tasks = ["sleep", "love", "cook", "go for a clothes", "walk", "swim"]
        for task in initial_tasks:
            self.create_task_row(task)

    def clear_placeholder(self, event):
        if self.task_entry.get() == "Add a new task...":
            self.task_entry.delete(0, tk.END)
            self.task_entry.config(fg="#2c3e50")

    def restore_placeholder(self, event):
        if not self.task_entry.get():
            self.task_entry.insert(0, "Add a new task...")
            self.task_entry.config(fg="#a0a0a0")

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text and task_text != "Add a new task...":
            self.create_task_row(task_text)
            self.task_entry.delete(0, tk.END)
            self.root.focus() # Pull focus away to restore the placeholder
            self.restore_placeholder(None)

    def create_task_row(self, text):
        # Single row container
        row = tk.Frame(self.tasks_frame, bg="#f8f9fa")
        row.pack(fill="x", pady=6)
        
        # Left blue accent strip
        accent = tk.Frame(row, bg="#007bff", width=4)
        accent.pack(side="left", fill="y")
        
        # Task description label
        label = tk.Label(row, text=text, font=("Segoe UI", 12), bg="#f8f9fa", fg="#2c3e50", anchor="w")
        label.pack(side="left", fill="both", expand=True, padx=15, pady=12)
        
        # "Delete" Button
        del_btn = tk.Button(row, text="Delete", font=("Segoe UI", 10, "bold"),
                             bg="#4ad1d4", fg="white", activebackground="#3bc2c5",
                             activeforeground="white", bd=0, cursor="hand2")
        # Direct the delete command to remove this row
        del_btn.config(command=lambda r=row: r.destroy())
        del_btn.pack(side="right", padx=15, ipadx=10, ipady=4)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()