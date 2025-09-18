import customtkinter as ctk
import common_controller as cc
import common_ctk as ck


from bol_fake_data import car_sample_data, driver_sample_data

import colors

class CarDriverTable(ctk.CTkFrame):
    def __init__(self, parent, go_to_dashboard1, reset_page):
        super().__init__(parent)

        self.pack(fill="both", expand=True)
        self.configure(fg_color=colors.light_green_1)

        self.go_to_dashboard1 = go_to_dashboard1
        self.reset_page = reset_page

        self.header_color = colors.dark_green_6
        self.header_hover = colors.green_3
        
        self.table_btns = {}


        self.canvas = ctk.CTkCanvas(self, bg=colors.light_green_1, highlightthickness=0)
        self.v_scrollbar = ctk.CTkScrollbar(self, orientation="vertical", command=self.canvas.yview)
        self.h_scrollbar = ctk.CTkScrollbar(self, orientation="horizontal", command=self.canvas.xview)

        self.canvas.configure(yscrollcommand=self.v_scrollbar.set, xscrollcommand=self.h_scrollbar.set)

        self.v_scrollbar.pack(side="right", fill="y")
        self.h_scrollbar.pack(side="bottom", fill="x")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.inner_frame = ctk.CTkFrame(self.canvas, fg_color=colors.light_green_1)
        self.inner_window = self.canvas.create_window((0,0), window=self.inner_frame, anchor="nw")
        
        for j, plate in enumerate(car_sample_data, 1):
            plate_btn = ctk.CTkButton(self.inner_frame, text=cc.car_id_true_format(plate['car_id']), 
                                      fg_color=colors.dark_green_6, text_color=colors.white, hover_color=colors.green_4,
                                      command=lambda p=plate: self.show_car_data(p), anchor="center")
            plate_btn.grid(row=0, column=j, padx=5, pady=5, sticky="nsew")
            self.table_btns[(0, j)] = plate_btn

        for i, driver in enumerate(driver_sample_data, 1):
            driver_btn = ck.make_button(self.inner_frame, driver['name'] + " " + driver['lastname'],
                                        150, 35, (None, 15), 20, colors.white, colors.light_green_1, 
                                        colors.dark_green_6, colors.green_4, lambda d=driver: self.show_driver_data(d),
                                        0, 0, 'center')
            driver_btn.grid(row=i, column=0, padx=5, pady=5, sticky="nsew")
            self.table_btns[(i, 0)] = driver_btn
            
            driver_btn.bind("<Enter>", lambda e, btn=driver_btn, d=driver: btn.configure(text = cc.eng_to_persian_date(d['phone'])))
            driver_btn.bind("<Leave>", lambda e, btn=driver_btn, d=driver: btn.configure(text = d['name'] + " " + d['lastname']))

        for i, driver in enumerate(driver_sample_data, 1):
            for j, plate in enumerate(car_sample_data, 1):
                if(self.car_vs_driver(driver, plate)):
                    btn = ctk.CTkButton(self.inner_frame, text="", 
                                        fg_color=colors.green_3, text_color=colors.black, hover_color=colors.green_5,
                                        width=50)
                    # command=lambda d=driver, p=plate: self.change_status(d, p, btn)
                    btn.grid(row=i, column=j, padx=5, pady=5)
                    self.table_btns[(i, j)] = btn
                else:
                    btn = ctk.CTkButton(self.inner_frame, text="", 
                                        fg_color=colors.red_color, text_color=colors.black, hover_color=colors.light_red_color,
                                        width=50)
                    btn.grid(row=i, column=j, padx=6, pady=6)
                    self.table_btns[(i, j)] = btn
                
                btn.bind("<Enter>", lambda event, r=i, c=j: self.on_cell_enter(r, c))
                btn.bind("<Leave>", lambda event, r=i, c=j: self.on_cell_leave(r, c))
                btn.bind("<Button-1>", lambda event, d=driver, p=plate, b=btn: self.change_status(d, p, b))

        
        for j in range(1, len(car_sample_data) + 1):
            self.table_btns[(0, j)].bind("<Enter>", lambda event, r=0, c=j: self.on_header_enter(r, c))
            self.table_btns[(0, j)].bind("<Leave>", lambda event, r=0, c=j: self.on_header_leave(r, c))
        for i in range(1, len(driver_sample_data) + 1):
            self.table_btns[(i, 0)].bind("<Enter>", lambda event, r=i, c=0: self.on_header_enter(r, c))
            self.table_btns[(i, 0)].bind("<Leave>", lambda event, r=i, c=0: self.on_header_leave(r, c))
        
        ck.make_button(self, "بازگشت", 150, 50, (None, 22, "bold"),
                       20, colors.white, colors.white,
                       colors.dark_green_5, colors.green_3, 
                       self.go_to_dashboard1, 0.075, 0.94, "center")  
                
                
        self.inner_frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
    def change_status(self, driver, car, btn):
        fullname = driver['name'] + " " + driver['lastname']
        if(driver['car_id'] == ''): 
            driver['car_id'] = car['car_id']
            car['driver_name'].append(fullname)
            btn.configure(fg_color = colors.green_3, hover_color=colors.green_5)
        elif(driver['car_id'] == car['car_id']): 
            driver['car_id'] = ''
            if(fullname in car['driver_name']): car['driver_name'].remove(fullname)
            btn.configure(fg_color = colors.red_color, hover_color=colors.light_red_color)
        # self.reset_page()
        
    def show_car_data(self, selected_data):
        edit_box = ck.make_frame(self, 600, 400, colors.dark_green_6, colors.dark_green_6, colors.dark_green_6, 0, 0, 0.5, 0.5, "center")
        ck.make_label(edit_box, 150, 50, colors.dark_green_6, colors.dark_green_6, colors.white,
                    "مشاهده اطلاعات نفتکش", 0, None, (None, 30, "bold"), 0.5, 0.1, "center")
        
        #پلاک ماشین
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                    "پلاک ماشین: " + cc.car_id_true_format(cc.eng_to_persian_date(selected_data["car_id"])), 0, None, (None, 20), 0.94, 0.25, "e")
        
        #هوشمند نفتکش
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                    "شماره هوشمند: " + cc.eng_to_persian_date(selected_data["smart_car_id"]), 0, None, (None, 20), 0.47, 0.25, "e")
        
        #نام مالک
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                    "نام مالک: " + selected_data["owner_name"], 0, None, (None, 20), 0.94, 0.35, "e")
        
        #تاریخ شروع اندازه‌گیری
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                    "تاریخ صدور اندازه‌گیری: " + cc.eng_to_persian_date(selected_data["start_date"]), 0, None, (None, 20), 0.94, 0.45, "e")
        
        #تاریخ پایان اندازه‌گیری
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                    "تاریخ انقضا اندازه‌گیری: " + cc.eng_to_persian_date(selected_data["end_date"]), 0, None, (None, 20), 0.94, 0.55, "e")
        
        #بنزین
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                    "بنزین: " + cc.cash_format(cc.eng_to_persian_date(selected_data["benzin"])), 0, None, (None, 20), 0.89, 0.65, "e")
        
        #سفید
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                    "نفت سفید: " + cc.cash_format(cc.eng_to_persian_date(selected_data["sefid"])), 0, None, (None, 20), 0.5, 0.65, "e")
        
        #گاز
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                    "نفت گاز: " + cc.cash_format(cc.eng_to_persian_date(selected_data["gas"])), 0, None, (None, 20), 0.89, 0.75, "e")
        
        #کوره
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                    "نفت کوره: " + cc.cash_format(cc.eng_to_persian_date(selected_data["koore"])), 0, None, (None, 20), 0.5, 0.75, "e")
        
        #دکمه ها
        #دکمه بستن
        ck.make_button(edit_box, "بستن", 100, 35, (None, 22, "bold"), 20, colors.dark_green_6, 
                    colors.dark_green_6, colors.white, colors.green_3, lambda: edit_box.destroy(), 
                    0.04, 0.95, "sw")
        

    def show_driver_data(self, selected_data):
        edit_box = ck.make_frame(self, 600, 400, colors.dark_green_6, colors.dark_green_6, colors.dark_green_6, 0, 0, 0.5, 0.5, "center")
        ck.make_label(edit_box, 150, 50, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "مشاهده اطلاعات راننده", 0, None, (None, 30, "bold"), 0.5, 0.1, "center")
        
        #نام راننده
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "نام راننده: " + selected_data["name"], 0, None, (None, 20), 0.97, 0.25, "e")
        
        #نام خانوادگی راننده
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "نام‌خانوادگی راننده: " + selected_data["lastname"], 0, None, (None, 20), 0.5, 0.25, "e")
        
        #کد ملی راننده
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "کد ملی: " + cc.eng_to_persian_date(selected_data["id"]), 0, None, (None, 20), 0.97, 0.35, "e")
        
        #شماره تماس
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "شماره تماس: " + cc.eng_to_persian_date(selected_data["phone"]), 0, None, (None, 20), 0.5, 0.35, "e")
        
        #هوشمند راننده
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "هوشمند راننده: " + cc.eng_to_persian_date(selected_data["smart_id"]), 0, None, (None, 20), 0.97, 0.45, "e")
        
        #شماره گواهینامه
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "شماره گواهینامه: " + cc.eng_to_persian_date(selected_data["licence_id"]), 0, None, (None, 20), 0.5, 0.45, "e")
        
        #تاریخ شروع و پایان اعتبار هوشمند راننده
        ck.make_label(edit_box, 100, 50, 
                      colors.dark_green_6, colors.dark_green_6, colors.white, 
                      "تاریخ شروع اعتبار هوشمند: " + cc.eng_to_persian_date(selected_data["start_smart_date"])
                      , 0, None, (None, 20), 0.97, 0.55, "e")
        ck.make_label(edit_box, 100, 50, 
                      colors.dark_green_6, colors.dark_green_6, colors.white, 
                      "تاریخ پایان اعتبار هوشمند: " + cc.eng_to_persian_date(selected_data["end_smart_date"])
                      , 0, None, (None, 20), 0.97, 0.65, "e")
        
        #دکمه ها
        #دکمه بستن
        ck.make_button(edit_box, "بستن", 100, 35, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, lambda: edit_box.destroy(), 
                       0.04, 0.95, "sw")
        



    def on_cell_enter(self, row, col):
        self.table_btns[(0, col)].configure(fg_color=self.header_hover)
        self.table_btns[(row, 0)].configure(fg_color=self.header_hover)

    def on_cell_leave(self, row, col):
        self.table_btns[(0, col)].configure(fg_color=self.header_color)
        self.table_btns[(row, 0)].configure(fg_color=self.header_color)

    def on_header_enter(self, row, col):
        self.table_btns[(row, col)].configure(fg_color=self.header_hover)

    def on_header_leave(self, row, col):
        self.table_btns[(row, col)].configure(fg_color=self.header_color)

    def car_vs_driver(self, driver, car):
        return driver['car_id'] == car['car_id']
    
