#main libraries
import customtkinter as ctk
import tkinter.ttk as ttk
import tkinter as tk
from PIL import Image, ImageTk

#data imports
import asset_paths
from bol_fake_data import workcart, archived_workcart

#controllers
import common_controller as cc
import common_ctk as ck
import register_controller as rc

#colors
import colors


class WorkcartPage(ctk.CTkFrame):
    def register_workcart(self):
        register_box = ck.make_frame(self, 600, 300, colors.dark_green_6, colors.dark_green_6, colors.dark_green_6, 0, 0, 0.5, 0.5, "center")
        
        ck.make_label(register_box, 200, 50, colors.dark_green_6, colors.dark_green_6, colors.white,
                          "ثبت کارت تردد", 0, "center", (None, 35, "bold"), 0.5, 0.1, "center")
        
        name = ck.make_entry(register_box, 200, 40, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "نام و نام خانوادگی", colors.gray_2, 20, "right", (None, 15), 0.9, 0.35, "e")
        id = ck.make_entry(register_box, 200, 40, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "کد ملی", colors.gray_2, 20, "right", (None, 15), 0.5, 0.35, "e")
        
        car = ck.make_entry(register_box, 200, 40, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "شماره نتفکش", colors.gray_2, 20, "right", (None, 15), 0.9, 0.525, "e")
        serial = ck.make_entry(register_box, 200, 40, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "سریال", colors.gray_2, 20, "right", (None, 15), 0.5, 0.525, "e")
        
        start_date = ck.make_button(register_box, "تاریخ صدور", 200, 38, (None, 15), 20, 
                                          colors.gray_2, colors.dark_green_6,colors.white,colors.green_3, 
                                          lambda: ck.open_calendar(register_box, start_date, 0.5, 0.5, colors.black), 0.9, 0.7, "e")
        start_date.configure(text_color=colors.gray_2)
        
        end_date = ck.make_button(register_box, "تاریخ انقضا", 200, 38, (None, 15), 20, 
                                          colors.gray_2, colors.dark_green_6,colors.white,colors.green_3, 
                                          lambda: ck.open_calendar(register_box, end_date, 0.5, 0.5, colors.black), 0.5, 0.7, "e")
        end_date.configure(text_color=colors.gray_2)
        
        
        ck.make_button(register_box, "بستن", 100, 35, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, lambda: register_box.destroy(), 
                       0.04, 0.95, "sw")
        
        ck.make_button(register_box, "ثبت‌نام", 100, 35, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, 
                       lambda: rc.register_workcart(name,
                                                    id,
                                                  car,
                                                  start_date,
                                                  end_date,
                                                  serial,
                                                  register_box,
                                                  self.reset_page), 
                       0.96, 0.95, "se")
    
    def archive_car(self):
        selected_data = workcart[int(self.tree.item(self.tree.selection()[0], 'values')[0]) - 1]
        def do_delete():
            workcart.remove(selected_data)
            archived_workcart.append(selected_data)
            dialog.destroy()
            self.reset_page()
        def cancel(): dialog.destroy()
        
        dialog = rc.show_confirmation_box(self, do_delete, cancel, "آیا از آرشیو این کارت تردد، مطمئن هستید؟", selected_data)
        
    def add_row(self, data_tuple):
        iid = self.tree.insert("", tk.END, values=data_tuple)
        self.tree.tag_configure(f"hover_{iid}", background=colors.light_green_5)
        self.tree.item(iid, tags=(f"hover_{iid}",))
        return iid
    
    def __init__(self, parent, back_to_dashboard2, go_to_archive, reset_page):
        super().__init__(parent)
        
        self.pack(fill="both", expand=True)
        self.configure(fg_color=colors.light_green_1)
        
        main_box = ck.make_frame(self, float(self.master.winfo_screenwidth() / 1.2), float(self.master.winfo_screenheight() / 1.5), 
                                 colors.white, colors.white, colors.white, 0, 0, 0.5, 0.5, "center")
        
        self.back_to_dashboard2 = back_to_dashboard2
        self.go_to_archive = go_to_archive
        self.reset_page = reset_page
        
        main_box = ck.make_frame(self, float(self.master.winfo_screenwidth() / 1.2), float(self.master.winfo_screenheight() / 1.5), 
                                 colors.white, colors.white, colors.white, 0, 0, 0.5, 0.5, "center")
        
        self.column_titles = ["ردیف", "نام راننده", "کد ملی", 'پلاک ماشین', 'تاریخ شروع', 'تاریخ انقضا', 'سریال']
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
        self.tree.column(0, width=int(50 / 1050 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(1, text=self.column_titles[1], anchor=tk.CENTER)
        self.tree.column(1, width=int(130 / 1050 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(2, text=self.column_titles[2], anchor=tk.CENTER)
        self.tree.column(2, width=int(130 / 1050 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(3, text=self.column_titles[3], anchor=tk.CENTER)
        self.tree.column(3, width=int(130 / 1050 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(4, text=self.column_titles[4], anchor=tk.CENTER)
        self.tree.column(4, width=int(130 / 1050 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(5, text=self.column_titles[5], anchor=tk.CENTER)
        self.tree.column(5, width=int(130 / 1050 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(6, text=self.column_titles[6], anchor=tk.CENTER)
        self.tree.column(6, width=int(130 / 1050 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        # اضافه‌کردن داده‌های نمونه با tag
        for i, item in enumerate(workcart):
            self.add_row((cc.eng_to_persian_date(str(i + 1)),
                        cc.eng_to_persian_date(item["driver_name"]),
                        cc.eng_to_persian_date(item["driver_id"]),
                        cc.car_id_true_format(cc.eng_to_persian_date(item["car_id"])),
                        cc.eng_to_persian_date(item["start_date"]),
                        cc.eng_to_persian_date(item["end_date"]),
                        cc.eng_to_persian_date(item["serial_number"])))

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

        def on_item_select(event):
            selected = self.tree.selection()
            if selected: 
                archive_btn.configure(state="normal", fg_color=colors.dark_green_6, text_color=colors.white)
            else: 
                archive_btn.configure(state="disabled", fg_color=colors.light_gray_1, text_color=colors.light_gray_6)
                
        self.tree.bind("<Motion>", on_tree_motion)
        self.tree.bind("<Leave>", on_tree_leave)
        self.tree.bind("<<TreeviewSelect>>", on_item_select)
        
        ck.make_label(main_box, 150, 50, colors.white, colors.white, colors.black, "کارت تردد", 0, 
                      None, (None, 45, "bold"), 0.5, 0.1, "center")
        
        ck.make_button(main_box, "ثبت کارت تردد جدید", 200, 45, (None, 22, "bold"), 20, 
                       colors.white, colors.white, colors.dark_green_5, colors.green_3,
                       self.register_workcart, 0.98, 0.05, "ne")
        
        ck.make_button(main_box, "مشاهده آرشیو کارت‌های تردد", 200, 45, (None, 22, "bold"), 20, 
                       colors.white, colors.white, colors.dark_green_5, colors.green_3,
                       go_to_archive, 0.98, 0.14, "ne")
        
        archive_btn = ck.make_button(main_box, "آرشیو کارت تردد", 150, 50, (None, 22, "bold"), 20,
                       colors.white, colors.white, colors.dark_green_5, colors.green_3,
                       self.archive_car, 0.98, 0.94, "e")
        archive_btn.configure(state="disabled", fg_color=colors.light_gray_1, text_color=colors.light_gray_6)
        
        ck.make_button(main_box, "بازگشت", 150, 50, (None, 22, "bold"), 20,
                       colors.white, colors.white, colors.dark_green_5, colors.green_3,
                       back_to_dashboard2, 0.075, 0.94, "center")
        
        # لوگو
        ck.make_image(main_box, asset_paths.Logo_path, 88, 90, 0.02, 0.04, "nw")