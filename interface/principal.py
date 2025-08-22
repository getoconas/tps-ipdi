import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class Window:
  def __init__(self, root):
    self.root = root
    self.root.title("Interfaz de Imágenes")
    self.root.geometry("800x600")

    # Marcos para las imágenes
    self.left_frame = tk.Frame(root, width=250, height=400, bd=2, relief=tk.SOLID)
    self.left_frame.place(x=50, y=100)
    self.right_frame = tk.Frame(root, width=250, height=400, bd=2, relief=tk.SOLID)
    self.right_frame.place(x=500, y=100)

    # Etiquetas para mostrar imágenes
    self.left_label = tk.Label(self.left_frame)
    self.left_label.pack(expand=True)
    self.right_label = tk.Label(self.right_frame)
    self.right_label.pack(expand=True)

    # Botones
    self.select_btn = tk.Button(root, text="Seleccionar imagen", command=self.select_image, width=20, height=2)
    self.select_btn.place(x=320, y=200)
    self.process_btn = tk.Button(root, text="Procesar", command=self.process_image, width=20, height=2)
    self.process_btn.place(x=320, y=300)

    # Variables para imágenes
    self.img = None
    self.img_tk = None
    
  def select_image(self):
    file_path = filedialog.askopenfilename(filetypes=[("Imagenes", "*.png;*.jpg;*.jpeg;*.bmp")])
    if file_path:
      self.img = Image.open(file_path)
      self.img = self.img.resize((240, 380))
      self.img_tk = ImageTk.PhotoImage(self.img)
      self.left_label.config(image=self.img_tk)
      self.left_label.image = self.img_tk

  def process_image(self):
    if self.img:
      # Por ahora solo muestra la misma imagen en el recuadro derecho
      img_proc = self.img.copy()
      img_proc_tk = ImageTk.PhotoImage(img_proc)
      self.right_label.config(image=img_proc_tk)
      self.right_label.image = img_proc_tk