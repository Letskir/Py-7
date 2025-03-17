from PIL import Image, ImageFilter

# with Image.open('photo.png') as photo:
#     photo.show()
#     print(photo.size)
#     print(photo.format)
#     print(photo.mode)
#     photo_blured=photo.filter(ImageFilter.BLUR)
#     photo_blured.save("photo_blur.png")
#     photo_blured.show()

while True:
    name = input("Задайте ім'я картинки")
    if name=="stop":
        break
    try:
        photo = Image.open(name + ".png")
        photo.show()
        
    except:
       print('Такої картинки не знайдено')