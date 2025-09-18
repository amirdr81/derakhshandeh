#main import
import customtkinter as ctk
import tkinter.ttk as ttk
import tkinter as tk

#data import
import asset_paths
from bol_fake_data import station_sample_data

#controllers
import common_controller as cc
import common_ctk as ck
import register_controller as rc

#colors
import colors


class StationInfo(ctk.CTkFrame):
    def edit_station(self):
        selected_data = station_sample_data[int(self.tree.item(self.tree.selection()[0], 'values')[0]) - 1]
        
        edit_box = ck.make_frame(self, 600, 250, colors.dark_green_6, colors.dark_green_6, colors.dark_green_6, 0, 0, 0.5, 0.5, "center")
        ck.make_label(edit_box, 150, 50, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "مشاهده/ویرایش اطلاعات جایگاه", 0, None, (None, 30, "bold"), 0.5, 0.1, "center")
        
        #کد جایگاه
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "کد جایگاه:", 0, None, (None, 20), 0.97, 0.3, "e")
        id_entry = ck.make_entry(edit_box, 160, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.83, 0.3, "e")
        ck.make_entry_with_text(id_entry, selected_data["id"])
        
        #نام جایگاه
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "نام جایگاه:", 0, None, (None, 20), 0.5, 0.3, "e")
        name_entry = ck.make_entry(edit_box, 200, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.36, 0.3, "e")
        ck.make_entry_with_text(name_entry, selected_data["name"])
        
        #آدرس جایگاه
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "آدرس جایگاه:", 0, None, (None, 20), 0.97, 0.55, "e")
        address_entry = ck.make_entry(edit_box, 460, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.79, 0.55, "e")
        ck.make_entry_with_text(address_entry, selected_data["address"])
        
        #دکمه ها
        #دکمه ثبت
        ck.make_button(edit_box, "ثبت اطلاعات", 150, 35, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, 
                       lambda: rc.edit_station(selected_data, 
                                              id_entry,
                                                name_entry,
                                                address_entry,
                                                edit_box,
                                                self.reset_page),   
                       0.96, 0.95, "se")
        
        #دکمه بستن
        ck.make_button(edit_box, "بستن", 100, 35, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, lambda: edit_box.destroy(), 
                       0.04, 0.95, "sw")
        
    def register_station(self):
        register_box = ck.make_frame(self, 600, 250, colors.dark_green_6, colors.dark_green_6, colors.dark_green_6, 0, 0, 0.5, 0.5, "center")
        
        ck.make_label(register_box, 200, 50, colors.dark_green_6, colors.dark_green_6, colors.white,
                          "ثبت اطلاعات جایگاه", 0, "center", (None, 35, "bold"), 0.5, 0.1, "center")
        
        id = ck.make_entry(register_box, 200, 40, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "کد جایگاه", colors.gray_2, 20, "right", (None, 15), 0.9, 0.3, "e")
        name = ck.make_entry(register_box, 200, 40, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "نام جایگاه", colors.gray_2, 20, "right", (None, 15), 0.45, 0.3, "e")
        address = ck.make_entry(register_box, 470, 40, colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                            "آدرس جایگاه", colors.gray_2, 20, "right", (None, 15), 0.9, 0.52, "e")
        
        ck.make_button(register_box, "بستن", 100, 40, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, lambda: register_box.destroy(), 
                       0.04, 0.92, "sw")
        
        ck.make_button(register_box, "ثبت اطلاعات", 120, 40, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, 
                       lambda: rc.register_station(id,
                                                   name,
                                                   address,
                                                   register_box,
                                                   self.reset_page),   
                       0.95, 0.92, "se")
    
    def delete_station(self):
        selected_data = station_sample_data[int(self.tree.item(self.tree.selection()[0], 'values')[0]) - 1]
        
        def do_delete():
            station_sample_data.remove(selected_data)
            dialog.destroy()
            self.reset_page()   
        def cancel(): dialog.destroy()
        
        dialog = rc.show_confirmation_box(self, do_delete, cancel, "آیا از حذف این جایگاه، مطمئن هستید؟", selected_data)
        
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
                
        self.column_titles = ["ردیف", "کد جایگاه", "نام جایگاه", "آدرس"]
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
        self.tree.column(1, width=int(70 / 860 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(2, text=self.column_titles[2], anchor=tk.CENTER)
        self.tree.column(2, width=int(150 / 860 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(3, text=self.column_titles[3], anchor=tk.CENTER)
        self.tree.column(3, width=int(430 / 860 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        # اضافه‌کردن داده‌های نمونه با tag
        for i, item in enumerate(station_sample_data):
            self.add_row((cc.eng_to_persian_date(str(i + 1)),
                                                 cc.eng_to_persian_date(item["id"]),
                                                 cc.eng_to_persian_date(item["name"]),
                                                 cc.eng_to_persian_date(item["address"])))

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

        sign_in_label = ctk.CTkLabel(main_box, text="اطلاعات جایگاه ها", font=(None, 45, "bold"), text_color=colors.black, bg_color=colors.white)
        sign_in_label.place(relx=0.5, rely=0.1, anchor="center")
        
        ck.make_button(main_box, "ثبت اطلاعات جایگاه", 200, 50, (None, 22, "bold"), 20, 
                       colors.white, colors.white, colors.dark_green_5, colors.green_3,
                       self.register_station, 0.98, 0.05, "ne")
        
        edit_bol_btn = ck.make_button(main_box, "ویرایش اطلاعات", 150, 50, (None, 22, "bold"),
                       20, colors.light_gray_6, colors.white,
                       colors.light_gray_1, colors.green_3, 
                       self.edit_station, 0.98, 0.94, "e")
        edit_bol_btn.configure(state="disabled")
        delete_bol_btn = ck.make_button(main_box, "حذف جایگاه", 150, 50, (None, 22, "bold"),
                       20, colors.light_gray_6, colors.white,
                       colors.light_gray_1, colors.green_3, 
                       self.delete_station, 0.81, 0.94, "e")
        delete_bol_btn.configure(state="disabled")
        
        
        ck.make_button(main_box, "بازگشت", 150, 50, (None, 22, "bold"),
                       20, colors.white, colors.white,
                       colors.dark_green_5, colors.green_3, 
                       go_to_dashboard1, 0.075, 0.94, "center")
        
        # لوگو
        ck.make_image(main_box, asset_paths.Logo_path, 88, 90, 0.02, 0.04, "nw")
