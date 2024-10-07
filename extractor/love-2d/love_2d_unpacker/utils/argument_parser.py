import sys

from love_2d_unpacker.utils.print.help import print_help_message


def parse_arguments(args, known_options, no_color):
    log_file = None
    pattern = None

    for arg in args:
        if '--help' in sys.argv or '-h' in sys.argv:
            print_help_message('--no-color' in sys.argv)
            sys.exit(1)
        elif arg.startswith('--log-file='):
            log_file = arg.split('=', 1)[1]
        elif arg.startswith('--pattern='):
            pattern = arg.split('=', 1)[1]
        elif arg not in known_options and arg.startswith('-'):
            if no_color:
                print(f"Warning: Unknown option '{arg}'")
            else:
                print(f"\033[1;31mWarning:\033[0m Unknown option \033[1;32m'{
                      arg}'\033[0m")

    return log_file, pattern
