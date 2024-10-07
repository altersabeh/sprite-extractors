import os
import sys
from xml.etree import ElementTree
from PIL import Image


def tree_to_dict(tree):
    d = {}
    for index, item in enumerate(tree):
        if item.tag == 'key':
            if tree[index + 1].tag == 'string':
                d[item.text] = tree[index + 1].text
            elif tree[index + 1].tag == 'true':
                d[item.text] = True
            elif tree[index + 1].tag == 'false':
                d[item.text] = False
            elif tree[index + 1].tag == 'dict':
                d[item.text] = tree_to_dict(tree[index + 1])
    return d


def unpack_cocos2dx(plist_filename, png_filename):
    file_path = plist_filename.replace('.plist', '')
    big_image = Image.open(png_filename)
    root = ElementTree.fromstring(open(plist_filename, 'r').read())
    plist_dict = tree_to_dict(root[0])

    def to_list(x): return x.replace('{', '').replace('}', '').split(',')

    for k, v in plist_dict['frames'].items():
        offset = [0, 0]  # Default value for offset
        rectlist = [0, 0, 0, 0]  # Default value for rectlist
        if 'textureRect' in v:
            rectlist = to_list(v['textureRect'])
            offset = to_list(v['spriteOffset'])
        elif 'frame' in v:
            rectlist = to_list(v['frame'])
        if 'textureRotated' in v:
            width = int(
                float(rectlist[3]) if v['textureRotated'] else float(rectlist[2]))
            height = int(
                float(rectlist[2]) if v['textureRotated'] else float(rectlist[3]))
        else:
            width = int(float(rectlist[2]))
            height = int(float(rectlist[3]))
        box = (
            int(float(rectlist[0])),
            int(float(rectlist[1])),
            int(float(rectlist[0])) + width,
            int(float(rectlist[1])) + height,
        )
        if 'spriteSize' in v:
            spriteSize = v['spriteSize']
        elif 'spriteSourceSize' in v:
            spriteSize = v['spriteSourceSize']

        sizelist = [int(float(x)) for x in to_list(v['spriteSourceSize'])]
        rect_on_big = big_image.crop(box)

        if ('textureRotated' in v and v['textureRotated']) or ('rotated' in v and v['rotated']):
            rect_on_big = rect_on_big.rotate(90, expand=True)

        result_image = Image.new('RGBA', sizelist, (0, 0, 0, 0))

        if ('textureRotated' in v and v['textureRotated']) or ('rotated' in v and v['rotated']):
            result_box = (
                (sizelist[0] - height) / 2 + int(float(offset[0])),
                (sizelist[1] - width) / 2 - int(float(offset[1])),
                (sizelist[0] + height) / 2 + int(float(offset[0])),
                (sizelist[1] + width) / 2 - int(float(offset[1]))
            )
        else:
            result_box = (
                (sizelist[0] - width) / 2 + int(float(offset[0])),
                (sizelist[1] - height) / 2 - int(float(offset[1])),
                (sizelist[0] + width) / 2 + int(float(offset[0])),
                (sizelist[1] + height) / 2 - int(float(offset[1]))
            )

        # Debug prints to check dimensions
        # print(f"rect_on_big size: {rect_on_big.size}")
        # print(f"result_image size: {result_image.size}")
        # print(f"result_box: {result_box}")

        result_image.paste(rect_on_big, tuple(
            map(int, result_box)), mask=0)  # type: ignore

        if not os.path.isdir(file_path):
            os.mkdir(file_path)
        k = k.replace('/', '_')
        outfile = file_path + '/' + k
        if outfile.find('.png') == -1:
            outfile = outfile + '.png'
        # print(outfile, "generated") # Commented out to avoid printing
        result_image.save(outfile)
