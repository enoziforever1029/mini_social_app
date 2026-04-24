import tkinter as tk
from tkinter import messagebox


class DashboardUI:
    def __init__(self, root, user, show_login_callback):
        self.root = root
        self.user = user
        self.show_login_callback = show_login_callback

        self.root.title("Mini Social App - Dashboard")
        self.root.geometry("800x500")
        self.root.resizable(True, True)

        self.show_dashboard()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_dashboard(self):
        self.clear_window()

        tk.Label(
            self.root,
            text="Mini Social App",
            font=("Arial", 24, "bold")
        ).pack(pady=20)

        tk.Label(
            self.root,
            text=f"Welcome, {self.user.username}!",
            font=("Arial", 14)
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="View Feed",
            width=25,
            command=self.view_feed
        ).pack(pady=8)

        tk.Button(
            self.root,
            text="Create Post",
            width=25,
            command=self.create_post
        ).pack(pady=8)

        tk.Button(
            self.root,
            text="Profile",
            width=25,
            command=self.view_profile
        ).pack(pady=8)

        tk.Button(
            self.root,
            text="Logout",
            width=25,
            command=self.logout
        ).pack(pady=20)

    def view_feed(self):
        messagebox.showinfo("View Feed", "Feed module will be added here.")

    def create_post(self):
        messagebox.showinfo("Create Post", "Post creation module will be added here.")

    def view_profile(self):
        messagebox.showinfo("Profile", "Profile module will be added here.")

    def logout(self):
        confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")

        if confirm:
            self.show_login_callback()