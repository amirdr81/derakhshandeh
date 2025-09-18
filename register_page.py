import customtkinter as ctk
from User_model import User
from insystem_data import users
import common_ctk as ck
from asset_paths import registerPage
import common_controller as cc
import jdatetime
from datetime import datetime
import colors

class RegisterPage(ctk.CTkFrame):
    def is_username_taken(self, target, input):
        for item in users:
            if(item[input] == target): return False
        return True
    
    def check_phone_format(self, phone_str):
        phone_str = cc.persian_to_eng_date(phone_str)
        return (len(phone_str) == 11 and phone_str[0:2] == "09")
    
    def check_email_format(self, email_str):
        return (("@" and ".") in email_str)
    
    def check_password(self, password, repetead_password):
        return password == repetead_password
    
    def is_password_strong(self, password_str):
        if(len(password_str) < 10): return "رمز وارد شده باید حداقل ۱۰ رقم باشد."
        return
        
    def __init__(self, parent, go_to_login):
        super().__init__(parent)        
        self.pack(fill="both", expand=True)
        self.configure(fg_color=colors.light_green_1)

        def show_error(text, delay_ms=3000):
            self.error_label.configure(text=text)
            self.error_label.place(relx=0.9, rely=0.92, anchor="e")
            self.error_label.after(delay_ms, lambda: self.error_label.place_forget())
        def register_user(delay_ms=3000):
            if(not (self.name_entry.get() and
               self.lastname_entry.get() and
               self.phone_number_entry.get() and
               self.nationalCode_entry.get() and
               self.email_entry.get() and
               self.username_entry.get() and
               self.password_entry.get() and
               self.repet_password_entry.get())): show_error("لطفا تمامی اطلاعات مورد نیاز را تکمیل کنید!")
            elif(not self.check_phone_format(self.phone_number_entry.get())): show_error("شماره تلفن وارد شده، صحیح نمی‌باشد.")
            elif(not self.is_username_taken(self.nationalCode_entry.get(), "id")): show_error("فردی با کد ملی وارد شده، قبلا ثبت نام کرده است!")
            elif(not self.check_email_format(self.email_entry.get())): show_error("آدرس ایمیل وارد شده، صحیح نمی‌باشد.")
            elif(not self.is_username_taken(self.username_entry.get(), "username")): show_error("نام کاربری قبلا انتخاب شده است، نام دیگری انتخاب کنید.")
            elif(not self.check_password(self.password_entry.get(), self.repet_password_entry.get())): show_error("رمز عبور ها، یکسان نیستند! دوباره تلاش کنید.")
            elif(self.is_password_strong(self.password_entry.get())): show_error(self.is_password_strong(self.password_entry.get()))
            else:
                self.error_label.configure(text="ثبت نام شما با موفقیت انجام شد.\nدر صورت تأیید مدیریت، می‌توانید به سیستم وارد شوید.", text_color=colors.green_1)
                self.error_label.place(relx=0.9, rely=0.92, anchor="e")
                self.error_label.after(3000, lambda: go_to_login())
                
                managers = cc.find_manager()
                for manager in managers:
                    manager['notifications'].append({
                        'type': 'register user',
                        'description': 'فردی با نام ' + self.name_entry.get() + " " + self.lastname_entry.get() + '، درخواست ثبت‌نام در سامانه را دارد.',
                        'params': {'user': {'name': self.name_entry.get(), 
                                       'lastname': self.lastname_entry.get(),
                                       'phone': self.phone_number_entry.get(),
                                       'id': self.nationalCode_entry.get(),
                                       'email': self.email_entry.get(),
                                       'username': self.username_entry.get(),
                                       'password': self.password_entry.get(),
                                       'role': self.selected_role_var.get(),
                                       'lastseen_date': jdatetime.date.today().strftime('%Y/%m/%d'),
                                       'lastseen_time': datetime.now().strftime('%H:%M'),
                                       'notifications': []}},
                        'date': {'date': jdatetime.date.today().strftime('%Y/%m/%d'), 'clock': datetime.now().strftime('%H:%M')}
                    })
                
        # کانتینر اصلی (باکس سبز سفید)
        main_box = ctk.CTkFrame(self, width=float(self.master.winfo_screenwidth() / 1.3), 
                                height=float(self.master.winfo_screenheight() / 1.5), 
                                fg_color=colors.white,
                                corner_radius=0)
        main_box.place(relx=0.5, rely=0.5, anchor="center")

        # کانتینر اصلی (باکس سبز)
        right_box = ctk.CTkFrame(main_box, width=float(1 + self.master.winfo_screenwidth() / 2.6), 
                                height=float(main_box.winfo_screenheight() / 1.5), 
                                fg_color=colors.dark_green_6,
                                corner_radius=0)
        right_box.place(relx=0.75, rely=0.5, anchor="center")

        #تصویر باکس سبز
        width = 1 + self.master.winfo_screenwidth() / 2.6
        height = self.master.winfo_screenheight() / 1.5

        box_w, box_h = int(width), int(height)
        picture_left = ctk.CTkFrame(main_box, width=box_w, height=box_h, fg_color="red", corner_radius=0)
        picture_left.place(relx=0.25, rely=0.5, anchor="center")

        ck.make_image(main_box, registerPage, int(box_w), int(box_h), 0.25, 0.5, "center")

        # Sign in بخش راست
        sign_in_label = ctk.CTkLabel(main_box, text="ثبت‌نام در سامانه", font=(None, 35, "bold"), text_color=colors.white, bg_color=colors.dark_green_6)
        sign_in_label.place(relx=0.85, rely=0.13, anchor="center")
        description_label = ctk.CTkLabel(main_box, 
                                         text="پس از پر کردن اطلاعات، در صورت تأیید مدیر، ثبت‌نام شما تکمیل خواهد شد ", 
                                         font=(None, 13), 
                                         text_color=colors.white,
                                         bg_color=colors.dark_green_6)
        description_label.place(relx=0.79, rely=0.19, anchor="center")
        
        #خط پایین توضیحات
        circle_canvas = ctk.CTkCanvas(main_box, width=float(main_box.winfo_screenwidth() / 2.3), height=2, bg=colors.dark_green_6, highlightthickness=0)
        circle_canvas.place(relx=0.5, rely=0.21)
        circle_canvas.create_line(float(main_box.winfo_screenwidth() / 22), 1, float(main_box.winfo_screenwidth() / 2.85), 1, fill=colors.white, width=1)
        
        #فیلد نام
        name_label = ctk.CTkLabel(main_box, text="نام:", font=(None, 18, "bold"), text_color=colors.white, bg_color=colors.dark_green_6)
        name_label.place(relx=0.94, rely=0.26, anchor="center")
        self.name_entry = ctk.CTkEntry(main_box, placeholder_text="نام", height=36 , justify="right", width=200, bg_color=colors.dark_green_6, corner_radius=8, border_color=colors.dark_green_6, fg_color=colors.light_gray_4, text_color=colors.black)
        self.name_entry.place(relx=0.87, rely=0.31, anchor="center")
        self.name_entry.focus()
        
        #فیلد نام خانوادگی
        lastname_label = ctk.CTkLabel(main_box, text="نام خانوادگی:", font=(None, 18, "bold"), text_color=colors.white, bg_color=colors.dark_green_6)
        lastname_label.place(relx=0.69, rely=0.26, anchor="center")
        self.lastname_entry = ctk.CTkEntry(main_box, placeholder_text="نام‌خانوادگی", height=36 , justify="right", width=200, bg_color=colors.dark_green_6, corner_radius=8, border_color=colors.dark_green_6, fg_color=colors.light_gray_4, text_color=colors.black)
        self.lastname_entry.place(relx=0.65, rely=0.31, anchor="center")
        
        #فیلد شماره تلفن
        phone_number_label = ctk.CTkLabel(main_box, text="شماره همراه:", font=(None, 18, "bold"), text_color=colors.white, bg_color=colors.dark_green_6)
        phone_number_label.place(relx=0.91, rely=0.36, anchor="center")
        self.phone_number_entry = ctk.CTkEntry(main_box, placeholder_text="تلفن", height=36 , justify="right", width=200, bg_color=colors.dark_green_6, corner_radius=8, border_color=colors.dark_green_6, fg_color=colors.light_gray_4, text_color=colors.black)
        self.phone_number_entry.place(relx=0.87, rely=0.41, anchor="center")
        
        #فیلد کد ملی
        nationalCode_label = ctk.CTkLabel(main_box, text="کد ملی:", font=(None, 18, "bold"), text_color=colors.white, bg_color=colors.dark_green_6)
        nationalCode_label.place(relx=0.71, rely=0.36, anchor="center")
        self.nationalCode_entry = ctk.CTkEntry(main_box, placeholder_text="کد ملی", height=36 , justify="right", width=200, bg_color=colors.dark_green_6, corner_radius=8, border_color=colors.dark_green_6, fg_color=colors.light_gray_4, text_color=colors.black)
        self.nationalCode_entry.place(relx=0.65, rely=0.41, anchor="center")
        
        #فیلد ایمیل
        email_label = ctk.CTkLabel(main_box, text="ایمیل:", font=(None, 18, "bold"), text_color=colors.white, bg_color=colors.dark_green_6)
        email_label.place(relx=0.93, rely=0.46, anchor="center")
        self.email_entry = ctk.CTkEntry(main_box, placeholder_text="ایمیل", height=36 , justify="right", width=200, bg_color=colors.dark_green_6, corner_radius=8, border_color=colors.dark_green_6, fg_color=colors.light_gray_4, text_color=colors.black)
        self.email_entry.place(relx=0.87, rely=0.51, anchor="center")
        
        #فیلد نام کاربری
        username_label = ctk.CTkLabel(main_box, text="نام کاربری:", font=(None, 18, "bold"), text_color=colors.white, bg_color=colors.dark_green_6)
        username_label.place(relx=0.70, rely=0.46, anchor="center")
        self.username_entry = ctk.CTkEntry(main_box, placeholder_text="نام کاربری", height=36 , justify="right", width=200, bg_color=colors.dark_green_6, corner_radius=8, border_color=colors.dark_green_6, fg_color=colors.light_gray_4, text_color=colors.black)
        self.username_entry.place(relx=0.65, rely=0.51, anchor="center")
        
        #فیلد پسورد
        password_label = ctk.CTkLabel(main_box, text="رمز عبور:", font=(None, 18, "bold"), text_color=colors.white, bg_color=colors.dark_green_6)
        password_label.place(relx=0.92, rely=0.56, anchor="center")
        self.password_entry = ctk.CTkEntry(main_box, placeholder_text="رمز عبور", height=36 , show="*", justify="right", width=200, bg_color=colors.dark_green_6, corner_radius=8, border_color=colors.dark_green_6, fg_color=colors.light_gray_4, text_color=colors.black)
        self.password_entry.place(relx=0.87, rely=0.61, anchor="center")
        
        #فیلد تکرار پسورد
        repet_password_label = ctk.CTkLabel(main_box, text="تکرار رمز عبور:", font=(None, 18, "bold"), text_color=colors.white, bg_color=colors.dark_green_6)
        repet_password_label.place(relx=0.69, rely=0.56, anchor="center")
        self.repet_password_entry = ctk.CTkEntry(main_box, placeholder_text="تکرار رمز عبور", show="*", height=36 , justify="right", width=200, bg_color=colors.dark_green_6, corner_radius=8, border_color=colors.dark_green_6, fg_color=colors.light_gray_4, text_color=colors.black)
        self.repet_password_entry.place(relx=0.65, rely=0.61, anchor="center")
        
        #فیلد انتخاب نقش
        radio_frame = ctk.CTkFrame(right_box, bg_color=colors.dark_green_6, fg_color=colors.dark_green_6, width=right_box.winfo_screenwidth(), height=40)
        radio_frame.place(relx=0.57, rely=0.7, anchor="center")
        self.selected_role_var = ctk.StringVar(value="مدیر")
        desired_gap = 60
        admin_radio = ctk.CTkRadioButton(
            master=radio_frame,
            text="مدیر",
            variable=self.selected_role_var,
            value="مدیر",
            text_color=colors.white,
            border_color=colors.white,
            hover_color=colors.white,
            fg_color=colors.green_1
        )
        admin_radio.pack(side=ctk.RIGHT, padx=(0, 5))
        spacer_frame = ctk.CTkFrame(
            master=radio_frame,
            width=desired_gap,
            height=10,
            fg_color="transparent"
        )
        spacer_frame.pack(side=ctk.RIGHT)
        employee_radio = ctk.CTkRadioButton(
            master=radio_frame,
            text="کارمند",
            variable=self.selected_role_var,
            value="کارمند",
            text_color=colors.white,
            border_color=colors.white,
            hover_color=colors.white,
            fg_color=colors.green_1
        )
        employee_radio.pack(side=ctk.RIGHT, padx=(5, 0))

        #خط بالای دکمه ها
        circle_canvas = ctk.CTkCanvas(main_box, width=float(main_box.winfo_screenwidth() / 2.3), height=2, bg=colors.dark_green_6, highlightthickness=0)
        circle_canvas.place(relx=0.5, rely=0.74)
        circle_canvas.create_line(float(main_box.winfo_screenwidth() / 22), 1, float(main_box.winfo_screenwidth() / 2.85), 1, fill=colors.white, width=1)
        
        #دکمه ثبت اطلاعات
        signin_btn = ctk.CTkButton(main_box, text="ثبت نام", 
                                   width=440, height=50, 
                                   font=(None, 30, "bold"), 
                                   corner_radius=8, 
                                   text_color=colors.white, 
                                   bg_color=colors.dark_green_6, 
                                   fg_color=colors.green_1, 
                                   hover_color=colors.green_3,
                                   command=register_user)
        signin_btn.place(relx=0.76, rely=0.8, anchor="center")
        
        forgot = ctk.CTkButton(main_box, text="قبلا ثبت‌نام کردید؟ وارد شوید...",
                               fg_color=colors.dark_green_6,
                               hover_color=colors.dark_green_6,
                               text_color=colors.blue_color,
                               bg_color=colors.dark_green_6,
                               width=80,
                               cursor="hand2",
                               command=go_to_login)
        forgot.place(relx=0.8, rely=0.87, anchor="w")

        #لیبل ارور ها
        self.error_label = ctk.CTkLabel(right_box, 
                                        text="لطفا تمامی اطلاعات مورد نیاز را تکمیل کنید!", 
                                        font=(None, 18, "bold"), 
                                        text_color=colors.red_color, 
                                        bg_color=colors.dark_green_6)