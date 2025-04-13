from skimage.transform import resize

def resize_image(image, proporcion):
    assert 0 <= proporcion <= 1, "Specify a valid proporcion between 0 and 1."
    heigth = round(image.shape[0] * proportion)
    width = round(image.shape[1] * proportion)
    image_resize = resize(image, (heigth, width), anti_aliasing = True)
    return image_resize