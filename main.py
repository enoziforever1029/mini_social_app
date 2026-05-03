import customtkinter as ctk
from ui.login_ui import LoginUI


def main():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    LoginUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
