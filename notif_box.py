import customtkinter as ctk
import insystem_data
import jdatetime
from datetime import timedelta
import common_ctk as ck
import common_controller as cc
import register_controller as rc
import colors
import scrollbar


class NotifBox(ctk.CTkFrame):                     
    def get_title(self, type):
        if(type == 'register user'): return 'درخواست ثبت‌نام'
        if(type == 'credit deal'): return 'اعتبار قرارداد'
        if(type == "credit smart cart driver"): return 'اعتبار هوشمند راننده'
        if(type == "credit smart cart car"): return 'اعتبار هوشمند نفتکش'
        if(type == 'credit workcart'): return 'اعتبار کارت تردد'
        if(type == 'credit security'): return 'اعتبار کارت ایمنی'
        if(type == 'credit licence'): return 'اعتبار گواهینامه تأیید صلاحیت'
        
    def add_notification(self, type, description, params, date, y):
        return NotifBox(self.box, type, description, params, date, y, self.show_dashboard, self.go_to_deals_page, self.go_to_drivers, self.go_to_cars, self.go_to_security, self.go_to_licence, self.go_to_workcart, self.super_parent)
    
    def remake_notifications(self):
        notifications = insystem_data.loged_in_user["notifications"]
        number_of_notifications = len(notifications)
        self.scrollable = scrollbar.ScrollableFrame(self.box, 250, colors.dark_green_6)
        self.scrollable.pack(side="top", fill="x", padx=5, pady=(150, 10))

        for i in range(number_of_notifications):
            self.add_notification(notifications[i]["type"], 
                                notifications[i]["description"], 
                                notifications[i]["params"], 
                                notifications[i]["date"], 
                                210 + 63 * i)
    
    def notification_type(self, object, menu_name, comm):
        def close_window():
            notification_box.destroy()
            cc.activate_all_widgets(self.super_parent)
        def remove_notification():
            def do_delete():
                insystem_data.loged_in_user['notifications'].remove({
                'type': self.type,
                'description': self.description,
                'params': self.params,
                'date': self.date
                })
                cancel()
                self.show_dashboard()
            def cancel():
                confirm_frame.destroy()
            confirm_frame = rc.show_confirmation_box(self.super_parent, do_delete, cancel, 'آیا از حذف این اعلان، اطمینان دارید؟', None)
        notification_box = ck.make_frame(self.super_parent, 600, 200, colors.green_3, colors.green_3, colors.green_3, 0, 0, 0.5, 0.5, 'center')
        new_object = self.params[object]
        if(object == 'deal'): text = 'یادآوری می‌شود که اعتبار قرارداد ' + new_object['name'] + ' به شماره قرارداد ' + cc.eng_to_persian_date(new_object['id']) + ' در تاریخ ' + cc.eng_to_persian_date(new_object['end_date']) + '، به اتمام خواهد رسید. لذا در اسرع وقت، نسبت به تمدید آن، اقدام فرمایید.'
        elif(object == 'driver'): text = 'یادآوری می‌شود که اعتبار کارت هوشمند راننده به نام ' + new_object['name'] + ' ' + new_object['lastname'] + ' با کد ملی ' + cc.eng_to_persian_date(new_object['id']) + ' در تاریخ ' + cc.eng_to_persian_date(new_object['end_smart_date']) + '، به اتمام خواهد رسید. لذا در اسرع وقت، نسبت به تمدید آن، اقدام فرمایید.'
        elif(object == 'car'): text = 'یادآوری می‌شود که اعتبار کارت هوشمند نفتکش به شماره ' + cc.car_id_true_format(new_object['car_id']) + ' به نام مالک ' + cc.eng_to_persian_date(new_object['owner_name']) + ' در تاریخ ' + cc.eng_to_persian_date(new_object['end_date']) + '، به اتمام خواهد رسید. لذا در اسرع وقت، نسبت به تمدید آن، اقدام فرمایید.'
        elif(object == 'security'): text = 'یادآوری می‌شود که اعتبار کارت ایمنی به شماره نفتکش ' + cc.car_id_true_format(new_object['car_id']) + ' و نام راننده ' + cc.eng_to_persian_date(new_object['driver_name']) + ' در تاریخ ' + cc.eng_to_persian_date(new_object['date']) + '، به اتمام خواهد رسید. لذا در اسرع وقت، نسبت به تمدید آن، اقدام فرمایید.'
        elif(object == 'licence'): text = 'یادآوری می‌شود که اعتبار گواهینامه تأیید صلاحیت نفتکش به شماره ' + cc.car_id_true_format(new_object['car_id']) + ' و شماره گواهینامه ' + cc.eng_to_persian_date(new_object['licence_id']) + ' در تاریخ ' + cc.eng_to_persian_date(new_object['end_date']) + '، به اتمام خواهد رسید. لذا در اسرع وقت، نسبت به تمدید آن، اقدام فرمایید.'
        elif(object == 'workcart'): text = 'یادآوری می‌شود که اعتبار کارت تردد نفتکش به شماره ' + cc.car_id_true_format(new_object['car_id']) + ' و نام راننده ' + cc.eng_to_persian_date(new_object['driver_name']) + ' در تاریخ ' + cc.eng_to_persian_date(new_object['end_date']) + '، به اتمام خواهد رسید. لذا در اسرع وقت، نسبت به تمدید آن، اقدام فرمایید.'
        description = ck.make_label(notification_box, 100, 30, colors.green_3, colors.green_3, colors.dark_green_6, text, 0, 'right', (None, 15, "bold"), 580, 80, 'e')
        description.configure(wraplength = 550)
        
        #دکمه ها
        cc.disable_all_widgets(self.super_parent)
        
        ck.make_button(notification_box, 'منوی ' + menu_name, 80, 35, (None, 15, "bold"), 60, colors.white, colors.green_3, colors.dark_green_6, colors.dark_green_2, comm, 0.34, 0.89, 'w')
        ck.make_button(notification_box, 'حذف اعلان', 80, 35, (None, 15, "bold"), 60, colors.white, colors.green_3, colors.dark_green_6, colors.dark_green_2, remove_notification, 0.15, 0.89, 'w')
        ck.make_button(notification_box, 'بستن', 80, 35, (None, 15, "bold"), 60, colors.white, colors.green_3, colors.dark_green_6, colors.dark_green_2, close_window, 0.01, 0.89, 'w')
        
        
    def show_register_notification(self):
        def register():
            insystem_data.users.append(new_user)
            reject()
            
        def reject():
            insystem_data.loged_in_user["notifications"].remove({
                "type": self.type,
                "description": self.description,
                "params": self.params,
                "date": self.date
            })
            notification_box.destroy()
            self.show_dashboard()
        
        def confirm_register():
            rc.show_confirmation_box(notification_box, register, reject, 'آیا از ثبت نام کابر، مطمئن هستید؟', None)
        def confirm_reject():
            frame = rc.show_confirmation_box(notification_box, reject, lambda: frame.destroy(), 'آیا از رد این کابر، مطمئن هستید؟', None)
        #باکس اصلی
        notification_box = ck.make_frame(self.super_parent, 600, 200, colors.green_3, colors.green_3, colors.green_3, 0, 0, 0.5, 0.5, 'center')
        new_user = self.params['user']
        text = 'نام و نام خانوادگی: ' + new_user['name'] + " " + new_user['lastname'] + '\n' + 'کد ملی: ' + cc.eng_to_persian_date(new_user['id']) + '\n' + 'شماره تماس: ' + cc.eng_to_persian_date(new_user['phone']) + '\n' + 'آدرس ایمیل: ' + new_user['email'] + '\n' + 'نام کابری: ' + new_user['username'] + '\n' + 'نقش: ' + new_user['role']
        ck.make_label(notification_box, 100, 30, colors.green_3, colors.green_3, colors.dark_green_6, text, 0, 'right', (None, 15, "bold"), 580, 80, 'e')
        
        #دکمه ها
        ck.make_button(notification_box, 'تأیید', 80, 35, (None, 15, "bold"), 60, colors.white, colors.green_3, colors.dark_green_6, colors.dark_green_2, confirm_register, 0.34, 0.89, 'center')
        ck.make_button(notification_box, 'رد', 60, 35, (None, 15, "bold"), 60, colors.white, colors.green_3, colors.dark_green_6, colors.dark_green_2, confirm_reject, 0.21, 0.89, 'center')
        ck.make_button(notification_box, 'بستن', 80, 35, (None, 15, "bold"), 60, colors.white, colors.green_3, colors.dark_green_6, colors.dark_green_2, lambda:notification_box.destroy(), 0.08, 0.89, 'center')
        
    def show_validate_notification(self):
        ck.make_frame(self.parent, 200, 100, colors.dark_green_6, colors.dark_green_6, colors.white, 0, 0, 0.5, 0.5, 'center')
        
    def __init__(self, parent, type, description, params, date, y, show_dashboard, go_to_deals_page, go_to_drivers, go_to_cars, 
                 go_to_security, go_to_licence, go_to_workcart, super_parent):
        
        self.type = type
        self.description = description
        self.params = params
        self.date = date
        self.show_dashboard = show_dashboard
        self.parent = parent
        self.go_to_deals_page = go_to_deals_page
        self.go_to_drivers = go_to_drivers
        self.go_to_cars = go_to_cars
        self.go_to_security = go_to_security
        self.go_to_licence = go_to_licence
        self.go_to_workcart = go_to_workcart
        self.super_parent = super_parent
        
        def get_lastseen_display():
            today = jdatetime.date.today().strftime('%Y/%m/%d')
            yesterday = (jdatetime.date.today() - timedelta(days=1)).strftime('%Y/%m/%d')
            if(self.date['date'] == today): return 'امروز ساعت ' + cc.eng_to_persian_date(self.date['clock'])
            elif(self.date['date'] == yesterday): return 'دیروز ساعت ' + cc.eng_to_persian_date(self.date['clock'])
            else: return cc.eng_to_persian_date(self.date['date'])
                
        def watch_notification():
            if(type == "register user"): self.show_register_notification()
            elif(type == 'credit deal'): self.notification_type('deal', 'قراردادها', lambda: self.go_to_deals_page())
            elif(type == 'credit smart cart driver'): self.notification_type('driver', 'راننده‌ها', lambda: self.go_to_drivers())
            elif(type == 'credit smart cart car'): self.notification_type('car', 'نفتکش‌ها', lambda: self.go_to_cars())
            elif(type == 'credit security'): self.notification_type('security', 'کارت ایمنی', lambda: self.go_to_security())
            elif(type == 'credit licence'): self.notification_type('licence', 'گواهینامه تأیید صلاحیت', lambda: self.go_to_licence())
            elif(type == 'credit workcart'): self.notification_type('workcart', 'کارت تردد', lambda: self.go_to_workcart())
            
        self.box = ctk.CTkFrame(parent, width=240, height=60, bg_color=colors.dark_green_6, fg_color=colors.white, corner_radius=15)
        self.box.pack(padx=5, pady=6, fill="x")

        ck.make_label(self.box, 100, 30, colors.white, colors.white, colors.dark_green_6, self.get_title(type), 0, 'center', (None, 13, 'bold'), 0.9, 0.18, 'e')
        ck.make_label(self.box, 100, 20, colors.white, colors.white, colors.dark_green_6, description, 0, 'center', (None, 8), 0.95, 0.52, 'e')
        ck.make_label(self.box, 75, 20, colors.white, colors.white, colors.dark_green_6, get_lastseen_display(), 0, 'center', (None, 8, "bold"), 0.03, 0.8, 'w')
        
        #دکمه 
        ck.make_button(self.box, 'مشاهده', 40, 17, (None, 8, "bold"), 60, colors.white, colors.white, colors.dark_green_6, colors.green_3, watch_notification, 0.85, 0.85, 'center')
        # ck.make_button(self.box, 'حذف', 40, 17, (None, 8, "bold"), 60, colors.white, colors.white, colors.dark_green_6, colors.green_3, delete_notification, 0.67, 0.85, 'center')
        