import os
import sys


def check_files_exist(config_base_name: str, no_color: bool):
    lua_file = f"{config_base_name}.lua"
    png_pattern = f"{config_base_name}-*.png"

    if not os.path.exists(lua_file):
        if no_color:
            print(f"Error: {lua_file} not found. Make sure you have both {
                  lua_file} and at least one PNG file in the same directory.")
        else:
            print(f"\033[1;31mError:\033[0m \033[1;33m{lua_file}\033[0m not found. Make sure you have both \033[1;33m{
                  lua_file}\033[0m and at least one PNG file in the same directory.")
        sys.exit(1)

    png_files = [f for f in os.listdir('.') if f.startswith(
        config_base_name) and f.endswith('.png')]

    if not png_files:
        if no_color:
            print(f"Error: No PNG files found matching pattern {
                  png_pattern}. Make sure you have at least one PNG file in the same directory.")
        else:
            print(f"\033[1;31mError:\033[0m No PNG files found matching pattern \033[1;33m{
                  png_pattern}\033[0m. Make sure you have at least one PNG file in the same directory.")
        sys.exit(1)
