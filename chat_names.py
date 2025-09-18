import customtkinter as ctk
from asset_paths import profile_default_photo
import insystem_data
from message_frame import Message
import jdatetime
from datetime import datetime
from datetime import timedelta
import tkinter.font as tkfont
import common_ctk as ck

import colors

class chatNames(ctk.CTk):   
    def fit_text_box(self, text, min_width=40, max_width=500, ideal_width=400):
        words = text.split(' ')
        lines = []
        current_line = ""
        for word in words:
            test = (current_line + ' ' + word).strip()
            if self.font.measure(test) <= ideal_width:
                current_line = test
            else:
                if self.font.measure(test) <= max_width:
                    current_line = test
                else:
                    lines.append(current_line)
                    current_line = word
        if current_line:
            lines.append(current_line)

        # حالا عرض هر خط رو اندازه بگیر و بین min و max clamp کن
        line_widths = [self.font.measure(line) for line in lines if line]
        widest = max(line_widths) if line_widths else 0
        # اگر هیچ خطی نداشتی، بذار حداقل عرض
        final_width = min(max(widest, min_width), max_width)
        line_height = self.font.metrics("linespace") + 3
        height = line_height * len(lines) if lines else line_height

        return final_width, height
    
    def eng_to_persian_date(self, date_str):
        english_digits = '0123456789'
        persian_digits = '۰۱۲۳۴۵۶۷۸۹'
        trans_table = str.maketrans(''.join(english_digits), ''.join(persian_digits))
        return date_str.translate(trans_table)
    
    def persian_to_english_date(self, date_str):
        english_digits = '0123456789'
        persian_digits = '۰۱۲۳۴۵۶۷۸۹'
        trans_table = str.maketrans(''.join(persian_digits), ''.join(english_digits))
        return date_str.translate(trans_table)
    
    def make_frame(self, box, width, height, bg_color, fg_color, radius, x, y, anchor):
        frame = ctk.CTkFrame(box,
                                width=width,
                                height=height,
                                bg_color=bg_color,
                                fg_color=fg_color,
                                corner_radius=radius)
        frame.place(relx=x, rely=y, anchor=anchor)
        return frame
        
    def make_label(self, box, text, x, y, image, text_color, bg_color, fg_color, font, anchor, width, height, radius):
        label = ctk.CTkLabel(box, text=text, 
                                image=image,
                                text_color=text_color,
                                bg_color=bg_color,
                                fg_color=fg_color,
                                font=font,
                                justify="center",
                                width=width,
                                height=height, 
                                corner_radius=radius)
        label.place(relx=x, rely=y, anchor=anchor)
        return label

    def get_chats_via_username_as_receiver(self, sender, receiver):
        messages = []
        for item in insystem_data.chats:
            if(item["sender"] == receiver and item["receiver"] == sender):
                messages.append(item)
        return messages
        
    def get_chats_total(self, sender, receiver):
        messages = []
        for item in insystem_data.chats:
            if((item["sender"] == sender and item["receiver"] == receiver) or
                item["sender"] == receiver and item["receiver"] == sender):
                messages.append(item)
        return messages
        
    def read_messages(self, user):
        for item in self.get_chats_via_username_as_receiver(insystem_data.loged_in_user["username"], user["username"]):
            item["seen"] = True
                  
    def show_chat(self, receiver):
        self.read_messages(receiver)
        if(self.notification_label):
            self.notification_label.destroy()
        #ایجاد فریم کانواس برای پیام ها
        canvas = ctk.CTkCanvas(self.chat_box, bg=colors.light_gray_2, highlightthickness=0, highlightbackground=colors.light_green_1)
        canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        scrollbar = ctk.CTkScrollbar(self.chat_box, orientation="vertical", command=canvas.yview)
        scrollbar.place(relx=0, rely=0, relheight=1)

        canvas.configure(yscrollcommand=scrollbar.set)
        
        scrollable_frame = ctk.CTkFrame(canvas, bg_color=colors.light_gray_2, fg_color=colors.light_gray_2)
        window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        scrollable_frame.bind("<Configure>", on_frame_configure)

        def resize_frame(event):
            canvas.itemconfig(window, width=event.width)
        canvas.bind("<Configure>", resize_frame)
        
        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1 * (e.delta)), "units"))

        

        lastseen_date = self.user["lastseen_date"]
        lastseen_time = self.user["lastseen_time"]
        def get_lastseen_display():
            today = jdatetime.date.today().strftime('%Y/%m/%d')
            yesterday = (jdatetime.date.today() - timedelta(days=1)).strftime('%Y/%m/%d')
            two_days_ago = (jdatetime.date.today() - timedelta(days=2)).strftime('%Y/%m/%d')
            if(lastseen_date == today): return ("ساعت " + self.eng_to_persian_date(lastseen_time) + "، اینجا بوده است...")
            elif(lastseen_date == yesterday): return ("دیروز ساعت " + self.eng_to_persian_date(lastseen_time) + "، اینجا بوده است...")
            elif(lastseen_date == two_days_ago): return ("دو روز پیش، ساعت " + self.eng_to_persian_date(lastseen_time) + "، اینجا بوده است...")
            else: return ("در تاریخ " + self.eng_to_persian_date(lastseen_date) + "، اینجا بوده است...")
            
        #تغییرات عناوین صفحه چت
        self.title_name.configure(text = self.title)
        self.title_lastseen.configure(text=get_lastseen_display())
        
        
        #تغییرات صفحه چت
        # for widget in self.chat_box.winfo_children():
        #     widget.destroy()
        message_height = 0
        messages = self.get_chats_total(insystem_data.loged_in_user["username"], receiver["username"])
        for message in messages:
            width, height = self.fit_text_box(message["message"])
            if(message["sender"] == insystem_data.loged_in_user["username"]):
                message = Message(canvas, message["sender"], message["receiver"], message["message"], message["time"], message["seen"], True, 50 + message_height, width, height)
            else:
                message = Message(canvas, message["sender"], message["receiver"], message["message"], message["time"], message["seen"], False, 50 + message_height, width, height)
            message_height += (height + 2 * self.corner + self.frames_space + self.date_height + 10)
            
        #فریم ارسال پیام
        def write_message():
            insystem_data.chats.append({
                "sender":insystem_data.loged_in_user["username"],
                "receiver":self.user["username"],
                "message":send_message_entry.get(),
                "date":jdatetime.date.today().strftime('%Y/%m/%d'),
                "time":self.eng_to_persian_date(datetime.now().strftime('%H:%M')),
                "seen":False
            })
            self.show_chat(self.user)

            frames = self.parent.winfo_children()[2:]
            users_count = 1
            for frame in frames:
                if(frame != self.main_box):
                    frame.place(relx=0.5, rely=0.225 + users_count * 0.079, anchor="center")
                    users_count += 1
                elif(frame == self.main_box):
                    frame.place(relx=0.5, rely=0.225, anchor="center")
                    
        def check_and_call(event=None):
            if send_message_entry.get().strip(): write_message()
        send_message_frame = self.make_frame(self.super_parent,
                   0.75 * self.chat_box.winfo_screenwidth(), 
                   50, colors.dark_green_4, colors.dark_green_4, 0, 0, 1, "sw")
        send_message_entry = ctk.CTkEntry(send_message_frame, 
                                        width=0.693 * self.chat_box.winfo_screenwidth(), 
                                        height=40, 
                                        placeholder_text="متن",
                                        placeholder_text_color=colors.gray_2,
                                        corner_radius=30,
                                        bg_color=colors.dark_green_4, 
                                        fg_color=colors.light_gray_3,
                                        border_color=colors.light_gray_3,
                                        text_color=colors.black,
                                        font=(None, 23),
                                        justify="right")
        send_message_entry.place(relx=0.535, rely=0.5, anchor="center")
        send_message_entry.focus()

        def click(event):
            def add_file():
                frame.destroy()
                print('add file')
            def add_photo():
                frame.destroy()
                print('add photo')
                
            frame = ck.make_frame(self.super_parent, 200, 95, colors.dark_green_6, colors.dark_green_6, colors.dark_green_6, 0,
                          0, 0.005, 0.885, 'w')
            self.super_parent.bind('<Button-1>', lambda e: frame.destroy())
            
            ck.make_button(frame, 'افزودن فایل', 190, 40, (None, 15), 0, colors.black,
                           colors.dark_green_6, colors.green_5, colors.green_2, add_file, 0.5, 0.05, 'n')
            ck.make_button(frame, 'افزودن تصویر', 190, 40, (None, 15), 0, colors.black,
                           colors.dark_green_6, colors.green_5, colors.green_2, add_photo, 0.5, 0.52, 'n')
            
        plus_label = self.make_label(send_message_frame, "+", 0.035, 0.5, None, colors.black,
                   colors.dark_green_4, colors.green_3, (None, 30, "bold"),
                   "center", 40, 40, 30)
        plus_label.bind("<Enter>", lambda e: plus_label.configure(fg_color=colors.dark_green_6))
        plus_label.bind("<Leave>", lambda e: plus_label.configure(fg_color=colors.green_3))
        plus_label.bind("<Button-1>", click)
        
        send_message_entry.bind("<Return>", check_and_call)
        
        canvas.update_idletasks()
        canvas.yview_moveto(1.0)
        
        #آپدیت آخرین پیام داخل باکس
        messages = self.get_chats_total(insystem_data.loged_in_user["username"], self.user["username"])
        if(len(messages) == 0):
            self.description_label.configure(text=None)
            self.date_label.configure(text=None)
        else:
            last_message = messages[len(messages) - 1]
            self.description_label.configure(text=last_message["message"])
            self.date_label.configure(text=last_message["time"])
        
        
    def hover_box(self):
        self.main_box.configure(fg_color=colors.light_gray_5)
    
    def unhover_box(self):
        self.main_box.configure(fg_color=colors.white)
            
    def __init__(self, parent, title, description, date, photo, y, width, chat_box, user, title_name, title_lastseen, super_parent):
        self.parent = parent
        self.title = title
        self.description = description
        self.date = date
        self.photo = photo
        self.y = y
        self.width = width
        self.chat_box = chat_box
        self.user = user
        self.username = user["username"]
        self.title_name = title_name
        self.title_lastseen = title_lastseen
        self.super_parent = super_parent
        self.corner = 10
        self.frames_space = 5
        self.date_height = 15
        self.notification_label = None
        self.font = tkfont.Font(size=18)
        
        self.main_box = ctk.CTkFrame(self.parent, width=self.width, height=70,
                                bg_color=colors.dark_green_6, fg_color=colors.white,
                                corner_radius=0)
        self.main_box.place(relx=0.5, rely=y, anchor="center")
        
        self.photo = ck.make_image(self.main_box, profile_default_photo, 65, 65, 0.9, 0.5, "center")
        
        self.title_label = ctk.CTkLabel(self.main_box, text=self.title, font=(None, 20, "bold"), text_color=colors.black)
        self.title_label.place(relx=0.75, rely=0.25, anchor="e")
        
        self.description_label = ctk.CTkLabel(self.main_box, text=self.description, font=(None, 15), text_color=colors.gray_2)
        self.description_label.place(relx=0.75, rely=0.7, anchor="e")
        
        self.date_label = ctk.CTkLabel(self.main_box, text=self.date, font=(None, 15, "bold"), text_color=colors.gray_2)
        self.date_label.place(relx=0.05, rely=0.3, anchor="w")
                
        number_of_unread_messages = 0
        for message in self.get_chats_via_username_as_receiver(insystem_data.loged_in_user["username"], user["username"]):
            if(not message["seen"]): number_of_unread_messages += 1
        if(number_of_unread_messages != 0):
            self.notification_label = ctk.CTkLabel(self.main_box, 
                                                text=self.eng_to_persian_date(str(number_of_unread_messages)), 
                                                fg_color=colors.light_green_2,
                                                bg_color=colors.white,
                                                font=(None, 15, "bold"),
                                                corner_radius=100,
                                                text_color=colors.dark_green_6)
            self.notification_label.place(relx=0.1, rely=0.7, anchor="center")
        
        self.main_box.bind("<Enter>", lambda event: self.hover_box())
        self.title_label.bind("<Enter>", lambda event: self.hover_box())
        self.description_label.bind("<Enter>", lambda event: self.hover_box())
        self.date_label.bind("<Enter>", lambda event: self.hover_box())
        self.photo.bind("<Enter>", lambda event: self.hover_box())
        
        self.main_box.bind("<Leave>", lambda event: self.unhover_box())
        self.title_label.bind("<Leave>", lambda event: self.unhover_box())
        self.description_label.bind("<Leave>", lambda event: self.unhover_box())
        self.date_label.bind("<Leave>", lambda event: self.unhover_box())
        self.photo.bind("<Leave>", lambda event: self.unhover_box())
        
        
        self.main_box.bind("<Button-1>", lambda event: self.show_chat(self.user))
        self.title_label.bind("<Button-1>", lambda event: self.show_chat(self.user))
        self.description_label.bind("<Button-1>", lambda event: self.show_chat(self.user))
        self.date_label.bind("<Button-1>", lambda event: self.show_chat(self.user))
        self.photo.bind("<Button-1>", lambda event: self.show_chat(self.user))
        