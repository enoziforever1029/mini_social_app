import customtkinter as ctk


BG_COLOR = ("#F5F5F5", "#1A1A1B")
CARD_COLOR = ("#FFFFFF", "#272729")
PRIMARY_COLOR = "#FF4500" 
SECONDARY_COLOR = "#0079D3"
TEXT_COLOR = ("#1C1C1C", "#D7DADC")
MUTED_TEXT_COLOR = ("#666666", "#818384")
BORDER_COLOR = ("#D7D7D7", "#343536")

def create_title(parent, text):
    return ctk.CTkLabel(
        parent,
        text=text,
        font=ctk.CTkFont(family="Arial", size=22, weight="bold"),
        text_color=TEXT_COLOR
    )


def create_section_title(parent, text):
    return ctk.CTkLabel(
        parent,
        text=text,
        font=ctk.CTkFont(family="Arial", size=14),
        text_color=TEXT_COLOR
    )


def create_subtitle(parent, text):
    return ctk.CTkLabel(
        parent,
        text=text,
        font=ctk.CTkFont(family="Arial", size=14),
        text_color=MUTED_TEXT_COLOR
    )


def create_normal_label(parent, text):
    return ctk.CTkLabel(
        parent,
        text=text,
        font=ctk.CTkFont(family="Arial", size=11),
        text_color=TEXT_COLOR
    )


def create_label(parent, text):
    return ctk.CTkLabel(
        parent,
        text=text,
        font=ctk.CTkFont(family="Arial", size=10),
        text_color=TEXT_COLOR
    )


def create_entry(parent, show=None, width=280, placeholder_text=""):
    return ctk.CTkEntry(
        parent,
        width=width,
        show=show if show else "",
        placeholder_text=placeholder_text,
        font=ctk.CTkFont(family="Arial", size=10),
        border_color=BORDER_COLOR,
        border_width=1
    )


def create_text_area(parent, width=500, height=150):
    return ctk.CTkTextbox(
        parent,
        width=width,
        height=height,
        font=ctk.CTkFont(family="Arial", size=11),
        border_color=BORDER_COLOR,
        border_width=1
    )

def create_primary_button(parent, text, command, width=160):
    return ctk.CTkButton(
        parent,
        text=text,
        command=command,
        width=width,
        fg_color=PRIMARY_COLOR,
        hover_color="#CC3700",
        text_color="white",
        corner_radius=8,
        font=ctk.CTkFont(family="Arial", size=10, weight="bold")
    )


def create_secondary_button(parent, text, command, width=160):
    return ctk.CTkButton(
        parent,
        text=text,
        command=command,
        width=width,
        fg_color=SECONDARY_COLOR,
        hover_color="#005FA3",
        text_color="white",
        corner_radius=8,
        font=ctk.CTkFont(family="Arial", size=10, weight="bold")
    )


def create_plain_button(parent, text, command, width=160):
    return ctk.CTkButton(
        parent,
        text=text,
        command=command,
        width=width,
        fg_color=("transparent", "transparent"),
        hover_color=("#EDEFF1", "#343536"),
        text_color=MUTED_TEXT_COLOR,
        corner_radius=8,
        border_width=1,
        border_color=BORDER_COLOR,
        font=ctk.CTkFont(family="Arial", size=10)
    )

def create_page_frame(parent):
    frame = ctk.CTkFrame(
        parent,
        fg_color=BG_COLOR,
        corner_radius=0
    )
    frame.pack(fill="both", expand=True)
    return frame


def create_card(parent):
    card = ctk.CTkFrame(
        parent,
        fg_color=CARD_COLOR,
        border_width=1,
        border_color=BORDER_COLOR,
        corner_radius=8
    )
    return card

def create_post_card(parent, post):
    card = create_card(parent)
    card.pack(fill="x", padx=10, pady=8)

    username = post.get("username", "Unknown")
    community = post.get("community_name") or "General"
    title = post.get("title", "Untitled")
    content = post.get("content", "")

    ctk.CTkLabel(
        card,
        text=f"Posted by {username} • {community}",
        font=ctk.CTkFont(family="Arial", size=9),
        text_color=MUTED_TEXT_COLOR,
        anchor="w"
    ).pack(fill="x", padx=12, pady=(10, 0))

    ctk.CTkLabel(
        card,
        text=title,
        font=ctk.CTkFont(family="Arial", size=15, weight="bold"),
        text_color=TEXT_COLOR,
        anchor="w",
        justify="left",
        wraplength=750
    ).pack(fill="x", padx=12, pady=(5, 3))

    ctk.CTkLabel(
        card,
        text=content,
        font=ctk.CTkFont(family="Arial", size=11),
        text_color=TEXT_COLOR,
        anchor="w",
        justify="left",
        wraplength=750
    ).pack(fill="x", padx=12, pady=(0, 8))

    action_frame = ctk.CTkFrame(card, fg_color="transparent")
    action_frame.pack(fill="x", padx=12, pady=(8, 10))

    create_plain_button(
        action_frame,
        "Upvote",
        command=lambda: print("Upvote clicked"),
        width=90
    ).pack(side="left", padx=(0, 5))

    create_plain_button(
        action_frame,
        "Downvote",
        command=lambda: print("Downvote clicked"),
        width=90
    ).pack(side="left", padx=5)

    create_plain_button(
        action_frame,
        "Comments",
        command=lambda: print("Comments clicked"),
        width=100
    ).pack(side="left", padx=5)

    return card