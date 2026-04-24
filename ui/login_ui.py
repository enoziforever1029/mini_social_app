import tkinter as tk
from tkinter import messagebox
from controllers.auth_controller import AuthController
from ui.dashboard_ui import DashboardUI


class LoginUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Social App - Login")
        self.root.geometry("400x420")
        self.root.resizable(False, False)

        self.show_login_form()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_login_form(self):
        self.clear_window()

        tk.Label(self.root, text="Mini Social App", font=("Arial", 20, "bold")).pack(pady=20)
        tk.Label(self.root, text="Login", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="Username").pack()
        self.login_username = tk.Entry(self.root, width=30)
        self.login_username.pack(pady=5)

        tk.Label(self.root, text="Password").pack()
        self.login_password = tk.Entry(self.root, width=30, show="*")
        self.login_password.pack(pady=5)

        tk.Button(self.root, text="Login", width=20, command=self.login).pack(pady=15)
        tk.Button(self.root, text="Create Account", width=20, command=self.show_register_form).pack()
        
        self.login_username.focus_set()
        
        self.login_username.bind("<Return>", lambda event: self.login_password.focus_set())
        self.login_password.bind("<Return>", lambda event: self.login())

    def show_register_form(self):
        self.clear_window()

        tk.Label(self.root, text="Mini Social App", font=("Arial", 20, "bold")).pack(pady=20)
        tk.Label(self.root, text="Register", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="Username").pack()
        self.register_username = tk.Entry(self.root, width=30)
        self.register_username.pack(pady=5)

        tk.Label(self.root, text="Email").pack()
        self.register_email = tk.Entry(self.root, width=30)
        self.register_email.pack(pady=5)

        tk.Label(self.root, text="Password").pack()
        self.register_password = tk.Entry(self.root, width=30, show="*")
        self.register_password.pack(pady=5)

        tk.Button(self.root, text="Register", width=20, command=self.register).pack(pady=15)
        tk.Button(self.root, text="Back to Login", width=20, command=self.show_login_form).pack()
        
        self.register_username.focus_set()
        
        self.register_username.bind("<Return>", lambda event: self.register_email.focus_set())
        self.register_email.bind("<Return>", lambda event: self.register_password.focus_set())
        self.register_password.bind("<Return>", lambda event: self.register())

    def login(self):
        username = self.login_username.get().strip()
        password = self.login_password.get().strip()

        success, message, user = AuthController.login(username, password)

        if success:
            DashboardUI(self.root, user, self.show_login_form)
        else:
            messagebox.showerror("Login Failed", message)

    def register(self):
        username = self.register_username.get().strip()
        email = self.register_email.get().strip()
        password = self.register_password.get().strip()

        success, message = AuthController.register(username, email, password)

        if success:
            messagebox.showinfo("Success", message)
            self.show_login_form()
        else:
            messagebox.showerror("Registration Failed", message)