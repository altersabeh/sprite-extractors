import os
import sys
from cocos_2dx_unpacker.sprite_cocos_2dx import unpack_cocos2dx


def print_help():
    help_message = """\033[1;34mA tool to extract sprites from a Cocos2d-x spritesheet.

\033[1;33mUsage:\033[0m
  sprite_extractor_cocos2dx \033[38;5;214m[OPTION] \033[1;35mSPRITE_SHEET<.plist,.png>\033[0m

\033[1;33mArguments:\033[0m
  \033[1;32mSPRITE_SHEET\033[0m    Base name of the sprite sheet files (without extension). 
                  The tool will look for corresponding .plist and .png files.

\033[1;33mOptions:\033[0m
  \033[1;32m--help, -h\033[0m      Show this help message and exit.
"""
    print(help_message)


def main():
    if len(sys.argv) != 2 or sys.argv[1] in {'--help', '-h'}:
        print_help()
        sys.exit(1)

    config_base_name = sys.argv[1]
    plist_file = f"{config_base_name}.plist"
    png_file = f"{config_base_name}.png"

    if not os.path.exists(plist_file):
        print(f"\033[1;31mError:\033[0m \033[1;33m{plist_file}\033[0m not found. Make sure you have both \033[1;33m{
              plist_file}\033[0m and \033[1;33m{png_file}\033[0m in the same directory.")
        sys.exit(1)

    if not os.path.exists(png_file):
        print(f"\033[1;31mError:\033[0m \033[1;33m{png_file}\033[0m not found. Make sure you have both \033[1;33m{
              plist_file}\033[0m and \033[1;33m{png_file}\033[0m in the same directory.")
        sys.exit(1)

    unpack_cocos2dx(plist_file, png_file)
