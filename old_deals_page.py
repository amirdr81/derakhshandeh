import customtkinter as ctk
import tkinter.ttk as ttk
import tkinter as tk
from PIL import Image, ImageTk
import asset_paths
from insystem_data import old_deals
from bol_fake_data import current_bols
from date import Date
from bol_inf import BolInf
import common_controller as cc
import common_ctk as ck
import colors


class oldDeals(ctk.CTkFrame):
    def __init__(self, parent, go_to_register_deal):
        super().__init__(parent)
        self.go_to_register_deal = go_to_register_deal
        self.bols_title = ""
        
        self.pack(fill="both", expand=True)
        self.configure(fg_color=colors.light_green_1)

        def open_bol(NewPage, wid):
            global bol_frame
            try: bol_frame.destroy()
            except: pass
            bol_frame = ctk.CTkFrame(self, fg_color=colors.light_green_1,
                                     width=float(self.master.winfo_screenwidth() / 1.3), 
                                     height=float(self.master.winfo_screenheight() / wid))
            bol_frame.place(relx=0.5, rely=0.5, anchor="center")

            cal = NewPage(bol_frame, None, current_bols[int(self.tree.item(self.tree.selection()[0], 'values')[0]) - 1])
            cal.place(relx=0.5, rely=0.5, anchor="center")
            
            def do_delete(): 
                bol_frame.destroy()
            close_btn = ctk.CTkButton(bol_frame, text="بستن", 
                                        width=120,
                                        height=30, 
                                        font=(None, 25),
                                        bg_color=colors.light_green_1, 
                                        corner_radius=60,
                                    fg_color=colors.dark_green_6,
                                    text_color=colors.light_green_1,
                                    hover_color=colors.green_3,
                                    command=do_delete)
            close_btn.place(relx=0.075, rely=0.91, anchor="center")
            
        #باکس اصلی
        main_box = ctk.CTkFrame(self, width=float(self.master.winfo_screenwidth() / 1.2), 
                                height=float(self.master.winfo_screenheight() / 1.5), 
                                fg_color=colors.white,
                                corner_radius=0)
        main_box.place(relx=0.5, rely=0.5, anchor="center")
        
        # عنوان
        main_label = ctk.CTkLabel(main_box, text="قرارداد های قدیمی", font=(None, 45, "bold"), text_color=colors.black, bg_color=colors.white)
        main_label.place(relx=0.5, rely=0.1, anchor="center")
        
        #مشخصات جدول
        def add_row(data_tuple):
            iid = self.tree.insert("", tk.END, values=data_tuple)
            self.tree.tag_configure(f"hover_{iid}", background=colors.light_green_5)
            self.tree.item(iid, tags=(f"hover_{iid}",))
            return iid
    
    
        self.column_titles = ["ردیف", "نام شرکت", "شماره قرارداد", "نام کالا/محموله", "فی شرکت", "فی راننده", "تاریخ شروع قرارداد", "تاریخ پایان قرارداد"]
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
                        font=(None, 10, "bold"),
                        padding=(5, 5))

        # رنگ ردیف انتخاب شده
        style.map("Treeview",
                  background=[("selected", selected_color)],
                  foreground=[("selected", "white")])

        tree_frame = ctk.CTkFrame(main_box)
        tree_frame.place(relx=0.5, rely=0.55, anchor="center")

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
        self.tree.column(0, width=int(47 / 1220 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(1, text=self.column_titles[1], anchor=tk.CENTER)
        self.tree.column(1, width=int(145 / 1220 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(2, text=self.column_titles[2], anchor=tk.CENTER)
        self.tree.column(2, width=int(125 / 1220 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(3, text=self.column_titles[3], anchor=tk.CENTER)
        self.tree.column(3, width=int(120 / 1220 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(4, text=self.column_titles[4], anchor=tk.CENTER)
        self.tree.column(4, width=int(100 / 1220 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(5, text=self.column_titles[5], anchor=tk.CENTER)
        self.tree.column(5, width=int(147 / 1220 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(6, text=self.column_titles[6], anchor=tk.CENTER)
        self.tree.column(6, width=int(127 / 1220 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(7, text=self.column_titles[7], anchor=tk.CENTER)
        self.tree.column(7, width=int(127 / 1220 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)

        # اضافه‌کردن داده‌های نمونه با tag
        for i, item in enumerate(old_deals): 
            add_row((cc.eng_to_persian_date(str(i + 1)),
                                         cc.eng_to_persian_date(item["name"]), 
                                    cc.eng_to_persian_date(item["id"]), 
                                    cc.eng_to_persian_date(item["load_name"]), 
                                    cc.eng_to_persian_date(item["fee_company"]), 
                                    cc.eng_to_persian_date(item["fee_driver"]), 
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

        
        # دکمه خروج
        back_to_dashboard_btn = ctk.CTkButton(main_box, text="بازگشت", 
                                   width=100, height=50, 
                                   font=(None, 22, "bold"), 
                                   corner_radius=20, 
                                   text_color=colors.white, 
                                   bg_color=colors.white, 
                                   fg_color=colors.dark_green_6, 
                                   hover_color=colors.green_2,
                                   command=go_to_register_deal)
        back_to_dashboard_btn.place(relx=0.07, rely=0.92, anchor="center")
        # لوگو
        ck.make_image(main_box, asset_paths.Logo_path, 88, 90, 0.02, 0.04, "nw")
        