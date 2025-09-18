import customtkinter as ctk
import common_ctk as ck
import common_controller as cc
import colors

class BolInf(ctk.CTkFrame):
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
        self.pack(fill="both", expand=True)
        
        def car_id_true_format(car_id_str):
            return "ایران " + car_id_str[12:14] + " - " + car_id_str[3:6] + " " + car_id_str[2] + " " + car_id_str[0:2] 
        
        def make_label(text, x_co, y_co):
            ctk.CTkLabel(parent, text=text, 
                                 font=(None, 17), 
                                 text_color=colors.dark_green_6, 
                                 bg_color=colors.light_green_1).place(relx=x_co, rely=y_co, anchor="e")
        #عنوان صفحه
        ctk.CTkLabel(parent, text="اطلاعات بارنامه", 
                                 font=(None, 30, "bold"), 
                                 text_color=colors.dark_green_6, 
                                 bg_color=colors.light_green_1).place(relx=0.5, rely=0.1, anchor="center")
        
        make_label("تاریخ ثبت: " + self.eng_to_persian_date(values["today_date"]), 0.96, 0.21)
        make_label("قرارداد: " + values["deal"], 0.96, 0.28)
        if(values['cash_id'] == '' or values['cash_id'] == None): make_label("شماره حواله: -", 0.96, 0.35)
        else: make_label("شماره حواله: " + values["cash_id"], 0.96, 0.35)
        make_label("شماره بارنامه: " + values["load_id"], 0.96, 0.42)
        if(values['load_group_id'] == '' or values['load_group_id'] == None): make_label("شماره صورت بارنامه: -", 0.96, 0.49)
        else: make_label("شماره صورت بارنامه: " + values["load_group_id"], 0.96, 0.49)
        make_label("نماینده: " + values["agent"], 0.96, 0.56)
        if(values['agent_group_id'] == '' or values['agent_group_id'] == None): make_label("شماره صورت نماینده: -", 0.96, 0.63)
        else: make_label("شماره صورت نماینده: " + values["agent_group_id"], 0.96, 0.63)
        if(values['send_date'] == 'تاریخ ارسال'): make_label("تاریخ ارسال: -", 0.96, 0.7)
        else: make_label("تاریخ ارسال: " + self.eng_to_persian_date(values["send_date"]), 0.96, 0.7)
        if(values['send2_date'] == 'تاریخ صدور'): make_label("تاریخ صدور: -", 0.96, 0.77)
        else: make_label("تاریخ صدور: " + self.eng_to_persian_date(values["send2_date"]), 0.96, 0.77)
        make_label("نام راننده: " + values["driver_name"], 0.62, 0.28)
        make_label("کد ملی راننده: " + values["driver_id"], 0.62, 0.35)
        make_label("هوشمند راننده: " + values["smart_cart_driver"], 0.62, 0.42)
        make_label("نام مالک: " + values["car_owner_name"], 0.62, 0.49)
        make_label("شماره نفتکش: " + car_id_true_format(values["car_id"]), 0.62, 0.56)
        make_label("هوشمند نفتکش: " + values["smart_cart_car"], 0.62, 0.63)
        
        make_label("مبدأ: " + values["start_location"], 0.62, 0.7)
        make_label("مقصد: " + values["des_location"], 0.62, 0.77)
        
        make_label("مقدار واقعی: " + self.eng_to_persian_date(self.cash_format(values["true_value"])), 0.22, 0.28)
        make_label("مقدار حمل‌شده: " + self.eng_to_persian_date(self.cash_format(values["load_weight"])), 0.22, 0.35)
        make_label("عنوان کالا: " + values["main_type"], 0.22, 0.42)
        make_label("نام فرآورده: " + values["load_name"], 0.22, 0.49)
        make_label("نوع ارسال: " + values["sent_type"], 0.22, 0.56)
        if(values["input_money"] == '' or values['input_money'] == None): make_label("کرایه دریافتی: -", 0.22, 0.63)
        else: make_label("کرایه دریافتی: " + self.eng_to_persian_date(self.cash_format(values["input_money"])), 0.22, 0.63)
        if(values["payed_money"] == '' or values['payed_money'] == None): make_label("کرایه پرداختی: -", 0.22, 0.7)
        else: make_label("کرایه پرداختی: " + self.eng_to_persian_date(self.cash_format(values["payed_money"])), 0.22, 0.7)
        
        ck.make_button(parent, 'چاپ بارنامه', 150, 50, (None, 22, 'bold'), 20, colors.white,
                       colors.light_green_1, colors.dark_green_6, colors.green_3, 
                       lambda: cc.make_photo_with_data(values), 
                       0.9, 0.9, 'center')