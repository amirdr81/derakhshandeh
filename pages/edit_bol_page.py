import customtkinter as ctk
import tkinter as tk
from insystem_data import agents, current_deals, load_main_type, sent_type
from date import Date
from bol_fake_data import current_bols, old_bols
import colors
import common_ctk as ck
import common_controller as cc

class EditBol(ctk.CTkFrame):
    def check_complete_bol_inf(self, parent):
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
        if(self.deal.get() not in [item["name"] + '/' + cc.eng_to_persian_date(item['id']) for item in current_deals]): flag = show_error_border(self.deal, colors.red_color, colors.green_2, flag, 1)
        if(not self.cash_id.get()): flag = show_error_border(self.cash_id, colors.red_color, colors.dark_green_6, flag, 0)
        if(not self.load_id.get()): flag = show_error_border(self.load_id, colors.red_color, colors.dark_green_6, flag, 0)
        if(not self.load_group_id.get()): flag = show_error_border(self.load_group_id, colors.red_color, colors.dark_green_6, flag, 0)
        if(self.agent.get() not in agents): flag = show_error_border(self.agent, colors.red_color, colors.green_2, flag, 1)
        if(not self.agent_group_id.get()): flag = show_error_border(self.agent_group_id, colors.red_color, colors.dark_green_6, flag, 0)
        if(self.send_date.cget("text") == "تاریخ ارسال"): show_error_border(self.send_date, colors.red_color, colors.dark_green_6, flag, 2)
        if(self.send2_date.cget("text") == "تاریخ صدور"): show_error_border(self.send2_date, colors.red_color, colors.dark_green_6, flag, 2)
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
        if(self.main_type.get() == "عنوان اصلی کالا"): flag = show_error_border(self.main_type, colors.red_color, colors.green_2, flag, 1)
        if(self.load_name.get() == "نام فرآورده"): flag = show_error_border(self.load_name, colors.red_color, colors.green_2, flag, 1)
        if(self.sent_type.get() == "نوع ارسال"): flag = show_error_border(self.sent_type, colors.red_color, colors.green_2, flag, 1)
        if(not self.input_money.get()): flag = show_error_border(self.input_money, colors.red_color, colors.green_4, flag, 0)
        if(not self.payed_money.get()): flag = show_error_border(self.payed_money, colors.red_color, colors.green_4, flag, 0)
        if(cc.eng_to_persian_date((self.values)['load_id']) != self.load_id.get() and 
           cc.eng_to_persian_date(self.load_id.get()) in [cc.eng_to_persian_date(item['load_id']) for item in current_bols + old_bols]): 
            flag = show_error_border(self.load_id, colors.red_color, colors.dark_green_6, flag, 0)
        if(not flag): self.show_register_confirm(parent)
    
    def show_register_confirm(self, box):
        dialog = ctk.CTkFrame(box, width=self.winfo_screenwidth() / 4.5, 
                              height=self.winfo_screenheight() / 8, 
                              fg_color=colors.dark_green_6)
        dialog.place(relx=0.5, rely=0.5, anchor="center") 
        lbl = ctk.CTkLabel(dialog, 
                           text="آیا از صحت اطلاعات وارد شده، اطمینان دارید؟...", 
                           font=(None, 16),
                           text_color=colors.white)
        lbl.place(relx=0.5, rely=0.2, anchor="center")
        def do_register():
            def get_bol_by_load_id(target):
                for i, item in enumerate(current_bols):
                    if(item["load_id"] == target): return i, item
                return None, None
            
            new_bol = {"today_date":self.eng_to_persian_date(self.today_date.cget("text")),
                         "deal":self.eng_to_persian_date(self.deal.get()),
                         "cash_id":self.eng_to_persian_date(self.cash_id.get()),
                         "load_id":self.eng_to_persian_date(self.load_id.get()),
                         "load_group_id":self.eng_to_persian_date(self.load_group_id.get()),
                         "agent":self.eng_to_persian_date(self.agent.get()),
                         "agent_group_id":self.eng_to_persian_date(self.agent_group_id.get()),
                         "send_date":self.eng_to_persian_date(self.send_date.cget("text")),
                         "send2_date":self.eng_to_persian_date(self.send2_date.cget("text")),
                         "driver_name":self.eng_to_persian_date(self.driver_name.get()),
                         "driver_id":self.eng_to_persian_date(self.driver_id.get()),
                         "smart_cart_driver":self.eng_to_persian_date(self.smart_cart_driver.get()),
                         "car_owner_name":self.eng_to_persian_date(self.car_owner_name.get()),
                         "car_id":self.eng_to_persian_date(self.car_id.get()),
                         "smart_cart_car":self.eng_to_persian_date(self.smart_cart_car.get()),
                         "start_location":self.eng_to_persian_date(self.start_location.get()),
                         "des_location":self.eng_to_persian_date(self.des_location.get()),
                         "true_value":self.persian_to_eng_date(self.true_value.get()),
                         "load_weight":self.persian_to_eng_date(self.load_weight.get()),
                         "main_type":self.eng_to_persian_date(self.main_type.get()),
                         "load_name":self.eng_to_persian_date(self.load_name.get()),
                         "sent_type":self.eng_to_persian_date(self.sent_type.get()),
                         "input_money":self.persian_to_eng_date(self.remove_commas(self.input_money.get())),
                         "payed_money":self.persian_to_eng_date(self.remove_commas(self.payed_money.get()))}
            i, item = get_bol_by_load_id(self.values["load_id"])
            current_bols[i] = new_bol
            self.go_to_veiw_bol()
            dialog.destroy()
        
        def cancel(): 
            dialog.destroy()
        
        # دو تا دکمه بله و خیر
        btn_yes = ctk.CTkButton(dialog, text="بله", width=70, command=do_register, fg_color=colors.dark_green_5, hover_color=colors.green_3)
        btn_no = ctk.CTkButton(dialog, text="خیر", width=70, command=cancel, fg_color=colors.dark_green_5, hover_color=colors.green_3)
        btn_yes.place(relx=0.35, rely=0.8, anchor="center")
        btn_no.place(relx=0.65, rely=0.8, anchor="center")
            
    def remove_commas(self, input_str):
        return input_str.replace(',', '')

    def persian_to_eng_date(self, date_str):
        english_digits = '0123456789'
        persian_digits = '۰۱۲۳۴۵۶۷۸۹'
        trans_table = str.maketrans(''.join(persian_digits), ''.join(english_digits))
        return date_str.translate(trans_table)
    
    def eng_to_persian_date(self, date_str):
        english_digits = '0123456789'
        persian_digits = '۰۱۲۳۴۵۶۷۸۹'
        trans_table = str.maketrans(''.join(english_digits), ''.join(persian_digits))
        return date_str.translate(trans_table)
    
    def cash_format(self, input):
        rem = len(input) % 3
        text = ""
        if(rem): text = str((input[0:rem])) + ","
        for i in range(int(len(input[rem:]) / 3)): text += (input[rem:][3 * i : 3 * i + 3] + ",")
        return text[0 : len(text) - 1]
         
    def __init__(self, parent, go_to_veiw_bol, values):
        super().__init__(parent, fg_color=colors.light_green_1)
        
        self.values = values
        self.go_to_veiw_bol = go_to_veiw_bol
        
        deals_list = [item["name"] + '/' + item['id'] for item in current_deals]
        load_main_list = [item["name"] for item in load_main_type]
        load_name_list = [item["sub_array"] for item in load_main_type if item["name"] == values["main_type"]][0]
        
        def open_calendar(box, entry, x_co, y_co):
            global calendar_frame
            try: calendar_frame.destroy()
            except: pass
            calendar_frame = tk.Frame(box, bd=2, relief=tk.RIDGE,
                                      bg=colors.light_green_1)
            calendar_frame.place(relx=x_co, rely=y_co, anchor="center")
            def on_date_selected(selected_date):
                entry.configure(text=self.eng_to_persian_date(str(selected_date).replace("-", "/")))  
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
            
        def make_label_for_entry(text, x_co, y_co):
            ctk.CTkLabel(parent, text=text, 
                                 font=(None, 17, "bold"), 
                                 fg_color=colors.light_green_1,
                                 text_color=colors.dark_green_6, 
                                 bg_color=colors.light_green_1).place(relx=x_co, rely=y_co, anchor="e")
            
        def make_list(text, x_co, y_co, list, width, func, state):
            list_tmp = ctk.CTkOptionMenu(
                parent,
                variable=ctk.StringVar(value=text),
                values=list,
                width=width,
                height=30,
                anchor="center",
                fg_color=colors.dark_green_6,
                text_color=colors.white,
                button_color=colors.green_2,
                corner_radius=60,
                state=state,
                button_hover_color=colors.dark_green_3,
                command=func)
            list_tmp.place(relx=x_co, rely=y_co, anchor="center")
            return list_tmp
            
        def make_date_entry(text, x_co, y_co, width):
            date_entry = ctk.CTkButton(
                parent,
                text=text,
                height=34,
                width=width,
                corner_radius=60,
                bg_color=colors.light_green_1,
                border_width=2,
                border_color=colors.dark_green_6,
                fg_color=colors.dark_green_6,
                hover_color=colors.green_3,
                text_color=colors.white,
                command=lambda:open_calendar(parent, date_entry, 0.5, 0.5)
            )
            date_entry.place(relx=x_co, rely=y_co, anchor="center")
            return date_entry
        
        def make_entry(text, x_co, y_co, width):
            my_var = ctk.StringVar()
            my_var.set(text)
            entry = ctk.CTkEntry(parent, textvariable=my_var, 
                                 font=(None, 15), 
                                 width=width,
                                 height=32,
                                 corner_radius=60,
                                 justify="center",
                                 fg_color=colors.dark_green_6,
                                 text_color=colors.white, 
                                 border_color=colors.dark_green_6,
                                 bg_color=colors.light_green_1)
            entry.place(relx=x_co, rely=y_co, anchor="e")
            return entry
        
        #عنوان صفحه
        ctk.CTkLabel(parent, text="ویرایش بارنامه", 
                                 font=(None, 30, "bold"), 
                                 text_color=colors.dark_green_6, 
                                 bg_color=colors.light_green_1).place(relx=0.5, rely=0.1, anchor="center")
        
        def update_first_list_options(selected_value):
            self.load_name.configure(text_color=colors.light_gray_3, 
                                     values=[item["sub_array"] for item in load_main_type if item["name"] == self.main_type.get()][0],
                                     variable=ctk.StringVar(value="نام فرآورده"))
            
        def update_second_list_options(selected_value):
            self.load_name.configure(text_color=colors.white)
            
            
        make_label_for_entry("تاریخ ثبت: ", 0.99, 0.21)
        self.today_date = make_date_entry(self.eng_to_persian_date(values["today_date"]), 0.87, 0.21, 100)
        make_label_for_entry("قرارداد: ", 0.99, 0.29)
        self.deal = make_list(values["deal"], 0.83, 0.29, deals_list, 210, None, "normal")
        make_label_for_entry("شماره حواله: ", 0.99, 0.37)
        self.cash_id = make_entry(values["cash_id"], 0.89, 0.37, 170)
        make_label_for_entry("شماره بارنامه: ", 0.99, 0.45)
        self.load_id = make_entry(values["load_id"], 0.89, 0.45, 170)
        make_label_for_entry("شماره صورت بارنامه: ", 0.99, 0.53)
        self.load_group_id = make_entry(values["load_group_id"], 0.835, 0.53, 110)
        make_label_for_entry("نماینده: ", 0.99, 0.61)
        self.agent = make_list(values["agent"], 0.83, 0.61, agents, 210 ,None, "normal")
        make_label_for_entry("شماره صورت نماینده: ", 0.99, 0.69)
        self.agent_group_id = make_entry(values["agent_group_id"], 0.835, 0.69, 110)
        make_label_for_entry("تاریخ ارسال: ", 0.99, 0.77)
        self.send_date = make_date_entry(self.eng_to_persian_date(values["send_date"]), 0.815, 0.77, 180)
        make_label_for_entry("تاریخ صدور: ", 0.99, 0.85)
        self.send2_date = make_date_entry(self.eng_to_persian_date(values["send2_date"]), 0.815, 0.85, 180)

        make_label_for_entry("نام راننده: ", 0.645, 0.29)
        self.driver_name = make_entry(values["driver_name"], 0.565, 0.29, 170)
        make_label_for_entry("کد ملی راننده: ", 0.645, 0.37)
        self.driver_id = make_entry(values["driver_id"], 0.54, 0.37, 140)
        make_label_for_entry("هوشمند راننده: ", 0.645, 0.45)
        self.smart_cart_driver = make_entry(values["smart_cart_driver"], 0.53, 0.45, 130)
        make_label_for_entry("نام مالک: ", 0.645, 0.53)
        self.car_owner_name = make_entry(values["car_owner_name"], 0.565, 0.53, 170)
        make_label_for_entry("شماره نفتکش: ", 0.645, 0.61)
        self.car_id = make_entry(values["car_id"], 0.53, 0.61, 130)
        make_label_for_entry("هوشمند نفتکش: ", 0.645, 0.69)
        self.smart_cart_car = make_entry(values["smart_cart_car"], 0.53, 0.69, 130)

        make_label_for_entry("مبدأ: ", 0.645, 0.77)
        self.start_location = make_entry(values["start_location"], 0.59, 0.77, 200)
        make_label_for_entry("مقصد: ", 0.645, 0.85)
        self.des_location = make_entry(values["des_location"], 0.59, 0.85, 200)

        make_label_for_entry("مقدار واقعی: ", 0.29, 0.29)
        self.true_value = make_entry(self.eng_to_persian_date(values["true_value"]), 0.17, 0.29, 95)
        make_label_for_entry("مقدار حمل‌شده: ", 0.29, 0.37)
        self.load_weight = make_entry(self.eng_to_persian_date(values["load_weight"]), 0.17, 0.37, 95)
        make_label_for_entry("کرایه دریافتی: ", 0.29, 0.45)
        self.input_money = make_entry(self.eng_to_persian_date(values["input_money"]), 0.17, 0.45, 100)
        make_label_for_entry("کرایه پرداختی: ", 0.29, 0.53)
        self.payed_money = make_entry(self.eng_to_persian_date(values["payed_money"]), 0.17, 0.53, 100)
        
        make_label_for_entry("عنوان کالا: ", 0.29, 0.61)
        self.main_type = make_list(values["main_type"], 0.11, 0.61, load_main_list, 200, update_first_list_options, "normal")
        make_label_for_entry("نام فرآورده: ", 0.29, 0.69)
        self.load_name = make_list(values["load_name"], 0.11, 0.69, load_name_list, 200, update_second_list_options, "normal")
        make_label_for_entry("نوع ارسال: ", 0.29, 0.77)
        self.sent_type = make_list(values["sent_type"], 0.11, 0.77, sent_type, 200, None, "normal")
        
        #دکمه ثبت
        edit_btn = ctk.CTkButton(parent, text="ویرایش", 
                                      width=120,
                                      height=30, 
                                      font=(None, 25),
                                      bg_color=colors.light_green_1, 
                                      corner_radius=60,
                                fg_color=colors.dark_green_6,
                                text_color=colors.light_green_1,
                                hover_color=colors.green_3,
                                command=lambda:self.check_complete_bol_inf(parent))
        edit_btn.place(relx=0.2, rely=0.91, anchor="center")
