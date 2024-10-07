import os


def print_success_message(sprite_count: int, config_base_name: str, verbose: bool, no_color: bool):
    if verbose:
        output_dir = os.path.abspath(config_base_name)
        if no_color:
            print(f"[VERBOSE] Output Directory: {output_dir}")
            print(f"[VERBOSE] Success: {sprite_count} sprites extracted successfully from {
                config_base_name}.")

        else:
            print(f"\033[1;34m[VERBOSE]\033[0m \033[1;35mOutput directory:\033[0m \033[38;2;255;192;203m{
                  output_dir}\033[0m")
            print(f"\033[1;34m[VERBOSE]\033[0m \033[1;32mSuccess:\033[0m \033[1;33m{
                  sprite_count}\033[0m sprites extracted successfully from \033[1;33m{config_base_name}\033[0m.")
    else:
        if no_color:
            print(f"Success: {sprite_count} sprites extracted successfully from {
                config_base_name}.")
        else:
            print(f"\033[1;32mSuccess:\033[0m \033[1;33m{
                  sprite_count}\033[0m sprites extracted successfully from \033[1;33m{config_base_name}\033[0m.")
