import customtkinter as ctk


# =========================
# COLORS / THEME SETTINGS
# =========================

BG_COLOR = ("#F5F5F5", "#1A1A1B")
CARD_COLOR = ("#FFFFFF", "#272729")
PRIMARY_COLOR = "#FF4500"       # Reddit-like orange
PRIMARY_HOVER = "#CC3700"
SECONDARY_COLOR = "#0079D3"     # Reddit-like blue
SECONDARY_HOVER = "#005FA3"
TEXT_COLOR = ("#1C1C1C", "#D7DADC")
MUTED_TEXT_COLOR = ("#666666", "#818384")
BORDER_COLOR = ("#D7D7D7", "#343536")
TRANSPARENT = "transparent"


# =========================
# WINDOW / PAGE HELPERS
# =========================

def clear_window(root):
    for widget in root.winfo_children():
        widget.destroy()


def create_page_frame(parent, **kwargs):
    frame = ctk.CTkFrame(
        parent,
        fg_color=kwargs.pop("fg_color", BG_COLOR),
        corner_radius=kwargs.pop("corner_radius", 0),
        **kwargs
    )
    frame.pack(fill="both", expand=True)
    return frame


def create_header(parent, title, right_button_text=None, right_button_command=None, **kwargs):
    header = ctk.CTkFrame(
        parent,
        fg_color=kwargs.pop("fg_color", TRANSPARENT),
        **kwargs
    )
    header.pack(fill="x", padx=20, pady=10)

    create_title(header, title).pack(side="left")

    if right_button_text and right_button_command:
        create_plain_button(
            header,
            right_button_text,
            right_button_command,
            width=150
        ).pack(side="right")

    return header


# =========================
# LABEL COMPONENTS
# =========================

def create_title(parent, text, **kwargs):
    return ctk.CTkLabel(
        parent,
        text=text,
        font=kwargs.pop("font", ctk.CTkFont(family="Arial", size=22, weight="bold")),
        text_color=kwargs.pop("text_color", TEXT_COLOR),
        **kwargs
    )


def create_section_title(parent, text, **kwargs):
    return ctk.CTkLabel(
        parent,
        text=text,
        font=kwargs.pop("font", ctk.CTkFont(family="Arial", size=14)),
        text_color=kwargs.pop("text_color", TEXT_COLOR),
        **kwargs
    )


def create_subtitle(parent, text, **kwargs):
    return ctk.CTkLabel(
        parent,
        text=text,
        font=kwargs.pop("font", ctk.CTkFont(family="Arial", size=14)),
        text_color=kwargs.pop("text_color", MUTED_TEXT_COLOR),
        **kwargs
    )


def create_normal_label(parent, text, **kwargs):
    return ctk.CTkLabel(
        parent,
        text=text,
        font=kwargs.pop("font", ctk.CTkFont(family="Arial", size=11)),
        text_color=kwargs.pop("text_color", TEXT_COLOR),
        **kwargs
    )


def create_label(parent, text, **kwargs):
    return ctk.CTkLabel(
        parent,
        text=text,
        font=kwargs.pop("font", ctk.CTkFont(family="Arial", size=10)),
        text_color=kwargs.pop("text_color", TEXT_COLOR),
        **kwargs
    )


# =========================
# INPUT COMPONENTS
# =========================

def create_entry(parent, show=None, width=280, placeholder_text="", **kwargs):
    return ctk.CTkEntry(
        parent,
        width=width,
        show=show if show else "",
        placeholder_text=placeholder_text,
        font=kwargs.pop("font", ctk.CTkFont(family="Arial", size=10)),
        border_color=kwargs.pop("border_color", BORDER_COLOR),
        border_width=kwargs.pop("border_width", 1),
        **kwargs
    )


def create_text_area(parent, width=500, height=150, **kwargs):
    return ctk.CTkTextbox(
        parent,
        width=width,
        height=height,
        font=kwargs.pop("font", ctk.CTkFont(family="Arial", size=11)),
        border_color=kwargs.pop("border_color", BORDER_COLOR),
        border_width=kwargs.pop("border_width", 1),
        **kwargs
    )


# =========================
# BUTTON COMPONENTS
# =========================

