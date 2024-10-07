import os
import re
import sys

from love_2d_unpacker.utils.argument_parser import parse_arguments
from love_2d_unpacker.utils.constants import known_options
from love_2d_unpacker.utils.print.help import print_help_message
from love_2d_unpacker.utils.process.all import process_all_files
from love_2d_unpacker.utils.process.pattern import process_files_by_pattern
from love_2d_unpacker.utils.process.single import process_single_file


def print_usage_message(no_color):
    print("\033[1;34mA tool to extract sprites from a LÖVE2D spritesheet.")
    print("\033[1;33mUsage:\033[0m sprite_extractor_love2d \033[38;5;214m[OPTION(S)] \033[1;35mSPRITE_SHEET<.lua,.png>\033[0m")
    print(
        "\033[1;31mMissing Operand:\033[0m Try \033[1;32m'-h'\033[0m or \033[1;32m'--help'\033[0m for more information.")


def main():
    if len(sys.argv) < 2:
        print_usage_message('--no-color' in sys.argv)
        sys.exit(1)

    verbose = '--verbose' in sys.argv or '-v' in sys.argv
    no_color = '--no-color' in sys.argv

    log_file, pattern = parse_arguments(sys.argv[1:], known_options, no_color)

    if 'all' in sys.argv:
        process_all_files(verbose, no_color, log_file)
    elif pattern:
        process_files_by_pattern(verbose, no_color, log_file, pattern)
    else:
        config_base_name = next(
            (arg for arg in sys.argv[1:] if not arg.startswith('-')), None)
        process_single_file(config_base_name, verbose, no_color, log_file)
