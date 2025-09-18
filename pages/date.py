import customtkinter as ctk
import tkinter as tk
import jdatetime

import colors

class Date(tk.Frame):
    def eng_to_persian_date(self, date_str):
        english_digits = '0123456789'
        persian_digits = '۰۱۲۳۴۵۶۷۸۹'
        trans_table = str.maketrans(''.join(english_digits), ''.join(persian_digits))
        return date_str.translate(trans_table)
    def __init__(self, master, callback=None):
        super().__init__(master,bg=colors.light_green_1)
        self.callback = callback
        self.today = jdatetime.date.today()
        self.displayed_month = self.today.month
        self.displayed_year = self.today.year
        self.labels = []

        self.header = tk.Label(self, text="", font=("B Nazanin", 14, "bold"), fg=colors.dark_green_6)
        self.header.grid(row=0, column=0, columnspan=7)

        for i, dayname in enumerate(['ج', 'پ', 'چ', 'س', 'د', 'ی', 'ش']):
            tk.Label(self, text=dayname, fg=colors.dark_green_6, bg=colors.light_green_1).grid(row=1, column=i)

        self.draw_days()
        self.navbar()

    def draw_days(self):
        # پاک‌کردن قبلی‌ها
        for label in self.labels:
            label.destroy()
        self.labels = []

        # لیبل ماه/سال
        self.header.config(text=f"{self.displayed_year}/{self.displayed_month}",
                           bg=colors.light_green_1, font=(None, 20, "bold"))
        first_day = jdatetime.date(self.displayed_year, self.displayed_month, 1)
        
        wd = (first_day.isoweekday() - 1) % 7

        days_in_month = jdatetime.j_days_in_month[self.displayed_month - 1]

        row = 2
        col = wd
        for day in range(1, days_in_month + 1):
            btn = ctk.CTkButton(self, text=str(self.eng_to_persian_date(str(day))), width=50,
                                bg_color=colors.light_green_1, 
                                fg_color=colors.dark_green_6,
                                text_color=colors.light_green_1,
                                hover_color=colors.green_3,
                            command=lambda d=day: self.select_day(d))
            btn.grid(row=row, column=6-col, padx=1, pady=1)
            self.labels.append(btn)
            col += 1
            if col > 6:
                col = 0
                row += 1
    def navbar(self):
        # کلید ماه قبلی/بعدی
        ctk.CTkButton(self, text="<", width=50,
                  bg_color=colors.light_green_1, 
                                fg_color=colors.dark_green_6,
                                text_color=colors.light_green_1,
                                hover_color=colors.green_3,
                                command=self.prev_month).grid(row=0, column=0, padx=1, pady=1)
        ctk.CTkButton(self, text=">", width=50,
                  bg_color=colors.light_green_1, 
                                fg_color=colors.dark_green_6,
                                text_color=colors.light_green_1,
                                hover_color=colors.green_3,
                                command=self.next_month).grid(row=0, column=6, padx=1, pady=1)

    def prev_month(self):
        if self.displayed_month == 1:
            self.displayed_month = 12
            self.displayed_year -= 1
        else:
            self.displayed_month -= 1
        self.draw_days()

    def next_month(self):
        if self.displayed_month == 12:
            self.displayed_month = 1
            self.displayed_year += 1
        else:
            self.displayed_month += 1
        self.draw_days()

    def select_day(self, day):
        selected = jdatetime.date(self.displayed_year, self.displayed_month, day)
        if self.callback:
            self.callback(selected)


