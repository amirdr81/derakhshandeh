import customtkinter as ctk
from PIL import Image, ImageTk
from asset_paths import notification

import colors

class Dashboard2(ctk.CTkFrame):
    def __init__(self, parent, 
                go_to_security,
                go_to_licence,
                go_to_taahod,
                go_to_workcart,
                 back_to_dashboard):
        super().__init__(parent)

        self.pack(fill="both", expand=True)
        self.configure(fg_color=colors.light_green_1)

        def make_button(text, x, y, command):
            button = ctk.CTkButton(main_box, text=text, 
                                   width=440, height=50, 
                                   font=(None, 30, "bold"), 
                                   corner_radius=8, 
                                   text_color=colors.white, 
                                   bg_color=colors.white, 
                                   fg_color=colors.dark_green_5, 
                                   hover_color=colors.green_3,
                                   command=command)
            button.place(relx=x, rely=y, anchor="center")
            return button
        
        # کانتینر اصلی (باکس اصلی)
        main_box = ctk.CTkFrame(self, width=float(self.master.winfo_screenwidth() / 3), 
                                height=float(self.master.winfo_screenheight() / 1.6), 
                                fg_color=colors.white,
                                corner_radius=0)
        main_box.place(relx=0.5, rely=0.5, anchor="center")
        
        #رسم دایره بالای باکس
        my_canvas = ctk.CTkCanvas(main_box, 
                                  width=float(main_box.winfo_screenwidth()), 
                                  height=float(2.6 * main_box.winfo_screenheight()), 
                                  bg="white",
                                  highlightthickness=0)
        my_canvas.place(relx=0.5, rely=0.75, anchor="center")
        r = 500
        x1 = main_box.winfo_screenwidth() / 2 - r
        y1 = main_box.winfo_screenheight() / 2 - r
        x2 = x1 + 2 * r
        y2 = y1 + 2 * r
        my_canvas.create_oval(x1, y1, x2, y2, fill=colors.dark_green_6, outline="")

        #عنوان صفحه
        dashboard_label = ctk.CTkLabel(main_box, text="مشخصات چهاربرگ", font=(None, 40, "bold"), 
                                   text_color=colors.white, 
                                   bg_color=colors.dark_green_6)
        dashboard_label.place(relx=0.5, rely=0.12, anchor="center")
        
        #دکمه ثبت اطلاعات
        make_button("اطلاعات کارت ایمنی", 0.5, 0.45, go_to_security)
        make_button("گواهینامه تأیید صلاحیت نفتکش", 0.5, 0.57, go_to_licence)
        make_button("تعهدنامه", 0.5, 0.69, go_to_taahod)
        make_button("اطلاعات کارت تردد", 0.5, 0.81, go_to_workcart)
        make_button("بازگشت", 0.5, 0.93, back_to_dashboard)