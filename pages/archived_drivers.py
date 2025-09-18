#main libraries
import customtkinter as ctk
import tkinter.ttk as ttk
import tkinter as tk
from PIL import Image, ImageTk

#data imports
import asset_paths
from bol_fake_data import old_drivers

#controllers
import common_controller as cc
import common_ctk as ck
import register_controller as rc

#colors
import colors


class ArchivedDrivers(ctk.CTkFrame):  
    def reveiw_driver(self):
        selected_data = old_drivers[int(self.tree.item(self.tree.selection()[0], 'values')[0]) - 1]
        
        edit_box = ck.make_frame(self, 600, 400, colors.dark_green_6, colors.dark_green_6, colors.dark_green_6, 0, 0, 0.5, 0.5, "center")
        ck.make_label(edit_box, 150, 50, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "مشاهده/ویرایش اطلاعات راننده", 0, None, (None, 30, "bold"), 0.5, 0.1, "center")
        
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
        
        
    def add_row(self, data_tuple):
        iid = self.tree.insert("", tk.END, values=data_tuple)
        self.tree.tag_configure(f"hover_{iid}", background=colors.light_green_5)
        self.tree.item(iid, tags=(f"hover_{iid}",))
        return iid

    def __init__(self, parent, go_to_drivers, reset_page):
        super().__init__(parent)
        
        self.go_to_drivers = go_to_drivers
        self.reset_page = reset_page
        self.pack(fill="both", expand=True)
        self.configure(fg_color=colors.light_green_1)
        
        
        main_box = ck.make_frame(self, float(self.master.winfo_screenwidth() / 1.2), float(self.master.winfo_screenheight() / 1.5), 
                                 colors.white, colors.white, colors.white, 0, 0, 0.5, 0.5, "center")
        
        ck.make_button(main_box, "چاپ رانندگان", 150, 45, (None, 22, "bold"), 20, 
                       colors.white, colors.white, colors.dark_green_5, colors.green_3,
                       lambda: cc.print_group(old_drivers), 0.98, 0.23, "ne")
        
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
        for i, item in enumerate(old_drivers):
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
        self.tree.bind("<Double-1>", lambda e: self.reveiw_driver())
        
        #اجزای صفحه
        ck.make_label(main_box, 150, 50, colors.white, colors.white, colors.black, "آرشیو رانندگان", 0, 
                      None, (None, 45, "bold"), 0.5, 0.1, "center")
        
        ck.make_button(main_box, "بازگشت", 150, 50, (None, 22, "bold"), 20,
                       colors.white, colors.white, colors.dark_green_5, colors.green_3,
                       go_to_drivers, 0.075, 0.94, "center")
        
        # لوگو
        ck.make_image(main_box, asset_paths.Logo_path, 88, 90, 0.02, 0.04, "nw")