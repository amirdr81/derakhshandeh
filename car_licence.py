#main libraries
import customtkinter as ctk
import tkinter.ttk as ttk
import tkinter as tk
from PIL import Image, ImageTk

#data imports
import asset_paths
from bol_fake_data import car_licence, archived_car_licence

#controllers
import common_controller as cc
import common_ctk as ck
import register_controller as rc

#colors
import colors


class CarLicence(ctk.CTkFrame):
    def register_licence(self):
        register_box = ck.make_frame(self, 600, 400, colors.dark_green_6, colors.dark_green_6, colors.dark_green_6, 0, 0, 0.5, 0.5, "center")
        
        ck.make_label(register_box, 200, 50, colors.dark_green_6, colors.dark_green_6, colors.white,
                          "ثبت اطلاعات ماشین", 0, "center", (None, 35, "bold"), 0.5, 0.1, "center")
        licence_id = ck.make_entry(register_box, 200, 40, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "شماره گواهینامه", colors.gray_2, 20, "right", (None, 15), 0.9, 0.3, "e")
        start_date = ck.make_button(register_box, "تاریخ صدور", 150, 30, (None, 15), 20, 
                                          colors.gray_2, colors.dark_green_6,colors.white,colors.green_3, 
                                          lambda: ck.open_calendar(register_box, start_date, 0.5, 0.5, colors.black), 0.785, 0.56, "e")
        start_date.configure(text_color=colors.gray_2)
        end_date = ck.make_button(register_box, "تاریخ انقضا", 150, 30, (None, 15), 20, 
                                          colors.gray_2, colors.dark_green_6,colors.white,colors.green_3, 
                                          lambda: ck.open_calendar(register_box, end_date, 0.5, 0.5, colors.black), 0.5, 0.56, "e")
        end_date.configure(text_color=colors.gray_2)
        car_id = ck.make_entry(register_box, 280, 40, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "شماره انتظامی وسیله نقلیه و یدک آن", colors.gray_2, 20, "right", (None, 15), 0.53, 0.3, "e")
        sign = ck.make_entry(register_box, 280, 40, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "نام و نام‌خانوادگی امضاکننده", colors.gray_2, 20, "right", (None, 15), 0.5, 0.43, "center")
        
        #دکمه ها
        ck.make_button(register_box, "بستن", 100, 35, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, lambda: register_box.destroy(), 
                       0.04, 0.95, "sw")
        
        ck.make_button(register_box, "ثبت‌نام", 100, 35, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, 
                       lambda: rc.register_licence(licence_id,
                                               start_date,
                                                  end_date,
                                                  car_id,
                                                  sign,
                                                  register_box,
                                                  self.reset_page),   
                       0.96, 0.95, "se")
    def archive_car(self):
        selected_data = car_licence[int(self.tree.item(self.tree.selection()[0], 'values')[0]) - 1]
        def do_delete():
            car_licence.remove(selected_data)
            archived_car_licence.append(selected_data)
            dialog.destroy()
            self.reset_page()
        def cancel(): 
            cc.activate_all_widgets(self)
            dialog.destroy()
        cc.disable_all_widgets(self)
        dialog = rc.show_confirmation_box(self, do_delete, cancel, "آیا از آرشیو این گواهینامه، مطمئن هستید؟", selected_data)
            
    def reveiw_licence(self):
        selected_data = car_licence[int(self.tree.item(self.tree.selection()[0], 'values')[0]) - 1]
        
        edit_box = ck.make_frame(self, 600, 400, colors.dark_green_6, colors.dark_green_6, colors.dark_green_6, 0, 0, 0.5, 0.5, "center")
        ck.make_label(edit_box, 150, 50, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "مشاهده اطلاعات گواهینامه تأیید صلاحیت", 0, None, (None, 30, "bold"), 0.5, 0.1, "center")
        
        #پلاک ماشین
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "شماره گواهینامه: " + cc.eng_to_persian_date(selected_data["licence_id"]), 0, None, (None, 20), 0.94, 0.25, "e")
        
        #هوشمند نفتکش
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "تاریخ صدور: " + cc.eng_to_persian_date(selected_data["start_date"]), 0, None, (None, 20), 0.94, 0.35, "e")
        
        #نام مالک
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "تاریخ پایان اعتبار: " + cc.eng_to_persian_date(selected_data["end_date"]), 0, None, (None, 20), 0.47, 0.35, "e")
        
        #تاریخ شروع اندازه‌گیری
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "شماره انتظامی وسیله نقلیه و یدک آن: " + cc.car_id_true_format(cc.eng_to_persian_date(selected_data["car_id"])), 0, None, (None, 20), 0.94, 0.45, "e")
        
        #تاریخ پایان اندازه‌گیری
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "نام و نام‌خانوادگی صادر و امضا کننده: " + selected_data["sign"], 0, None, (None, 20), 0.94, 0.55, "e")
        
        #دکمه ها
        #دکمه تمدید اعتبار
        ck.make_button(edit_box, "تمدید اعتبار هوشمند", 200, 35, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, 
                       lambda: rc.extend_licence(edit_box, "تمدید اعتبار", selected_data), 
                       0.98, 0.95, "se")
        
        #دکمه آرشیو
        ck.make_button(edit_box, "آرشیو گواهینامه", 200, 35, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, 
                       self.archive_car, 
                       0.98, 0.85, "se")
        
        #دکمه بستن
        ck.make_button(edit_box, "بستن", 100, 35, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, lambda: edit_box.destroy(), 
                       0.04, 0.95, "sw")
    
    def add_row(self, data_tuple):
        iid = self.tree.insert("", tk.END, values=data_tuple)
        self.tree.tag_configure(f"hover_{iid}", background=colors.light_green_5)
        self.tree.item(iid, tags=(f"hover_{iid}",))
        return iid

    def __init__(self, parent, back_to_dashboard2, go_to_archive, reset_page):
        super().__init__(parent)
        
        self.pack(fill="both", expand=True)
        self.configure(fg_color=colors.light_green_1)
        self.back_to_dashboard2 = back_to_dashboard2
        self.go_to_archive = go_to_archive
        self.reset_page = reset_page
        
        main_box = ck.make_frame(self, float(self.master.winfo_screenwidth() / 1.2), float(self.master.winfo_screenheight() / 1.5), 
                                 colors.white, colors.white, colors.white, 0, 0, 0.5, 0.5, "center")
        
        self.column_titles = ["ردیف", "شماره گواهینمامه", "شماره انتظامی"]
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
        self.tree.column(0, width=int(50 / 400 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(1, text=self.column_titles[1], anchor=tk.CENTER)
        self.tree.column(1, width=int(130 / 400 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(2, text=self.column_titles[2], anchor=tk.CENTER)
        self.tree.column(2, width=int(130 / 400 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        # اضافه‌کردن داده‌های نمونه با tag
        for i, item in enumerate(car_licence):
            self.add_row((cc.eng_to_persian_date(str(i + 1)),
                        cc.eng_to_persian_date(item["licence_id"]),
                        cc.car_id_true_format(cc.eng_to_persian_date(item["car_id"]))))

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
        self.tree.bind("<Double-1>", lambda e: self.reveiw_licence())

        ck.make_button(main_box, "ثبت گواهینامه جدید", 200, 45, (None, 22, "bold"), 20, 
                       colors.white, colors.white, colors.dark_green_5, colors.green_3,
                       self.register_licence, 0.98, 0.05, "ne")
        
        ck.make_button(main_box, "مشاهده آرشیو گواهینامه‌ها", 200, 45, (None, 22, "bold"), 20, 
                       colors.white, colors.white, colors.dark_green_5, colors.green_3,
                       self.go_to_archive, 0.98, 0.14, "ne")
        
        ck.make_label(main_box, 150, 50, colors.white, colors.white, colors.black, "گواهینامه تأیید صلاحیت", 0, 
                      None, (None, 45, "bold"), 0.5, 0.1, "center")
        
        ck.make_button(main_box, "بازگشت", 150, 50, (None, 22, "bold"), 20,
                       colors.white, colors.white, colors.dark_green_5, colors.green_3,
                       back_to_dashboard2, 0.075, 0.94, "center")
        
        # لوگو
        ck.make_image(main_box, asset_paths.Logo_path, 88, 90, 0.02, 0.04, "nw")