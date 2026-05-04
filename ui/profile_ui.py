import customtkinter as ctk


class ProfileUI(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(fg_color="#212121")

        self.top_bar = ctk.CTkFrame(self, fg_color="transparent")
        self.top_bar.pack(fill="x", padx=20, pady=20)

        self.back_button = ctk.CTkButton(
            self.top_bar,
            text="← Back",
            width=80,
            fg_color="transparent",
            hover_color="#333333",
            border_width=1,
            border_color="#555555",
            text_color="white",
            font=ctk.CTkFont(size=14)
        )
        self.back_button.pack(side="left")

        self.profile_card = ctk.CTkFrame(self, fg_color="#2b2b2b", corner_radius=15, border_width=1,
                                         border_color="#333333")
        self.profile_card.pack(fill="both", expand=True, padx=80, pady=(0, 60))

        self.avatar_placeholder = ctk.CTkLabel(
            self.profile_card,
            text="👤",
            width=120,
            height=120,
            fg_color="#3a3a3a",
            corner_radius=60,
            font=ctk.CTkFont(size=60)
        )
        self.avatar_placeholder.pack(pady=(40, 15))

        self.username_label = ctk.CTkLabel(
            self.profile_card,
            text="u/traveler_99",
            font=ctk.CTkFont(size=26, weight="bold"),
            text_color="#5fa8d3"
        )
        self.username_label.pack(pady=(0, 5))

        self.email_label = ctk.CTkLabel(
            self.profile_card,
            text="traveler@example.com",
            font=ctk.CTkFont(size=14),
            text_color="#a0a0a0"
        )
        self.email_label.pack(pady=(0, 25))

        bio_text = (
            "The view from my office today.\n"
            "Exploring the world one line of code at a time."
        )
        self.bio_label = ctk.CTkLabel(
            self.profile_card,
            text=bio_text,
            font=ctk.CTkFont(size=15),
            text_color="white",
            justify="center"
        )
        self.bio_label.pack(pady=(0, 40))

        self.edit_button = ctk.CTkButton(
            self.profile_card,
            text="Edit Profile",
            fg_color="#226699",
            hover_color="#1a4d73",
            font=ctk.CTkFont(size=15, weight="bold"),
            corner_radius=8,
            width=200,
            height=40
        )
        self.edit_button.pack(pady=(0, 40))


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")

    app = ctk.CTk()
    app.geometry("800x600")
    app.title("Reddit-Style Profile UI")
    app.configure(fg_color="#1a1a1a")

    profile_view = ProfileUI(master=app)
    profile_view.pack(fill="both", expand=True)

    app.mainloop()
