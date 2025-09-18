#main imports
import customtkinter as ctk
import tkinter as tk
import jdatetime

#module imports
from date import Date
from suggestion_list import SuggestionList

#data imports
from bol_fake_data import current_bols, old_bols, driver_sample_data, car_sample_data, station_sample_data, startpoint_sample_data, route_sample_data
from insystem_data import load_main_type, sent_type, current_deals, agents

#controllers
import common_controller as cc
import common_ctk as ck

#colors
import colors

class RegisterBol(ctk.CTkFrame):
    #Logic methods
    #تابع چک کننده پلاک ماشین
    def get_load_group_id(self):
        if(self.deal.get() != "قراردادی وجود ندارد"):
            return str(len(cc.does_item_exist(current_deals, "id", self.deal.get().split('/')[-1])["packages"]) + 1)
        return "-"
            
    def get_load_type(self, text):
        if(text == "بنزین"): return "benzin"
        if(text == "نفت سفید"): return "sefid"
        if(text == "نفت گاز"): return "gas"
        if(text == "نفت کوره"): return "koore"
        return None
        
    def car_id_format_is_right(self,s):
        error_text = "فرمت پلاک وارد شده، صحیح نمی‌باشد!"
        if len(s) != 14: return error_text
        persian_digits = '۰۱۲۳۴۵۶۷۸۹'
        digit_indexes = [0, 1, 3, 4, 5, 12, 13]
        for i in digit_indexes:
            if s[i] not in persian_digits: return error_text
        if not ('\u0600' <= s[2] <= '\u06FF' and s[2].isalpha()): return error_text
        if s[6] != '-': return error_text
        if s[7:12] != "ایران": return error_text
        return None

    #کمتر بودن مقدار حمل شده نسبت به واقعی و کمتر بودن کرایه پرداختی نسبت به پرداختی
    def out_is_less(self, input, output, is_cash):
        if(input and output):
            input = int(cc.persian_to_eng_date(input))
            output = int(cc.persian_to_eng_date(output))
            error_text = ""
            if(is_cash): error_text = "کرایه پرداختی باید کمتر از کرایه دریافتی بیشتر باشد!"
            else: error_text = "وزن حمل شده باید کمتر از وزن واقعی باشد!"
            if(input < output): return error_text
        return None
    
    #UI methods
    def check_complete_bol_inf(self):
        label = ck.make_label(self, 150, 25, 
                    colors.white, colors.white, colors.red_color,
                    "", 0, None, (None, 15), 0.565, 0.865, "ne")
        label.configure(wraplength=240, justify="right")
        flag = 0
        def show_error_border(widget, error_color, normal_color, flag, type, delay_ms=2000):
            flag += 1
            #ورودی عادی
            if(type == 0):
                widget.configure(border_color=error_color)
                widget.after(delay_ms, lambda: widget.configure(border_color=normal_color))
            #لیست
            elif(type == 1):
                widget.configure(button_color=error_color)
                widget.after(delay_ms, lambda: widget.configure(button_color=normal_color))
            #تاریخ
            elif(type == 2):
                widget.configure(border_color=error_color)
                widget.after(delay_ms, lambda: widget.configure(border_color=normal_color))
            return flag
        
        if(not self.load_id.get()): flag = show_error_border(self.load_id, colors.red_color, colors.dark_green_6, flag, 0)
        if(self.send_date.cget("text") == "تاریخ ارسال" and self.send2_date.cget("text") == "تاریخ صدور"): 
            flag = show_error_border(self.send_date, colors.red_color, colors.dark_green_6, flag, 2)
            flag = show_error_border(self.send2_date, colors.red_color, colors.dark_green_6, flag, 2)
        if(not self.driver_name.get()): flag = show_error_border(self.driver_name, colors.red_color, colors.dark_green_1, flag, 0)
        if(not self.driver_id.get()): flag = show_error_border(self.driver_id, colors.red_color, colors.dark_green_1, flag, 0)
        if(not self.smart_cart_driver.get()): flag = show_error_border(self.smart_cart_driver, colors.red_color, colors.dark_green_1, flag, 0)
        if(not self.car_owner_name.get()): flag = show_error_border(self.car_owner_name, colors.red_color, colors.green_4, flag, 0)
        if(not self.car_id.get()): flag = show_error_border(self.car_id, colors.red_color, colors.green_4, flag, 0)
        if(not self.smart_cart_car.get()): flag = show_error_border(self.smart_cart_car, colors.red_color, colors.green_4, flag, 0)
        if(not self.start_location.get()): flag = show_error_border(self.start_location, colors.red_color, colors.dark_green_6, flag, 0)
        if(not self.des_location.get()): flag = show_error_border(self.des_location, colors.red_color, colors.dark_green_6, flag, 0)
        if(not self.true_value.get()): flag = show_error_border(self.true_value, colors.red_color, colors.dark_green_6, flag, 0)
        if(not self.load_weight.get()): flag = show_error_border(self.load_weight, colors.red_color, colors.dark_green_6, flag, 0)
        deal = cc.get_deal_by_name_and_id((self.deal.get()).split('/')[0], (self.deal.get()).split('/')[1])
        if(deal['fee_company'] != '' and deal['fee_company'] != None and not self.input_money.get()): 
            flag = show_error_border(self.input_money, colors.red_color, colors.green_4, flag, 0)
        if(deal['fee_driver'] != '' and deal['fee_driver'] != None and not self.payed_money.get()): 
            flag = show_error_border(self.payed_money, colors.red_color, colors.green_4, flag, 0)
        if(not flag): 
            
            #ارور های لیبل دار
            if(self.cash_id.get() and cc.does_item_exist(current_bols + old_bols, "cash_id", self.cash_id.get())): 
                ck.show_error(self.cash_id, colors.dark_green_6, 2000)
                ck.update_label_error(label, 2000, "حواله با این شماره، قبلا ثبت شده است!")
            elif(cc.does_item_exist(current_bols + old_bols, "load_id", self.load_id.get())): 
                ck.show_error(self.load_id, colors.dark_green_6, 2000)
                ck.update_label_error(label, 2000, "بارنامه با این شماره، قبلا ثبت شده است!")
            elif(not cc.car_id_format_is_right(self.car_id.get())): 
                ck.show_error(self.car_id, colors.green_4, 2000)
                ck.update_label_error(label, 2000, "پلاک وارد شده، صحیح نمی‌باشد!(توجه داشته باشید پلاک بدون فاصله وارد شود)")
            elif(self.out_is_less(self.input_money.get(), self.payed_money.get(), 1)): 
                ck.show_error(self.input_money, colors.green_4, 2000)
                ck.show_error(self.payed_money, colors.green_4, 2000)
                ck.update_label_error(label, 2000, "کرایه پرداختی باید کمتر از کرایه دریافتی باشد!")
            elif(self.out_is_less(self.true_value.get(), self.load_weight.get(), 1)): 
                ck.show_error(self.true_value, colors.dark_green_6, 2000)
                ck.show_error(self.load_weight, colors.dark_green_6, 2000)
                ck.update_label_error(label, 2000, "وزن محموله باید کمتر از وزن حقیقی باشد!")
            else:
                self.show_register_confirm()
         
    def show_register_bol_page(self):
        for child in self.winfo_children():
            child.destroy()
        self.register_bol_page = RegisterBol(self, 
                                             go_to_dashboard=self.go_to_dashboard, 
                                             go_to_veiw_bol=self.go_to_veiw_bol)
        self.register_bol_page.pack(fill="both", expand=True)
    def reset_page(self):
        self.show_register_bol_page()
    def toggle_mode(self, label, is_input, live_label):
        if is_input.get(): 
            label.configure(text="رنگی")
            live_label.set("دسته اصلی: رنگی")
        else: 
            label.configure(text="نفت کوره")
            live_label.set("دسته اصلی: نفت کوره")
    def show_register_confirm(self):
        dialog = ctk.CTkFrame(self, width=self.winfo_screenwidth() / 4.5, 
                              height=self.winfo_screenheight() / 8, 
                              fg_color=colors.light_green_1)
        dialog.place(relx=0.5, rely=0.5, anchor="center") 
        lbl = ctk.CTkLabel(dialog, 
                           text="آیا از صحت اطلاعات وارد شده، اطمینان دارید؟...", 
                           font=(None, 16),
                           text_color=colors.black)
        lbl.place(relx=0.5, rely=0.2, anchor="center")
        def do_register():
            new_bol = {"id": len(current_bols) + 1,
                         "today_date":cc.eng_to_persian_date(self.today_date.cget("text")),
                         "deal":cc.eng_to_persian_date(self.deal.get()),
                         "cash_id":cc.eng_to_persian_date(self.cash_id.get()),
                         "load_id":cc.eng_to_persian_date(self.load_id.get()),
                         "load_group_id":cc.eng_to_persian_date(self.load_group_id.get()),
                         "agent":cc.eng_to_persian_date(self.agent.get()),
                         "agent_group_id":cc.eng_to_persian_date(self.agent_group_id.get()),
                         "send_date":cc.eng_to_persian_date(self.send_date.cget("text")),
                         "send2_date":cc.eng_to_persian_date(self.send2_date.cget("text")),
                         "driver_name":cc.eng_to_persian_date(self.driver_name.get()),
                         "driver_id":cc.eng_to_persian_date(self.driver_id.get()),
                         "smart_cart_driver":cc.eng_to_persian_date(self.smart_cart_driver.get()),
                         "car_owner_name":cc.eng_to_persian_date(self.car_owner_name.get()),
                         "car_id":cc.eng_to_persian_date(self.car_id.get()),
                         "smart_cart_car":cc.eng_to_persian_date(self.smart_cart_car.get()),
                         "start_location":cc.eng_to_persian_date(self.start_location.get()),
                         "des_location":cc.eng_to_persian_date(self.des_location.get()),
                         "true_value":cc.persian_to_eng_date(self.true_value.get()),
                         "load_weight":cc.persian_to_eng_date(self.load_weight.get()),
                         "main_type":cc.eng_to_persian_date(self.main_type.get()),
                         "load_name":cc.eng_to_persian_date(self.load_name.get()),
                         "sent_type":cc.eng_to_persian_date(self.sent_type.get()),
                         "input_money":cc.persian_to_eng_date(self.input_money.get()),
                         "payed_money":cc.persian_to_eng_date(self.payed_money.get())}
            current_bols.append(new_bol)
            self.go_to_veiw_bol()
            dialog.destroy()
            
        def cancel(): 
            cc.activate_all_widgets(self)
            dialog.destroy()

        cc.disable_all_widgets(self)
        # دو تا دکمه بله و خیر
        btn_yes = ctk.CTkButton(dialog, text="بله", width=70, command=do_register, fg_color=colors.dark_green_5, hover_color=colors.green_3)
        btn_no = ctk.CTkButton(dialog, text="خیر", width=70, command=cancel, fg_color=colors.dark_green_5, hover_color=colors.green_3)
        btn_yes.place(relx=0.35, rely=0.8, anchor="center")
        btn_no.place(relx=0.65, rely=0.8, anchor="center")
        
    def __init__(self, parent,go_to_dashboard,go_to_veiw_bol):
        super().__init__(parent)

        self.go_to_dashboard = go_to_dashboard
        self.go_to_veiw_bol = go_to_veiw_bol
        
        deals_list = [(item["name"] + "/" + cc.eng_to_persian_date(item["id"])) for item in current_deals]
        
        def update_live_information(entry, entry_live, title_text, box, x_co, y_co):
            entry.bind("<KeyRelease>", lambda event: update_label_on_key_release(text=title_text, source_widget=entry, source_widget_live=entry_live, event=event))
            entry.bind("<FocusOut>", lambda event: update_label_on_key_release(text=title_text, source_widget=entry, source_widget_live=entry_live, event=event))
            label = ctk.CTkLabel(box, textvariable=entry_live, font=(None, 15), text_color=colors.dark_green_6, bg_color=colors.white)
            label.place(relx=x_co, rely=y_co, anchor="e")
            
        def update_live_information_3digit(entry, entry_live, title_text, box, x_co, y_co):
            entry.bind("<KeyRelease>", lambda event: update_label_on_key_release_3digit(text=title_text, source_widget=entry, source_widget_live=entry_live, event=event))
            entry.bind("<FocusOut>", lambda event: update_label_on_key_release_3digit(text=title_text, source_widget=entry, source_widget_live=entry_live, event=event))
            label = ctk.CTkLabel(box, textvariable=entry_live, font=(None, 15), text_color=colors.dark_green_6, bg_color=colors.white)
            label.place(relx=x_co, rely=y_co, anchor="e")
                  
        def open_calendar(box, entry, x_co, y_co, entry_live, text):
            global calendar_frame
            try: calendar_frame.destroy()
            except: pass
            calendar_frame = tk.Frame(box, bd=2, relief=tk.RIDGE,
                                      bg=colors.light_green_1)
            calendar_frame.place(relx=x_co, rely=y_co, anchor="center")
            def on_date_selected(selected_date):
                entry.configure(text=cc.eng_to_persian_date(str(selected_date).replace("-", "/")), text_color=colors.black)  
                entry_live.set(text + " " + cc.eng_to_persian_date(str(selected_date).replace("-", "/")))
                calendar_frame.destroy()

            cal = Date(calendar_frame, callback=on_date_selected)
            cal.pack()

            close_btn = ctk.CTkButton(calendar_frame, text="بستن", 
                                      width=100,
                                      bg_color=colors.light_green_1, 
                                fg_color=colors.dark_green_6,
                                text_color=colors.light_green_1,
                                hover_color=colors.green_3,
                                command=calendar_frame.destroy)
            close_btn.pack(pady=4)

        self.go_to_veiw_bol = go_to_veiw_bol
        self.pack(fill="both", expand=True)
        self.configure(fg_color=colors.light_green_1)
        
        load_name_live = ctk.StringVar(value="نام فرآورده: " + load_main_type[0]["sub_array"][0])
        main_type_live = ctk.StringVar(value="دسته اصلی: " + load_main_type[0]["name"])
        today_date_live = ctk.StringVar(value="تاریخ ثبت: " + cc.eng_to_persian_date(jdatetime.date.today().strftime('%Y/%m/%d')))
        send_date_live = ctk.StringVar(value="تاریخ ارسال: -")
        send2_date_live = ctk.StringVar(value="تاریخ صدور: -")
        start_location_live = ctk.StringVar(value="مبدأ: -")
        agent_live = ctk.StringVar(value="نماینده: " + agents[0])
        cash_id_live = ctk.StringVar(value="شماره حواله: -")
        agent_group_id_live = ctk.StringVar(value="شماره صورت نماینده: -")
        load_group_id_live = ctk.StringVar(value="شماره صورت بارنامه: -")
        deal_live = ctk.StringVar(value="قرارداد: " + deals_list[0] if deals_list else "-")
        load_id_live = ctk.StringVar(value="شماره بارنامه: -")
        des_location_live = ctk.StringVar(value="مقصد: -")
        car_id_live = ctk.StringVar(value="شماره نفتکش: -")
        driver_name_live = ctk.StringVar(value="نام راننده: -")
        driver_id_live = ctk.StringVar(value="کد ملی راننده: -")
        car_owner_name_live = ctk.StringVar(value="نام مالک: -")
        sent_type_live = ctk.StringVar(value="نوع ارسال: " + sent_type[0])
        true_value_live = ctk.StringVar(value="مقدار طبیعی: -")
        load_weight_live = ctk.StringVar(value="وزن محموله: -")
        smart_cart_driver_live = ctk.StringVar(value="شماره کارت هوشمند راننده: -")
        smart_cart_car_live = ctk.StringVar(value="شماره کارت هوشمند نفتکش: -")
        input_money_live = ctk.StringVar(value="کرایه دریافتی: -")
        payed_money_live = ctk.StringVar(value="کرایه پرداختی: -")
        
        def update_label_on_key_release_3digit(text, source_widget, source_widget_live, event=None):
            if(source_widget.get()): flag = source_widget_live.set(text + " " + cc.eng_to_persian_date(cc.cash_format(source_widget.get())))
            else: source_widget_live.set(text + " -")
        
        def update_label_on_key_release(text, source_widget, source_widget_live, event=None):
            if(self.start_location.get()): 
                target_route = cc.does_item_exist(route_sample_data, 'id', self.start_location.get())
                if(target_route and target_route['id'] != 'فاقد کد'): 
                    self.start_location.delete(0, 'end')
                    self.start_location.insert(0, target_route['start'])
                    self.des_location.delete(0, 'end')
                    self.des_location.insert(0, target_route['end'])
                    start_location_live.set('مبدأ: ' + self.start_location.get())
                    des_location_live.set('مقصد: ' + self.des_location.get())
            if(self.car_id.get()):
                   target_car = cc.does_item_exist(car_sample_data, 'car_id', self.car_id.get())  
                   if(target_car): 
                       #مشخصات ماشین
                        self.car_owner_name.delete(0, 'end')
                        self.car_owner_name.insert(0, target_car['owner_name'])
                        car_owner_name_live.set('نام مالک: ' + self.car_owner_name.get())
                        self.smart_cart_car.delete(0, 'end')
                        self.smart_cart_car.insert(0, target_car['smart_car_id'])
                        smart_cart_car_live.set('شماره کارت هوشمند نفتکش: ' + self.smart_cart_car.get())
                        if(self.get_load_type(self.load_name.get()) != None):
                            self.true_value.delete(0, 'end')
                            self.true_value.insert(0, cc.eng_to_persian_date(target_car[self.get_load_type(self.load_name.get())]))
                            true_value_live.set('مقدار طبیعی: ' + self.true_value.get())
                        
                        #مشخصات راننده
                        if(len(target_car['driver_name']) == 1): 
                            target_driver = cc.get_driver_by_fullname(target_car['driver_name'][0])
                            self.driver_name.delete(0, 'end')
                            self.driver_name.insert(0, target_driver['name'] + " " + target_driver['lastname'])
                            driver_name_live.set('نام راننده: ' + self.driver_name.get())
                            self.driver_id.delete(0, 'end')
                            self.driver_id.insert(0, cc.eng_to_persian_date(target_driver['id']))
                            driver_id_live.set('کد ملی راننده: ' + cc.eng_to_persian_date(self.driver_id.get()))
                            self.smart_cart_driver.delete(0, 'end')
                            self.smart_cart_driver.insert(0, cc.eng_to_persian_date(target_driver['smart_id']))
                            smart_cart_driver_live.set('شماره کارت هوشمند راننده: ' + cc.eng_to_persian_date(self.smart_cart_driver.get()))
                        
                        #مشخصات کرایه
                        a = self.deal.get().split('/')
                        main_deal = cc.get_deal_by_name_and_id(a[0], a[1])
                        if(main_deal['fee_company'] and self.true_value.get() != None and self.true_value.get() != ''): 
                            self.input_money.delete(0, 'end')
                            self.input_money.insert(0, cc.eng_to_persian_date(str(int(cc.persian_to_eng_date(self.true_value.get())) * int(cc.persian_to_eng_date(main_deal['fee_company'])))))
                            input_money_live.set('کرایه دریافتی: ' + cc.cash_format(self.input_money.get()))
                        if(main_deal['fee_driver'] and self.true_value.get() != None and self.true_value.get() != ''):  
                            self.payed_money.delete(0, 'end')
                            self.payed_money.insert(0, cc.eng_to_persian_date(str(int(cc.persian_to_eng_date(self.true_value.get())) * int(cc.persian_to_eng_date(main_deal['fee_driver'])))))
                            payed_money_live.set('کرایه پرداختی: ' + cc.cash_format(self.payed_money.get()))
            if(cc.does_item_exist(driver_sample_data, 'id', self.driver_id.get())):
                target_driver = cc.does_item_exist(driver_sample_data, 'id', self.driver_id.get())
                self.driver_name.delete(0, 'end')
                self.driver_name.insert(0, target_driver['name'] + " " + target_driver['lastname'])   
                driver_name_live.set('نام راننده: ' + (self.driver_name.get()))
                self.smart_cart_driver.delete(0, 'end')
                self.smart_cart_driver.insert(0, target_driver['smart_id'])    
                smart_cart_driver_live.set('شماره کارت هوشمند راننده: ' + (self.smart_cart_driver.get()))
                        
            if(source_widget.get()): flag = source_widget_live.set(text + " " + cc.eng_to_persian_date(source_widget.get()))
            else: source_widget_live.set(text + " -")
            
        #کانتنر اصلی بک‌گراند
        main_box = ctk.CTkFrame(self, width=float(self.master.winfo_screenwidth()), 
                                height=float(self.master.winfo_screenheight()), 
                                fg_color=colors.light_green_1,
                                corner_radius=0)
        main_box.place(relx=0.5, rely=0.5, anchor="center")
        
        #ابعاد صفحه اصلی
        screen_width=float(main_box.winfo_screenwidth())
        screen_height=float(main_box.winfo_screenheight())
        margin_radius = 60
        corners_right_x = (0.3 * screen_width - (margin_radius / 2))
        corners_left_x = (margin_radius / 2)
        corners_down_y = (0.3 * screen_height - (margin_radius / 2))
        corners_up_y = (margin_radius / 2)
        
        #کرنر های باکس متصل کننده
        #بالا چپ 
        my_canvas = ctk.CTkCanvas(main_box, width=margin_radius/2, height=margin_radius/2, bg=colors.dark_green_6,highlightthickness=0)
        my_canvas.place(x=1092.5, y=212.2, anchor="center")
        my_canvas.create_oval(-margin_radius/2,0 , margin_radius/2, margin_radius, fill=colors.light_green_1, outline="")
        
        #پایین چپ 
        my_canvas = ctk.CTkCanvas(main_box, width=margin_radius/2, height=margin_radius/2, bg=colors.dark_green_6,highlightthickness=0)
        my_canvas.place(x=1092.5, y=255, anchor="center")
        my_canvas.create_oval(-margin_radius/2, -margin_radius/2 , margin_radius/2, margin_radius/2, fill=colors.light_green_1, outline="")
        
        #اضافه کردن آپشن های صفحه اصلی(مستطیل ها)        
        #مستطیل بالایی
        top_box = ctk.CTkFrame(main_box, width=float(0.34 * screen_width), 
                                height=float(0.1 * screen_height), 
                                bg_color=colors.light_green_1,
                                fg_color=colors.dark_green_6,
                                corner_radius=60)
        top_box.place(relx=0.701, rely=0.17, anchor="center")
        
        #مستطیل متصل کننده
        middle_box = ctk.CTkFrame(main_box, width=float(0.1 * screen_width), 
                                height=float(0.2 * screen_height), 
                                bg_color=colors.dark_green_6,
                                fg_color=colors.dark_green_6)
        middle_box.place(relx=0.8195, rely=0.27, anchor="center")
        
        #مستطیل چهارم سفید
        white_box = ctk.CTkFrame(main_box, width=float(0.3 * screen_width), 
                                height=float(0.55 * screen_height), 
                                fg_color=colors.white,
                                corner_radius=60)
        white_box.place(relx=0.25, rely=0.573, anchor="center")
        
        #مستطیل چهارم سفید - بخش نتایج
        white_box_result = ctk.CTkFrame(white_box, width=float(0.3 * screen_width), 
                                height=float(0.3 * screen_height), 
                                bg_color=colors.white,
                                fg_color=colors.green_4,
                                corner_radius=60)
        white_box_result.place(relx=0.5, rely=0.73, anchor="center")
        
        #بالا راست باکس چهارم
        my_canvas = ctk.CTkCanvas(white_box, width=margin_radius, height=margin_radius, bg=colors.green_4,highlightthickness=0)
        my_canvas.place(x=172, y=196, anchor="center")
        my_canvas.create_oval(-margin_radius, -margin_radius, margin_radius, margin_radius, fill=colors.white, outline="")
        
        #پایین چپ باکس چهارم
        my_canvas = ctk.CTkCanvas(white_box_result, width=margin_radius, height=margin_radius, bg=colors.light_green_1,highlightthickness=0)
        my_canvas.place(x=corners_left_x, y=corners_down_y, anchor="center")
        my_canvas.create_oval(0, -margin_radius, 2*margin_radius, margin_radius, fill=colors.green_4, outline="")
        
        #مستطیل سوم سبز روشن تر
        third_box = ctk.CTkFrame(main_box, width=float(0.3 * screen_width), 
                                height=float(0.55 * screen_height), 
                                bg_color=colors.white,
                                fg_color=colors.green_4,
                                corner_radius=60)
        third_box.place(relx=0.39, rely=0.573, anchor="center")
        
        #مستطیل سوم سبز رنگ - بخش نتایج
        third_box_result = ctk.CTkFrame(third_box, width=float(0.3 * screen_width), 
                                height=float(0.3 * screen_height), 
                                bg_color=colors.green_4,
                                fg_color=colors.dark_green_1,
                                corner_radius=60)
        third_box_result.place(relx=0.5, rely=0.73, anchor="center")
        
        #بالا راست باکس سوم
        my_canvas = ctk.CTkCanvas(third_box, width=margin_radius, height=margin_radius, bg=colors.dark_green_1,highlightthickness=0)
        my_canvas.place(x=200, y=196, anchor="center")
        my_canvas.create_oval(-margin_radius, -margin_radius, margin_radius, margin_radius, fill=colors.green_4, outline="")
        
        #پایین چپ باکس سوم
        my_canvas = ctk.CTkCanvas(third_box_result, width=margin_radius, height=margin_radius, bg=colors.green_4,highlightthickness=0)
        my_canvas.place(x=corners_left_x, y=corners_down_y, anchor="center")
        my_canvas.create_oval(0, -margin_radius, 2*margin_radius, margin_radius, fill=colors.dark_green_1, outline="")
        
        #مستطیل دوم سبز روشن تر
        second_box = ctk.CTkFrame(main_box, width=float(0.3 * screen_width), 
                                height=float(0.55 * screen_height), 
                                bg_color=colors.green_4,
                                fg_color=colors.dark_green_1,
                                corner_radius=60)
        second_box.place(relx=0.55, rely=0.573, anchor="center")
        
        #مستطیل دوم سبز رنگ - بخش نتایج
        second_box_result = ctk.CTkFrame(second_box, width=float(0.3 * screen_width), 
                                height=float(10 + 0.3 * screen_height), 
                                bg_color=colors.dark_green_1,
                                fg_color=colors.dark_green_6,
                                corner_radius=60)
        second_box_result.place(relx=0.5, rely=0.73, anchor="center")

        #بالا راست باکس دوم
        my_canvas = ctk.CTkCanvas(second_box, width=margin_radius, height=margin_radius, bg=colors.dark_green_6,highlightthickness=0)
        my_canvas.place(x=214, y=191, anchor="center")
        my_canvas.create_oval(-margin_radius, -margin_radius, margin_radius, margin_radius, fill=colors.dark_green_1, outline="")
        
        #پایین چپ باکس دوم
        my_canvas = ctk.CTkCanvas(second_box_result, width=margin_radius, height=margin_radius, bg=colors.dark_green_1,highlightthickness=0)
        my_canvas.place(x=corners_left_x, y=corners_down_y+5, anchor="center")
        my_canvas.create_oval(0, -margin_radius, 2*margin_radius, margin_radius, fill=colors.dark_green_6, outline="")
        
        #مستطیل اصلی سبز رنگ
        first_box = ctk.CTkFrame(main_box, width=float(0.3 * screen_width), 
                                height=float(0.55 * screen_height), 
                                bg_color=colors.dark_green_1,
                                fg_color=colors.dark_green_6,
                                corner_radius=60)
        first_box.place(relx=0.7193, rely=0.573, anchor="center")
        
        #باکس سفید  پایین
        buttom_white_box_result = ctk.CTkFrame(main_box, width=float(0.47 * screen_width), 
                                height=float(0.2 * screen_height), 
                                bg_color=colors.white,
                                fg_color=colors.white,
                                corner_radius=60)
        buttom_white_box_result.place(relx=0.635, rely=0.86, anchor="center")
        
        #بالا چپ باکس سفید پایین
        my_canvas = ctk.CTkCanvas(buttom_white_box_result, width=margin_radius, height=margin_radius, bg=colors.dark_green_6,highlightthickness=0)
        my_canvas.place(x=corners_left_x, y=corners_up_y, anchor="center")
        my_canvas.create_oval(0, 0, 2*margin_radius, 2*margin_radius, fill=colors.white, outline="")
        
        #پایین چپ باکس سفید پایین
        my_canvas = ctk.CTkCanvas(buttom_white_box_result, width=margin_radius, height=margin_radius, bg=colors.light_green_1,highlightthickness=0)
        my_canvas.place(x=corners_left_x, y=150, anchor="center")
        my_canvas.create_oval(0, -margin_radius, 2*margin_radius, margin_radius, fill=colors.white, outline="")
        #پایین راست باکس سفید پایین
        my_canvas = ctk.CTkCanvas(buttom_white_box_result, width=margin_radius, height=margin_radius, bg=colors.light_green_1,highlightthickness=0)
        my_canvas.place(relx=float(((0.77 * screen_width) - (margin_radius/2) - 18) / ((0.77 * screen_width))), y=150, anchor="center")
        my_canvas.create_oval(-margin_radius, -margin_radius, margin_radius, margin_radius, fill=colors.white, outline="")
        
        # #بالا راست
        # my_canvas = ctk.CTkCanvas(main_box, width=margin_radius/2, height=margin_radius/2, bg=colors.white_color,highlightthickness=0)
        # my_canvas.place(x=806, y=669, anchor="center")
        # my_canvas.create_oval(-margin_radius/2, -margin_radius/2 , margin_radius/2, margin_radius/2, fill=colors.dark_green_color, outline="")
        
        #مستطیل اصلی سبز رنگ - بخش نتایج
        first_box_result = ctk.CTkFrame(main_box, width=float(0.3 * screen_width), 
                                height=float(0.3 * screen_height), 
                                bg_color=colors.dark_green_6,
                                fg_color=colors.white,
                                corner_radius=60)
        first_box_result.place(relx=0.72, rely=0.7, anchor="center")
        
        #بالا راست باکس اول
        my_canvas = ctk.CTkCanvas(first_box, width=margin_radius, height=margin_radius, bg=colors.white,highlightthickness=0)
        my_canvas.place(x=corners_right_x, y=196, anchor="center")
        my_canvas.create_oval(-margin_radius, -margin_radius, margin_radius, margin_radius, fill=colors.dark_green_6, outline="")
        my_canvas = ctk.CTkCanvas(first_box_result, width=margin_radius, height=margin_radius, bg=colors.white,highlightthickness=0)
        my_canvas.place(x=corners_right_x, y=corners_up_y, anchor="center")
        my_canvas.create_oval(-margin_radius, -margin_radius, margin_radius, margin_radius, fill=colors.white, outline="")
        
        #پایین راست باکس اول
        my_canvas = ctk.CTkCanvas(first_box_result, width=margin_radius, height=margin_radius, bg=colors.white,highlightthickness=0)
        my_canvas.place(x=corners_right_x, y=corners_down_y, anchor="center")
        my_canvas.create_oval(-margin_radius, -margin_radius, margin_radius, margin_radius, fill=colors.white, outline="")
        
        #پایین چپ باکس اول
        my_canvas = ctk.CTkCanvas(first_box_result, width=margin_radius, height=margin_radius, bg=colors.white,highlightthickness=0)
        my_canvas.place(x=corners_left_x, y=corners_down_y+1, anchor="center")
        my_canvas.create_oval(0, -margin_radius, 2*margin_radius, margin_radius, fill=colors.white, outline="")
        
        #باکس پر کننده بالا راست قسمت اول
        tmp_box = ctk.CTkFrame(main_box, width=float(0.05 * screen_width), 
                                height=float(0.1 * screen_height), 
                                bg_color=colors.dark_green_6,
                                fg_color=colors.dark_green_6)
        tmp_box.place(relx=0.8445, rely=0.294, anchor="center")
        tmp_box = ctk.CTkFrame(main_box, width=5, 
                                height=float(0.1 * screen_height), 
                                bg_color=colors.dark_green_6,
                                fg_color=colors.dark_green_6)
        tmp_box.place(relx=0.867, rely=0.32, anchor="center")
        
        #عنوان صفحه
        label = ctk.CTkLabel(main_box, text="صفحه ثبت بارنامه", font=(None, 50, "bold"), 
                                   text_color=colors.white, 
                                   bg_color=colors.dark_green_6)
        label.place(relx=0.71, rely=0.17, anchor="center")
        
        #عنوان باکس قرارداد
        label = ctk.CTkLabel(main_box, text="مشخصات قرارداد", font=(None, 25, "bold"), 
                                   text_color=colors.white, 
                                   bg_color=colors.dark_green_6,
                                   justify="right")
        label.place(relx=0.78, rely=0.323, anchor="center")
        
        #عنوان باکس راننده
        label = ctk.CTkLabel(main_box, text="اطلاعات راننده", font=(None, 25, "bold"), 
                                   text_color=colors.white, 
                                   bg_color=colors.dark_green_1,
                                   justify="right")
        label.place(relx=0.51, rely=0.323, anchor="center")
        
        #عنوان باکس نفتکش
        label = ctk.CTkLabel(main_box, text="اطلاعات نفتکش", font=(None, 25, "bold"), 
                                   text_color=colors.dark_green_6, 
                                   bg_color=colors.green_4,
                                   justify="right")
        label.place(relx=0.337, rely=0.323, anchor="center")
        
        #عنوان باکس هزینه ها
        label = ctk.CTkLabel(main_box, text="هزینه ها", font=(None, 25, "bold"), 
                                   text_color=colors.dark_green_6, 
                                   bg_color=colors.green_4,
                                   justify="right")
        label.place(relx=0.2, rely=0.59, anchor="center")
        
        #عنوان باکس فرآورده
        label = ctk.CTkLabel(main_box, text="مشخصات فرآورده", font=(None, 25, "bold"), 
                                   text_color=colors.white, 
                                   bg_color=colors.dark_green_1,
                                   justify="right")
        label.place(relx=0.327, rely=0.59, anchor="center")
        
        #عنوان باکس جزئیات بار
        label = ctk.CTkLabel(main_box, text="جزئیات بار", font=(None, 25, "bold"), 
                                   text_color=colors.white, 
                                   bg_color=colors.dark_green_6,
                                   justify="right")
        label.place(relx=0.525, rely=0.59, anchor="center")
        
        #خط های باکس گزارش
        #خط افقی نصفه بالا
        circle_canvas = ctk.CTkCanvas(first_box_result, width=float(0.15*first_box_result.winfo_screenwidth()), height=2, bg=colors.dark_green_6, highlightthickness=0)
        circle_canvas.place(relx=0.175, rely=0.35, anchor="center")
        
        #خط عمودی نصفه بالا
        circle_canvas = ctk.CTkCanvas(first_box_result, height=float(0.135*buttom_white_box_result.winfo_screenwidth() / 3.05), width=2, bg=colors.dark_green_6, highlightthickness=0)
        circle_canvas.place(relx=0.4245, rely=0.347)
        
        #خط افقی اول
        circle_canvas = ctk.CTkCanvas(first_box_result, width=float(first_box_result.winfo_screenwidth()), height=2, bg=colors.dark_green_6, highlightthickness=0)
        circle_canvas.place(relx=0.5, rely=0.59, anchor="center")
        
        #خط افقی دوم
        circle_canvas = ctk.CTkCanvas(first_box_result, width=float(first_box_result.winfo_screenwidth()), height=2, bg=colors.dark_green_6, highlightthickness=0)
        circle_canvas.place(relx=0.5, rely=0.8, anchor="center")
        
        #خط افقی سوم
        circle_canvas = ctk.CTkCanvas(buttom_white_box_result, width=float(first_box_result.winfo_screenwidth()), height=2, bg=colors.dark_green_6, highlightthickness=0)
        circle_canvas.place(relx=0.5, rely=0.5, anchor="center")
        
        #خط عمودی اول
        circle_canvas = ctk.CTkCanvas(buttom_white_box_result, height=float(buttom_white_box_result.winfo_screenwidth() / 3.05), width=2, bg=colors.dark_green_6, highlightthickness=0)
        circle_canvas.place(relx=0.359, rely=0)
        
        #ورودی ها و تکمیل اطلاعات
        def update_second_list_options(selected_value):
            self.main_type.configure(text_color=colors.black)
            values = [item["sub_array"] for item in load_main_type if item["name"] == selected_value][0]
            self.load_name.configure(values = values)
            self.load_name.configure(variable=ctk.StringVar(value=values[0]))
            main_type_live.set("دسته اصلی: " + selected_value)
            load_name_live.set("نام فرآورده: " + values[0])
        
        def update_agent(selected_value):
            self.agent.configure(text_color=colors.black)
            agent_live.set("نماینده: " + selected_value)
            
        def update_deal(selected_value):
            self.deal.configure(text_color=colors.black)
            deal_live.set("قرارداد: " + selected_value)
            
        def update_load_name(selected_value):
            self.load_name.configure(text_color=colors.black)
            load_name_live.set("نام فرآورده: " + selected_value)
            
        def update_sent_type(selected_value):
            self.sent_type.configure(text_color=colors.black)
            sent_type_live.set("نوع ارسال: " + selected_value)
            
        #تاریخ ثبت
        self.today_date = ck.make_button(first_box, cc.eng_to_persian_date(jdatetime.date.today().strftime('%Y/%m/%d')),
                                         160, 34, None, 60, colors.black, colors.dark_green_6, colors.light_gray_4,
                                         colors.green_3, lambda:open_calendar(main_box, self.today_date, 0.5, 0.5, today_date_live, "تاریخ ثبت:"), 
                                         0.26, 0.06, "center")
        update_live_information(self.today_date, today_date_live, "تاریخ ثبت:", first_box_result, 0.4, 0.08)
        
        #قرارداد    
        self.deal = ck.make_list(first_box, deals_list[0] if deals_list else "قراردادی وجود ندارد", deals_list, 180, 30, colors.black, colors.dark_green_6, 
                                  colors.light_gray_4, colors.green_2, colors.dark_green_3, 60, update_deal, "e", 0.73, 0.145, "center")
        self.deal.configure(font=(None, 10))
        update_live_information(self.deal, deal_live, "قرارداد:", first_box_result, 0.95, 0.06)
        
        #شماره حواله
        self.cash_id = ck.make_entry(first_box, 185, 36, colors.dark_green_6, colors.light_gray_4, colors.dark_green_6, colors.black,
                                         "شماره حواله", None, 60, "right", None, 0.28, 0.145, "center")
        update_live_information(self.cash_id, cash_id_live, "شماره حواله:", first_box_result, 0.95, 0.15)
        
        #شماره بارنامه
        self.load_id = ck.make_entry(first_box, 185, 36, colors.dark_green_6, colors.light_gray_4, colors.dark_green_6, colors.black,
                                         "شماره بارنامه", None, 60, "right", None, 0.73, 0.23, "center")
        update_live_information(self.load_id, load_id_live, "شماره بارنامه:", first_box_result, 0.95, 0.24)
        
        #شماره صورت بارنامه
        self.load_group_id = ck.make_entry(first_box, 185, 36, colors.dark_green_6, colors.light_gray_4, colors.dark_green_6, colors.black,
                                         "شماره صورت بارنامه", None, 60, "right", None, 0.28, 0.23, "center")
        update_live_information(self.load_group_id, load_group_id_live, "شماره صورت بارنامه:", first_box_result, 0.95, 0.33)
        
        #نماینده
        self.agent = ck.make_list(first_box, agents[0], agents, 180, 30, colors.black, colors.dark_green_6, 
                                  colors.light_gray_4, colors.green_2, colors.dark_green_3, 60, update_agent, "e", 0.73, 0.315, "center")
        update_live_information(self.agent, agent_live, "نماینده:", first_box_result, 0.95, 0.42)
        
        # شماره صورت نماینده
        self.agent_group_id = ck.make_entry(first_box, 185, 36, colors.dark_green_6, colors.light_gray_4, colors.dark_green_6, colors.black,
                                         "شماره صورت نماینده", None, 60, "right", None, 0.28, 0.315, "center")
        update_live_information(self.agent_group_id, agent_group_id_live, "شماره صورت نماینده:", first_box_result, 0.95, 0.51)
        
        #تاریخ ارسال
        self.send_date = ck.make_button(first_box, "تاریخ ارسال", 185, 34, None, 60, colors.gray_1, colors.dark_green_6, 
                                         colors.light_gray_4, colors.green_3, 
                                         lambda:open_calendar(main_box, self.send_date, 0.5, 0.5, send_date_live, "تاریخ ارسال:"),
                                         0.73, 0.4, "center")
        self.send_date.configure(border_width=2, border_color=colors.dark_green_6)
        update_live_information(self.send_date, send_date_live, "تاریخ ارسال:", first_box_result, 0.4, 0.18)
        
        #تاریخ صدور
        self.send2_date = ck.make_button(first_box, "تاریخ صدور", 185, 34, None, 60, colors.gray_1, colors.dark_green_6, 
                                         colors.light_gray_4, colors.green_3, 
                                         lambda:open_calendar(main_box, self.send2_date, 0.5, 0.5, send2_date_live, "تاریخ صدور:"),
                                         0.28, 0.4, "center")
        self.send2_date.configure(border_width=2, border_color=colors.dark_green_6)
        update_live_information(self.send2_date, send2_date_live, "تاریخ صدور:", first_box_result, 0.4, 0.28)
        
        #نام راننده
        self.driver_name = ck.make_entry(second_box, 230, 36, colors.dark_green_1, colors.light_gray_4, colors.dark_green_1, colors.black, 
                                         "نام راننده", None, 60, "right", None, 0.285, 0.14, "center")
        update_live_information(self.driver_name, driver_name_live, "نام راننده:", first_box_result, 0.95, 0.65)   
        
        
        
        #شماره کارت هوشمند راننده
        self.smart_cart_driver = ck.make_entry(second_box, 230, 36, colors.dark_green_1, colors.light_gray_4, colors.dark_green_1, colors.black, 
                                         "شماره کارت هوشمند راننده", None, 60, "right", None, 0.285, 0.31, "center")
        update_live_information(self.smart_cart_driver, smart_cart_driver_live, "شماره کارت هوشمند راننده:", first_box_result, 0.95, 0.74)
        
        # #نام مالک خودرو
        self.car_owner_name = ck.make_entry(third_box, 210, 36, colors.green_4, colors.light_gray_4, colors.green_4, colors.black,
                                         "نام مالک", None, 60, "right", None, 0.275, 0.14, "center")
        update_live_information(self.car_owner_name, car_owner_name_live, "نام مالک:", first_box_result, 0.95, 0.87)
        
        #شماره نفتکش
        self.car_id = ck.make_entry(third_box, 210, 36, colors.green_4, colors.light_gray_4, colors.green_4, colors.black,
                                         "شماره نفتکش", None, 60, "right", None, 0.275, 0.225, "center")
        update_live_information(self.car_id, car_id_live, "شماره نفتکش:", first_box_result, 0.46, 0.87)
        car_suggestion = SuggestionList(parent, self.car_id, None, None, [item['car_id'] for item in car_sample_data],
                                                        0.321, 0.445, "n", 1, 210)
        car_suggestion.hide_box()
        self.car_id.bind("<FocusIn>", lambda e: car_suggestion.show_box())
        self.car_id.bind("<KeyRelease>", lambda e: car_suggestion.show_box())
        self.car_id.bind("<FocusOut>", lambda e: car_suggestion.hide_box())
        
        # #کد ملی راننده
        self.driver_id = ck.make_entry(second_box, 230, 36, colors.dark_green_1, colors.light_gray_4, colors.dark_green_1, colors.black, 
                                         "کد ملی راننده", None, 60, "right", None, 0.285, 0.225, "center")
        update_live_information(self.driver_id, driver_id_live, "کد ملی راننده:", first_box_result, 0.46, 0.65)
        driver_id_suggestion = SuggestionList(parent, self.driver_id, self.car_id, ['name', 'id'], [driver['id'] for driver in driver_sample_data],
                                                        0.486, 0.445, "n", 4, 220)
        driver_id_suggestion.hide_box()
        self.driver_id.bind("<FocusIn>", lambda e: driver_id_suggestion.show_box())
        self.driver_id.bind("<KeyRelease>", lambda e: driver_id_suggestion.show_box())
        self.driver_id.bind("<FocusOut>", lambda e: driver_id_suggestion.hide_box())
        
        #شماره کارت هوشمند نفتکش
        self.smart_cart_car = ck.make_entry(third_box, 210, 36, colors.green_4, colors.light_gray_4, colors.green_4, colors.black,
                                         "شماره کارت هوشمند نفتکش", None, 60, "right", None, 0.275, 0.31, "center")
        update_live_information(self.smart_cart_car, smart_cart_car_live, "شماره کارت هوشمند نفتکش:", first_box_result, 0.95, 0.97)
        
        #مبدأ
        self.start_location = ck.make_entry(second_box_result, 220, 36, colors.dark_green_6, colors.light_gray_4, 
                                         colors.dark_green_6, colors.black,
                                         "مبدأ", None, 60, "right", None, 0.283, 0.3, "center")
        update_live_information(self.start_location, start_location_live, "مبدأ:", buttom_white_box_result, 0.98, 0.62)
        start_destination_suggestion = SuggestionList(parent, self.start_location, None, ['name', 'id'], startpoint_sample_data,
                                                        0.483, 0.66, "n", 2, 220)
        start_destination_suggestion.hide_box()
        self.start_location.bind("<FocusIn>", lambda e: start_destination_suggestion.show_box())
        self.start_location.bind("<KeyRelease>", lambda e: start_destination_suggestion.show_box())
        self.start_location.bind("<FocusOut>", lambda e: start_destination_suggestion.hide_box())
        
        #مقصد
        self.des_location = ck.make_entry(second_box_result, 220, 36, colors.dark_green_6, colors.light_gray_4, 
                                         colors.dark_green_6, colors.black,
                                         "مقصد", None, 60, "right", None, 0.283, 0.45, "center")
        update_live_information(self.des_location, des_location_live, "مقصد:", buttom_white_box_result, 0.98, 0.74)
        end_destination_suggestion = SuggestionList(parent, self.des_location, None, ['name', 'id'], station_sample_data,
                                                        0.483, 0.705, "n", 2, 220)
        end_destination_suggestion.hide_box()
        self.des_location.bind("<FocusIn>", lambda e: end_destination_suggestion.show_box())
        self.des_location.bind("<KeyRelease>", lambda e: end_destination_suggestion.show_box())
        self.des_location.bind("<FocusOut>", lambda e: end_destination_suggestion.hide_box())
        
        #مقدار طبیعی
        self.true_value = ck.make_entry(main_box, 105, 36, colors.dark_green_6, colors.light_gray_4, 
                                         colors.dark_green_6, colors.black,
                                         "وزن طبیعی", None, 60, "right", None, 0.525, 0.73, "center")
        update_live_information_3digit(self.true_value, true_value_live, "مقدار طبیعی:", buttom_white_box_result, 0.9, 0.9)
        
        #وزن محموله
        self.load_weight = ck.make_entry(second_box_result, 105, 36, colors.dark_green_6, colors.light_gray_4, 
                                         colors.dark_green_6, colors.black,
                                         "وزن محموله", None, 60, "right", None, 0.155, 0.6, "center")
        update_live_information_3digit(self.load_weight, load_weight_live, "وزن محموله:", buttom_white_box_result, 0.66, 0.9)
        
        #کوره/رنگی
        self.main_type = ck.make_list(third_box_result, "رنگی", [item["name"] for item in load_main_type], 200, 30, 
                                      colors.black, colors.dark_green_2, colors.light_gray_4,
                                      colors.green_2, colors.dark_green_3, 60,
                                      update_second_list_options, "e", 0.27, 0.3, "center")
        update_live_information(self.main_type, main_type_live, "عنوان اصلی کالا:", buttom_white_box_result, 0.35, 0.1)
        
        #نام فرآورده
        self.load_name = ck.make_list(third_box_result, "بنزین", [item["sub_array"] for item in load_main_type if item["name"] == "رنگی"][0], 200, 30,
                                      colors.black, colors.dark_green_2, colors.light_gray_4,
                                      colors.green_2, colors.dark_green_3, 60,
                                      update_load_name, "e", 0.27, 0.45, "center")
        update_live_information(self.load_name, load_name_live, "نام فرآورده:", buttom_white_box_result, 0.35, 0.24)
        
        #نوع ارسال
        self.sent_type = ck.make_list(third_box_result, "تدارکات", sent_type, 200, 30, 
                                      colors.black, colors.dark_green_2, colors.light_gray_4,
                                      colors.green_2, colors.dark_green_3, 60,
                                      update_sent_type, "e", 0.27, 0.6, "center")
        update_live_information(self.sent_type, sent_type_live, "نوع ارسال:", buttom_white_box_result, 0.35, 0.38)
        
        #کرایه دریافتی
        self.input_money = ck.make_entry(white_box_result, 185, 36, colors.green_4, colors.light_gray_4, 
                                         colors.green_4, colors.black, "کرایه دریافتی", None,
                                         60, "right", None, 0.235, 0.4, "center")
        update_live_information_3digit(self.input_money, input_money_live, "کرایه دریافتی:", first_box_result, 0.4, 0.42)
        
        #کرایه پرداختی
        self.payed_money = ck.make_entry(white_box_result, 185, 36, colors.green_4, colors.light_gray_4, 
                                         colors.green_4, colors.black, "کرایه پرداختی", None,
                                         60, "right", None, 0.235, 0.55, "center")
        update_live_information_3digit(self.payed_money, payed_money_live, "کرایه پرداختی:", first_box_result, 0.4, 0.51)
        
        #دکمه ها
        #ثبت بارنامه
        ck.make_button(white_box, "ثبت", 150, 50, (None, 30, "bold"), 60, colors.white, colors.white,
                       colors.dark_green_5, colors.green_3, self.check_complete_bol_inf, 0.25, 0.11, "center")
        
        # دکمه ریست
        ck.make_button(white_box, "دوباره", 150, 50, (None, 30, "bold"), 60, colors.white, colors.white,
                       colors.dark_green_5, colors.green_3, self.reset_page, 0.25, 0.24, "center")
        
        #دکمه خروج
        ck.make_button(white_box, "خروج", 150, 50, (None, 30, "bold"), 60, colors.white, colors.white,
                       colors.dark_green_5, colors.green_3, go_to_dashboard, 0.25, 0.37, "center")
    
        