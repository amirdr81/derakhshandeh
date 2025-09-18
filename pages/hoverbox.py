import customtkinter as ctk

class HoverBox(ctk.CTkToplevel):
    def __init__(self, widget, text, **kwargs):
        super().__init__(widget)
        self.withdraw()
        self.overrideredirect(True)
        self.transient(widget)
        self.label = ctk.CTkLabel(self, text=text, font=("IRANSans", 12, "normal"), fg_color="#222b22", text_color="#fff", corner_radius=8, padx=8, pady=4)
        self.label.pack()
        self.lift(widget)
        self.attributes('-topmost', True)

    def show_at(self, x, y):
        self.geometry(f"+{x}+{y}")
        self.deiconify()
    
    def hide(self):
        self.withdraw()