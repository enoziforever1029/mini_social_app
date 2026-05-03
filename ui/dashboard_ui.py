from tkinter import messagebox

from ui.post_ui import PostUI
from ui.feed_ui import FeedUI
from ui.profile_ui import ProfileUI
from ui.components import (
    clear_window,
    create_page_frame,
    create_title,
    create_subtitle,
    create_primary_button,
    create_secondary_button,
    create_plain_button,
)


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
        clear_window(self.root)

    def show_dashboard(self):
        self.clear_window()

        frame = create_page_frame(self.root)

        create_title(frame, "Mini Social App").pack(pady=20)
        create_subtitle(frame, f"Welcome, {self.user.username}!").pack(pady=10)

        create_primary_button(frame, "View Feed", self.view_feed, width=220).pack(pady=8)
        create_secondary_button(frame, "Create Post", self.create_post, width=220).pack(pady=8)
        create_plain_button(frame, "Profile", self.view_profile, width=220).pack(pady=8)
        create_plain_button(frame, "Logout", self.logout, width=220).pack(pady=20)

    def view_feed(self):
        FeedUI(self.root, self.user, self.show_dashboard)

    def create_post(self):
        PostUI(self.root, self.user, self.show_dashboard)

    def view_profile(self):
        ProfileUI(self.root, self.user, self.show_dashboard)

    def logout(self):
        confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")

        if confirm:
            self.show_login_callback()
