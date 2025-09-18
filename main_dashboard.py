import customtkinter as ctk
from asset_paths import notification
import insystem_data
from notificationBox import NotificationBox
import common_ctk as ck

import colors

class Dashboard(ctk.CTkFrame):
    def __init__(self, parent,go_to_login, 
                 go_to_register_bol, 
                 go_to_view_bol,
                 go_to_report,
                 go_to_register_deal,
                 go_to_dashboard,
                 go_to_dashboard1,
                 go_to_chat_box,
                 go_to_profile, 
                 go_to_insystem_data, 
                 go_to_driver,
                 go_to_cars,
                 go_to_security,
                 go_to_licence,
                 go_to_workcart):
        super().__init__(parent)
        
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

        self.pack(fill="both", expand=True)
        self.configure(fg_color=colors.light_green_1)

        # کانتینر اصلی (باکس اصلی)
        main_box = ctk.CTkFrame(self, width=float(self.master.winfo_screenwidth() / 3), 
                                height=float(self.master.winfo_screenheight() / 1.1), 
                                fg_color=colors.white,
                                corner_radius=0)
        main_box.place(relx=0.5, rely=0.5, anchor="center")
        
        #رسم دایره بالای باکس
        my_canvas = ctk.CTkCanvas(main_box, 
                                  width=float(main_box.winfo_screenwidth()), 
                                  height=float(2.6 * main_box.winfo_screenheight()), 
                                  bg="white",
                                  highlightthickness=0)
        my_canvas.place(relx=0.5, rely=0.5, anchor="center")
        r = 500
        x1 = main_box.winfo_screenwidth() / 2 - r
        y1 = main_box.winfo_screenheight() / 2 - r
        x2 = x1 + 2 * r
        y2 = y1 + 2 * r
        my_canvas.create_oval(x1, y1, x2, y2, fill=colors.dark_green_6, outline="")

        #عنوان صفحه
        dashboard_label = ctk.CTkLabel(main_box, text="منوی اصلی", font=(None, 50, "bold"), 
                                   text_color=colors.white, 
                                   bg_color=colors.dark_green_6)
        dashboard_label.place(relx=0.5, rely=0.1, anchor="center")
        
        dashboard_label_welcome = ctk.CTkLabel(main_box, text=insystem_data.loged_in_user["name"] + " عزیز، خوش اومدی...", font=(None, 20), 
                                   text_color=colors.white, 
                                   bg_color=colors.dark_green_6)
        dashboard_label_welcome.place(relx=0.5, rely=0.165, anchor="center")
        
        #دکمه ثبت اطلاعات
        make_button("ثبت بارنامه", 0.5, 0.3, go_to_register_bol)
        make_button("مشاهده بارنامه ها", 0.5, 0.39, go_to_view_bol)
        make_button("گزارش‌گیری", 0.5, 0.48, go_to_report)
        make_button("ثبت قرارداد", 0.5, 0.57, go_to_register_deal)
        make_button("اطلاعات سیستمی", 0.5, 0.66, go_to_insystem_data)
        data_button = make_button("اطلاعات رانندگان، ماشین‌ها و جایگاه‌ها", 0.5, 0.75, go_to_dashboard1)
        data_button.configure(font=(None, 25, "bold"))
        letters_btn = make_button("دبیرخانه", 0.5, 0.84, None)
        letters_btn.configure(state='disabled')
        def exit():
            # insystem_data.loged_in_user = {}
            go_to_login()
        make_button("خروج از سامانه", 0.5, 0.93, exit)
        
        #اعلانات
        #عکس اعلانات
        img_label = ck.make_image(main_box, notification, 60, 60, 0.085, 0.05, "center")
        img_label.configure(bg_color=colors.dark_green_6, corner_radius=8)
        number_of_notifications = len(insystem_data.loged_in_user["notifications"])
        NotificationBox(self, img_label, 200 + number_of_notifications * 63, go_to_dashboard, go_to_register_deal, go_to_driver, go_to_cars, go_to_security, go_to_licence, go_to_workcart, parent, offset=(10, 0))
        
        #نمایش تعداد اعلانات بالا راست عکس لوگوی اعلانات
        if(len(insystem_data.loged_in_user["notifications"]) != 0):
            number_label = ctk.CTkLabel(main_box, width=10, height=20,
                                        text=len(insystem_data.loged_in_user["notifications"]),
                                        font=(None, 10, "bold"),
                                        bg_color=colors.dark_green_6,
                                        fg_color=colors.red_color,
                                        text_color=colors.white,
                                        corner_radius=150)
            number_label.place(x=70, y=20, anchor="w")
            
        ck.make_button(main_box, "گفت‌و‌گو", 60, 30, (None, 15, "bold"),
                       60, colors.white,
                       colors.dark_green_6,
                       colors.green_3,
                       colors.light_green_1,
                       go_to_chat_box, 0.97, 0.022, "ne")
        
        
        ck.make_button(main_box, "پروفایل", 60, 30, (None, 15, "bold"),
                       60, colors.white,
                       colors.dark_green_6,
                       colors.green_3,
                       colors.light_green_1,
                       go_to_profile, 0.97, 0.072, "ne")
        