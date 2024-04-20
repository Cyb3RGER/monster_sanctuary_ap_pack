from PIL import Image, ImageOps
import os

from utils import format_code


def main():
    check_path = '../images/items/monsters'
    if not os.path.exists(check_path+'/resized'):
        os.mkdir(check_path+'/resized')

    max_size = 0
    for entry in os.scandir(check_path):
        if entry.is_file() and entry.name.endswith('.png'):
            im = Image.open(entry.path)
            size = im.size
            max_size = max(*size, max_size)

    for entry in os.scandir(check_path):
        if entry.is_file() and entry.name.endswith('.png'):
            im = Image.open(entry.path)
            check_path, ext = os.path.splitext(entry.path)
            head, tail = os.path.split(check_path)
            size = im.size
            if size[0] != size[1]:
                new_size = max(*size)
                if size[0] > size[1]:
                    pos = (0, (size[0] - size[1]) // 2)
                else:
                    pos = ((size[1] - size[0]) // 2, 0)
                im2 = Image.new(im.mode, (new_size, new_size), (0, 0, 0, 0))
                im2.paste(im, pos)
            else:
                im2 = im.copy()
            # im2 = im2.resize((max_size, max_size), Image.NONE)
            im2.save(f"{head}/resized/{format_code(tail)}.png", "png")
            print(entry.path, '->', f"{head}/resized/{format_code(tail)}.png")


if __name__ == "__main__":
    main()
