import os
from PIL import Image, ImageOps
from lupa import LuaRuntime


def unpack_love2d(config_base_name):
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

    # Extract and save each sprite
    for key, value in config.items():
        size = value['size']
        f_quad = value['f_quad']
        trim = value['trim']
        spritesheet_name = value['a_name']

        # Change the extension from .pkm to .png
        spritesheet_name_png = spritesheet_name.replace('.pkm', '.png')

        # Load the spritesheet if not already loaded
        if spritesheet_name_png not in spritesheets:
            spritesheets[spritesheet_name_png] = Image.open(
                spritesheet_name_png)

        # Execute only if the a_name extension is .pkm
        if spritesheet_name.endswith('.pkm'):
            # Change the extension from .pkm to .png
            spritesheet_name_png = spritesheet_name.replace('.pkm', '.png')

        # Extract the sprite using the coordinates and dimensions
        sprite = spritesheets[spritesheet_name_png].crop(
            (f_quad[1], f_quad[2], f_quad[1] + f_quad[3], f_quad[2] + f_quad[4]))

        # Apply the trim values
        sprite = ImageOps.expand(sprite, border=(
            trim[1], trim[2], trim[3], trim[4]), fill=0)

        # Save the sprite as an individual image file in the output directory
        sprite.save(os.path.join(output_dir, f'{key}.png'))

        # Check for alias key and save aliases as well
        if 'alias' in value:
            for alias_name in value['alias']:
                # Print alias name
                sprite.save(os.path.join(output_dir, f'{
                            value['alias'][alias_name]}.png'))

    # print(f"{config_base_name} extracted successfully.")
