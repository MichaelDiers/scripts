import argparse
import os
from PIL import Image

def crop(image, x, y, width, height):
    return image.crop((x, y, x + width, y + height))

def resize(image, width, height):
    return image.resize((width, height))

def main(imageFile, cropInfo, resizeInfo, outFile):
    with Image.open(imageFile) as image:
        if cropInfo:
            x, y, width, height = cropInfo
            image = crop(image, x, y, width, height)
        if resizeInfo:
            width, height = resizeInfo
            image = resize(image, width, height)
        image.save(outFile)
            
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process images.')
    parser.add_argument('image', help='The input image file.')
    parser.add_argument('--crop', nargs=4, required=False, type=int, metavar=('x', 'y', 'width', 'height'), help='The new image spans a rectangle from (x,y) to (x+width, y+height)')
    parser.add_argument('--resize', nargs=2, required=False, type=int, metavar=('width', 'height'), help='Resizes the image to given width and height')
    parser.add_argument('--web', action='store_true', required=False, help='Creates images in different sizes.')
    parser.add_argument('out', metavar='outputFile', help='The output image')
    args = parser.parse_args()

    if not os.path.exists(args.image):
        parser.error(f'Image file {args.image} not found.')

    if os.path.exists(args.out):
        parser.error(f'Image file {args.out} already exists.')

    if args.resize and args.web:
        parser.error('Please specify resize or --web and not both.')

    cropInfo = None if not args.crop else args.crop

    if args.resize:
        main(args.image, cropInfo, resizeInfo, args.out)
    elif args.web:
        width, height = 300, 100
        for i in range(1, 5):
            name = f'{args.out[:-3]}{width * i}_{height * i}.{args.out[-3:]}'
            main(args.image, cropInfo, (width * i, height * i), name)
    else:
        main(args.image, cropInfo, None, args.out)
