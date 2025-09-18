import customtkinter as ctk
import colors

class ShowBol(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.pack(fill="both", expand=True)
        self.configure(fg_color=colors.red_color)
        
        
