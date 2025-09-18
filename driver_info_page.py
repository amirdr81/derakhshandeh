#main libraries
import customtkinter as ctk
import tkinter.ttk as ttk
import tkinter as tk
from PIL import Image, ImageTk

#data imports
import asset_paths
from bol_fake_data import driver_sample_data, old_drivers

#controllers
import common_controller as cc
import common_ctk as ck
import register_controller as rc

#colors
import colors


class DriverInfo(ctk.CTkFrame):  
    def edit_driver(self):
        selected_data = driver_sample_data[int(self.tree.item(self.tree.selection()[0], 'values')[0]) - 1]
        
        edit_box = ck.make_frame(self, 600, 400, colors.dark_green_6, colors.dark_green_6, colors.dark_green_6, 0, 0, 0.5, 0.5, "center")
        ck.make_label(edit_box, 150, 50, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "مشاهده/ویرایش اطلاعات راننده", 0, None, (None, 30, "bold"), 0.5, 0.1, "center")
        
        #نام راننده
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "نام راننده:", 0, None, (None, 20), 0.97, 0.25, "e")
        name_entry = ck.make_entry(edit_box, 130, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.84, 0.25, "e")
        ck.make_entry_with_text(name_entry, selected_data["name"])
        
        #نام خانوادگی راننده
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "نام‌خانوادگی راننده:", 0, None, (None, 20), 0.5, 0.25, "e")
        lastname_entry = ck.make_entry(edit_box, 130, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.03, 0.25, "w")
        ck.make_entry_with_text(lastname_entry, selected_data["lastname"])
        
        #کد ملی راننده
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "کد ملی:", 0, None, (None, 20), 0.97, 0.35, "e")
        id_entry = ck.make_entry(edit_box, 140, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.84, 0.35, "e")
        ck.make_entry_with_text(id_entry, selected_data["id"])
        
        #شماره تماس
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "شماره تماس:", 0, None, (None, 20), 0.5, 0.35, "e")
        phone_entry = ck.make_entry(edit_box, 170, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.03, 0.35, "w")
        ck.make_entry_with_text(phone_entry, selected_data["phone"])
        
        #هوشمند راننده
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "هوشمند راننده:", 0, None, (None, 20), 0.97, 0.45, "e")
        smart_id_entry = ck.make_entry(edit_box, 150, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.5, 0.45, "w")
        ck.make_entry_with_text(smart_id_entry, selected_data["smart_id"])
        
        #شماره گواهینامه
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "شماره گواهینامه:", 0, None, (None, 20), 0.97, 0.55, "e")
        licence_id_entry = ck.make_entry(edit_box, 140, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.75, 0.55, "e")
        ck.make_entry_with_text(licence_id_entry, selected_data["licence_id"])
        
        #تاریخ شروع و پایان اعتبار هوشمند راننده
        ck.make_label(edit_box, 100, 50, 
                      colors.dark_green_6, colors.dark_green_6, colors.white, 
                      "تاریخ شروع اعتبار هوشمند: " + cc.eng_to_persian_date(selected_data["start_smart_date"])
                      , 0, None, (None, 20), 0.5, 0.65, "center")
        ck.make_label(edit_box, 100, 50, 
                      colors.dark_green_6, colors.dark_green_6, colors.white, 
                      "تاریخ پایان اعتبار هوشمند: " + cc.eng_to_persian_date(selected_data["end_smart_date"])
                      , 0, None, (None, 20), 0.5, 0.75, "center")
        
        #دکمه ها
        #دکمه ثبت
        ck.make_button(edit_box, "ثبت اطلاعات", 150, 35, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, 
                       lambda: rc.edit_driver(selected_data, 
                                              name_entry,
                                                lastname_entry,
                                                id_entry,
                                                phone_entry,
                                                smart_id_entry,
                                                licence_id_entry,
                                                selected_data["start_smart_date"],
                                                selected_data["end_smart_date"],
                                                edit_box,
                                                self.reset_page),
                       0.96, 0.95, "se")
        
        #دکمه تمدید اعتبار
        ck.make_button(edit_box, "تمدید اعتبار هوشمند", 200, 35, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, 
                       lambda: rc.extend_smart_driver(edit_box, "تمدید اعتبار هوشمند راننده", selected_data), 
                       0.69, 0.95, "se")
        
        #دکمه بستن
        ck.make_button(edit_box, "بستن", 100, 35, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, lambda: edit_box.destroy(), 
                       0.04, 0.95, "sw")
        
        
    def register_driver(self):
        register_box = ck.make_frame(self, 600, 400, colors.dark_green_6, colors.dark_green_6, colors.dark_green_6, 0, 0, 0.5, 0.5, "center")
        
        ck.make_label(register_box, 200, 50, colors.dark_green_6, colors.dark_green_6, colors.white,
                          "ثبت‌نام راننده", 0, "center", (None, 35, "bold"), 0.5, 0.1, "center")
        name = ck.make_entry(register_box, 200, 40, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "نام", colors.gray_2, 20, "right", (None, 15), 0.9, 0.3, "e")
        lastname = ck.make_entry(register_box, 200, 40, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "نام خانوادگی", colors.gray_2, 20, "right", (None, 15), 0.45, 0.3, "e")
        id = ck.make_entry(register_box, 200, 40, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "کد ملی", colors.gray_2, 20, "right", (None, 15), 0.9, 0.43, "e")
        phone = ck.make_entry(register_box, 200, 40, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "شماره تلفن", colors.gray_2, 20, "right", (None, 15), 0.45, 0.43, "e")
        smartID = ck.make_entry(register_box, 200, 40, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "شماره هوشمند", colors.gray_2, 20, "right", (None, 15), 0.9, 0.56, "e")
        licenceID = ck.make_entry(register_box, 200, 40, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "شماره گواهینامه", colors.gray_2, 20, "right", (None, 15), 0.45, 0.56, "e")
        start_smart_date = ck.make_button(register_box, "تاریخ شروع هوشمند", 200, 35, (None, 15), 20, 
                                          colors.gray_2, colors.dark_green_6,colors.white,colors.green_3, 
                                          lambda: ck.open_calendar(register_box, start_smart_date, 0.5, 0.5, colors.black), 0.9, 0.69, "e")
        
        end_smart_date = ck.make_button(register_box, "تاریخ پایان هوشمند", 200, 35, (None, 15), 20, 
                                          colors.gray_2, colors.dark_green_6,colors.white,colors.green_3, 
                                          lambda: ck.open_calendar(register_box, end_smart_date, 0.5, 0.5, colors.black), 0.45, 0.69, "e")
        
        
        ck.make_button(register_box, "بستن", 100, 35, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, lambda: register_box.destroy(), 
                       0.04, 0.95, "sw")
        
        ck.make_button(register_box, "ثبت‌نام", 100, 35, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, 
                       lambda: rc.register_driver(name,
                                                  lastname,
                                                  id,
                                                  phone,
                                                  smartID,
                                                  licenceID,
                                                  start_smart_date,
                                                  end_smart_date,
                                                  register_box,
                                                  self.reset_page), 
                       0.96, 0.95, "se")
        
        
    def archive_driver(self):
        selected_data = driver_sample_data[int(self.tree.item(self.tree.selection()[0], 'values')[0]) - 1]
        label = ck.make_label(self, 150, 25, 
                          colors.white, colors.white, colors.red_color,
                          "", 0, None, (None, 18, "bold"), 0.91, 0.36, "e")
        if(selected_data['car_id'] != None and selected_data['car_id'] != ''):
            ck.update_label_error(label, 2000, 'برای آرشیو راننده، ابتدا پلاک ماشین را حذف کنید!')
        else:
            def do_delete():
                driver_sample_data.remove(selected_data)
                old_drivers.append(selected_data)
                dialog.destroy()
                self.go_to_archive()
            def cancel(): 
                cc.activate_all_widgets(self)
                dialog.destroy()
            cc.disable_all_widgets(self)
            dialog = rc.show_confirmation_box(self, do_delete, cancel, "آیا از آرشیو کردن این راننده، مطمئن هستید؟", selected_data)
        
    def add_row(self, data_tuple):
        iid = self.tree.insert("", tk.END, values=data_tuple)
        self.tree.tag_configure(f"hover_{iid}", background=colors.light_green_5)
        self.tree.item(iid, tags=(f"hover_{iid}",))
        return iid

    def __init__(self, parent, go_to_dashboard1, go_to_archive, reset_page):
        super().__init__(parent)
        
        self.go_to_dashboard1 = go_to_dashboard1
        self.go_to_archive = go_to_archive
        self.reset_page = reset_page
        self.pack(fill="both", expand=True)
        self.configure(fg_color=colors.light_green_1)

        def on_item_select(event):
            selected = self.tree.selection()
            if selected: 
                delete_bol_btn.configure(state="normal", fg_color=colors.dark_green_6, text_color=colors.white)
            else: 
                delete_bol_btn.configure(state="disabled", fg_color=colors.light_gray_1, text_color=colors.light_gray_6)
        
        main_box = ck.make_frame(self, float(self.master.winfo_screenwidth() / 1.2), float(self.master.winfo_screenheight() / 1.5), 
                                 colors.white, colors.white, colors.white, 0, 0, 0.5, 0.5, "center")
        
        
        self.column_titles = ["ردیف", "نام", "نام خانوادگی", "کد ملی", "شماره تلفن", "شماره نفتکش", "شماره هوشمند", "شماره گواهینامه"]
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
        self.tree.column(0, width=int(50 / 1175 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(1, text=self.column_titles[1], anchor=tk.CENTER)
        self.tree.column(1, width=int(130 / 1175 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(2, text=self.column_titles[2], anchor=tk.CENTER)
        self.tree.column(2, width=int(130 / 1175 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(3, text=self.column_titles[3], anchor=tk.CENTER)
        self.tree.column(3, width=int(130 / 1175 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(4, text=self.column_titles[4], anchor=tk.CENTER)
        self.tree.column(4, width=int(130 / 1175 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(5, text=self.column_titles[5], anchor=tk.CENTER)
        self.tree.column(5, width=int(130 / 1175 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(6, text=self.column_titles[6], anchor=tk.CENTER)
        self.tree.column(6, width=int(130 / 1175 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(7, text=self.column_titles[7], anchor=tk.CENTER)
        self.tree.column(7, width=int(130 / 1175 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        # اضافه‌کردن داده‌های نمونه با tag
        for i, item in enumerate(driver_sample_data):
            carID = ''
            if(item["car_id"] == '' or item['car_id'] == None): carID = '-'
            else: carID = cc.eng_to_persian_date(cc.car_id_true_format(item["car_id"]))
            self.add_row((
                cc.eng_to_persian_date(str(i + 1)),
                cc.eng_to_persian_date(item["name"]),
                cc.eng_to_persian_date(item["lastname"]),
                cc.eng_to_persian_date(item["id"]),
                cc.eng_to_persian_date(item["phone"]),
                carID,
                cc.eng_to_persian_date(item["smart_id"]),
                cc.eng_to_persian_date(item["licence_id"])
            ))

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
        self.tree.bind("<Double-1>", lambda e: self.edit_driver())
        
        #اجزای صفحه
        ck.make_label(main_box, 150, 50, colors.white, colors.white, colors.black, "اطلاعات راننده ها", 0, 
                      None, (None, 45, "bold"), 0.5, 0.1, "center")
        
        ck.make_button(main_box, "ثبت راننده جدید", 200, 45, (None, 22, "bold"), 20, 
                       colors.white, colors.white, colors.dark_green_5, colors.green_3,
                       self.register_driver, 0.98, 0.05, "ne")
        ck.make_button(main_box, "مشاهده آرشیو راننده‌ها", 200, 45, (None, 22, "bold"), 20, 
                       colors.white, colors.white, colors.dark_green_5, colors.green_3,
                       self.go_to_archive, 0.98, 0.14, "ne")
        ck.make_button(main_box, "چاپ رانندگان", 150, 50, (None, 22, "bold"), 20, 
                       colors.white, colors.white, colors.dark_green_5, colors.green_3,
                       lambda: cc.print_group(driver_sample_data), 0.84, 0.94, "e")
        
        delete_bol_btn = ck.make_button(main_box, "آرشیو راننده", 150, 50, (None, 22, "bold"), 20,
                       colors.light_gray_6, colors.white, colors.light_gray_1, colors.green_3,
                       self.archive_driver, 0.98, 0.94, "e")
        delete_bol_btn.configure(state="disabled")
        
        ck.make_button(main_box, "بازگشت", 150, 50, (None, 22, "bold"), 20,
                       colors.white, colors.white, colors.dark_green_5, colors.green_3,
                       go_to_dashboard1, 0.075, 0.94, "center")
        
        # لوگو
        ck.make_image(main_box, asset_paths.Logo_path, 88, 90, 0.02, 0.04, "nw")