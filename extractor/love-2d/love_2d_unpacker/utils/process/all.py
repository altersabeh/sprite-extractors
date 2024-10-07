import os

from love_2d_unpacker.sprite_love_2d import unpack_love2d
from love_2d_unpacker.utils.file_checks import check_files_exist
from love_2d_unpacker.utils.print.success import print_success_message


def process_all_files(verbose, no_color, log_file):
    files = os.listdir('.')
    base_names = set()

    for file in files:
        if file.endswith('.lua'):
            base_name = file[:-4]
            png_files = [f for f in files if f.startswith(
                base_name) and f.endswith('.png')]
            if png_files:
                base_names.add(base_name)

    total_sprites = 0
    for base_name in base_names:
        check_files_exist(base_name, no_color)
        sprite_count = unpack_love2d(base_name, verbose, no_color)
        total_sprites += sprite_count
        print_success_message(sprite_count, base_name, verbose, no_color)

        if log_file:
            with open(log_file, 'a') as f:
                f.write(f"Extracted {sprite_count} sprites from {base_name}\n")

    if verbose:
        if no_color:
            print(f"[VERBOSE] Success: {total_sprites} sprites extracted successfully from {
                  len(base_names)} sprite atlases.")
        else:
            print(f"\033[1;34m[VERBOSE]\033[0m \033[1;32mSuccess:\033[0m \033[1;33m{
                  total_sprites}\033[0m sprites extracted successfully from \033[1;33m{len(base_names)}\033[0m sprite atlases.")
    else:
        if no_color:
            print(f"Success: {total_sprites} sprites extracted successfully from {
                  len(base_names)} sprite atlases.")
        else:
            print(f"\033[1;32mSuccess:\033[0m \033[1;33m{
                total_sprites}\033[0m sprites extracted successfully from \033[1;33m{len(base_names)}\033[0m sprite atlases.")

    if log_file:
        with open(log_file, 'a') as f:
            f.write(f"Total sprites extracted: {total_sprites} from {
                    len(base_names)} sprite sheets\n")
