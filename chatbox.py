import customtkinter as ctk
from PIL import Image, ImageTk
from asset_paths import chat_background, profile_default_photo, search_icon_photo
from chat_names import chatNames
import insystem_data
from functools import cmp_to_key
import common_controller as cc

import colors

class chatBox(ctk.CTkFrame):
    def show_users_names(self, names_box, chat_box, title_name, title_lastseen, parent):
        users_count = 0
        target_users = []
        for name in names_box.winfo_children()[2:]: name.destroy()
        if(self.search_entry_box.get() == '' or self.search_entry_box.get() == None): 
            target_users = self.sort_users_on_lastmessages_date()
        else:
            for user in self.sort_users_on_lastmessages_date():
                if(cc.match_input(self.search_entry_box.get(), user['name'] + " " + user['lastname'])): target_users.append(user)
        for user in target_users:
            if(insystem_data.loged_in_user["username"] != user["username"]):
                messages = self.get_chats_total(insystem_data.loged_in_user["username"], user["username"])
                if(len(messages) == 0): 
                    chatNames(names_box, user["name"] + " " + user["lastname"], 
                        None, 
                        None, 
                        ImageTk.PhotoImage(Image.open(profile_default_photo).resize((65, 65))), 
                        0.225 + users_count * 0.079, 
                        0.254 * self.winfo_screenwidth(),
                        chat_box,
                        user,
                        title_name,
                        title_lastseen,
                        parent)
                else:
                    last_message = messages[len(messages) - 1]
                    chatNames(names_box, user["name"] + " " + user["lastname"], 
                            last_message["message"], 
                            last_message["time"], 
                            ImageTk.PhotoImage(Image.open(profile_default_photo).resize((65, 65))), 
                            0.225 + users_count * 0.079, 
                            0.254 * self.winfo_screenwidth(),
                            chat_box,
                            user,
                            title_name,
                            title_lastseen,
                            parent)
                users_count += 1
        
    def sort_users_on_lastmessages_date(self):
        last_messages = []
        for user in insystem_data.users:
            if(insystem_data.loged_in_user["username"] != user["username"] and self.get_last_message(insystem_data.loged_in_user, user) != None):
                last_messages.append(self.get_last_message(insystem_data.loged_in_user, user))
        last_messages = sorted(last_messages, key=cmp_to_key(self.is_date_closer))
        sorted_users = []

        def get_user(message):
            def get_user_by_username(username):
                for user in insystem_data.users:
                    if(user["username"] == username): return user
                return None
            if(message["sender"] != insystem_data.loged_in_user["username"]): return get_user_by_username(message["sender"])
            else: return get_user_by_username(message["receiver"])
        for message in last_messages: sorted_users.append(get_user(message))
        for user in insystem_data.users: 
            if(user not in sorted_users): sorted_users.append(user)
        return sorted_users
            
    def get_last_message(self, sender, receiver):
        messages = self.get_chats_total(sender["username"], receiver["username"])
        if(len(messages) == 0): return None
        return messages[len(messages) - 1]
        
    def is_date_closer(self, message1, message2):
        if(not message1 and not message2): return 0
        elif(message1 and not message2): return -1
        elif(not message1 and message2): return 1
        else:
            date = message1["date"]
            target_date = message2["date"]
            time = self.persian_to_english_date(message1["time"])
            target_time = self.persian_to_english_date(message2["time"])
            
            y1, m1, d1 = map(int, date.split('/'))
            y2, m2, d2 = map(int, target_date.split('/'))
            hour1, minute1 = map(int, time.split(':'))
            hour2, minute2 = map(int, target_time.split(':'))
            
            if(y1 > y2): return -1
            elif(y1 < y2): return 1
            else:
                if(m1 > m2): return -1        
                elif(m1 < m2): return 1
                else:
                    if(d1 > d2): return -1        
                    elif(d1 < d2): return 1
            if(hour1 > hour2): return -1
            elif(hour1 < hour2): return 1
            else:
                if(minute1 > minute2): return -1
                elif(minute1 < minute2): return 1
            return 0
    def get_chats_total(self, sender, receiver):
        messages = []
        for item in insystem_data.chats:
            if((item["sender"] == sender and item["receiver"] == receiver) or
                item["sender"] == receiver and item["receiver"] == sender):
                messages.append(item)
        return messages
    
    def persian_to_english_date(self, date_str):
        english_digits = '0123456789'
        persian_digits = '۰۱۲۳۴۵۶۷۸۹'
        trans_table = str.maketrans(''.join(persian_digits), ''.join(english_digits))
        return date_str.translate(trans_table)
    
    def __init__(self, parent, go_to_dashboard):
        super().__init__(parent)
        
        self.pack(fill="both", expand=True)
        self.configure(fg_color=colors.light_gray_5)
            
        def make_frame(box, width, height, bg_color, fg_color, radius, x, y, anchor):
            frame = ctk.CTkFrame(box,
                                    width=width,
                                    height=height,
                                    bg_color=bg_color,
                                    fg_color=fg_color,
                                    corner_radius=radius)
            frame.place(relx=x, rely=y, anchor=anchor)
            return frame
        
        def make_label(box, text, x, y, image, text_color, bg_color, fg_color, font, anchor, width, height, radius):
            label = ctk.CTkLabel(box, text=text, 
                                 image=image,
                                 text_color=text_color,
                                 bg_color=bg_color,
                                 fg_color=fg_color,
                                 font=font,
                                 width=width,
                                 height=height, 
                                 corner_radius=radius)
            label.place(relx=x, rely=y, anchor=anchor)
            return label
            
        #باکس چت
        chat_box = make_label(parent, "", 0, 0.1, None,
                   colors.light_gray_2, colors.light_gray_2, colors.light_gray_2, None, "nw", 0.75 * self.winfo_screenwidth(), 0.9 * self.winfo_screenheight() - 75, 0)
        make_label(parent, "", 0, 0.917, None,
                   colors.light_gray_2, colors.light_gray_2, colors.light_gray_2, None, "nw", 0.75 * self.winfo_screenwidth(), 75, 0)
        #اسامی
        names_box = make_frame(parent, 0.25 * self.winfo_screenwidth(), self.winfo_screenheight(), colors.light_gray_4, colors.light_gray_4, 0, 0.75, 0.5, "w")
        
        #عناوین صفحه
        title_box = make_frame(parent, 0.75 * self.winfo_screenwidth(), 97, colors.light_gray_5, colors.green_3, 0, 0, 0, "nw")
        title_name = make_label(title_box, "موردی برای نمایش وجود ندارد...", 0.98, 0.35, None, colors.white, colors.green_3, colors.green_3, (None, 30, "bold"), "e", 100, 30, 0)
        title_lastseen = make_label(title_box, "", 0.98, 0.75, None, colors.white, colors.green_3, colors.green_3, (None, 15), "e", 100, 20, 0)
        
        names_title = make_frame(names_box, 0.25 * self.winfo_screenwidth(), 100, colors.dark_green_4, colors.dark_green_4, 0, 0, 0, "nw")
        make_label(names_title, "سامانه درخشنده‌بار", 0.5, 0.5, None, colors.white, colors.dark_green_4, colors.dark_green_4, (None, 30, "bold"), "center", 0.25 * self.winfo_screenwidth(), 100, 0)
        search_box_frame = make_frame(names_box, 0.25 * self.winfo_screenwidth(), 70, colors.white, colors.white,
                   0, 0.5, 0.145, "center")
        self.search_entry_box = ctk.CTkEntry(search_box_frame, width=0.24 * self.winfo_screenwidth(), height=55, 
                                        corner_radius=15,
                                        bg_color=colors.white, 
                                        placeholder_text="جست‌و‌جو...",
                                        placeholder_text_color=colors.gray_2,
                                        fg_color=colors.light_gray_5,
                                        border_color=colors.light_gray_5,
                                        text_color=colors.black,
                                        font=(None, 20),
                                        justify="right")
        self.search_entry_box.place(relx=0.5, rely=0.5, anchor="center")
        self.search_entry_box.bind("<KeyRelease>", lambda e: self.show_users_names(names_box, chat_box, title_name, title_lastseen, parent))
        
        self.show_users_names(names_box, chat_box, title_name, title_lastseen, parent)
        # دکمه خروج
        back_to_dashboard_btn = ctk.CTkButton(title_box, text="بازگشت", 
                                   width=120, height=50, 
                                   font=(None, 22, "bold"), 
                                   corner_radius=20, 
                                   text_color=colors.dark_green_6, 
                                   bg_color=colors.green_3, 
                                   fg_color=colors.white, 
                                   hover_color=colors.light_green_3,
                                   command=go_to_dashboard)
        back_to_dashboard_btn.place(relx=0.01, rely=0.5, anchor="w")