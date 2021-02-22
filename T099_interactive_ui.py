"""
By: William Dorval 101187466
Class: ECOR1042
"""
import sys

import T099_image_filters as filters

REF = {'l': filters.load_image, 's': filters.save_as, '3': filters.three_tone, 'x': filters.extreme_contrast,
       't': filters.sepia, 'p': filters.posterize, 'e': filters.detect_edges, 'd': filters.draw_curve,
       'v': filters.flip_vertical, 'h': filters.flip_horizontal, 'q': sys.exit}

def command(cmd_in: str, image=None) -> filters.Image:
    """
    executes the command specified by the input string on the given image, the load (l) and quit (q) commands will
    work without providing an image
    >>> input_image = command('l')
    >>> filtered = command('t', input_image)
    >>> command('s', filtered)
    """
    cmd = REF.get(cmd_in := cmd_in.lower())

    if cmd is not None:
        if cmd_in == 'q':
            final = cmd
        elif cmd_in == 's':
            def final():
                return cmd(image)
        elif cmd_in == 'l':
            def final():
                return cmd(filters.choose_file())
        elif cmd_in == '3':
            def final():
                colours = []
                while True:
                    print("valid colour names are black, white, blood, green, blue, lemon, cyan, magenta, gray")
                    colours.append(input("please enter a colour to use for the three tone: "))
                    if filters.color_names(colours[-1]) is None:
                        print("please enter a valid colour name ")
                        colours.pop(-1)
                    else:
                        if colours.__len__() == 3:
                            break
                return cmd(image, *colours)
        elif cmd_in == 'x' or cmd_in == 't' or cmd_in == 'p' or cmd_in == 'h' or cmd_in == 'v':
            def final():
                return cmd(image)
        elif cmd_in == 'e':
            def final():
                threshold = -1
                while 0 > threshold or 255 < threshold:
                    threshold = int(input("Please enter the threshold for the edge detection (0-255)"))
                    if threshold > 255 or threshold < 0:
                        print("please enter an integer between 0 and 255")
                return cmd(image, threshold)
        else:
            def final():
                while True:
                    print("valid colour names are black, white, blood, green, blue, lemon, cyan, magenta, gray")
                    colour = input("please enter the colour to draw: ")
                    if filters.color_names(colour) is None:
                        print("please enter a valid colour name ")
                    else:
                        break
                return cmd(image, colour)
    else:
        print("Invalid Argument")

        return image
    if cmd_in != 'l' and cmd_in != 'q' and image is None:
        print("No image loaded")
        return image

    return final()


def main():
    image = None
    while True:
        print("L)oad image  S)ave-as\n3)-tone  X)treme contrast  T)int sepia  P)osterize\nE)dge detect  D)raw curve "
              " V)ertical flip  H)orizontal flip\nQ)uit\n")
        cmd = input(": ")
        image = command(cmd, image)
        if image is not None:
            filters.show(image)


if __name__ == '__main__':
    main()
