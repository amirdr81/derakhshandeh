import customtkinter as ctk
from PIL import Image, ImageTk
from asset_paths import notification

import colors

class Dashboard1(ctk.CTkFrame):
    def __init__(self, parent, 
                 go_to_driver_info,
                 go_to_car_info,
                 go_to_startpoint_info, 
                 go_to_station_info,
                 go_to_route_info,
                 back_to_dashboard,
                 go_to_dashboard2,
                 go_to_car_driver_assign):
        super().__init__(parent)

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
        my_canvas.place(relx=0.5, rely=0.65, anchor="center")
        r = 500
        x1 = main_box.winfo_screenwidth() / 2 - r
        y1 = main_box.winfo_screenheight() / 2 - r
        x2 = x1 + 2 * r
        y2 = y1 + 2 * r
        my_canvas.create_oval(x1, y1, x2, y2, fill=colors.dark_green_6, outline="")

        #عنوان صفحه
        dashboard_label = ctk.CTkLabel(main_box, text="اطلاعات رانندگان، \nماشین‌ها و جایگاه‌ها", font=(None, 40, "bold"), 
                                   text_color=colors.white, 
                                   bg_color=colors.dark_green_6)
        dashboard_label.place(relx=0.5, rely=0.12, anchor="center")
        
        #دکمه ها
        #اساین راننده به نفتکش
        dar_driver_btn = ctk.CTkButton(main_box, text="مدل‌سازی راننده و نفتکش", 
                                   width=350, height=50, 
                                   font=(None, 30, "bold"), 
                                   corner_radius=8, 
                                   text_color=colors.dark_green_5, 
                                   bg_color=colors.dark_green_5, 
                                   fg_color=colors.white, 
                                   hover_color=colors.green_3,
                                   command=go_to_car_driver_assign)
        dar_driver_btn.place(relx=0.5, rely=0.25, anchor="center")
        
        #ثبت اطلاعات راننده
        register_driver_btn = ctk.CTkButton(main_box, text="ثبت اطلاعات راننده", 
                                   width=440, height=50, 
                                   font=(None, 30, "bold"), 
                                   corner_radius=8, 
                                   text_color=colors.white, 
                                   bg_color=colors.white, 
                                   fg_color=colors.dark_green_5, 
                                   hover_color=colors.green_3,
                                   command=go_to_driver_info)
        register_driver_btn.place(relx=0.5, rely=0.43, anchor="center")
        
        #ثبت اطلاعات نفتکش
        register_car_btn = ctk.CTkButton(main_box, text="ثبت اطلاعات نفتکش", 
                                   width=440, height=50, 
                                   font=(None, 30, "bold"), 
                                   corner_radius=8, 
                                   text_color=colors.white, 
                                   bg_color=colors.white, 
                                   fg_color=colors.dark_green_5, 
                                   hover_color=colors.green_3,
                                   command=go_to_car_info)
        register_car_btn.place(relx=0.5, rely=0.515, anchor="center")
        
        #ثبت اطلاعات مبدا
        register_start_btn = ctk.CTkButton(main_box, text="ثبت اطلاعات مبدأ", 
                                   width=440, height=50, 
                                   font=(None, 30, "bold"), 
                                   corner_radius=8, 
                                   text_color=colors.white, 
                                   bg_color=colors.white, 
                                   fg_color=colors.dark_green_5, 
                                   hover_color=colors.green_3,
                                   command=go_to_startpoint_info)
        register_start_btn.place(relx=0.5, rely=0.6, anchor="center")
        
        #ثبت اطلاعات جایگاه
        register_station_btn = ctk.CTkButton(main_box, text="ثبت اطلاعات مقصد", 
                                   width=440, height=50, 
                                   font=(None, 30, "bold"), 
                                   corner_radius=8, 
                                   text_color=colors.white, 
                                   bg_color=colors.white, 
                                   fg_color=colors.dark_green_5, 
                                   hover_color=colors.green_3,
                                   command=go_to_station_info)
        register_station_btn.place(relx=0.5, rely=0.685, anchor="center")
        
        #ثبت اطلاعات جایگاه
        register_route_btn = ctk.CTkButton(main_box, text="ثبت اطلاعات مسیر", 
                                   width=440, height=50, 
                                   font=(None, 30, "bold"), 
                                   corner_radius=8, 
                                   text_color=colors.white, 
                                   bg_color=colors.white, 
                                   fg_color=colors.dark_green_5, 
                                   hover_color=colors.green_3,
                                   command=go_to_route_info)
        register_route_btn.place(relx=0.5, rely=0.77, anchor="center")
        
        #چهاربرگ
        register_route_btn = ctk.CTkButton(main_box, text="چهاربرگ", 
                                   width=440, height=50, 
                                   font=(None, 30, "bold"), 
                                   corner_radius=8, 
                                   text_color=colors.white, 
                                   bg_color=colors.white, 
                                   fg_color=colors.dark_green_5, 
                                   hover_color=colors.green_3,
                                   command=go_to_dashboard2)
        register_route_btn.place(relx=0.5, rely=0.855, anchor="center")
        
        #دکمه بازگشت به منوی اصلی
        back_to_dashboard_btn = ctk.CTkButton(main_box, text="برگشت به منوی اصلی", 
                                   width=440, height=50, 
                                   font=(None, 30, "bold"), 
                                   corner_radius=8, 
                                   text_color=colors.white, 
                                   bg_color=colors.white, 
                                   fg_color=colors.dark_green_5, 
                                   hover_color=colors.green_3,
                                   command=back_to_dashboard)
        back_to_dashboard_btn.place(relx=0.5, rely=0.94, anchor="center")