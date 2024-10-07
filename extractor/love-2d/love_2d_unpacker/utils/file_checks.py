import os
import sys


def check_files_exist(config_base_name: str, no_color: bool):
    lua_file = f"{config_base_name}.lua"
    png_file = f"{config_base_name}.png"

    if not os.path.exists(lua_file):
        if no_color:
            print(f"Error: {lua_file} not found. Make sure you have both {
                  lua_file} and {png_file} in the same directory.")
        else:
            print(f"\033[1;31mError:\033[0m \033[1;33m{lua_file}\033[0m not found. Make sure you have both \033[1;33m{
                  lua_file}\033[0m and \033[1;33m{png_file}\033[0m in the same directory.")
        sys.exit(1)

    if not os.path.exists(png_file):
        if no_color:
            print(f"Error: {png_file} not found. Make sure you have both {
                  lua_file} and {png_file} in the same directory.")
        else:
            print(f"\033[1;31mError:\033[0m \033[1;33m{png_file}\033[0m not found. Make sure you have both \033[1;33m{
                  lua_file}\033[0m and \033[1;33m{png_file}\033[0m in the same directory.")
        sys.exit(1)
