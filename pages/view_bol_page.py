import customtkinter as ctk
import tkinter.ttk as ttk
import tkinter as tk
from bol_fake_data import current_bols, old_bols
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox
from bol_inf import BolInf
from edit_bol_page import EditBol
import common_controller as cc
import common_ctk as ck
import register_controller as rc
import asset_paths
import colors

class ViewBol(ctk.CTkFrame):    
    def set_series_cashID(self):
        selected_items = self.tree.selection()
        
        def confirm():
            def change_cashID():
                for i, item_id in enumerate(selected_items):
                    selected_data = current_bols[int(self.tree.item(item_id, 'values')[0]) - 1]
                    selected_data['cash_id'] = cc.eng_to_persian_date(str(int(cc.persian_to_eng_date(entry.get())) + i))
                cancel()
                self.reset_page()
            def cancel():
                if(confirm_box): confirm_box.destroy()
                if(second_frame): second_frame.destroy()
                self.reset_page()
                
            if(entry.get() == '' or entry.get() == None): return
            start_num = cc.eng_to_persian_date(entry.get())
            end_num = cc.eng_to_persian_date(str(int(cc.persian_to_eng_date(entry.get())) + len(selected_items) - 1))
            second_frame = rc.show_confirmation_box(self, change_cashID, cancel, 'شماره بارنامه ها از ' + start_num +
                                     ' تا ' + end_num + '، خواهد بود.', None)
            
        confirm_box = ck.make_frame(self, 350, 150, colors.light_green_1, colors.light_green_1, None, 0, 0, 0.5, 0.5, "center")
        
        entry = ck.make_entry(confirm_box, 250, 40, colors.light_green_1, colors.light_gray_5, colors.light_gray_5,
                      colors.black, 'شروع شماره حواله از...', colors.dark_gray_color, 20, 'right',
                      (None, 15), 0.5, 0.4, 'center')
        ck.make_label(confirm_box, 300, 30, colors.light_green_1,
                    colors.light_green_1, colors.dark_green_6, 'شماره حواله بارنامه اول را وارد کنید:',
                    0, "center", (None, 16), 0.5, 0.15, "center")

        ck.make_button(confirm_box, "بله", 70, 30, None, 10, 
                    colors.light_green_1, colors.light_green_1, colors.dark_green_6,
                    colors.green_3, confirm, 0.35, 0.8, "center")
        ck.make_button(confirm_box, "خیر", 70, 30, None, 10, 
                    colors.light_green_1, colors.light_green_1, colors.dark_green_6,
                    colors.green_3, lambda: confirm_box.destroy(), 0.65, 0.8, "center")
            
          
    def __init__(self, parent, go_to_dashboard, go_to_bol_groups, go_to_archived_bols, reset_page):
        super().__init__(parent)
        
        self.pack(fill="both", expand=True)
        self.configure(fg_color=colors.light_green_1)
        self.go_to_bol_groups = go_to_bol_groups
        self.go_to_archived_bols=go_to_archived_bols
        self.reset_page = reset_page
        self.shown_data = current_bols
        
            
        def activate_all_widgets(parent):
            for child in parent.winfo_children():
                if isinstance(child, ctk.CTkButton):
                    child.configure(state='normal')
                activate_all_widgets(child)
                        
        def disable_all_widgets(parent):
            for child in parent.winfo_children():
                if isinstance(child, ctk.CTkButton):
                    child.configure(state='disabled')
                disable_all_widgets(child)      
        def show_delete_confirm():
            disable_all_widgets(parent)
            selected_data = []
            for i, item_id in enumerate(self.tree.selection()):
                    selected_data.append(current_bols[int(self.tree.item(item_id, 'values')[0]) - 1])
            # selected_data = current_bols[int(self.tree.item(self.tree.selection()[0], 'values')[0]) - 1]
            dialog = ctk.CTkFrame(self, width=self.winfo_screenwidth() / 4.5, 
                                height=self.winfo_screenheight() / 8, 
                                fg_color="#FFFFFF")
            dialog.place(relx=0.5, rely=0.5, anchor="center")

            lbl = ctk.CTkLabel(dialog, 
                            text="آیا از آرشیو این بارنامه/بارنامه‌ها، مطمئن هستید؟", 
                            font=(None, 16),
                            text_color=colors.black)
            lbl.place(relx=0.5, rely=0.2, anchor="center")

            def do_delete():
                activate_all_widgets(parent)
                for item_id in selected_data:
                    current_bols.remove(item_id)
                    old_bols.append(item_id)
                self.reset_page()
                dialog.destroy()
            def cancel(): 
                activate_all_widgets(parent)
                dialog.destroy()

            btn_yes = ctk.CTkButton(dialog, text="بله", width=70, command=do_delete, fg_color=colors.dark_green_5, hover_color=colors.green_3)
            btn_no = ctk.CTkButton(dialog, text="خیر", width=70, command=cancel, fg_color=colors.dark_green_5, hover_color=colors.green_3)
            btn_yes.place(relx=0.35, rely=0.8, anchor="center")
            btn_no.place(relx=0.65, rely=0.8, anchor="center")
            
        def add_row(data_tuple):
            iid = self.tree.insert("", tk.END, values=data_tuple)
            self.tree.tag_configure(f"hover_{iid}", background=colors.light_green_5)
            self.tree.item(iid, tags=(f"hover_{iid}",))
            return iid

        def edit_bol():
            global bol_frame
            try: bol_frame.destroy()
            except: pass
            bol_frame = ck.make_frame(self, float(self.master.winfo_screenwidth() / 1.3), float(self.master.winfo_screenheight() / 1.8),
                                      colors.light_green_1, colors.light_green_1, colors.light_green_1, 0, 0, 0.5, 0.5, "center")

            cal = EditBol(bol_frame, reset_page, self.shown_data[int(self.tree.item(self.tree.selection()[0], 'values')[0]) - 1])
            cal.place(relx=0.5, rely=0.5, anchor="center")
            ck.make_button(bol_frame, 'بستن', 120, 30, (None, 25), 60, colors.light_green_1,
                           colors.light_green_1, colors.dark_green_6, colors.green_3,
                           lambda: bol_frame.destroy(), 0.075, 0.91, "center")
        
        def open_bol():
            global bol_frame
            try: bol_frame.destroy()
            except: pass
            bol_frame = ck.make_frame(self, float(self.master.winfo_screenwidth() / 1.3), float(self.master.winfo_screenheight() / 2.5),
                                      colors.light_green_1, colors.light_green_1, colors.light_green_1, 0, 0, 0.5, 0.5, "center")

            cal = BolInf(bol_frame, go_to_archived_bols, self.shown_data[int(self.tree.item(self.tree.selection()[0], 'values')[0]) - 1])
            cal.place(relx=0.5, rely=0.5, anchor="center")
            ck.make_button(bol_frame, 'بستن', 120, 30, (None, 25), 60, colors.light_green_1,
                           colors.light_green_1, colors.dark_green_6, colors.green_3,
                           lambda: bol_frame.destroy(), 0.075, 0.91, "center")
        
        
            
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
                                 selectmode='extended')

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
        for i, item in enumerate(current_bols): 
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

        
        

        sign_in_label = ctk.CTkLabel(main_box, text="بارنامه‌های فعال", font=(None, 45, "bold"), text_color=colors.black, bg_color=colors.white)
        sign_in_label.place(relx=0.5, rely=0.1, anchor="center")
        
        #ویرایش بارنامه
        edit_bol_btn = ctk.CTkButton(main_box, text="ویرایش بارنامه", 
                                   width=150, height=50, 
                                   font=(None, 22, "bold"), 
                                   corner_radius=20, 
                                   bg_color=colors.white, 
                                   fg_color=colors.light_gray_1, 
                                   text_color=colors.light_gray_6, 
                                   hover_color=colors.green_3, 
                                   state="disabled",
                                   command=lambda:edit_bol())
        edit_bol_btn.place(relx=0.91, rely=0.94, anchor="center")
        
        #حذف بارنامه
        delete_bol_btn = ctk.CTkButton(main_box, text="آرشیو بارنامه", 
                                   width=150, height=50, 
                                   font=(None, 22, "bold"), 
                                   corner_radius=20, 
                                   bg_color=colors.white, 
                                   fg_color=colors.light_gray_1, 
                                   text_color=colors.light_gray_6, 
                                   hover_color=colors.green_3, 
                                   state="disabled",
                                   command=show_delete_confirm)
        delete_bol_btn.place(relx=0.765, rely=0.94, anchor="center")
        
        ck.make_button(main_box, "صورت‌های بسته شده", 150, 50, (None, 22, "bold"), 20, 
                       colors.white, colors.white, colors.dark_green_6, colors.green_3, 
                       self.go_to_bol_groups, 0.98, 0.04, "ne")
        ck.make_button(main_box, "آرشیو بارنامه‌ها", 150, 50, (None, 22, "bold"), 20, 
                       colors.white, colors.white, colors.dark_green_6, colors.green_3, 
                       self.go_to_archived_bols, 0.98, 0.13, "ne")
        consequence_cashID = ck.make_button(main_box, "حواله ترتیبی", 150, 50, (None, 22, "bold"), 20, 
                       colors.light_gray_6, colors.white, colors.light_gray_1, colors.green_3, 
                       self.set_series_cashID, 0.98, 0.22, "ne")
        consequence_cashID.configure(state='disabled')
        
        
        back_to_dashboard_btn = ctk.CTkButton(main_box, text="بازگشت", 
                                   width=150, height=50, 
                                   font=(None, 22, "bold"), 
                                   corner_radius=20, 
                                   text_color=colors.white, 
                                   bg_color=colors.white, 
                                   fg_color=colors.dark_green_5, 
                                   hover_color=colors.green_3,
                                   command=go_to_dashboard)
        back_to_dashboard_btn.place(relx=0.075, rely=0.94, anchor="center")
        
        def on_item_select(event):
            selected_items = self.tree.selection()
            if len(selected_items) == 1: 
                consequence_cashID.configure(state="disabled", fg_color=colors.light_gray_1, text_color = colors.light_gray_6)
                edit_bol_btn.configure(state="normal", fg_color=colors.dark_green_6, text_color = colors.white)
                delete_bol_btn.configure(state="normal", fg_color=colors.dark_green_6, text_color = colors.white)
            elif(len(selected_items) == 0): 
                consequence_cashID.configure(state="disabled", fg_color=colors.light_gray_1, text_color = colors.light_gray_6)
                edit_bol_btn.configure(state="disabled", fg_color=colors.light_gray_1, text_color = colors.light_gray_6)
                delete_bol_btn.configure(state="disabled", fg_color=colors.light_gray_1, text_color = colors.light_gray_6)
            else:
                consequence_cashID.configure(state="normal", fg_color=colors.dark_green_6, text_color = colors.white)
                edit_bol_btn.configure(state="disabled", fg_color=colors.light_gray_1, text_color = colors.light_gray_6)
                delete_bol_btn.configure(state="normal", fg_color=colors.dark_green_6, text_color = colors.white)
                
        self.tree.bind("<<TreeviewSelect>>", on_item_select)
        
        def on_tree_double_click(event):
            item_id = self.tree.focus()
            if item_id: open_bol()
        self.tree.bind("<Double-1>", on_tree_double_click)
        
        
        # لوگو
        ck.make_image(main_box, asset_paths.Logo_path, 88, 90, 0.02, 0.04, "nw")