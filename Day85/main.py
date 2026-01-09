import os
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk


class WaterMark(Tk):
    def __init__(self):
        super().__init__()

        self.title("Watermarker")
        self.configure(bg="white")
        self.config(padx=20, pady=20)
        self.resizable(True, True)

        self.canvas = Canvas(self, bg="white", width=400, height=400)
        self.canvas.grid(row=0, column=0, columnspan=3)

        self.btn_select_img = Button(self, text="Select Image", command=self.select_image)
        self.btn_watermark_img = Button(self, text="Add Watermark", command=self.add_watermark)
        self.btn_save_img = Button(self, text="Save Image", command=self.save_img)

        self.btn_select_img.grid(row=1, column=0)
        self.btn_watermark_img.grid(row=1, column=1)
        self.btn_save_img.grid(row=1, column=2)

        self.image_tk = None
        self.image_id = None
        self.current_image_path = None
        self.watermarked_image = None
        # Watermark text input
        Label(self, text="Watermark Text:", bg="white").grid(row=2, column=0)
        self.text_entry = Entry(self, width=20)
        self.text_entry.grid(row=2, column=1)

        # Font size input
        Label(self, text="Font Size:", bg="white").grid(row=3, column=0)
        self.font_size = IntVar(value=20)
        self.font_spinbox = Spinbox(
            self,
            from_=10,
            to=100,
            textvariable=self.font_size,
            width=5
        )
        self.font_spinbox.grid(row=3, column=1)

        self.mainloop()

    def select_image(self):
        self.current_image_path = filedialog.askopenfilename(
            title="Select Image File",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
        )

        if self.current_image_path:
            self.display_image(self.current_image_path)

    def add_watermark(self):
        if not self.current_image_path:
            return

        image = Image.open(self.current_image_path).convert("RGBA")
        draw = ImageDraw.Draw(image)

        # 🔹 Get values from Tkinter inputs
        text = self.text_entry.get()
        size = self.font_size.get()

        if not text:
            return  # prevent empty watermark

        try:
            font = ImageFont.truetype("arial.ttf", size)
        except IOError:
            font = ImageFont.load_default()

        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        width, height = image.size
        position = (width - text_width - 10, height - text_height - 10)

        draw.text(position, text, fill=(255, 255, 255, 180), font=font)

        self.watermarked_image = image
        self.display_image_from_pil(image)

    def save_img(self):
        if self.watermarked_image is None:
            return

        os.makedirs("output_image", exist_ok=True)
        save_path = filedialog.asksaveasfilename(
            filetypes=[
                ("PNG Image", "*.png"),
                ("JPEG Image", "*.jpg"),
                ("JPEG Image", "*.jpeg"),
                ("All Images", "*.png *.jpg *.jpeg")
            ]

        )

        if save_path:
            self.watermarked_image.convert("RGB").save(save_path)

    def display_image(self, file_path):
        image = Image.open(file_path)
        self.display_image_from_pil(image)

    def display_image_from_pil(self, image):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        image.thumbnail((canvas_width, canvas_height), Image.Resampling.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(image)

        if self.image_id:
            self.canvas.delete(self.image_id)

        self.image_id = self.canvas.create_image(0, 0, anchor="nw", image=self.image_tk)


WaterMark()
