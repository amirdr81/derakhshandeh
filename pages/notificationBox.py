import customtkinter as ctk
from notif_box import NotifBox
import insystem_data
import common_ctk as ck
import scrollbar
import colors

class NotificationBox(ctk.CTkFrame):     
    def add_notification(self, title, description, full_text, date, y, show_dashboard):
        return NotifBox(self.scrollable.inner_frame, title, description, full_text, date, y, show_dashboard, self.go_to_deals_page, self.go_to_drivers, self.go_to_cars, 
                        self.go_to_security, self.go_to_licence, self.go_to_workcart, self.super_parent)
    
    def remake_notifications(self, show_dashboard):
        notifications = insystem_data.loged_in_user["notifications"]
        number_of_notifications = len(notifications)
        if(number_of_notifications == 0):
            ck.make_label(self.box, 30, 30, colors.dark_green_6, colors.dark_green_6, colors.white, "مطلبی برای نمایش وجود ندارد.", 0, 'center', (None, 15, "bold"), 0.5, 180, 'center')
        else:
            self.scrollable = scrollbar.ScrollableFrame(self.box, 250, colors.dark_green_6)
            self.scrollable.pack(side="top", fill="x", padx=5, pady=(150, 10))

            for i in range(number_of_notifications):
                self.add_notification(notifications[i]["type"], 
                                    notifications[i]["description"], 
                                    notifications[i]["params"], 
                                    notifications[i]["date"], 
                                    225 + 63 * i,
                                    show_dashboard)
                               
    def __init__(self, parent, input_box, height, show_dashboard, go_to_deals_page, go_to_drivers, go_to_cars, go_to_security, go_to_licence, go_to_workcart, super_parent, offset=(0, 0)):
        self.parent = parent
        self.input_box = input_box
        self.height = height
        self.offset = offset
        self.show_dashboard = show_dashboard
        self.go_to_deals_page = go_to_deals_page
        self.go_to_drivers = go_to_drivers
        self.go_to_cars = go_to_cars
        self.go_to_security = go_to_security
        self.go_to_licence = go_to_licence
        self.go_to_workcart = go_to_workcart
        self.super_parent = super_parent
        self.box = None
        self.main_box = None

        self.input_box.bind("<Enter>", self.show_box)
        self.input_box.bind("<Leave>", self._on_label_leave)

    def show_box(self, event):
        if self.box:
            return
        #رسم باکس اصلی
        self.box = ctk.CTkFrame(self.parent, width=250, height=self.height,
                                corner_radius=20,
                                bg_color=colors.light_green_1,
                                fg_color=colors.dark_green_6)
        self.box.place(relx=0.24, rely=0.045, anchor="n")
        #رسم دایره بالای باکس
        ctk.CTkFrame(self.box, width=400, height=400,
                                corner_radius=200,
                                bg_color=colors.dark_green_6,
                                fg_color=colors.white).place(relx=0.5, y=-50, anchor="center")
        
        #عنوان باکس اعلانات
        ctk.CTkLabel(self.box, text="اعلانات", bg_color=colors.white, 
                     text_color=colors.dark_green_6,
                     font=(None, 45, "bold")).place(relx=0.5, y=50, anchor="center")
        #اضافه کردن نوتیفیکیشن ها
        self.remake_notifications(self.show_dashboard)
        
        self._inside_box = False

    def hide_box(self):
        if self.box:
            self.box.destroy()
            self.box = None

    def _on_label_leave(self, event):
        self.input_box.after(100, self._check_leave)

    def _on_box_enter(self, event):
        self._inside_box = True

    def _on_box_leave(self, event):
        self._inside_box = False
        self.box.after(100, self._check_leave)

    def _check_leave(self):
        if not self._mouse_over_widget(self.input_box) and self.box and not self._mouse_over_widget(self.box):
            self.hide_box()

    def _mouse_over_widget(self, widget):
        try:
            x, y = widget.winfo_pointerxy()
            widget_x = widget.winfo_rootx()
            widget_y = widget.winfo_rooty()
            return (widget_x <= x <= widget_x + widget.winfo_width() and
                    widget_y <= y <= widget_y + widget.winfo_height())
        except:
            return False