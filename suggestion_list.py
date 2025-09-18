#main imports
import customtkinter as ctk

import bol_fake_data

#controllers
import common_controller as cc
import common_ctk as ck

#colors
import colors

class ItemDisplay():
    def __init__(self, box, y, item, input, widget, widget2, type, width):
        def hover(event):
            name_frame.configure(fg_color = colors.red_color)
            name_label.configure(fg_color = colors.red_color)
            
        def unhover(event):
            name_frame.configure(fg_color = colors.dark_gray_color)
            name_label.configure(fg_color = colors.dark_gray_color)
            
        def clicked(event):
            widget.delete(0, "end")
            if(type == 0): 
                widget.delete(0, 'end')
                widget.insert(0, item[input[0]] + " " + item[input[1]])
                name_frame.destroy()
            elif(type == 1 or type == 5): 
                widget.delete(0, 'end')
                widget.insert(0, item)
                name_frame.destroy()
            elif(type == 2): 
                widget.delete(0, 'end')
                widget.insert(0, item[input[0]] + "/" + item[input[1]])
                name_frame.destroy()
            elif(type == 3): 
                widget.delete(0, 'end')
                widget2.delete(0, 'end')
                widget.insert(0, item[input[0]])
                widget2.insert(0, item[input[1]])
                name_frame.destroy()
            elif(type == 4):
                widget.delete(0, 'end')
                widget.insert(0, cc.eng_to_persian_date(item.split('/')[1]))
                
                
            box.focus_set()
            
            
        name_frame = ck.make_frame(box, width, 30, colors.light_gray_2, colors.dark_gray_color, colors.dark_gray_color, 0, 0, 
                              0.5, y, "n")
        if(type == 0):
            name_label = ck.make_label(name_frame, 200, 30, colors.dark_gray_color, colors.dark_gray_color, colors.white, 
                                    item[input[0]] + " " + item[input[1]] + " - " + cc.eng_to_persian_date(item[input[2]]), 0, None, (None, 15), 0.5, 0.5, "center")
        elif(type == 1 or type == 4 or type == 5):
            name_label = ck.make_label(name_frame, 200, 30, colors.dark_gray_color, colors.dark_gray_color, colors.white, 
                                    item, 0, None, (None, 15), 0.5, 0.5, "center")
        elif(type == 2 or type == 3):
            name_label = ck.make_label(name_frame, 200, 30, colors.dark_gray_color, colors.dark_gray_color, colors.white, 
                                    item[input[0]] + "/" + item[input[1]], 0, None, (None, 15), 0.5, 0.5, "center")
        name_frame.bind("<Enter>", hover)
        name_label.bind("<Enter>", hover)
        name_frame.bind("<Leave>", unhover)
        name_label.bind("<Leave>", unhover)
        name_frame.bind("<Button-1>", clicked)
        name_label.bind("<Button-1>", clicked)
        
        
class SuggestionList(ctk.CTkFrame):    
    def hide_box(self):
        self.sug_box.place_forget()
        
    def show_box(self):
        if(self.type == 0):
            self.shown_data = [item for item in self.target_arr if (cc.match_input2(self.widget.get(), item[self.input[0]] + " " + item[self.input[1]]) and cc.doe)]
        elif(self.type == 1):
            self.shown_data = [item for item in self.target_arr if cc.match_input2(self.widget.get(), item)]
        elif(self.type == 2 or self.type == 3):
            self.shown_data = [item for item in self.target_arr if cc.match_input2(self.widget.get(), item[self.input[0]] + "/" + item[self.input[1]])]
        elif(self.type == 4):
            if(cc.does_item_exist(bol_fake_data.car_sample_data, 'car_id', self.widget2.get())):
                driver_names = cc.get_car_by_carid(self.widget2.get())['driver_name']
                drivers = []
                for fullname in driver_names: drivers.append(cc.get_driver_by_fullname(fullname))
                self.shown_data = [item['name'] + " " + item['lastname'] + "/" + cc.eng_to_persian_date(item['id']) for item in drivers]
            else:
                self.shown_data = [item for item in self.target_arr if (cc.match_input2(self.widget.get(), item))]
        elif(self.type == 5):
            self.shown_data = [item['name'] + " " + item['lastname'] + '/' + cc.eng_to_persian_date(item['id']) for item in self.target_arr if (cc.match_input2(self.widget.get(), item['name'] + " " + item['lastname'] + '/' + cc.eng_to_persian_date(item['id'])))]
            
        each_y = float(1 / max(1, len(self.shown_data)))
        for child in self.sug_box.winfo_children(): child.destroy()
        
        self.sug_box.configure(height = 31 * (len(self.shown_data)))
        for i, item in enumerate(self.shown_data):
            ItemDisplay(self.sug_box, i * each_y, item, self.input, self.widget, self.widget2, self.type, self.width)
            
        self.sug_box.place(relx=self.x, rely=self.y, anchor = self.anchor)
            
    def __init__(self, parent, widget, widget2, input, target_arr, x, y, anchor, type, width):
        super().__init__(parent)
        self.widget = widget
        self.widget2 = widget2
        self.input = input
        self.target_arr = target_arr
        self.x = x
        self.y = y
        self.anchor = anchor
        self.type = type
        self.width = width
        self.shown_data = []
        
        if(self.type == 0):
            self.shown_data = [item for item in target_arr if cc.match_input2(widget.get(), item[input[0]] + " " + item[input[1]])]
        elif(self.type == 1):
            self.shown_data = [item for item in target_arr if (cc.match_input2(widget.get(), item))]
        elif(self.type == 2 or self.type == 3):
            self.shown_data = [item for item in self.target_arr if cc.match_input2(self.widget.get(), item[self.input[0]] + "/" + item[self.input[1]])]
        elif(self.type == 4):
            if(cc.does_item_exist(bol_fake_data.car_sample_data, 'car_id', widget2.get())):
                driver_names = cc.get_car_by_carid(widget2.get())['driver_name']
                drivers = []
                for fullname in driver_names: drivers.append(cc.get_driver_by_fullname(fullname))
                self.shown_data = [item['name'] + " " + item['lastname'] + "/" + cc.eng_to_persian_date(item['id']) for item in drivers]
            else:
                self.shown_data = [item for item in target_arr if (cc.match_input2(widget.get(), item))]
        elif(self.type == 5):
            self.shown_data = [item['name'] + " " + item['lastname'] + '/' + cc.eng_to_persian_date(item['id']) for item in target_arr if (cc.match_input2(widget.get(), item['name'] + " " + item['lastname'] + '/' + cc.eng_to_persian_date(item['id'])))]
            
        each_y = float(1 / max(1, len(self.shown_data)))
        
        self.sug_box = ck.make_frame(parent, width, 31 * (len(self.shown_data)), colors.dark_green_6, 
                                    colors.light_gray_2, colors.blue_color, 0, 0, x, y, anchor)
        # self.hide_box()
        for i, item in enumerate(self.shown_data):
            ItemDisplay(self.sug_box, i * each_y, item, self.input, self.widget, self.widget2, self.type, self.width)