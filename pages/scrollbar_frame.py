import customtkinter as ctk

class ScrollableFrame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.canvas = ctk.CTkCanvas(self, bg=kwargs.get("fg_color","white"), highlightthickness=0)
        self.v_scrollbar = ctk.CTkScrollbar(self, orientation="vertical", command=self.canvas.yview)
        self.h_scrollbar = ctk.CTkScrollbar(self, orientation="horizontal", command=self.canvas.xview)

        self.canvas.configure(yscrollcommand=self.v_scrollbar.set, xscrollcommand=self.h_scrollbar.set)

        self.v_scrollbar.pack(side="right", fill="y")
        self.h_scrollbar.pack(side="bottom", fill="x")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.inner_frame = ctk.CTkFrame(self.canvas, fg_color=kwargs.get("fg_color","white"))
        self.inner_window = self.canvas.create_window((0,0), window=self.inner_frame, anchor="nw")
        
        self.inner_frame.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)

        # فعالسازی اسکرول موس  
        self.inner_frame.bind("<Enter>", lambda e:self._bind_mousewheel())
        self.inner_frame.bind("<Leave>", lambda e:self._unbind_mousewheel())

    def _on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all")) # محدوده اسکرول

    def _on_canvas_configure(self, event):
        # سایز جدول داخل کانواس
        self.canvas.itemconfig(self.inner_window, width=event.width)

    def _bind_mousewheel(self):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind_all("<Shift-MouseWheel>", self._on_shiftmousewheel)

    def _unbind_mousewheel(self):
        self.canvas.unbind_all("<MouseWheel>")
        self.canvas.unbind_all("<Shift-MouseWheel>")

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(-int(event.delta/120), "units")
    def _on_shiftmousewheel(self, event):
        self.canvas.xview_scroll(-int(event.delta/120), "units")
