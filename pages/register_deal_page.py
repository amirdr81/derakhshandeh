import customtkinter as ctk
import tkinter.ttk as ttk
import tkinter as tk
from insystem_data import current_deals, old_deals
from date import Date
import common_controller as cc
import common_ctk as ck
import register_controller as rc

import colors

class RegisterDeal(ctk.CTkFrame):
    def edit_deal(self, event):
        selected_data = current_deals[int(self.tree.item(self.tree.selection()[0], 'values')[0]) - 1]
        
        edit_box = ck.make_frame(self, 600, 400, colors.dark_green_6, colors.dark_green_6, colors.dark_green_6, 0, 0, 0.5, 0.5, "center")
        ck.make_label(edit_box, 150, 50, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "مشاهده/ویرایش اطلاعات قرارداد", 0, None, (None, 30, "bold"), 0.5, 0.1, "center")
        
         #نام شرکت
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "نام شرکت:", 0, None, (None, 20), 0.97, 0.4, "e")
        company_name = ck.make_entry(edit_box, 150, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.81, 0.4, "e")
        ck.make_entry_with_text(company_name, selected_data["name"])
        
        #شماره قرارداد
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "شماره قرارداد:", 0, None, (None, 20), 0.97, 0.25, "e")
        deal_id = ck.make_entry(edit_box, 150, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.77, 0.25, "e")
        ck.make_entry_with_text(deal_id, selected_data["id"])
        
        #نام کالا/محموله
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "نام کالا/محموله:", 0, None, (None, 20), 0.5, 0.4, "e")
        load_name = ck.make_entry(edit_box, 150, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.29, 0.4, "e")
        ck.make_entry_with_text(load_name, selected_data["load_name"])
        
        #فی شرکت
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "فی شرکت:", 0, None, (None, 20), 0.9, 0.55, "e")
        fee_company = ck.make_entry(edit_box, 100, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.74, 0.55, "e")
        ck.make_entry_with_text(fee_company, selected_data["fee_company"])
        
        #فی راننده
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "فی شرکت:", 0, None, (None, 20), 0.5, 0.55, "e")
        fee_driver = ck.make_entry(edit_box, 100, 30, 
                      colors.dark_green_6, colors.white, colors.dark_green_6, colors.black,
                      None, None, 20, "right", (None, 15), 0.34, 0.55, "e")
        ck.make_entry_with_text(fee_driver, selected_data["fee_driver"])
        
        #تاریخ شروع قرارداد
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "تاریخ شروع قرارداد:", 0, None, (None, 20), 0.97, 0.7, "e")
        start_date = ck.make_button(edit_box, cc.eng_to_persian_date(selected_data["start_date"]), 150, 30, (None, 15), 20, 
                                          colors.gray_2, colors.dark_green_6,colors.white,colors.green_3, 
                                          lambda: ck.open_calendar(edit_box, start_date, 0.5, 0.5, colors.black), 0.71, 0.7, "e")
        start_date.configure(text_color=colors.black)
        
        #تاریخ پایان قرارداد
        ck.make_label(edit_box, 30, 40, colors.dark_green_6, colors.dark_green_6, colors.white,
                      "تاریخ پایان قرارداد:", 0, None, (None, 20), 0.97, 0.8, "e")
        end_date = ck.make_button(edit_box, cc.eng_to_persian_date(selected_data["end_date"]), 150, 30, (None, 15), 20, 
                                          colors.gray_2, colors.dark_green_6,colors.white,colors.green_3, 
                                          lambda: ck.open_calendar(edit_box, end_date, 0.5, 0.5, colors.black), 0.71, 0.8, "e")
        end_date.configure(text_color=colors.black)
        
        #دکمه ها
        # دکمه ثبت
        ck.make_button(edit_box, "ثبت اطلاعات", 150, 35, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, 
                       lambda: rc.edit_deal(selected_data,
                                           company_name,
                                            deal_id,
                                            load_name,
                                            fee_company,
                                            fee_driver,
                                            start_date,
                                            end_date,
                                            edit_box,
                                            self.reset_page), 
                       0.96, 0.95, "se")
        
        
        #دکمه بستن
        ck.make_button(edit_box, "بستن", 100, 35, (None, 22, "bold"), 20, colors.dark_green_6, 
                       colors.dark_green_6, colors.white, colors.green_3, lambda: edit_box.destroy(), 
                       0.04, 0.95, "sw")
        
    def archive_confirm(self):
        selected_data = current_deals[int(self.tree.item(self.tree.selection()[0], 'values')[0]) - 1]
        
        def do_archive():
            current_deals.remove(selected_data)
            old_deals.append(selected_data)
            cancel()
            self.reset_page()
        def cancel(): confirm_box.destroy()
        confirm_box = rc.show_confirmation_box(self, do_archive, cancel, "آیا از آرشیو کردن این قرارداد، اطمینان دارید؟",
                                 selected_data)
        
    def show_register_confirm(self):
        dialog = ctk.CTkFrame(self, width=self.winfo_screenwidth() / 4.5, 
                              height=self.winfo_screenheight() / 8, 
                              fg_color=colors.light_green_1)
        dialog.place(relx=0.5, rely=0.5, anchor="center") 
        lbl = ctk.CTkLabel(dialog, 
                           text="آیا از صحت اطلاعات وارد شده، اطمینان دارید؟...", 
                           font=(None, 16),
                           text_color=colors.black)
        lbl.place(relx=0.5, rely=0.2, anchor="center")

        def do_register(): 
            current_deals.append({"name": self.company_name.get(),
                         "id": self.deal_id.get(),
                         "load_name": self.load_name.get(),
                         "start_date": self.start_date.cget("text"),
                         "end_date": self.end_date.cget("text"),
                         "fee_company": self.fee_rate_company.get(),
                         "fee_driver": self.fee_rate_driver.get(),
                         "packages": []}
                         )
            self.reset_page()
            dialog.destroy()
            
        def cancel(): dialog.destroy()

        # دو تا دکمه بله و خیر
        btn_yes = ctk.CTkButton(dialog, text="بله", width=70, command=do_register, fg_color=colors.dark_green_5, hover_color=colors.green_3)
        btn_no = ctk.CTkButton(dialog, text="خیر", width=70, command=cancel, fg_color=colors.dark_green_5, hover_color=colors.green_3)
        btn_yes.place(relx=0.35, rely=0.8, anchor="center")
        btn_no.place(relx=0.65, rely=0.8, anchor="center")
        
    
    def show_errors(self):
        label = ck.make_label(self, 150, 25, 
                          colors.dark_green_6, colors.dark_green_6, colors.red_color,
                          "", 0, None, (None, 18, "bold"), 0.89, 0.7, "e")
        if(not self.company_name.get()): ck.show_error(self.company_name, colors.dark_green_6, 1000)
        elif(not self.deal_id.get()): ck.show_error(self.deal_id, colors.dark_green_6, 1000)
        elif(not self.load_name.get()): ck.show_error(self.load_name, colors.dark_green_6, 1000)
        elif(self.start_date.cget('text') == 'شروع قرارداد'): ck.show_error(self.start_date, colors.dark_green_6, 1000)
        elif(self.end_date.cget('text') == 'پایان قرارداد'): ck.show_error(self.end_date, colors.dark_green_6, 1000)
        elif(cc.does_item_exist(current_deals + current_deals, 'id', self.deal_id.get())): 
            ck.show_error(self.deal_id, colors.dark_green_6, 2000)
            ck.update_label_error(label, 2000, 'قراردادی با این شماره، قبلا ثبت شده است!')
        elif(cc.is_date_above(self.start_date.cget('text'), self.end_date.cget('text'))): 
            ck.show_error(self.start_date, colors.dark_green_6, 2000)
            ck.show_error(self.end_date, colors.dark_green_6, 2000)
            ck.update_label_error(label, 2000, 'تاریخ پایان قرارداد، باید بعد از تاریخ شروع قرارداد باشد!')
        else:
            self.show_register_confirm()
    def add_row(self, data_tuple):
        iid = self.tree.insert("", tk.END, values=data_tuple)
        self.tree.tag_configure(f"hover_{iid}", background=colors.light_green_5)
        self.tree.item(iid, tags=(f"hover_{iid}",))
        return iid

    def __init__(self, parent, go_to_dashboard, go_to_old_deals, reset_page):
        super().__init__(parent)
        self.go_to_dashboard = go_to_dashboard
        self.go_to_old_deals = go_to_old_deals
        self.reset_page = reset_page
        self.bols_title = ""
        self.pack(fill="both", expand=True)
            
        def open_calendar(box, entry, x_co, y_co):
            global calendar_frame
            try: calendar_frame.destroy()
            except: pass
            calendar_frame = tk.Frame(box, bd=2, relief=tk.RIDGE,
                                      bg=colors.light_green_1)
            calendar_frame.place(relx=x_co, rely=y_co, anchor="center")
            def on_date_selected(selected_date):
                entry.configure(text=str(selected_date).replace("-", "/"), text_color=colors.black)  
                calendar_frame.destroy()

            cal = Date(calendar_frame, callback=on_date_selected)
            cal.pack()

            close_btn = ctk.CTkButton(calendar_frame, text="بستن", 
                                      width=100,
                                      bg_color=colors.light_green_1, 
                                fg_color=colors.dark_green_6,
                                text_color=colors.light_green_1,
                                hover_color=colors.green_3,
                                command=calendar_frame.destroy)
            close_btn.pack(pady=4)
            
        def make_entry_box(box, text, height, width, x_co, y_co):
            entry = ctk.CTkEntry(box, 
                                placeholder_text=text, 
                                height=height , justify="right", width=width, 
                                corner_radius=60, 
                                bg_color=colors.dark_green_6, 
                                border_color=colors.dark_green_6, 
                                fg_color=colors.light_gray_4, 
                                text_color=colors.black)
            entry.place(relx=x_co, rely=y_co, anchor="center")
            return entry
        
        def make_date_box(box, text, height, width, x_co, y_co):
            date_btn = ctk.CTkButton(box)
            date_btn.configure(
                box,
                text=text,
                height=height,
                width=width,
                corner_radius=60,
                bg_color=colors.dark_green_6,
                border_color=colors.dark_green_6,
                fg_color=colors.light_gray_4,
                hover_color=colors.green_3,
                text_color=colors.gray_1,
                command=lambda:open_calendar(main_box, date_btn, 0.5, 0.5)
            )
            date_btn.place(relx=x_co, rely=y_co, anchor="center")
            return date_btn
        self.configure(fg_color=colors.light_green_1)

        #باکس اصلی
        main_box = ctk.CTkFrame(self, width=float(self.master.winfo_screenwidth() / 1.2), 
                                height=float(self.master.winfo_screenheight() / 1.5), 
                                fg_color=colors.white,
                                corner_radius=0)
        main_box.place(relx=0.5, rely=0.5, anchor="center")

        #باکس راست
        right_box = ctk.CTkFrame(main_box, width=float(self.master.winfo_screenwidth() / 2.5), 
                                height=float(self.master.winfo_screenheight() / 1.9), 
                                bg_color=colors.white,
                                fg_color=colors.dark_green_6,
                                corner_radius=20)
        right_box.place(relx=0.74, rely=0.58, anchor="center")
        
        self.column_titles = ["ردیف", "نام شرکت", "شماره قرارداد", "عنوان کالا", "شروع قرارداد", "اتمام قرارداد", "فی شرکت", "فی راننده"]
        self.column_ids = [f"col{i}" for i in range(len(self.column_titles))]

        # استایل Treeview
        style = ttk.Style(self)
        style.theme_use("default")
        style.configure("Treeview", background=colors.light_green_5,
                        foreground=colors.black, fieldbackground=colors.light_green_4, rowheight=30)
        style.configure("Treeview.Heading", background=colors.dark_green_6,
                        foreground=colors.white, font=(None, 10, "bold"),
                        padding=(5, 5))
        # رنگ ردیف انتخاب شده
        style.map("Treeview",
                  background=[("selected", colors.green_2)],
                  foreground=[("selected", "white")])

        style.configure("Custom.Vertical.TScrollbar", 
            background=colors.dark_green_6,
            troughcolor=colors.light_green_1,
            bordercolor=colors.white,
            arrowcolor=colors.white,
            relief="flat")
        style.map("Custom.Vertical.TScrollbar",
            background=[("active", colors.green_2)],
            arrowcolor=[("active", colors.white)]
        )

        style.configure("Custom.Horizontal.TScrollbar", 
            background=colors.dark_green_6,
            troughcolor=colors.light_green_1,
            bordercolor=colors.white,
            arrowcolor=colors.white,
            relief="flat")
        style.map("Custom.Horizontal.TScrollbar",
            background=[("active", colors.green_2)],
            arrowcolor=[("active", colors.white)]
        )
        
        table_width = main_box.winfo_screenwidth() / 2.6
        table_height = main_box.winfo_screenheight() / 1.9
        scroll_bar_width = 16
        
        # Frame والد با ابعاد دقیقاً ۲۰۰x۱۰۰
        tree_frame = ctk.CTkFrame(main_box, width=table_width, height=table_height, fg_color=colors.white)
        tree_frame.place(relx=0.25, rely=0.58, anchor="center")
        tree_frame.pack_propagate(False)

        # Treeview با ابعاد کاملاً فیکس
        self.tree = ttk.Treeview(
            tree_frame,
            columns=self.column_ids,
            show="headings",
            height=4,   # صرفاً ارتفاع پیش‌فرض ردیف‌ها برای دید اولیه، تاثیری در ابعاد نهایی ندارد
            selectmode="browse"
        )
        self.tree.place(x=scroll_bar_width, y=0, width=table_width, height=table_height)

        tree_scrollbar_y = ttk.Scrollbar(tree_frame, 
                                         orient="vertical", 
                                         command=self.tree.yview, 
                                         style="Custom.Vertical.TScrollbar")
        tree_scrollbar_y.place(x=0, y=0, width=scroll_bar_width, height=table_height)
        
        scroll_x = ttk.Scrollbar(tree_frame, 
                                 orient="horizontal", 
                                 command=self.tree.xview,
                                 style="Custom.Horizontal.TScrollbar")
        scroll_x.place(x=scroll_bar_width, y=table_height-scroll_bar_width, width=table_width-scroll_bar_width, height=scroll_bar_width)

        self.tree.configure(yscrollcommand=tree_scrollbar_y.set, xscrollcommand=scroll_x.set)

        # هر ستون غیرقابل استرچ، و با عرض کوچک (اگر زیاد بودن، فقط با اسکرول ظاهر می‌شوند)
        for i, name in enumerate(self.column_titles):
            if i == 0:
                self.tree.heading(i, text=name, anchor=tk.CENTER)
                self.tree.column(i, width=70, minwidth=50, anchor=tk.CENTER, stretch=tk.NO) 
            elif i == 1:
                self.tree.heading(i, text=name, anchor=tk.CENTER)
                self.tree.column(i, width=140, minwidth=50, anchor=tk.CENTER, stretch=tk.NO) 
            elif i == 4 or i == 5:
                self.tree.heading(i, text=name, anchor=tk.CENTER)
                self.tree.column(i, width=110, minwidth=50, anchor=tk.CENTER, stretch=tk.NO) 
            elif i == 6:
                self.tree.heading(i, text=name, anchor=tk.CENTER)
                self.tree.column(i, width=85, minwidth=50, anchor=tk.CENTER, stretch=tk.NO) 
            else:
                self.tree.heading(i, text=name, anchor=tk.CENTER)
                self.tree.column(i, width=120, minwidth=50, anchor=tk.CENTER, stretch=tk.NO)
        # داده‌ها
        # for item in [item for item in deals]:
        #     self.add_row(item)
        for i, item in enumerate(current_deals): 
            self.add_row((cc.eng_to_persian_date(str(i + 1)),
                                         cc.eng_to_persian_date(item["name"]), 
                                    cc.eng_to_persian_date(item["id"]), 
                                    cc.eng_to_persian_date(item["load_name"]), 
                                    cc.eng_to_persian_date(item["start_date"]), 
                                    cc.eng_to_persian_date(item["end_date"]),
                                    cc.eng_to_persian_date(item["fee_company"]),
                                    cc.eng_to_persian_date(item["fee_driver"])))

        # هوور ساده
        self._last_hovered = None
        def on_tree_motion(event):
            row = self.tree.identify_row(event.y)
            if row != self._last_hovered:
                if self._last_hovered is not None and self.tree.exists(self._last_hovered):
                    self.tree.tag_configure(f"hover_{self._last_hovered}", background=colors.light_green_5)
                if row and self.tree.exists(row):
                    self.tree.tag_configure(f"hover_{row}", background=colors.green_2)
                self._last_hovered = row
        def on_tree_leave(event):
            if self._last_hovered and self.tree.exists(self._last_hovered):
                self.tree.tag_configure(f"hover_{self._last_hovered}", background=colors.light_green_5)
            self._last_hovered = None

        def on_item_select(event):
            selected_row = self.tree.selection()
            if selected_row: 
                deal = current_deals[int(self.tree.item(selected_row[0], 'values')[0]) - 1]
                self.bols_title = deal["name"] + "/" + cc.eng_to_persian_date(deal["id"])
                
                watch_bol_btn.configure(state="normal")
                archive_deal_btn.configure(state="normal", fg_color=colors.white, text_color = colors.dark_green_6)
            else: 
                watch_bol_btn.configure(state="disabled")
                archive_deal_btn.configure(state="disabled")
        self.tree.bind("<<TreeviewSelect>>", on_item_select)
        
        self.tree.bind("<Motion>", on_tree_motion)
        self.tree.bind("<Leave>", on_tree_leave)
        self.tree.bind("<Double-1>", self.edit_deal)

        # عنوان
        main_label = ctk.CTkLabel(main_box, text="اطلاعات قرارداد ها", font=(None, 45, "bold"), text_color=colors.black, bg_color=colors.white)
        main_label.place(relx=0.5, rely=0.1, anchor="center")

        #عناوین باکس ثبت
        #عنوان
        box_main_label = ctk.CTkLabel(right_box, text="ثبت قرارداد جدید", font=(None, 35, "bold"), text_color=colors.white, bg_color=colors.dark_green_6)
        box_main_label.place(relx=0.5, rely=0.1, anchor="center")

        #نام شرکت
        self.company_name = make_entry_box(right_box, "نام شرکت", 40, 210, 0.72, 0.3)
        self.deal_id = make_entry_box(right_box, "شماره قرارداد", 40, 210, 0.28, 0.3)
        self.load_name = make_entry_box(right_box, "نام کالا/محموله", 40, 210, 0.72, 0.42)
        self.fee_rate_company = make_entry_box(right_box, "فی شرکت", 40, 105, 0.37, 0.42)
        self.fee_rate_driver = make_entry_box(right_box, "فی راننده", 40, 105, 0.18, 0.42)
        self.start_date = make_date_box(right_box, "شروع قرارداد", 37, 205, 0.72, 0.54)
        self.end_date = make_date_box(right_box, "پایان قرارداد", 37, 205, 0.28, 0.54)
        
        #دکمه
        #ثبت قرارداد
        archive_deal_btn = ck.make_button(right_box, "آرشیو", 80, 35, (None, 20, "bold"), 20,
                                          colors.light_gray_6, colors.dark_green_6, 
                                          colors.light_gray_1, colors.green_3, 
                                          self.archive_confirm,
                                          0.1, 0.07, "center")
        archive_deal_btn.configure(state="disabled")
        
        watch_bol_btn = ctk.CTkButton(right_box, text="ثبت قرارداد", 
                                   width=130, height=50, 
                                   font=(None, 22, "bold"), 
                                   corner_radius=20, 
                                   text_color=colors.dark_green_6, 
                                   bg_color=colors.dark_green_6, 
                                   fg_color=colors.white, 
                                   hover_color=colors.green_2,
                                   command=self.show_errors)
        watch_bol_btn.place(relx=0.85, rely=0.9, anchor="center")
        
        # نمایش قرارداد های قدیمی
        old_deals = ctk.CTkButton(right_box, text="قرارداد های قدیمی", 
                                   width=140, height=50, 
                                   font=(None, 22, "bold"), 
                                   corner_radius=20, 
                                   text_color=colors.dark_green_6, 
                                   bg_color=colors.dark_green_6, 
                                   fg_color=colors.white, 
                                   hover_color=colors.green_2,
                                   command=go_to_old_deals)
        old_deals.place(relx=0.44, rely=0.9, anchor="center")
        
        # دکمه خروج
        back_to_dashboard_btn = ctk.CTkButton(right_box, text="بازگشت", 
                                   width=100, height=50, 
                                   font=(None, 22, "bold"), 
                                   corner_radius=20, 
                                   text_color=colors.dark_green_6, 
                                   bg_color=colors.dark_green_6, 
                                   fg_color=colors.white, 
                                   hover_color=colors.green_2,
                                   command=go_to_dashboard)
        back_to_dashboard_btn.place(relx=0.135, rely=0.9, anchor="center")
