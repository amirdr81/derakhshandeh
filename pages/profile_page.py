import customtkinter as ctk
from asset_paths import profile_view_photo, edit_icon_photo, accept_icon, reject_icon
import insystem_data
from hoverbox import HoverBox
import common_ctk as ck
import colors

def eng_to_persian_date(date_str):
        english_digits = '0123456789'
        persian_digits = '۰۱۲۳۴۵۶۷۸۹'
        trans_table = str.maketrans(''.join(english_digits), ''.join(persian_digits))
        return date_str.translate(trans_table)
    
class item():
    def __init__(self, box, title, eng_item, text_color, bg_color, fg_color, x, y, anchor):
        label = ctk.CTkLabel(box, text=title + ": " + eng_to_persian_date(insystem_data.loged_in_user[eng_item]), 
                             text_color=text_color,
                             bg_color=bg_color, 
                             fg_color=fg_color,
                             font=(None, 20, "bold"))
        label.place(relx = x - 0.02, rely = y, anchor=anchor)
        
        img_label = ck.make_image(box, edit_icon_photo, 20, 20, x, y, anchor)
        
        change_hover = HoverBox(img_label, "تغییر " + title)

        accept_photo = ck.make_image(box, accept_icon, 20, 20, x - 0.15, y, anchor)
        reject_photo = ck.make_image(box, reject_icon, 20, 20, x - 0.175, y, anchor)
        accept_hover = HoverBox(accept_photo, "تایید")
        reject_hover = HoverBox(reject_photo, "بستن")
        accept_photo.place_forget()
        reject_photo.place_forget()
        
        error_label = ctk.CTkLabel(box, 
                                   text_color=colors.red_color,
                                   font=(None, 15, "bold"))
        entry_new_value = ctk.CTkEntry(box, width=150)
        entry_new_value2 = ctk.CTkEntry(box, width=150)
        
        def show_error(text):
            entry_new_value.configure(border_color = colors.red_color)
            entry_new_value.after(2000, lambda: entry_new_value.configure(border_color = colors.dark_green_6))
            error_label.configure(text=text)
            error_label.after(2000, lambda: error_label.configure(text = ""))
            error_label.place(relx=0.98, rely=0.65, anchor="e")
            
        def chagne_item(event):
            label.configure(text="")
            entry_new_value.delete(0, "end")
            entry_new_value.focus()
            entry_new_value.configure(height=25,
                                           bg_color=colors.white,
                                           fg_color=colors.dark_green_6,
                                           text_color=colors.white,
                                           border_color=colors.dark_green_6,
                                           placeholder_text_color=colors.light_green_1,
                                           justify="right")
            entry_new_value.place(relx=x - 0.02, rely=y, anchor=anchor)
            if(eng_item == "password"):
                entry_new_value2.configure(height=25,
                                           bg_color=colors.white,
                                           fg_color=colors.dark_green_6,
                                           text_color=colors.white,
                                           border_color=colors.dark_green_6,
                                           placeholder_text = "تکرار رمز عبور",
                                           placeholder_text_color=colors.light_green_1,
                                           justify="right")
                entry_new_value2.place(relx=x - 0.02, rely=y + 0.05, anchor=anchor)
            accept_photo.place(relx=x - 0.15, rely=y, anchor=anchor)
            reject_photo.place(relx=x - 0.175, rely=y, anchor=anchor)
    
        def accept_and_close(event):
            def is_username_taken(target, input):
                for item in insystem_data.users:
                    if(item[input] == target): return False
                return True
            
            def check_phone_format(phone_str):
                return (len(phone_str) == 11 and phone_str[0:2] == "09")
            
            def check_email_format(email_str):
                return (("@" and ".") in email_str)
            
            def check_password(password, repetead_password):
                return password == repetead_password
    
            def is_password_strong(password_str):
                if(len(password_str) < 10): return False
                return True
            
            if((eng_item == "phone" and not check_phone_format(entry_new_value.get()))):
                show_error("شماره تلفن وارد شده، صحیح نیست.")
            elif((eng_item == "email" and not check_email_format(entry_new_value.get()))):
                show_error("ایمیل وارد شده، صحیح نمی‌باشد.")
            elif(eng_item == "username" and not is_username_taken(entry_new_value.get(), "username")):
                show_error("نام کاربری انتخاب شده، قبلا انتخاب شده است.")
            elif(eng_item == "id" and not is_username_taken(entry_new_value.get(), "id")):
                show_error("کد ملی انتخاب شده، قبلا در سیستم ثبت شده است.")
            elif(eng_item == "password" and not is_password_strong(entry_new_value.get())):
                show_error("رمز وارد شده باید حداقل ۱۰ رقم باشد.")
            elif(eng_item == "password" and not check_password(entry_new_value.get(), entry_new_value2.get())):
                show_error("دو رمز عبور، یکسان نیستند!")
            else:
                entry_new_value.place_forget()
                entry_new_value2.place_forget()
                accept_photo.place_forget()
                reject_photo.place_forget()
                insystem_data.loged_in_user[eng_item] = entry_new_value.get()
                label.configure(text=title + ": " + eng_to_persian_date(insystem_data.loged_in_user[eng_item]))
            
        def reject(event):
            entry_new_value.place_forget()
            entry_new_value2.place_forget()
            accept_photo.place_forget()
            reject_photo.place_forget()
            label.configure(text=title + ": " + eng_to_persian_date(insystem_data.loged_in_user[eng_item]))
            
        def show_hover(event, widget, hover):
            x = widget.winfo_rootx() + 35
            y = widget.winfo_rooty() + 20
            hover.show_at(x, y)

        def hide_hover(event, hover):
            hover.hide()
            
        img_label.bind("<Enter>", lambda e: show_hover(e, img_label, change_hover))
        img_label.bind("<Leave>", lambda e: hide_hover(e, change_hover))
        
        accept_photo.bind("<Enter>", lambda e: show_hover(e, accept_photo, accept_hover))
        accept_photo.bind("<Leave>", lambda e: hide_hover(e, accept_hover))
        
        reject_photo.bind("<Enter>", lambda e: show_hover(e, reject_photo, reject_hover))
        reject_photo.bind("<Leave>", lambda e: hide_hover(e, reject_hover))
        
        img_label.bind("<Button-1>", chagne_item)
        accept_photo.bind("<Button-1>", accept_and_close)
        reject_photo.bind("<Button-1>", reject)
        
