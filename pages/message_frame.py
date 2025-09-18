import customtkinter as ctk
import tkinter.font as tkfont
from PIL import Image, ImageTk
from asset_paths import unseen_photo, seen_photo
import common_ctk as ck
import colors

class Message(ctk.CTkFrame):       
    def __init__(self, canvas, sender, receiver, message, date, isSeen, isMe, y, width, height):
        self.canvas = canvas
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.date = date
        self.isSeen = isSeen
        self.isMe = isMe
        self.y = y
        self.corner = 10
        self.frames_space = 5
        self.date_width = 30
        self.date_height = 15
        
        self.width = width
        self.height = height
        
        self.font = tkfont.Font(size=18)
        
        if(isMe):
            main_box = ctk.CTkFrame(self.canvas, 
                                    width=max(self.width, self.date_width + 25) + 2 * self.corner,
                                    height=self.height + 2 * self.corner + self.frames_space + self.date_height,
                                    bg_color=colors.light_gray_2, 
                                    fg_color=colors.dark_green_6,
                                    corner_radius=self.corner + 5)
            self.canvas.create_window(1050, y, anchor="ne", window=main_box)
            
            message_frame = ctk.CTkFrame(main_box, 
                                    width=self.width,
                                    height=self.height, 
                                    bg_color=colors.dark_green_6, 
                                    fg_color=colors.dark_green_6,
                                    corner_radius=0)
            message_frame.place(x=self.corner, y=self.corner, anchor="nw")
            
            date_frame = ctk.CTkFrame(main_box, 
                                    width=self.date_width, 
                                    height=self.date_height, 
                                    bg_color=colors.dark_green_6, 
                                    fg_color=colors.dark_green_6,
                                    corner_radius=0)
            date_frame.place(x=self.corner, y=self.height + self.corner + self.frames_space + self.date_height, anchor="sw")
            
            label = ctk.CTkLabel(message_frame, 
                                 text=self.message, 
                                 text_color=colors.white,
                                 font=(None, 18),
                                 wraplength=self.width,
                                 justify="right")
            label.place(relx=1, rely=0, anchor="ne")
            
            date_label = ctk.CTkLabel(date_frame, 
                                      text=self.date, 
                                      text_color=colors.white,
                                      font=(None, 12))
            date_label.place(relx=0, rely=0.5, anchor="w")
            
            if(not isSeen):
                seen_photo_label = ctk.CTkLabel(main_box, image=ImageTk.PhotoImage(Image.open(unseen_photo).resize((15, 10))),
                                    text="", width=15, height=10, 
                                    bg_color=colors.dark_green_6,
                                    corner_radius=8,
                                    )
                seen_photo_label.place(x=max(self.width, self.date_width + 25) + self.corner, y=self.height + self.corner + self.frames_space + self.date_height, anchor="se")
            else:
                seen_photo_label = ctk.CTkLabel(main_box, image=ImageTk.PhotoImage(Image.open(seen_photo).resize((15, 10))),
                                    text="", width=15, height=10, 
                                    bg_color=colors.dark_green_6,
                                    corner_radius=8,
                                    )
                seen_photo_label.place(x=max(self.width, self.date_width + 25) + self.corner, y=self.height + self.corner + self.frames_space + self.date_height, anchor="se")
        else:
            main_box = ctk.CTkFrame(self.canvas, 
                                    width=self.width + 2 * self.corner,
                                    height=self.height + 2 * self.corner + self.frames_space + self.date_height,
                                    bg_color=colors.light_gray_2, 
                                    fg_color=colors.white,
                                    corner_radius=self.corner + 5)
            self.canvas.create_window(50, y, anchor="nw", window=main_box)
            
            message_frame = ctk.CTkFrame(main_box, 
                                    width=self.width,
                                    height=self.height, 
                                    bg_color=colors.white, 
                                    fg_color=colors.white,
                                    corner_radius=0)
            message_frame.place(x=self.corner, y=self.corner, anchor="nw")
            
            date_frame = ctk.CTkFrame(main_box, 
                                    width=self.date_width, 
                                    height=self.date_height, 
                                    bg_color=colors.white, 
                                    fg_color=colors.white,
                                    corner_radius=0)
            date_frame.place(x=self.corner, y=self.height + self.corner + self.frames_space + self.date_height, anchor="sw")
            
            label = ctk.CTkLabel(message_frame, 
                                 text=self.message, 
                                 text_color=colors.black,
                                 font=(None, 18),
                                 wraplength=self.width,
                                 justify="right")
            label.place(relx=1, rely=0, anchor="ne")
            
            date_label = ctk.CTkLabel(date_frame, 
                                      text=self.date, 
                                      text_color=colors.black,
                                      font=(None, 12))
            date_label.place(relx=0, rely=0.5, anchor="w")
            