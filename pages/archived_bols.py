import customtkinter as ctk
import tkinter.ttk as ttk
import tkinter as tk
from bol_fake_data import old_bols
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox
from bol_inf import BolInf
from edit_bol_page import EditBol
import common_controller as cc
import common_ctk as ck
import asset_paths
import colors

class ArchivedBols(ctk.CTkFrame):      
    def __init__(self, parent, back_to_view_bol):
        super().__init__(parent)
        
        self.pack(fill="both", expand=True)
        self.configure(fg_color=colors.light_green_1)
        self.back_to_view_bol = back_to_view_bol
        self.shown_data = old_bols
        
        def add_row(data_tuple):
            iid = self.tree.insert("", tk.END, values=data_tuple)
            self.tree.tag_configure(f"hover_{iid}", background=colors.light_green_5)
            self.tree.item(iid, tags=(f"hover_{iid}",))
            return iid
    
        main_box = ctk.CTkFrame(self, width=float(self.master.winfo_screenwidth() / 1.2), 
                                height=float(self.master.winfo_screenheight() / 1.5), 
                                fg_color=colors.white,
                                corner_radius=0)
        main_box.place(relx=0.5, rely=0.5, anchor="center")
        
        # self.column_titles = ["ردیف", "شماره بارنامه", "نوع فرآورده", "مبدأ", "مقصد", "شماره نفتکش", "وزن محموله"]
        self.column_titles = ["ردیف", "شماره بارنامه", "قرارداد", "شماره حواله", "مقصد", "شماره نفتکش", "فرآورده"]
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
                                 selectmode="extended")

        tree_scrollbar_y.config(command=self.tree.yview)
        tree_scrollbar_y.grid(row=0, column=1, sticky="ns")
        self.tree.grid(row=0, column=0, sticky="nsew")
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)
        
        table_width = self.tree.winfo_screenwidth() 

        self.tree.heading(0, text=self.column_titles[0], anchor=tk.CENTER)
        self.tree.column(0, width=int(47 / 1212 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(1, text=self.column_titles[1], anchor=tk.CENTER)
        self.tree.column(1, width=int(127 / 1212 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(2, text=self.column_titles[2], anchor=tk.CENTER)
        self.tree.column(2, width=int(147 / 1212 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(3, text=self.column_titles[3], anchor=tk.CENTER)
        self.tree.column(3, width=int(97 / 1212 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(4, text=self.column_titles[4], anchor=tk.CENTER)
        self.tree.column(4, width=int(297 / 1212 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(5, text=self.column_titles[5], anchor=tk.CENTER)
        self.tree.column(5, width=int(147 / 1212 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(6, text=self.column_titles[6], anchor=tk.CENTER)
        self.tree.column(6, width=int(127 / 1212 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)

        # اضافه‌کردن داده‌های نمونه با tag
        for i, item in enumerate(self.shown_data): 
            add_row((cc.eng_to_persian_date(str(i + 1)), 
                    cc.eng_to_persian_date(item["load_id"]), 
                    cc.eng_to_persian_date(item["deal"]), 
                    cc.eng_to_persian_date(item["cash_id"]), 
                    cc.eng_to_persian_date(item["des_location"]), 
                    cc.car_id_true_format(item["car_id"]), 
                    cc.eng_to_persian_date(item["load_name"])))

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

        sign_in_label = ctk.CTkLabel(main_box, text="آرشیو بارنامه‌ها", font=(None, 45, "bold"), text_color=colors.black, bg_color=colors.white)
        sign_in_label.place(relx=0.5, rely=0.1, anchor="center")
        
        back_to_dashboard_btn = ctk.CTkButton(main_box, text="بازگشت", 
                                   width=150, height=50, 
                                   font=(None, 22, "bold"), 
                                   corner_radius=20, 
                                   text_color=colors.white, 
                                   bg_color=colors.white, 
                                   fg_color=colors.dark_green_5, 
                                   hover_color=colors.green_3,
                                   command=back_to_view_bol)
        back_to_dashboard_btn.place(relx=0.075, rely=0.94, anchor="center")
        
        def update_bol_box(event):
            b_type = self.deal.get()
            if(b_type == 'بارنامه‌های صورت‌شده'): self.shown_data = cc.get_grouped_bols()
            elif(b_type == 'بارنامه‌های آرشیوشده'): self.shown_data = [item for item in old_bols if item not in cc.get_grouped_bols()]
            elif(b_type == 'همه بارنامه‌ها'): self.shown_data = old_bols
            else: self.shown_data = old_bols
            
            for child in self.tree.get_children(): self.tree.delete(child)
            for i, item in enumerate(self.shown_data):
                add_row((
                            cc.eng_to_persian_date(str(i + 1)),
                            cc.eng_to_persian_date(item["load_id"]),
                            cc.eng_to_persian_date(item["load_name"]),
                            cc.eng_to_persian_date(item["start_location"]),
                            cc.eng_to_persian_date(item["des_location"]),
                            cc.eng_to_persian_date(cc.car_id_true_format(item["car_id"])),
                            cc.eng_to_persian_date(item["load_weight"])
                ))
            
        #انتخاب نوع بارنامه
        self.deal = ck.make_list(main_box, "همه بارنامه‌ها", ['بارنامه‌های صورت‌شده', 'بارنامه‌های آرشیوشده', 'همه بارنامه‌ها'], 150, 30, colors.black,
                     colors.white, colors.light_green_2, colors.green_4, colors.green_1, 20, 
                     update_bol_box, "e", 0.985, 0.28, "e")
        
        # لوگو
        ck.make_image(main_box, asset_paths.Logo_path, 88, 90, 0.02, 0.04, "nw")
        
        def open_bol():
            global bol_frame
            try: bol_frame.destroy()
            except: pass
            bol_frame = ck.make_frame(self, float(self.master.winfo_screenwidth() / 1.3), float(self.master.winfo_screenheight() / 2.5),
                                      colors.light_green_1, colors.light_green_1, colors.light_green_1, 0, 0, 0.5, 0.5, "center")

            bol = self.shown_data[int(self.tree.item(self.tree.selection()[0], 'values')[0]) - 1]
            cal = BolInf(bol_frame, back_to_view_bol, bol)
            cal.place(relx=0.5, rely=0.5, anchor="center")
            
            ck.make_button(bol_frame, 'بستن', 120, 30, (None, 25), 60, colors.light_green_1,
                           colors.light_green_1, colors.dark_green_6, colors.green_3,
                           lambda: bol_frame.destroy(), 0.075, 0.91, "center")
        def on_item_select(event):
            if self.tree.selection(): open_bol()
        self.tree.bind("<Double-1>", on_item_select)
        