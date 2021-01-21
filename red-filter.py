from Cimpl import choose_file, load_image, copy, create_color, set_color,show, Image, get_color


def red_channel(image: Image) -> Image:
    new_image = copy(image)
    for pixel in new_image:
        x, y, (r, g, b) = pixel
        red = create_color(0, 0, b)
        set_color(new_image, x, y, red)
    return new_image
