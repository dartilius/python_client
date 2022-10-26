import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()
# создаем рабочую область
frame = tkinter.Frame(root)
frame.grid()
# Добавим изображение
canvas = tkinter.Canvas(root, height=1080, width=1920)
image = Image.open("files/image_rmc_8800.png")
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw',image=photo)
canvas.grid(row=1, column=1)
root.mainloop()