#main import
import customtkinter as ctk
import tkinter.ttk as ttk
import tkinter as tk

#data import
import asset_paths
from bol_fake_data import startpoint_sample_data
from insystem_data import current_deals
from suggestion_list import SuggestionList

#controllers
import common_controller as cc
import common_ctk as ck
import register_controller as rc

#colors
import colors


class StartPointInfo(ctk.CTkFrame):
    def edit_startpoint(self):
        selected_data = startpoint_sample_data[int(self.tree.item(self.tree.selection()[0], 'values')[0]) - 1]
        
        edit_box = ck.make_frame(self, 600, 250, colors.dark_green_6, colors.dark_green_6, colors.dark_green_6, 0, 0, 0.5, 0.5, "center")
        ck.make_label(edit_box, 150, 50, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "مشاهده/ویرایش اطلاعات مبدأ", 0, None, (None, 30, "bold"), 0.5, 0.1, "center")
        
        #کد مبدأ
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "کد مبدأ:", 0, None, (None, 20), 0.97, 0.3, "e")
        id_entry = ck.make_entry(edit_box, 170, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.85, 0.3, "e")
        ck.make_entry_with_text(id_entry, selected_data["id"])
        
        #نام مبدأ
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "نام مبدأ:", 0, None, (None, 20), 0.5, 0.3, "e")
        name_entry = ck.make_entry(edit_box, 210, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.38, 0.3, "e")
        ck.make_entry_with_text(name_entry, selected_data["name"])
        
        #آدرس مبدأ
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "آدرس مبدأ:", 0, None, (None, 20), 0.97, 0.48, "e")
        address_entry = ck.make_entry(edit_box, 470, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.81, 0.48, "e")
        ck.make_entry_with_text(address_entry, selected_data["address"])
        
        #نام قرارداد
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "نام قرارداد:", 0, None, (None, 20), 0.97, 0.66, "e")
        deal_name = ck.make_entry(edit_box, 180, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.82, 0.66, "e")
        ck.make_entry_with_text(deal_name, selected_data["deal"]['name'])
        
        #شماره قرارداد
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "شماره قرارداد:", 0, None, (None, 20), 0.5, 0.66, "e")
        deal_id = ck.make_entry(edit_box, 165, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.3, 0.66, "e")
        ck.make_entry_with_text(deal_id, selected_data["deal"]['id'])
        
        #دکمه ها
        #دکمه ثبت
        ck.make_button(edit_box, "ثبت اطلاعات", 150, 35, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, 
                       lambda: rc.edit_startpoint(selected_data, 
                                                name_entry,
                                              id_entry,
                                                address_entry,
                                                deal_name, 
                                                deal_id,
                                                edit_box,
                                                self.reset_page),   
                       0.96, 0.95, "se")
        
        #دکمه بستن
        ck.make_button(edit_box, "بستن", 100, 35, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, lambda: edit_box.destroy(), 
                       0.04, 0.95, "sw")
        
    def register_startpoint(self):
        register_box = ck.make_frame(self, 600, 250, colors.dark_green_6, colors.dark_green_6, colors.dark_green_6, 0, 0, 0.5, 0.5, "center")
        
        ck.make_label(register_box, 200, 50, colors.dark_green_6, colors.dark_green_6, colors.white,
                          "ثبت اطلاعات مبدأ", 0, "center", (None, 35, "bold"), 0.5, 0.1, "center")
        
        id = ck.make_entry(register_box, 200, 30, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "کد مبدأ", colors.gray_2, 20, "right", (None, 15), 0.9, 0.3, "e")
        name = ck.make_entry(register_box, 200, 30, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "نام مبدأ", colors.gray_2, 20, "right", (None, 15), 0.45, 0.3, "e")
        address = ck.make_entry(register_box, 470, 30, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "آدرس مبدأ", colors.gray_2, 20, "right", (None, 15), 0.9, 0.45, "e")
        deal_name = ck.make_entry(register_box, 200, 30, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "نام قرارداد", colors.gray_2, 20, "right", (None, 15), 0.9, 0.6, "e")
        deal_id = ck.make_entry(register_box, 200, 30, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "شماره قرارداد", colors.gray_2, 20, "right", (None, 15), 0.45, 0.6, "e")
        deal_suggestion = SuggestionList(self, deal_name, deal_id, ['name', 'id'], current_deals,
                                                        0.597, 0.55, "n", 3, 200)
        
        deal_suggestion.hide_box()
        deal_name.bind("<FocusIn>", lambda e: deal_suggestion.show_box())
        deal_name.bind("<KeyRelease>", lambda e: deal_suggestion.show_box())
        deal_name.bind("<FocusOut>", lambda e: deal_suggestion.hide_box())
        
        
        ck.make_button(register_box, "بستن", 100, 40, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, lambda: register_box.destroy(), 
                       0.04, 0.92, "sw")
        
        ck.make_button(register_box, "ثبت اطلاعات", 120, 40, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, 
                       lambda: rc.register_startpoint(name,
                                                      id,
                                                   address,
                                                   deal_name, 
                                                   deal_id,
                                                   register_box,
                                                   self.reset_page),   
                       0.95, 0.92, "se")
    
    def delete_startpoint(self):
        selected_data = startpoint_sample_data[int(self.tree.item(self.tree.selection()[0], 'values')[0]) - 1]
        
        def do_delete():
            startpoint_sample_data.remove(selected_data)
            dialog.destroy()
            self.reset_page()   
        def cancel(): dialog.destroy()
        
        dialog = rc.show_confirmation_box(self, do_delete, cancel, "آیا از حذف این مبدأ، مطمئن هستید؟", selected_data)
        
    def add_row(self, data_tuple):
        iid = self.tree.insert("", tk.END, values=data_tuple)
        self.tree.tag_configure(f"hover_{iid}", background=colors.light_green_5)
        self.tree.item(iid, tags=(f"hover_{iid}",))
        return iid

    def __init__(self, parent, go_to_dashboard1, reset_page):
        super().__init__(parent)
        
        self.pack(fill="both", expand=True)
        self.configure(fg_color=colors.light_green_1)
        self.reset_page = reset_page

        main_box = ctk.CTkFrame(self, width=float(self.master.winfo_screenwidth() / 1.2), 
                                height=float(self.master.winfo_screenheight() / 1.5), 
                                fg_color=colors.white,
                                corner_radius=0)
        main_box.place(relx=0.5, rely=0.5, anchor="center")
        
        def on_item_select(event):
            selected = self.tree.selection()
            if selected: 
                edit_bol_btn.configure(state="normal", fg_color=colors.dark_green_6, text_color=colors.white)
                delete_bol_btn.configure(state="normal", fg_color=colors.dark_green_6, text_color=colors.white)
            else: 
                edit_bol_btn.configure(state="disabled", fg_color=colors.light_gray_1, text_color=colors.light_gray_6)
                delete_bol_btn.configure(state="disabled", fg_color=colors.light_gray_1, text_color=colors.light_gray_6)
                
        self.column_titles = ["ردیف", "کد مبدأ", "نام مبدأ", "آدرس", "قرارداد"]
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
        self.tree.column(1, width=int(70 / 1050 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(2, text=self.column_titles[2], anchor=tk.CENTER)
        self.tree.column(2, width=int(150 / 1050 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(3, text=self.column_titles[3], anchor=tk.CENTER)
        self.tree.column(3, width=int(430 / 1050 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(4, text=self.column_titles[4], anchor=tk.CENTER)
        self.tree.column(4, width=int(140 / 1050 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        # اضافه‌کردن داده‌های نمونه با tag
        for i, item in enumerate(startpoint_sample_data):
            self.add_row((cc.eng_to_persian_date(str(i + 1)),
                                                 cc.eng_to_persian_date(item["id"]),
                                                 cc.eng_to_persian_date(item["name"]),
                                                 cc.eng_to_persian_date(item["address"]),
                                                 (item["deal"]['name'] + "/" + cc.eng_to_persian_date(item['deal']['id']))))

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

        sign_in_label = ctk.CTkLabel(main_box, text="اطلاعات مبدأ بارگیری", font=(None, 45, "bold"), text_color=colors.black, bg_color=colors.white)
        sign_in_label.place(relx=0.5, rely=0.1, anchor="center")
        
        ck.make_button(main_box, "ثبت اطلاعات مبدأ", 200, 50, (None, 22, "bold"), 20, 
                       colors.white, colors.white, colors.dark_green_5, colors.green_3,
                       self.register_startpoint, 0.98, 0.05, "ne")
        
        edit_bol_btn = ck.make_button(main_box, "ویرایش اطلاعات", 150, 50, (None, 22, "bold"),
                       20, colors.light_gray_6, colors.white,
                       colors.light_gray_1, colors.green_3, 
                       self.edit_startpoint, 0.98, 0.94, "e")
        edit_bol_btn.configure(state="disabled")
        delete_bol_btn = ck.make_button(main_box, "حذف مبدأ", 150, 50, (None, 22, "bold"),
                       20, colors.light_gray_6, colors.white,
                       colors.light_gray_1, colors.green_3, 
                       self.delete_startpoint, 0.81, 0.94, "e")
        delete_bol_btn.configure(state="disabled")
        
        
        ck.make_button(main_box, "بازگشت", 150, 50, (None, 22, "bold"),
                       20, colors.white, colors.white,
                       colors.dark_green_5, colors.green_3, 
                       go_to_dashboard1, 0.075, 0.94, "center")
        
        # لوگو
        ck.make_image(main_box, asset_paths.Logo_path, 88, 90, 0.02, 0.04, "nw")
