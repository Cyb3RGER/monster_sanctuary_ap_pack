from PIL import Image
import os

from utils import format_code


def main():
    for entry in os.scandir('../images/items/monsters'):
        if entry.is_file() and entry.name.endswith('.webp'):
            im = Image.open(entry.path)
            path, ext = os.path.splitext(entry.path)
            head, tail = os.path.split(path)
            im.save(f"{head}/{format_code(tail)}.png", "png")
            print(entry.path, '->', f"{head}/{format_code(tail)}.png")


if __name__ == "__main__":
    main()
