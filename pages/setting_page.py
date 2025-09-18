#main import
import customtkinter as ctk

#controllers
import common_controller as cc
import common_ctk as ck
import register_controller as rc

#colors
import colors

class Setting(ctk.CTkFrame):
    def __init__(self, parent, go_to_dashboard):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        self.configure(fg_color=colors.light_green_1)
        
        main_box = ck.make_frame(self, float(self.master.winfo_screenwidth() / 1.2),
                                 float(self.master.winfo_screenheight() / 1.5),
                                 colors.white, colors.white, colors.white, 0, 0, 0.5, 0.5, "center")
        
        ck.make_label(main_box, 150, 40, colors.white, colors.white, colors.black, "تنظیمات برنامه", 0, 
                      None, (None, 45, "bold"), 0.5, 0.07, "n")
        
        ck.make_list(main_box, "رنگ", ["سبز", "آبی", "قرمز", "بنفش", "قهوه‌ای"], 
                     100, 35, colors.gray_1, colors.light_gray_4, colors.green_2, colors.dark_green_3,
                     60, None, "e", 0.8, 0.2, "ne")
        
        ck.make_button(main_box, "بازگشت", 150, 50, (None, 22, "bold"),
                       20, colors.white, colors.white,
                       colors.dark_green_5, colors.green_3, 
                       go_to_dashboard, 0.075, 0.94, "center")
