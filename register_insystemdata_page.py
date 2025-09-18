import customtkinter as ctk
import tkinter.ttk as ttk
import tkinter as tk
from insystem_data import load_main_type, agents, sent_type
from PIL import Image, ImageTk
from asset_paths import Logo_path
import tkinter.messagebox as messagebox
import colors
import asset_paths
import common_ctk as ck
import re
import common_controller as cc
import register_controller as rc

class RegisterInsystemdata(ctk.CTkFrame):
    def add_row(self, tree, data_tuple):
        iid = tree.insert("", tk.END, values=data_tuple)
        tree.tag_configure(f"hover_{iid}", background=colors.light_green_5)
        tree.item(iid, tags=(f"hover_{iid}",))
        return iid
    
    def __init__(self, parent, go_to_dashboard, reset_page):
        super().__init__(parent)
        
        self.pack(fill="both", expand=True)
        self.configure(fg_color=colors.light_green_1)
        self.reset_page = reset_page

        def confirm_sent_type():
            label = ck.make_label(middle_box, 150, 40, 
                          colors.dark_green_6, colors.dark_green_6, colors.red_color,
                          "", 0, None, (None, 17, "bold"), 0.65, 0.9, "e")
            if(not sent_type_entry.get()): ck.show_error(sent_type_entry, colors.dark_green_6, 1000)
            elif(sent_type_entry.get() in sent_type): 
                ck.update_label_error(label, 2000, 'نوع ارسال، قبلا ثبت شده است!')
                ck.show_error(sent_type_entry, colors.dark_green_6, 2000)
            else:
                def do_register():
                    sent_type.append(sent_type_entry.get())
                    cancel()
                    self.reset_page()
                def cancel():
                    confirm_frame.destroy()
                
                confirm_frame = rc.show_confirmation_box(self, do_register, cancel, 'آیا از اطلاعات وارد شده، مطمئن هستید؟', None)
            
        def confirm_agent():
            label = ck.make_label(left_box, 150, 40, 
                          colors.dark_green_6, colors.dark_green_6, colors.red_color,
                          "", 0, None, (None, 17, "bold"), 0.65, 0.9, "e")
            if(not agent_name.get()): ck.show_error(agent_name, colors.dark_green_6, 1000)
            elif(agent_name.get() in agents): 
                ck.update_label_error(label, 2000, 'نماینده، قبلا ثبت شده است!')
                ck.show_error(agent_name, colors.dark_green_6, 2000)
            else:
                def do_register():
                    agents.append(agent_name.get())
                    cancel()
                    self.reset_page()
                def cancel():
                    confirm_frame.destroy()
                
                confirm_frame = rc.show_confirmation_box(self, do_register, cancel, 'آیا از اطلاعات وارد شده، مطمئن هستید؟', None)
                
                
        def confirm_load():
            label = ck.make_label(right_box, 150, 40, 
                          colors.dark_green_6, colors.dark_green_6, colors.red_color,
                          "", 0, None, (None, 17, "bold"), 0.65, 0.9, "e")
            if(not main_type.get()): ck.show_error(main_type, colors.dark_green_6, 1000)
            elif(not load_name.get()): ck.show_error(load_name, colors.dark_green_6, 1000)
            elif(cc.does_item_exist(load_main_type, 'name', main_type.get()) and 
                 load_name.get() in cc.does_item_exist(load_main_type, 'name', main_type.get())['sub_array']): 
                ck.update_label_error(label, 2000, 'فرآورده، قبلا ثبت شده است!')
                ck.show_error(load_name, colors.dark_green_6, 2000)
            else:
                def do_register():
                    if(cc.does_item_exist(load_main_type, 'name', main_type.get())):
                        cc.does_item_exist(load_main_type, 'name', main_type.get())['sub_array'].append(load_name.get())
                    else:
                        load_main_type.append({
                            'name': main_type.get(),
                            'sub_array': [load_name.get()]
                        })
                    cancel()
                    self.reset_page()
                def cancel():
                    confirm_frame.destroy()
                
                confirm_frame = rc.show_confirmation_box(self, do_register, cancel, 'آیا از اطلاعات وارد شده، مطمئن هستید؟', None)
        #باکس اصلی +‌ عنوان
        main_box = ck.make_frame(self, float(self.master.winfo_screenwidth() / 1.2), float(self.master.winfo_screenheight() / 1.5),
                                 colors.white, colors.white, colors.white, 0, 0, 0.5, 0.5, 'center')
        right_box = ck.make_frame(main_box, float(self.master.winfo_screenwidth() / 4), float(self.master.winfo_screenheight() / 2),
                                 colors.white, colors.dark_green_6, colors.dark_green_6, 0, 20, 0.82, 0.58, 'center')
        middle_box = ck.make_frame(main_box, float(self.master.winfo_screenwidth() / 4), float(self.master.winfo_screenheight() / 2),
                                 colors.white, colors.dark_green_6, colors.dark_green_6, 0, 20, 0.5, 0.58, 'center')
        left_box = ck.make_frame(main_box, float(self.master.winfo_screenwidth() / 4), float(self.master.winfo_screenheight() / 2),
                                 colors.white, colors.dark_green_6, colors.dark_green_6, 0, 20, 0.18, 0.58, 'center')
        ck.make_label(main_box, 200, 40, colors.white, colors.white, colors.dark_green_6, 'ثبت اطلاعات سیستمی',
                      0, None, (None, 50, "bold"), 0.5, 0.1, 'center')
        ck.make_label(right_box, 200, 40, colors.dark_green_6, colors.dark_green_6, colors.white, 'ثبت اطلاعات فرآورده',
                      0, None, (None, 35, "bold"), 0.5, 0.07, 'center')
        ck.make_label(left_box, 200, 40, colors.dark_green_6, colors.dark_green_6, colors.white, 'ثبت اطلاعات نماینده',
                      0, None, (None, 35, "bold"), 0.5, 0.1, 'center')
        ck.make_label(middle_box, 200, 40, colors.dark_green_6, colors.dark_green_6, colors.white, 'ثبت نوع ارسال',
                      0, None, (None, 35, "bold"), 0.5, 0.1, 'center')
        ck.make_label(right_box, 200, 15, colors.dark_green_6, colors.dark_green_6, colors.white, 
                      'برای ثبت اطلاعات، یک عنوان و یک کالا وارد کنید، در صورتی که چند کالا برای یک عنوان',
                      0, None, (None, 10), 0.97, 0.14, 'e')
        ck.make_label(right_box, 40, 15, colors.dark_green_6, colors.dark_green_6, colors.white, 
                      ' نیاز دارید، به صورت جداگانه اقدام کنید!',
                      0, None, (None, 10), 0.97, 0.18, 'e')
        
        
        #محتوای ثبت فرآورده
        main_type = ck.make_entry(right_box, 140, 40, colors.dark_green_6, colors.light_gray_1, colors.light_gray_1,
                      colors.black, 'عنوان اصلی', colors.light_gray_7, 20, 'right', (None, 15), 0.92, 0.27, 'e')
        load_name = ck.make_entry(right_box, 140, 40, colors.dark_green_6, colors.light_gray_1, colors.light_gray_1,
                      colors.black, 'نام کالا', colors.light_gray_7, 20, 'right', (None, 15), 0.45, 0.27, 'e')
        
        #محتوای ثبت نماینده
        agent_name = ck.make_entry(left_box, 200, 40, colors.dark_green_6, colors.light_gray_1, colors.light_gray_1,
                      colors.black, 'نام نماینده', colors.light_gray_7, 20, 'right', (None, 15), 0.5, 0.27, 'center')
        
        #محتوای ثبت نوع ارسال
        sent_type_entry = ck.make_entry(middle_box, 200, 40, colors.dark_green_6, colors.light_gray_1, colors.light_gray_1,
                      colors.black, 'نوع ارسال', colors.light_gray_7, 20, 'right', (None, 15), 0.5, 0.27, 'center')
        #دکمه ها
        #دکمه بازگشت به منوی اصلی
        ck.make_button(main_box, 'بازگشت', 140, 50, (None, 30, "bold"), 20, colors.white, colors.white,
                       colors.dark_green_5, colors.green_3, go_to_dashboard, 0.92, 0.1, 'center')
        ck.make_button(right_box, 'ثبت', 80, 50, (None, 25, "bold"), 20, colors.dark_green_5, colors.dark_green_5,
                       colors.white, colors.green_3, confirm_load, 0.85, 0.9, 'center')
        ck.make_button(left_box, 'ثبت', 80, 50, (None, 25, "bold"), 20, colors.dark_green_5, colors.dark_green_5,
                       colors.white, colors.green_3, confirm_agent, 0.85, 0.9, 'center')
        ck.make_button(middle_box, 'ثبت', 80, 50, (None, 25, "bold"), 20, colors.dark_green_5, colors.dark_green_5,
                       colors.white, colors.green_3, confirm_sent_type, 0.85, 0.9, 'center')
        
        #لوگو
        ck.make_image(main_box, asset_paths.Logo_path, 88, 90, 0.02, 0.04, "nw")
        
        #درخت فرآورده
        #--------------------------------
        self.column_titles = ["ردیف", "عنوان", "زیرکالا"]
        self.column_ids = [f"col{i}" for i in range(len(self.column_titles))]
        
        style = ttk.Style(self)

        bg_color = colors.white
        text_color = colors.black
        heading_bg_color = colors.green_4
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
                        foreground=colors.dark_green_6,
                        font=(None, 10, "bold"),
                        padding=(5, 5))

        # رنگ ردیف انتخاب شده
        style.map("Treeview",
                  background=[("selected", selected_color)],
                  foreground=[("selected", "white")])

        tree_frame = ctk.CTkFrame(right_box)
        tree_frame.place(relx=0.5, rely=0.58, anchor="center")

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
                                 selectmode="browse",
                                 height=6)

        tree_scrollbar_y.config(command=self.tree.yview)
        tree_scrollbar_y.grid(row=0, column=1, sticky="ns")
        self.tree.grid(row=0, column=0, sticky="nsew")
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)
        
        table_width = self.tree.winfo_screenwidth() 

        self.tree.heading(0, text=self.column_titles[0], anchor=tk.CENTER)
        self.tree.column(0, width=int(35 / 1150 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(1, text=self.column_titles[1], anchor=tk.CENTER)
        self.tree.column(1, width=int(70 / 1150 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading(2, text=self.column_titles[2], anchor=tk.CENTER)
        self.tree.column(2, width=int(165 / 1150 * table_width), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        # اضافه‌کردن داده‌های نمونه با tag
        for i, item in enumerate(load_main_type):
            loads = item['sub_array'][0]
            for load in item['sub_array'][1:]:
                loads += (' - ' + load)
            self.add_row(self.tree, (cc.eng_to_persian_date(str(i + 1)),
                                                item["name"],
                                                loads))

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
        
        #درخت نماینده
        #------------------------------
        
        self.column_titles2 = ["ردیف", "نام نماینده"]
        self.column_ids2 = [f"col{i}" for i in range(len(self.column_titles2))]
        
        style2 = ttk.Style(self)

        bg_color = colors.white
        text_color = colors.black
        heading_bg_color = colors.green_4
        selected_color = colors.green_2

        style2.theme_use("default")

        # استایل اصلی Treeview
        style2.configure("Treeview",
                        background=bg_color,
                        foreground=text_color,
                        fieldbackground=colors.light_green_4,
                        rowheight=30)
        
        # استایل هدر
        style2.configure("Treeview.Heading",
                        background=heading_bg_color,
                        foreground=colors.dark_green_6,
                        font=(None, 13, "bold"),
                        padding=(5, 5))

        # رنگ ردیف انتخاب شده
        style2.map("Treeview",
                  background=[("selected", selected_color)],
                  foreground=[("selected", "white")])

        tree_frame2 = ctk.CTkFrame(left_box)
        tree_frame2.place(relx=0.5, rely=0.58, anchor="center")

        style2.configure("Custom.Vertical.TScrollbar", 
            background=colors.dark_green_6,
            troughcolor=colors.light_green_1,
            bordercolor=colors.white,
            arrowcolor=colors.white,
            relief="flat")

        tree_scrollbar_y2 = ttk.Scrollbar(
            tree_frame2,
            orient="vertical",
            style="Custom.Vertical.TScrollbar"
        )
        
        self.tree2 = ttk.Treeview(tree_frame2,
                                 columns=self.column_ids2,
                                 show="headings",
                                 yscrollcommand=tree_scrollbar_y2.set,
                                 selectmode="browse",
                                 height=6)

        tree_scrollbar_y2.config(command=self.tree.yview)
        tree_scrollbar_y2.grid(row=0, column=1, sticky="ns")
        self.tree2.grid(row=0, column=0, sticky="nsew")
        tree_frame2.grid_rowconfigure(0, weight=1)
        tree_frame2.grid_columnconfigure(0, weight=1)
        
        table_width2 = self.tree2.winfo_screenwidth() 

        self.tree2.heading(0, text=self.column_titles2[0], anchor=tk.CENTER)
        self.tree2.column(0, width=int(50 / 1150 * table_width2), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree2.heading(1, text=self.column_titles2[1], anchor=tk.CENTER)
        self.tree2.column(1, width=int(220 / 1150 * table_width2), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        # اضافه‌کردن داده‌های نمونه با tag
            
        for i, item in enumerate(agents):
            self.add_row(self.tree2, (cc.eng_to_persian_date(str(i + 1)),
                                                item))

        # هَوِر ساده روی ردیف های جدول (بدون transition)
        self._last_hovered2 = None

        def on_tree_motion2(event):
            row = self.tree2.identify_row(event.y)
            if row != self._last_hovered2:
                # ردیف قبلی رو به رنگ عادی برگردون
                if self._last_hovered2 is not None and self.tree2.exists(self._last_hovered2):
                    self.tree2.tag_configure(f"hover_{self._last_hovered2}", background=colors.light_green_5)
                # ردیف جدید رو رنگ hover بده
                if row and self.tree2.exists(row):
                    self.tree2.tag_configure(f"hover_{row}", background=colors.green_2)
                self._last_hovered2 = row

        def on_tree_leave2(event):
            if self._last_hovered2 and self.tree2.exists(self._last_hovered2):
                self.tree2.tag_configure(f"hover_{self._last_hovered2}", background=colors.light_green_5)
            self._last_hovered2 = None

        self.tree2.bind("<Motion>", on_tree_motion2)
        self.tree2.bind("<Leave>", on_tree_leave2)
        
        #درخت نوع ارسال
        #------------------------------
        
        self.column_titles3 = ["ردیف", "نوع ارسال"]
        self.column_ids3 = [f"col{i}" for i in range(len(self.column_titles3))]
        
        style3 = ttk.Style(self)

        bg_color = colors.white
        text_color = colors.black
        heading_bg_color = colors.green_4
        selected_color = colors.green_2

        style3.theme_use("default")

        # استایل اصلی Treeview
        style3.configure("Treeview",
                        background=bg_color,
                        foreground=text_color,
                        fieldbackground=colors.light_green_4,
                        rowheight=30)
        
        # استایل هدر
        style3.configure("Treeview.Heading",
                        background=heading_bg_color,
                        foreground=colors.dark_green_6,
                        font=(None, 13, "bold"),
                        padding=(5, 5))

        # رنگ ردیف انتخاب شده
        style3.map("Treeview",
                  background=[("selected", selected_color)],
                  foreground=[("selected", "white")])

        tree_frame3 = ctk.CTkFrame(middle_box)
        tree_frame3.place(relx=0.5, rely=0.58, anchor="center")

        style3.configure("Custom.Vertical.TScrollbar", 
            background=colors.dark_green_6,
            troughcolor=colors.light_green_1,
            bordercolor=colors.white,
            arrowcolor=colors.white,
            relief="flat")

        tree_scrollbar_y3 = ttk.Scrollbar(
            tree_frame3,
            orient="vertical",
            style="Custom.Vertical.TScrollbar"
        )
        
        self.tree3 = ttk.Treeview(tree_frame3,
                                 columns=self.column_ids3,
                                 show="headings",
                                 yscrollcommand=tree_scrollbar_y3.set,
                                 selectmode="browse",
                                 height=6)

        tree_scrollbar_y3.config(command=self.tree.yview)
        tree_scrollbar_y3.grid(row=0, column=1, sticky="ns")
        self.tree3.grid(row=0, column=0, sticky="nsew")
        tree_frame3.grid_rowconfigure(0, weight=1)
        tree_frame3.grid_columnconfigure(0, weight=1)
        
        table_width3 = self.tree3.winfo_screenwidth() 

        self.tree3.heading(0, text=self.column_titles3[0], anchor=tk.CENTER)
        self.tree3.column(0, width=int(50 / 1150 * table_width3), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        self.tree3.heading(1, text=self.column_titles3[1], anchor=tk.CENTER)
        self.tree3.column(1, width=int(220 / 1150 * table_width3), minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        # اضافه‌کردن داده‌های نمونه با tag
            
        for i, item in enumerate(sent_type):
            self.add_row(self.tree3, (cc.eng_to_persian_date(str(i + 1)),
                                                item))

        # هَوِر ساده روی ردیف های جدول (بدون transition)
        self._last_hovered3 = None

        def on_tree_motion3(event):
            row = self.tree3.identify_row(event.y)
            if row != self._last_hovered3:
                # ردیف قبلی رو به رنگ عادی برگردون
                if self._last_hovered3 is not None and self.tree3.exists(self._last_hovered3):
                    self.tree3.tag_configure(f"hover_{self._last_hovered3}", background=colors.light_green_5)
                # ردیف جدید رو رنگ hover بده
                if row and self.tree3.exists(row):
                    self.tree3.tag_configure(f"hover_{row}", background=colors.green_3)
                self._last_hovered3 = row

        def on_tree_leave3(event):
            if self._last_hovered3 and self.tree3.exists(self._last_hovered3):
                self.tree3.tag_configure(f"hover_{self._last_hovered3}", background=colors.light_green_5)
            self._last_hovered3 = None

        self.tree3.bind("<Motion>", on_tree_motion3)
        self.tree3.bind("<Leave>", on_tree_leave3)