def create_primary_button(parent, text, command, width=160, **kwargs):
    return ctk.CTkButton(
        parent,
        text=text,
        command=command,
        width=width,
        fg_color=kwargs.pop("fg_color", PRIMARY_COLOR),
        hover_color=kwargs.pop("hover_color", PRIMARY_HOVER),
        text_color=kwargs.pop("text_color", "white"),
        corner_radius=kwargs.pop("corner_radius", 8),
        font=kwargs.pop("font", ctk.CTkFont(family="Arial", size=10, weight="bold")),
        **kwargs
    )


def create_secondary_button(parent, text, command, width=160, **kwargs):
    return ctk.CTkButton(
        parent,
        text=text,
        command=command,
        width=width,
        fg_color=kwargs.pop("fg_color", SECONDARY_COLOR),
        hover_color=kwargs.pop("hover_color", SECONDARY_HOVER),
        text_color=kwargs.pop("text_color", "white"),
        corner_radius=kwargs.pop("corner_radius", 8),
        font=kwargs.pop("font", ctk.CTkFont(family="Arial", size=10, weight="bold")),
        **kwargs
    )


def create_plain_button(parent, text, command, width=160, **kwargs):
    return ctk.CTkButton(
        parent,
        text=text,
        command=command,
        width=width,
        fg_color=kwargs.pop("fg_color", TRANSPARENT),
        hover_color=kwargs.pop("hover_color", ("#EDEFF1", "#343536")),
        text_color=kwargs.pop("text_color", MUTED_TEXT_COLOR),
        corner_radius=kwargs.pop("corner_radius", 8),
        border_width=kwargs.pop("border_width", 1),
        border_color=kwargs.pop("border_color", BORDER_COLOR),
        font=kwargs.pop("font", ctk.CTkFont(family="Arial", size=10)),
        **kwargs
    )


# =========================
# FRAME COMPONENTS
# =========================

def create_card(parent, **kwargs):
    return ctk.CTkFrame(
        parent,
        fg_color=kwargs.pop("fg_color", CARD_COLOR),
        border_width=kwargs.pop("border_width", 1),
        border_color=kwargs.pop("border_color", BORDER_COLOR),
        corner_radius=kwargs.pop("corner_radius", 8),
        **kwargs
    )


def create_transparent_frame(parent, **kwargs):
    return ctk.CTkFrame(
        parent,
        fg_color=kwargs.pop("fg_color", TRANSPARENT),
        **kwargs
    )


def create_scrollable_frame(parent, **kwargs):
    return ctk.CTkScrollableFrame(
        parent,
        fg_color=kwargs.pop("fg_color", BG_COLOR),
        **kwargs
    )


# =========================
# POST CARD COMPONENT
# =========================

def create_post_card(
    parent,
    post,
    upvote_command=None,
    downvote_command=None,
    comments_command=None,
    **kwargs
):
    card = create_card(parent, **kwargs)
    card.pack(fill="x", padx=10, pady=8)

    username = post.get("username", "Unknown")
    community = post.get("community_name") or "General"
    title = post.get("title", "Untitled")
    content = post.get("content", "")
    created_at = post.get("created_at", "")

    create_label(
        card,
        f"Posted by {username} • {community}",
        font=ctk.CTkFont(family="Arial", size=9),
        text_color=MUTED_TEXT_COLOR,
        anchor="w"
    ).pack(fill="x", padx=12, pady=(10, 0))

    create_title(
        card,
        title,
        font=ctk.CTkFont(family="Arial", size=15, weight="bold"),
        anchor="w",
        justify="left",
        wraplength=750
    ).pack(fill="x", padx=12, pady=(5, 3))

    create_normal_label(
        card,
        content,
        anchor="w",
        justify="left",
        wraplength=750
    ).pack(fill="x", padx=12, pady=(0, 8))

    if created_at:
        create_label(
            card,
            f"Created: {created_at}",
            font=ctk.CTkFont(family="Arial", size=8),
            text_color=MUTED_TEXT_COLOR,
            anchor="w"
        ).pack(fill="x", padx=12)

    action_frame = create_transparent_frame(card)
    action_frame.pack(fill="x", padx=12, pady=(8, 10))

    create_plain_button(
        action_frame,
        "Upvote",
        command=upvote_command or (lambda: None),
        width=90
    ).pack(side="left", padx=(0, 5))

    create_plain_button(
        action_frame,
        "Downvote",
        command=downvote_command or (lambda: None),
        width=90
    ).pack(side="left", padx=5)

    create_plain_button(
        action_frame,
        "Comments",
        command=comments_command or (lambda: None),
        width=100
    ).pack(side="left", padx=5)

    return card
