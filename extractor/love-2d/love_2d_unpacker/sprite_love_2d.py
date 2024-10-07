import os
from PIL import Image, ImageOps
from lupa import LuaRuntime


def unpack_love2d(config_base_name, verbose=False, no_color=False):
    # Load the Lua configuration
    lua = LuaRuntime(unpack_returned_tuples=True)
    lua_config_file = f'{config_base_name}.lua'
    with open(lua_config_file, 'r') as file:
        lua_config = file.read()

    config = lua.execute(lua_config)

    # Create a directory with the same name as the config base name
    output_dir = config_base_name
    os.makedirs(output_dir, exist_ok=True)

    # Dictionary to cache loaded spritesheets
    spritesheets = {}

    sprite_count = 0

    # Extract and save each sprite
    for key, value in config.items():
        # size = value['size']
        f_quad = value['f_quad']
        trim = value['trim']
        spritesheet_name = value['a_name']

        # Execute only if the spritesheet_name extension is .pkm
        # if spritesheet_name.endswith('.pkm'):
        #     # Change the extension from .pkm to .png
        #     spritesheet_name_png = spritesheet_name.replace('.pkm', '.png')
        # else:
        #     spritesheet_name_png = spritesheet_name
        spritesheet_name_png = spritesheet_name.replace('.pkm', '.png')

        # Load the spritesheet if not already loaded
        if spritesheet_name_png not in spritesheets:
            spritesheets[spritesheet_name_png] = Image.open(
                spritesheet_name_png)

        # Extract the sprite using the coordinates and dimensions
        sprite = spritesheets[spritesheet_name_png].crop(
            (f_quad[1], f_quad[2], f_quad[1] + f_quad[3], f_quad[2] + f_quad[4]))

        # Apply the trim values
        sprite = ImageOps.expand(sprite, border=(
            trim[1], trim[2], trim[3], trim[4]), fill=0)

        # Save the sprite as an individual image file in the output directory
        sprite.save(os.path.join(output_dir, f'{key}.png'))
        sprite_count += 1

        if verbose:
            if no_color:
                print(f"[VERBOSE] Extracted Sprite: {key}.png")
            else:
                print(
                    f"\033[1;34m[VERBOSE]\033[0m \033[1;35mExtracted Sprite:\033[0m {key}.png")

        # Check for alias key and save aliases as well
        if 'alias' in value:
            for alias_name in value['alias']:
                alias_file = os.path.join(
                    output_dir, f'{value["alias"][alias_name]}.png')
                sprite.save(alias_file)
                sprite_count += 1
                if verbose:
                    if no_color:
                        print(f"[VERBOSE] Extracted Sprite: {alias_file}")
                    else:
                        print(f"\033[1;34m[VERBOSE]\033[0m \033[1;35mExtracted Sprite:\033[0m {
                              alias_file}")

    return sprite_count
