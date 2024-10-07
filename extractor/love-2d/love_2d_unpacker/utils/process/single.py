import sys

from love_2d_unpacker.sprite_love_2d import unpack_love2d
from love_2d_unpacker.utils.file_checks import check_files_exist
from love_2d_unpacker.utils.print.help import print_help_message
from love_2d_unpacker.utils.print.success import print_success_message


def process_single_file(config_base_name, verbose, no_color, log_file):
    if not config_base_name:
        print_help_message(no_color)
        sys.exit(1)

    check_files_exist(config_base_name, no_color)

    sprite_count = unpack_love2d(config_base_name, verbose, no_color)

    print_success_message(sprite_count, config_base_name, verbose, no_color)

    if log_file:
        with open(log_file, 'a') as f:
            f.write(f"Extracted {sprite_count} sprites from {
                    config_base_name}\n")
