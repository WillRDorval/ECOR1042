"""
By: William Dorval 101187466
Class: ECOR1042
"""
import sys
import inspect

import T099_image_filters as filters

REF = {'l': filters.load_image, 's': filters.save_as, '3': filters.three_tone, 'x': filters.extreme_contrast,
       't': filters.sepia, 'p': filters.posterize, 'e': filters.detect_edges, 'd': filters.draw_curve,
       'v': filters.flip_vertical, 'h': filters.flip_horizontal, 'q': sys.exit}

def command(cmd_in: str) -> filters.Image:
    cmd = REF.get(cmd_in.lower())

    if cmd is not None:
        if (args := inspect.getfullargspec(cmd)).args.__len__ == 0:
            final = cmd
        else:
            in_args = []
            if args.args.__len__ == 1:
                if args.args[0] == "input_image":
                    def final():
                        return cmd(filters.load_image(filters.choose_file()))
                elif args.args[0] == "filename":
                    def final():
                        return cmd(filters.choose_file())
            elif args.args.__len__ == 2:
                def final():
                    threshold = -1
                    while 0 > threshold or 255 > threshold:
                        try:
                            threshold = int(input("Please enter the threshold for the edge detection (0-255)"))
                            if threshold > 255 or threshold < 0:
                                raise ValueError
                        except ValueError:
                            print("please enter an integer between 0 and 255")

                    return cmd(filters.load_image(filters.choose_file()), threshold)
            elif args.args.__len__ == 3:
                def final():
                    while True:
                        print("valid colour names are black, white, blood, green, blue, lemon, cyan, magenta, gray")
                        colour = input("please enter the colour to draw: ")
                        if filters.color_names(colour) is None:
                            print("please enter a valid colour name ")
                        else:
                            break
                    return cmd(filters.load_image(filters.choose_file()), colour)
            else:
                def final():
                    colours = []
                    while True:
                        print("valid colour names are black, white, blood, green, blue, lemon, cyan, magenta, gray")
                        colours.append(input("please enter the colour to draw: "))
                        if filters.color_names(colours[-1]) is None:
                            print("please enter a valid colour name ")
                            colours.pop(-1)
                        else:
                            if colours.__len__ == 3:
                                break
                    return cmd(filters.load_image(filters.choose_file()), *colours)
    else:
        raise ValueError("invalid argument")
    return final()


if __name__ == '__main__':
    command('d')
