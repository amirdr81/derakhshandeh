#main libraries
import customtkinter as ctk
import tkinter.ttk as ttk
import tkinter as tk
from PIL import Image, ImageTk

#data imports
import asset_paths
from bol_fake_data import car_sample_data, old_cars

#controllers
import common_controller as cc
import common_ctk as ck
import register_controller as rc

#colors
import colors


class CarInfo(ctk.CTkFrame):
    def edit_car(self):
        selected_data = car_sample_data[int(self.tree.item(self.tree.selection()[0], 'values')[0]) - 1]
        
        edit_box = ck.make_frame(self, 600, 400, colors.dark_green_6, colors.dark_green_6, colors.dark_green_6, 0, 0, 0.5, 0.5, "center")
        ck.make_label(edit_box, 150, 50, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "مشاهده/ویرایش اطلاعات نفتکش", 0, None, (None, 30, "bold"), 0.5, 0.1, "center")
        
        #پلاک ماشین
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "پلاک ماشین:", 0, None, (None, 20), 0.97, 0.25, "e")
        car_id = ck.make_entry(edit_box, 150, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.81, 0.25, "e")
        ck.make_entry_with_text(car_id, selected_data["car_id"])
        
        #هوشمند نفتکش
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "شماره هوشمند:", 0, None, (None, 20), 0.5, 0.3, "e")
        smart_car_id = ck.make_entry(edit_box, 145, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.03, 0.3, "w")
        ck.make_entry_with_text(smart_car_id, selected_data["smart_car_id"])
        
        #نام مالک
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "نام مالک:", 0, None, (None, 20), 0.97, 0.35, "e")
        owner_name = ck.make_entry(edit_box, 175, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.84, 0.35, "e")
        ck.make_entry_with_text(owner_name, selected_data["owner_name"])
        
        #تاریخ شروع اندازه‌گیری
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "تاریخ صدور اندازه‌گیری:", 0, None, (None, 20), 0.85, 0.45, "e")
        start_smart_date = ck.make_button(edit_box, cc.eng_to_persian_date(selected_data["start_date"]), 150, 30, (None, 15), 20, 
                                          colors.gray_2, colors.dark_green_6,colors.white,colors.green_3, 
                                          lambda: ck.open_calendar(edit_box, start_smart_date, 0.5, 0.5, colors.black), 0.52, 0.45, "e")
        start_smart_date.configure(text_color=colors.black)
        
        #تاریخ پایان اندازه‌گیری
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "تاریخ انقضا اندازه‌گیری:", 0, None, (None, 20), 0.85, 0.55, "e")
        end_smart_date = ck.make_button(edit_box, cc.eng_to_persian_date(selected_data["end_date"]), 150, 30, (None, 15), 20, 
                                          colors.gray_2, colors.dark_green_6,colors.white,colors.green_3, 
                                          lambda: ck.open_calendar(edit_box, end_smart_date, 0.5, 0.5, colors.black), 0.52, 0.55, "e")
        end_smart_date.configure(text_color=colors.black)
        
        #بنزین
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "بنزین:", 0, None, (None, 20), 0.89, 0.65, "e")
        benzin = ck.make_entry(edit_box, 100, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.8, 0.65, "e")
        ck.make_entry_with_text(benzin, cc.eng_to_persian_date(selected_data["benzin"]))
        
        #سفید
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "نفت سفید:", 0, None, (None, 20), 0.5, 0.65, "e")
        sefid = ck.make_entry(edit_box, 100, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.35, 0.65, "e")
        ck.make_entry_with_text(sefid, cc.eng_to_persian_date(selected_data["sefid"]))
        
        #گاز
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "نفت گاز:", 0, None, (None, 20), 0.91, 0.75, "e")
        gas = ck.make_entry(edit_box, 100, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.79, 0.75, "e")
        ck.make_entry_with_text(gas, cc.eng_to_persian_date(selected_data["gas"]))
        
        #کوره
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "نفت کوره:", 0, None, (None, 20), 0.5, 0.75, "e")
        koore = ck.make_entry(edit_box, 100, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.35, 0.75, "e")
        ck.make_entry_with_text(koore, cc.eng_to_persian_date(selected_data["koore"]))
        

        
        #دکمه ها
        # دکمه ثبت
        ck.make_button(edit_box, "ثبت اطلاعات", 150, 35, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, 
                       lambda: rc.edit_car(selected_data,
                                           car_id,
                                            smart_car_id,
                                            owner_name,
                                            start_smart_date,
                                            end_smart_date,
                                            benzin,
                                            sefid,
                                            gas,
                                            koore,
                                            edit_box,
                                            self.reset_page), 
                       0.96, 0.95, "se")
        
        
        #دکمه بستن
        ck.make_button(edit_box, "بستن", 100, 35, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, lambda: edit_box.destroy(), 
                       0.04, 0.95, "sw")
        
        
    def register_car(self):
        register_box = ck.make_frame(self, 600, 400, colors.dark_green_6, colors.dark_green_6, colors.dark_green_6, 0, 0, 0.5, 0.5, "center")
        
        ck.make_label(register_box, 200, 50, colors.dark_green_6, colors.dark_green_6, colors.white,
                          "ثبت اطلاعات ماشین", 0, "center", (None, 35, "bold"), 0.5, 0.1, "center")
        car_id = ck.make_entry(register_box, 200, 40, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "پلاک ماشین", colors.gray_2, 20, "right", (None, 15), 0.9, 0.3, "e")
        smart_car_id = ck.make_entry(register_box, 200, 40, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "هوشمند نفتکش", colors.gray_2, 20, "right", (None, 15), 0.45, 0.3, "e")
        owner_name = ck.make_entry(register_box, 200, 40, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "نام مالک", colors.gray_2, 20, "right", (None, 15), 0.5, 0.43, "center")
        measurement_start_date = ck.make_button(register_box, "تاریخ صدور", 150, 30, (None, 15), 20, 
                                          colors.gray_2, colors.dark_green_6,colors.white,colors.green_3, 
                                          lambda: ck.open_calendar(register_box, measurement_start_date, 0.5, 0.5, colors.black), 0.785, 0.56, "e")
        measurement_start_date.configure(text_color=colors.gray_2)
        measurement_end_date = ck.make_button(register_box, "تاریخ انقضا", 150, 30, (None, 15), 20, 
                                          colors.gray_2, colors.dark_green_6,colors.white,colors.green_3, 
                                          lambda: ck.open_calendar(register_box, measurement_end_date, 0.5, 0.5, colors.black), 0.5, 0.56, "e")
        measurement_end_date.configure(text_color=colors.gray_2)
        
        #اندازه های موارد
        benzin = ck.make_entry(register_box, 100, 40, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "بنزین", colors.gray_2, 20, "right", (None, 12), 0.9, 0.69, "e")
        sefid = ck.make_entry(register_box, 100, 40, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "نفت سفید", colors.gray_2, 20, "right", (None, 12), 0.7, 0.69, "e")
        gas = ck.make_entry(register_box, 100, 40, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "نفت گاز", colors.gray_2, 20, "right", (None, 12), 0.5, 0.69, "e")
        koore = ck.make_entry(register_box, 100, 40, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "نفت کوره", colors.gray_2, 20, "right", (None, 12), 0.13, 0.69, "w")
        
        #دکمه ها
        ck.make_button(register_box, "بستن", 100, 35, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, lambda: register_box.destroy(), 
                       0.04, 0.95, "sw")
        
        ck.make_button(register_box, "ثبت‌نام", 100, 35, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, 
                       lambda: rc.register_car(car_id,
                                               smart_car_id,
                                                  owner_name,
                                                  measurement_start_date,
                                                  measurement_end_date,
                                                  benzin,
                                                  sefid,
                                                  gas,
                                                  koore,
                                                  register_box,
                                                  self.reset_page),   
                       0.96, 0.95, "se")
    
    def archive_car(self):
        selected_data = car_sample_data[int(self.tree.item(self.tree.selection()[0], 'values')[0]) - 1]
        label = ck.make_label(self, 150, 25, 
                          colors.white, colors.white, colors.red_color,
                          "", 0, None, (None, 18, "bold"), 0.91, 0.36, "e")
        if(selected_data['driver_name'] != None and selected_data['driver_name'] != []):
            ck.update_label_error(label, 2000, 'برای آرشیو نفتکش، ابتدا راننده(راننده‌ها) را حذف کنید!')
        else:
            def do_delete():
                car_sample_data.remove(selected_data)
                old_cars.append(selected_data)
                dialog.destroy()
                self.go_to_archive()
            def cancel(): 
                cc.activate_all_widgets(self)
                dialog.destroy()
            cc.disable_all_widgets(self)
            dialog = rc.show_confirmation_box(self, do_delete, cancel, "آیا از آرشیو این نفتکش، مطمئن هستید؟", selected_data)
        
    def add_row(self, data_tuple):
        iid = self.tree.insert("", tk.END, values=data_tuple)
        self.tree.tag_configure(f"hover_{iid}", background=colors.light_green_5)
        self.tree.item(iid, tags=(f"hover_{iid}",))
        return iid

    def __init__(self, parent, go_to_dashboard1, go_to_archive, go_to_car_licence, reset_page):
        super().__init__(parent)
        
        self.pack(fill="both", expand=True)
        self.configure(fg_color=colors.light_green_1)
        self.go_to_archive = go_to_archive
        self.reset_page = reset_page
        
        def on_item_select(event):
            selected = self.tree.selection()
            if selected: 
                delete_bol_btn.configure(state="normal", fg_color=colors.dark_green_6, text_color=colors.white)
            else: 
                delete_bol_btn.configure(state="disabled", fg_color=colors.light_gray_1, text_color=colors.light_gray_6)
                
        main_box = ck.make_frame(self, float(self.master.winfo_screenwidth() / 1.2), float(self.master.winfo_screenheight() / 1.5), 
                                 colors.white, colors.white, colors.white, 0, 0, 0.5, 0.5, "center")
        
        self.column_titles = ["ردیف", "پلاک ماشین", "نام مالک", "نام راننده", "تاریخ شروع اندازه‌گیری", "تاریخ پایان اندازه‌گیری"]
        self.column_ids = [f"col{i}" for i in range(len(self.column_titles))]

        style = ttk.Style(self)

        bg_color = colors.light_green_5
        text_color = colors.black
        heading_bg_color = colors.dark_green_6
        selected_color = colors.green_2

        style.theme_use("default")

        # استایل اصلی Treeview
        style.configure("Treeview",
                        background=bg_color,
                        foreground=text_color,
                        fieldbackground=colors.light_green_4,
                        rowheight=30)
        
        # استایل هدر
        style.configure("Treeview.Heading",
                        background=heading_bg_color,
                        foreground=colors.white,
                        font=(None, 15, "bold"),
                        padding=(5, 5))

        # رنگ ردیف انتخاب شده
        style.map("Treeview",
                  background=[("selected", selected_color)],
                  foreground=[("selected", "white")])

        tree_frame = ctk.CTkFrame(main_box)
        tree_frame.place(relx=0.5, rely=0.6, anchor="center")

        style.configure("Custom.Vertical.TScrollbar", 
            background=colors.dark_green_6,
            troughcolor=colors.light_green_1,
            bordercolor=colors.white,
            arrowcolor=colors.white,
            relief="flat")

        tree_scrollbar_y = ttk.Scrollbar(
            tree_frame,
            orient="vertical",
            style="Custom.Vertical.TScrollbar"
        )
        
        self.tree = ttk.Treeview(tree_frame,
                                 columns=self.column_ids,
                                 show="headings",
                                 yscrollcommand=tree_scrollbar_y.set,
                                 selectmode="browse")

        tree_scrollbar_y.config(command=self.tree.yview)
        tree_scrollbar_y.grid(row=0, column=1, sticky="ns")
        self.tree.grid(row=0, column=0, sticky="nsew")
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)
        
        table_width = self.tree.winfo_screenwidth() 

        self.tree.heading(0, text=self.column_titles[0], anchor=tk.CENTER)
        self.tree.column(0, width=int(50 / 860 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(1, text=self.column_titles[1], anchor=tk.CENTER)
        self.tree.column(1, width=int(130 / 860 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(2, text=self.column_titles[2], anchor=tk.CENTER)
        self.tree.column(2, width=int(130 / 860 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(3, text=self.column_titles[3], anchor=tk.CENTER)
        self.tree.column(3, width=int(130 / 860 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(4, text=self.column_titles[4], anchor=tk.CENTER)
        self.tree.column(4, width=int(130 / 860 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(5, text=self.column_titles[5], anchor=tk.CENTER)
        self.tree.column(5, width=int(130 / 860 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        # اضافه‌کردن داده‌های نمونه با tag
        for i, item in enumerate(car_sample_data):
            self.add_row((cc.eng_to_persian_date(str(i + 1)),
                        cc.car_id_true_format(cc.eng_to_persian_date(item["car_id"])),
                        cc.eng_to_persian_date(item["owner_name"]),
                        cc.make_string_arr(item["driver_name"]),
                        cc.eng_to_persian_date(item["start_date"]),
                        cc.eng_to_persian_date(item["end_date"])))

        # هَوِر ساده روی ردیف های جدول (بدون transition)
        self._last_hovered = None

        def on_tree_motion(event):
            row = self.tree.identify_row(event.y)
            if row != self._last_hovered:
                # ردیف قبلی رو به رنگ عادی برگردون
                if self._last_hovered is not None and self.tree.exists(self._last_hovered):
                    self.tree.tag_configure(f"hover_{self._last_hovered}", background=colors.light_green_5)
                # ردیف جدید رو رنگ hover بده
                if row and self.tree.exists(row):
                    self.tree.tag_configure(f"hover_{row}", background=colors.green_2)
                self._last_hovered = row

        def on_tree_leave(event):
            if self._last_hovered and self.tree.exists(self._last_hovered):
                self.tree.tag_configure(f"hover_{self._last_hovered}", background=colors.light_green_5)
            self._last_hovered = None

        self.tree.bind("<Motion>", on_tree_motion)
        self.tree.bind("<Leave>", on_tree_leave)
        self.tree.bind("<<TreeviewSelect>>", on_item_select)
        self.tree.bind("<Double-1>", lambda e: self.edit_car())

        #اجزای صفحه
        ck.make_label(main_box, 150, 50, colors.white, colors.white, colors.black, "اطلاعات ماشین ها", 0, 
                      None, (None, 45, "bold"), 0.5, 0.1, "center")
        
        ck.make_button(main_box, "ثبت ماشین جدید", 200, 45, (None, 22, "bold"), 20, 
                       colors.white, colors.white, colors.dark_green_5, colors.green_3,
                       self.register_car, 0.98, 0.05, "ne")
        ck.make_button(main_box, "مشاهده آرشیو نفتکش‌ها", 200, 45, (None, 22, "bold"), 20, 
                       colors.white, colors.white, colors.dark_green_5, colors.green_3,
                       self.go_to_archive, 0.98, 0.14, "ne")
        
        delete_bol_btn = ck.make_button(main_box, "آرشیو ماشین", 150, 50, (None, 22, "bold"), 20,
                       colors.light_gray_6, colors.white, colors.light_gray_1, colors.green_3,
                       self.archive_car, 0.98, 0.94, "e")
        delete_bol_btn.configure(state="disabled")
        
        ck.make_button(main_box, "چاپ نفتکش‌ها", 150, 50, (None, 22, "bold"), 20, 
                       colors.white, colors.white, colors.dark_green_5, colors.green_3,
                       lambda: cc.print_group(car_sample_data), 0.84, 0.94, "e")
        
        ck.make_button(main_box, "بازگشت", 150, 50, (None, 22, "bold"), 20,
                       colors.white, colors.white, colors.dark_green_5, colors.green_3,
                       go_to_dashboard1, 0.075, 0.94, "center")
        
        # لوگو
        ck.make_image(main_box, asset_paths.Logo_path, 88, 90, 0.02, 0.04, "nw")