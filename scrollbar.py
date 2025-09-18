import customtkinter as ctk
import colors

class ScrollableFrame(ctk.CTkFrame):
    def __init__(self, master, width, color, **kwargs):
        super().__init__(master, **kwargs)

        # کانتینر داخلی: یک سطر از canvas و اسکرول‌بار
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        # CTkCanvas
        self.canvas = ctk.CTkCanvas(self.container,  width=width, bg=color, highlightthickness=0)
        # حالا اسکرول‌بار با تم customtkinter
        self.scrollbar = ctk.CTkScrollbar(self.container, bg_color=color, fg_color=color, orientation="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # قاب داخلی
        self.inner_frame = ctk.CTkFrame(self.canvas, fg_color=color)
        # self.inner_frame.pack_propagate(False)
        self.inner_frame_window = self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        # layout
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # بروزرسانی اسکرول‌ریجن و هماهنگی عرض
        self.inner_frame.bind("<Configure>", lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<Configure>", lambda event: self.canvas.itemconfig(self.inner_frame_window, width=event.width))

        # اسکرول با موس (برای فقط همین فریم، نه کل برنامه)
        self.canvas.bind("<Enter>", lambda e: self.canvas.bind_all("<MouseWheel>", self._on_mousewheel))
        self.canvas.bind("<Leave>", lambda e: self.canvas.unbind_all("<MouseWheel>"))

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
