import os
import sys
from love_2d_unpacker.sprite_love_2d import unpack_love2d


def print_help():
    help_message = """\033[1;34mA tool to extract sprites from a LÖVE2D spritesheet.

\033[1;33mUsage:\033[0m
  sprite_extractor_love2d \033[38;5;214m[OPTION] \033[1;35mSPRITE_SHEET<.lua,.png>\033[0m

\033[1;33mArguments:\033[0m
  \033[1;32mSPRITE_SHEET\033[0m    Base name of the sprite sheet files (without extension). 
                  The tool will look for corresponding .lua and .png files.

\033[1;33mOptions:\033[0m
  \033[1;32m--help, -h\033[0m      Show this help message and exit.
"""
    print(help_message)


def main():
    if len(sys.argv) != 2 or sys.argv[1] in {'--help', '-h'}:
        print_help()
        sys.exit(1)

    config_base_name = sys.argv[1]
    lua_file = f"{config_base_name}.lua"
    png_file = f"{config_base_name}.png"

    if not os.path.exists(lua_file):
        print(f"\033[1;31mError:\033[0m \033[1;33m{lua_file}\033[0m not found. Make sure you have both \033[1;33m{
              lua_file}\033[0m and \033[1;33m{png_file}\033[0m in the same directory.")
        sys.exit(1)

    if not os.path.exists(png_file):
        print(f"\033[1;31mError:\033[0m \033[1;33m{png_file}\033[0m not found. Make sure you have both \033[1;33m{
              lua_file}\033[0m and \033[1;33m{png_file}\033[0m in the same directory.")
        sys.exit(1)

    unpack_love2d(config_base_name)
