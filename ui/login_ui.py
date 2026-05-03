from tkinter import messagebox

from controllers.auth_controller import AuthController
from ui.dashboard_ui import DashboardUI
from ui.components import (
    clear_window,
    create_page_frame,
    create_title,
    create_section_title,
    create_label,
    create_entry,
    create_primary_button,
    create_secondary_button,
)


class LoginUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Social App - Login")
        self.root.geometry("400x420")
        self.root.resizable(False, False)

        self.show_login_form()

    def clear_window(self):
        clear_window(self.root)

    def show_login_form(self):
        self.clear_window()

        frame = create_page_frame(self.root)

        create_title(frame, "Mini Social App").pack(pady=20)
        create_section_title(frame, "Login").pack(pady=10)

        create_label(frame, "Username").pack()
        self.login_username = create_entry(frame, placeholder_text="Enter username")
        self.login_username.pack(pady=5)

        create_label(frame, "Password").pack()
        self.login_password = create_entry(frame, show="*", placeholder_text="Enter password")
        self.login_password.pack(pady=5)

        create_primary_button(frame, "Login", self.login).pack(pady=15)
        create_secondary_button(frame, "Create Account", self.show_register_form).pack()

        self.login_username.focus_set()
        self.login_username.bind("<Return>", lambda event: self.login_password.focus_set())
        self.login_password.bind("<Return>", lambda event: self.login())

    def show_register_form(self):
        self.clear_window()

        frame = create_page_frame(self.root)

        create_title(frame, "Mini Social App").pack(pady=20)
        create_section_title(frame, "Register").pack(pady=10)

        create_label(frame, "Username").pack()
        self.register_username = create_entry(frame, placeholder_text="Choose a username")
        self.register_username.pack(pady=5)

        create_label(frame, "Email").pack()
        self.register_email = create_entry(frame, placeholder_text="Enter email")
        self.register_email.pack(pady=5)

        create_label(frame, "Password").pack()
        self.register_password = create_entry(frame, show="*", placeholder_text="Choose a password")
        self.register_password.pack(pady=5)

        create_primary_button(frame, "Register", self.register).pack(pady=15)
        create_secondary_button(frame, "Back to Login", self.show_login_form).pack()

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