class Profile(ctk.CTkFrame):    
    def __init__(self, parent, go_to_dashboard):
        super().__init__(parent)
        
        self.pack(fill="both", expand=True)
        self.configure(fg_color=colors.light_green_1)

        width = int(self.master.winfo_screenwidth() / 1.2)
        height = int(self.master.winfo_screenheight() / 1.5)
        
        main_box = ctk.CTkFrame(self, width=width, 
                                height=height, 
                                fg_color=colors.white,
                                corner_radius=0)
        main_box.place(relx=0.5, rely=0.5, anchor="center")
        
        ck.make_image(main_box, profile_view_photo, int(width * 2 / 3), height, 0.3, 0.5, "center")
        
        title_label = ctk.CTkLabel(main_box, text="مشخصات کاربری", 
                             text_color=colors.black,
                             bg_color=colors.white, 
                             fg_color=colors.white,
                             font=(None, 35, "bold"))
        title_label.place(relx = 0.98, rely = 0.07, anchor="e")
        item(main_box, "نام", "name", colors.black, colors.white, colors.white, 0.98, 0.15, "e")
        item(main_box, "نام خانوادگی", "lastname", colors.black, colors.white, colors.white, 0.98, 0.2, "e")
        item(main_box, "شماره تماس", "phone", colors.black, colors.white, colors.white, 0.98, 0.25, "e")
        item(main_box, "کد ملی", "id", colors.black, colors.white, colors.white, 0.98, 0.3, "e")
        item(main_box, "ایمیل", "email", colors.black, colors.white, colors.white, 0.98, 0.35, "e")
        item(main_box, "نام کابری", "username", colors.black, colors.white, colors.white, 0.98, 0.4, "e")
        item(main_box, "رمز عبور", "password", colors.black, colors.white, colors.white, 0.98, 0.45, "e")
        
        
        
        def change_theme_color(input):
            # print(input)
            if(input == "سبز"): colors.set_theme_colors("green")
            elif(input == "آبی"): colors.set_theme_colors("blue")
            elif(input == "قرمز"): colors.set_theme_colors("red")
            elif(input == "بنفش"): colors.set_theme_colors("purple")
            elif(input == "قهوه‌ای"): colors.set_theme_colors("brown")
            elif(input == "زرد"): colors.set_theme_colors("yellow")
            elif(input == "نارنجی"): colors.set_theme_colors("orange")
            elif(input == "طوسی"): colors.set_theme_colors("gray")
            elif(input == "صورتی"): colors.set_theme_colors("pink")
            else: colors.set_theme_colors("green")
            go_to_dashboard()
            
        list = ck.make_list(main_box, colors.get_current_color(), ["سبز", "آبی", "قرمز", "بنفش", "قهوه‌ای", "زرد", "نارنجی", "طوسی", "صورتی"], 
                     120, 35, colors.gray_1, colors.white, colors.light_gray_4, colors.green_2, colors.dark_green_3,
                     60, lambda e: change_theme_color(list.get()), "e", 0.7, 0.07, "center")
        
        back_to_dashboard_btn = ctk.CTkButton(main_box, text="بازگشت", 
                                   width=150, height=50, 
                                   font=(None, 22, "bold"), 
                                   corner_radius=20, 
                                   text_color=colors.white, 
                                   bg_color=colors.white, 
                                   fg_color=colors.dark_green_5, 
                                   hover_color=colors.green_3,
                                   command=go_to_dashboard)
        back_to_dashboard_btn.place(relx=0.715, rely=0.94, anchor="center")
        