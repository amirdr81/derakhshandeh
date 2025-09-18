#main libraries
import customtkinter as ctk
import tkinter as tk
from customtkinter import *
from PIL import Image
from date import Date

#controllers
import common_controller as cc

#data imports
import asset_paths

#colors
import colors

def update_label_error(widget, delay, text):
    widget.configure(text=text)
    widget.after(delay, lambda: widget.configure(text=""))
    
def show_error(widget, normal_color, delay):
    widget.configure(border_color = colors.red_color, border_width=2)
    widget.after(delay, lambda: widget.configure(border_color=normal_color))
    
def open_calendar(box, entry, x_co, y_co, selected_text):
    global calendar_frame
    try: calendar_frame.destroy()
    except: pass
    calendar_frame = tk.Frame(box, bd=2, relief=tk.RIDGE,
                                bg=colors.light_green_1)
    calendar_frame.place(relx=x_co, rely=y_co, anchor="center")
    def on_date_selected(selected_date):
        entry.configure(text=cc.eng_to_persian_date(str(selected_date).replace("-", "/")), text_color=selected_text)  
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
            
def make_entry_with_text(entry, text):
    my_var = ctk.StringVar()
    my_var.set(cc.eng_to_persian_date(text))
    entry.configure(textvariable=my_var)
    
def make_entry(box, width, height, 
                       bg_color, fg_color, border_color, text_color, 
                       placeholder_text, placeholder_text_color,
                       corner_radius, 
                       justify,
                       font, x, y, anchor):
        entry_box = ctk.CTkEntry(box,
                                 width = width,
                                 height = height,
                                 bg_color = bg_color,
                                 fg_color = fg_color,
                                 border_color = border_color, 
                                 text_color = text_color,
                                 placeholder_text = placeholder_text,
                                 placeholder_text_color = placeholder_text_color,
                                 corner_radius = corner_radius,
                                 justify = justify,
                                 font=font)
        entry_box.place(relx=x, rely=y, anchor=anchor)
        return entry_box

def make_label(box, width, height, 
                       bg_color, fg_color, text_color, 
                       text,
                       corner_radius, 
                       justify,
                       font, x, y, anchor):
        label = ctk.CTkLabel(box,
                                 width = width,
                                 height = height,
                                 bg_color = bg_color,
                                 fg_color = fg_color,
                                 text_color = text_color,
                                 text = text,
                                 corner_radius = corner_radius,
                                 justify = justify,
                                 font=font)
        if(x < 1 and y < 1): label.place(relx=x, rely=y, anchor=anchor)
        elif(y < 1): label.place(x=x, rely=y, anchor=anchor)
        elif(x < 1): label.place(relx=x, y=y, anchor=anchor)
        else: label.place(x=x, y=y, anchor=anchor)
        return label

def make_button(box, text, width, height, font, corner_radius, text_color,
                bg_color, fg_color, hover_color, command, x, y, anchor):
    btn = ctk.CTkButton(box, 
                        text = text, 
                        width = width, 
                        height = height, 
                        font = font, 
                        corner_radius = corner_radius, 
                        text_color = text_color, 
                        bg_color = bg_color, 
                        fg_color = fg_color, 
                        hover_color = hover_color,
                        command=command)
    btn.place(relx=x, rely=y, anchor=anchor)
    return btn

def make_frame(box, width, height, bg_color, fg_color, border_color, border_width, corner_radius, x, y, anchor):
    frame = ctk.CTkFrame(box, 
                        width=width, 
                        height=height,
                        bg_color=bg_color,
                        fg_color=fg_color,
                        border_color=border_color,
                        border_width=border_width,
                        corner_radius=corner_radius)
    frame.place(relx=x, rely=y, anchor=anchor)
    return frame

def make_frame2(box, width, height, bg_color, fg_color, border_color, border_width, corner_radius, x, y, anchor):
    frame = ctk.CTkFrame(box, 
                        width=width, 
                        height=height,
                        bg_color=bg_color,
                        fg_color=fg_color,
                        border_color=border_color,
                        border_width=border_width,
                        corner_radius=corner_radius)
    frame.place(relx=x, y=y, anchor=anchor)
    return frame

def make_list(box, text, options, width, height, text_color, bg_color, fg_color, button_color, button_hover_color, 
              corner_radius, command, anchor1, x, y, anchor):
    list_box = ctk.CTkOptionMenu(
        box,
        variable=ctk.StringVar(value=text),
        values=options,
        width=width,
        height=height,
        text_color=text_color,
        bg_color=bg_color,
        fg_color=fg_color,
        button_color=button_color,
        button_hover_color=button_hover_color,
        corner_radius=corner_radius,
        anchor=anchor1,
        command=command
    )
    list_box.place(relx=x, rely=y, anchor=anchor)
    return list_box

    
def make_image(box, path, logo_width, logo_height, x, y, anchor):
    photo = Image.open(path)
    ctk_image = CTkImage(light_image=photo, size=(logo_width, logo_height))
    img_label = ctk.CTkLabel(box, image=ctk_image, text="", width= logo_width, height=logo_height)
    img_label.place(relx=x, rely=y, anchor=anchor)
    return img_label