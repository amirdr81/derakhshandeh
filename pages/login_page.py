import customtkinter as ctk
from PIL import Image, ImageTk
import insystem_data
from main_dashboard import Dashboard

import colors

class LoginPage(ctk.CTkFrame):
    def get_user_all_data_via_username(self, username):
        for user in insystem_data.users:
            if(user["username"] == username):
                return user
        return None
    
    def get_user(self):
        return self.username_entry.get()
        
    def does_user_exists(self, username):
        for item in insystem_data.users:
            if(item["username"] == username): return True
        return False
    
    def does_match(self, username, password):
        for item in insystem_data.users:
            if(item["username"] == username and
               item["password"] == password):
                return True
        return False
    
    def __init__(self, parent, go_to_register, go_to_dashboard):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        self.configure(fg_color=colors.light_green_1)
    
        def get_error():
            if(not (self.username_entry.get() and self.password_entry.get())): return "لطفا مشخصات خود را وارد کنید."
            elif(not self.does_user_exists(self.username_entry.get())): return "کاربری با این نام کاربری، وجود ندارد!"
            elif(not self.does_match(self.username_entry.get(), self.password_entry.get())): return "رمز ورود اشتباه است!"
            return "OK!"
        
        def show_error(text, delay_ms=3000):
            if(text != "OK!"):
                self.error_label.configure(text=text)
                self.error_label.place(relx=0.91, rely=0.91, anchor="e")
                self.error_label.after(delay_ms, lambda: self.error_label.place_forget())
            else: 
                insystem_data.loged_in_user = self.get_user_all_data_via_username(self.username_entry.get())
                # print(insystem_data.loged_in_user)
                go_to_dashboard()
            
        def login_check():
            show_error(get_error())
        

        # کانتینر اصلی (باکس سبز سفید)
        main_box = ctk.CTkFrame(self, width=float(self.master.winfo_screenwidth() / 3), 
                                height=float(self.master.winfo_screenheight() / 1.5), 
                                fg_color=colors.white,
                                corner_radius=0)
        main_box.place(relx=0.5, rely=0.5, anchor="center")

        # کانتینر اصلی (باکس سبز)
        top_box = ctk.CTkFrame(main_box, width=float(main_box.winfo_screenwidth()),
                                height=float(main_box.winfo_screenheight() / 5), 
                                fg_color=colors.dark_green_6,
                                corner_radius=0)
        top_box.place(relx=0.5, rely=0.1, anchor="center")
        
        #عنوان صفحه
        login_label = ctk.CTkLabel(top_box, text="صفحه ورود", font=(None, 35, "bold"), 
                                   text_color=colors.white, 
                                   bg_color=colors.dark_green_6)
        login_label.place(relx=0.5, rely=0.5, anchor="center")
        
        login_description_label = ctk.CTkLabel(top_box, text="برای ورود به صفحه، مشخصات خود را وارد کنید", 
                                               font=(None, 15), 
                                               text_color=colors.white, 
                                               bg_color=colors.dark_green_6)
        login_description_label.place(relx=0.5, rely=0.7, anchor="center")
        
        #فیلد نام کاربری
        username_label = ctk.CTkLabel(main_box, 
                                      text="نام کاربری:", 
                                      font=(None, 18, "bold"), 
                                      text_color=colors.black, 
                                      bg_color=colors.white)
        username_label.place(relx=0.83, rely=0.38, anchor="center")
        self.username_entry = ctk.CTkEntry(main_box, 
                                      placeholder_text="نام کاربری", 
                                      height=50 , justify="right", 
                                      width=float(main_box.winfo_screenwidth() / 3.5), 
                                      bg_color=colors.white, 
                                      corner_radius=8, 
                                      border_color=colors.white, 
                                      fg_color=colors.light_gray_4, 
                                      text_color=colors.black)
        self.username_entry.place(relx=0.5, rely=0.45, anchor="center")
        self.username_entry.focus()
        #فیلد رمز عبور
        password_label = ctk.CTkLabel(main_box, 
                                      text="رمز عبور:", 
                                      font=(None, 18, "bold"), 
                                      text_color=colors.black, 
                                      bg_color=colors.white)
        password_label.place(relx=0.84, rely=0.54, anchor="center")
        self.password_entry = ctk.CTkEntry(main_box, 
                                      placeholder_text="رمز عبور", 
                                      height=50 , justify="right", 
                                      width=float(main_box.winfo_screenwidth() / 3.5), 
                                      bg_color=colors.white, 
                                      corner_radius=8, 
                                      border_color=colors.white, 
                                      fg_color=colors.light_gray_4, 
                                      text_color=colors.black,
                                      show="*")
        self.password_entry.place(relx=0.5, rely=0.61, anchor="center")
        
        #خط بالای دکمه ها
        circle_canvas = ctk.CTkCanvas(main_box, width=float(main_box.winfo_screenwidth() / 3.05), height=2, bg=colors.white, highlightthickness=0)
        circle_canvas.place(relx=-0.06, rely=0.74)
        circle_canvas.create_line(float(main_box.winfo_screenwidth() / 22), 1, float(main_box.winfo_screenwidth() / 2.85), 1, fill=colors.dark_green_6, width=1)
        
        #دکمه ورود
        login_btn = ctk.CTkButton(main_box, text="ورود", 
                                   width=float(main_box.winfo_screenwidth() / 3.5), 
                                   height=50, 
                                   font=(None, 30, "bold"), 
                                   corner_radius=8, 
                                   text_color=colors.white, 
                                   bg_color=colors.white, 
                                   fg_color=colors.dark_green_5, 
                                   hover_color=colors.green_3,
                                   command=login_check,)
        login_btn.place(relx=0.5, rely=0.8, anchor="center")
        forgot = ctk.CTkButton(main_box, text="اکانت ندارید؟ ثبت نام کنید...",
                               fg_color=colors.white,
                               hover_color=colors.white,
                               text_color=colors.blue_color,
                               bg_color=colors.white,
                               width=80,
                               cursor="hand2",
                               command=go_to_register)
        forgot.place(relx=0.59, rely=0.87, anchor="w")

        #لیبل ارور ها
        self.error_label = ctk.CTkLabel(main_box, 
                                        text="", 
                                        font=(None, 13, "bold"), 
                                        text_color=colors.red_color, 
                                        bg_color=colors.white)