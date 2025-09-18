import customtkinter as ctk
import common_ctk as ck
import insystem_data
import bol_fake_data
import jdatetime
import common_controller as cc
from datetime import datetime
from datetime import timedelta
from asset_paths import splashPage
import colors

class SplashPage(ctk.CTkFrame):
    def __init__(self, parent, go_to_login):
        super().__init__(parent)

        self.pack(fill="both", expand=True)
        self.configure(fg_color=colors.light_green_1)
        
        # کانتینر اصلی (باکس سبز سفید)
        main_box = ctk.CTkFrame(self, width=float(self.master.winfo_screenwidth() / 1.3), 
                                height=float(self.master.winfo_screenheight() / 1.5), 
                                fg_color=colors.white,
                                corner_radius=0)
        main_box.place(relx=0.5, rely=0.5, anchor="center")

        # کانتینر اصلی (باکس سبز)
        right_box = ctk.CTkFrame(main_box, width=float(1 + self.master.winfo_screenwidth() / 2.6), 
                                height=float(main_box.winfo_screenheight() / 1.5), 
                                fg_color=colors.white,
                                corner_radius=0)
        right_box.place(relx=0.25, rely=0.5, anchor="center")

        #تصویر باکس سبز
        width = 1 + self.master.winfo_screenwidth() / 2.6
        height = self.master.winfo_screenheight() / 1.5

        box_w, box_h = int(width), int(height)
        picture_left = ctk.CTkFrame(main_box, width=box_w, height=box_h, fg_color="red", corner_radius=0)
        picture_left.place(relx=0.75, rely=0.5, anchor="center")
        
        ck.make_image(main_box, splashPage, int(box_w), int(box_h), 0.75, 0.5, "center")
        
        #عنوان صفحه
        label = ctk.CTkLabel(main_box, text="به سامانه شرکت حمل و نقل", font=(None, 40, "bold"), 
                                   text_color=colors.black, 
                                   bg_color=colors.white)
        label.place(relx=0.28, rely=0.08, anchor="center")
        label = ctk.CTkLabel(main_box, text=" درخشنده‌بار خوش آمدید...", font=(None, 40, "bold"), 
                                   text_color=colors.black, 
                                   bg_color=colors.white)
        label.place(relx=0.29, rely=0.16, anchor="center")
        
        self.loading_label = ctk.CTkLabel(main_box, text="در حال بارگذاری سامانه", font=(None, 20), 
                                   text_color=colors.black, 
                                   bg_color=colors.white)
        self.loading_label.place(relx=0.48, rely=0.3, anchor="e")
        
        self.dots_count = 0
        self.cycels = 0
        
        def update_credit_notifications():
            for driver in bol_fake_data.driver_sample_data:
                input_date = jdatetime.date.fromisoformat(driver['end_smart_date'].replace('/', '-'))
                today = jdatetime.date.today()
                diff_days = (input_date.togregorian() - today.togregorian()).days
                if 0 <= diff_days <= 4:
                    for user in insystem_data.users:
                        user['notifications'].append({
                            'type': 'credit smart cart driver',
                            'description': 'اعتبار کارت هوشمند ' + driver['name'] + ' ' + driver['lastname'] +  '، رو به اتمام است!',
                            'params': {'driver': driver},
                            'date': {'date': jdatetime.date.today().strftime('%Y/%m/%d'), 'clock': datetime.now().strftime('%H:%M')}
                        })
                if -4 < diff_days < 0:
                    for user in insystem_data.users:
                        user['notifications'].append({
                            'type': 'credit smart cart driver',
                            'description': 'اعتبار کارت هوشمند ' + driver['name'] + ' ' + driver['lastname'] +  '، تمام شده است!',
                            'params': {'driver': driver},
                            'date': {'date': jdatetime.date.today().strftime('%Y/%m/%d'), 'clock': datetime.now().strftime('%H:%M')}
                        })
            for car in bol_fake_data.car_sample_data:
                input_date = jdatetime.date.fromisoformat(car['end_date'].replace('/', '-'))
                today = jdatetime.date.today()
                diff_days = (input_date.togregorian() - today.togregorian()).days
                if 0 <= diff_days <= 4:
                    for user in insystem_data.users:
                        user['notifications'].append({
                            'type': 'credit smart cart car',
                            'description': 'اعتبار کارت هوشمند نفتکش به شماره ' + cc.car_id_true_format(car['car_id']) +  '، رو به اتمام است!',
                            'params': {'car': car},
                            'date': {'date': jdatetime.date.today().strftime('%Y/%m/%d'), 'clock': datetime.now().strftime('%H:%M')}
                        })
                if -4 < diff_days < 0:
                    for user in insystem_data.users:
                        user['notifications'].append({
                            'type': 'credit smart cart car',
                            'description': 'اعتبار کارت هوشمند نفتکش به شماره ' + cc.car_id_true_format(car['car_id']) +  '، تمام شده است!',
                            'params': {'car': car},
                            'date': {'date': jdatetime.date.today().strftime('%Y/%m/%d'), 'clock': datetime.now().strftime('%H:%M')}
                        })
            for deal in insystem_data.current_deals:
                input_date = jdatetime.date.fromisoformat(deal['end_date'].replace('/', '-'))
                today = jdatetime.date.today()
                diff_days = (input_date.togregorian() - today.togregorian()).days
                if 0 <= diff_days <= 4:
                    for user in insystem_data.users:
                        user['notifications'].append({
                            'type': 'credit deal',
                            'description': 'مدت‌زمان اعتبار قرارداد ' + deal['name'] + '/' + cc.eng_to_persian_date(deal['id']) + '، رو به اتمام است!',
                            'params': {'deal': deal},
                            'date': {'date': jdatetime.date.today().strftime('%Y/%m/%d'), 'clock': datetime.now().strftime('%H:%M')}
                        })
                if -4 < diff_days < 0:
                    for user in insystem_data.users:
                        user['notifications'].append({
                            'type': 'credit deal',
                            'description': 'مدت‌زمان اعتبار قرارداد ' + deal['name'] + '/' + cc.eng_to_persian_date(deal['id']) + '، تمام شده است!',
                            'params': {'deal': deal},
                            'date': {'date': jdatetime.date.today().strftime('%Y/%m/%d'), 'clock': datetime.now().strftime('%H:%M')}
                        })
            for workcart in bol_fake_data.workcart:
                input_date = jdatetime.date.fromisoformat(workcart['end_date'].replace('/', '-'))
                today = jdatetime.date.today()
                diff_days = (input_date.togregorian() - today.togregorian()).days
                if 0 <= diff_days <= 4:
                    for user in insystem_data.users:
                        user['notifications'].append({
                            'type': 'credit workcart',
                            'description': 'مدت‌زمان اعتبار کارت تردد ' + cc.car_id_true_format(workcart['car_id']) + '، رو به اتمام است!',
                            'params': {'workcart': workcart},
                            'date': {'date': jdatetime.date.today().strftime('%Y/%m/%d'), 'clock': datetime.now().strftime('%H:%M')}
                        })
                if -4 < diff_days < 0:
                    for user in insystem_data.users:
                        user['notifications'].append({
                            'type': 'credit workcart',
                            'description': 'مدت‌زمان اعتبار کارت تردد ' + cc.car_id_true_format(workcart['car_id']) + '، تمام شده است!',
                            'params': {'workcart': workcart},
                            'date': {'date': jdatetime.date.today().strftime('%Y/%m/%d'), 'clock': datetime.now().strftime('%H:%M')}
                        })
            for licence in bol_fake_data.car_licence:
                input_date = jdatetime.date.fromisoformat(licence['end_date'].replace('/', '-'))
                today = jdatetime.date.today()
                diff_days = (input_date.togregorian() - today.togregorian()).days
                if 0 <= diff_days <= 4:
                    for user in insystem_data.users:
                        user['notifications'].append({
                            'type': 'credit licence',
                            'description': 'مدت‌زمان اعتبار گواهی تأیید صلاحیت ' + cc.car_id_true_format(licence['car_id']) + '، رو به اتمام است!',
                            'params': {'licence': licence},
                            'date': {'date': jdatetime.date.today().strftime('%Y/%m/%d'), 'clock': datetime.now().strftime('%H:%M')}
                        })
                if -4 < diff_days < 0:
                    for user in insystem_data.users:
                        user['notifications'].append({
                            'type': 'credit licence',
                            'description': 'مدت‌زمان اعتبار گواهی تأیید صلاحیت ' + cc.car_id_true_format(licence['car_id']) + '، تمام شده است!',
                            'params': {'licence': licence},
                            'date': {'date': jdatetime.date.today().strftime('%Y/%m/%d'), 'clock': datetime.now().strftime('%H:%M')}
                        })
            
            
        def animate_loading():
            self.loading_label.configure(text="در حال بارگذاری سامانه" + "." * self.dots_count)
            self.dots_count = (self.dots_count + 1) % 4
            if(self.dots_count == 0):
                self.cycels += 1
            if(self.cycels < 5):
                self.loading_label.after(250, animate_loading)
            else:
                go_to_login()
                
        animate_loading()
        
        update_credit_notifications()