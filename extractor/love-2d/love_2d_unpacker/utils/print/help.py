def print_help_message(no_color=False):
    if no_color:
        help_message = """A tool to extract sprites from a LÖVE2D spritesheet.

Usage:
    sprite_extractor_love2d [OPTION(S)] SPRITE_SHEET<.lua,.png>

Arguments:
    SPRITE_SHEET
        Base name of the sprite sheet files (without extension). 
        The tool will look for corresponding .lua and .png files.

    all
        Process all files in the current directory that have matching .lua and .png extensions.

Options:
    --help, -h      
        Show this help message and exit.

    --verbose, -v   
        Enable detailed logging of the extraction process.
    
    --no-color      
        Disable colored output in the terminal.

    --log-file=FILE
        Specify a log file to save the verbose output.

    --pattern=PATTERN
        Process files matching a specific pattern.

Examples:
    A. Using the tool as a command line utility:
        1. Extract sprites from a specific image:
            
            sprite_extractor_love2d sample-image

        2. Extract sprites from a specific image with verbose logging:
            
            sprite_extractor_love2d --verbose sample-image

        3. Extract sprites from all images in the current directory:
            
            sprite_extractor_love2d all

    B. Using the tool as a python module:
        1. Extract sprites from a specific image:
            
            from love_2d_unpacker.sprite_love_2d import unpack_love2d
            unpack_love2d("sample-image")

        2. Extract sprites from a specific image with verbose logging:
            
            from love_2d_unpacker.sprite_love_2d import unpack_love2d
            unpack_love2d("sample-image", verbose=True)

    C. Using the tool with python -m:
        1. Extract sprites from a specific image:
            
            python -m love_2d_unpacker sample-image

        2. Extract sprites from a specific image with verbose logging:
            
            python -m love_2d_unpacker --verbose sample-image
"""
    else:
        help_message = """\033[1;34mA tool to extract sprites from a LÖVE2D spritesheet.

\033[1;33mUsage:\033[0m
    sprite_extractor_love2d \033[38;5;214m[OPTION(S)] \033[1;35mSPRITE_SHEET<.lua,.png>\033[0m

\033[1;33mArguments:\033[0m
    \033[1;32mSPRITE_SHEET\033[0m    
        Base name of the sprite sheet files (without extension). 
        The tool will look for corresponding .lua and .png files.

    \033[1;32mall\033[0m
        Process all files in the current directory that have matching .lua and .png extensions.

\033[1;33mOptions:\033[0m
    \033[1;32m--help, -h\033[0m      
        Show this help message and exit.

    \033[1;32m--verbose, -v\033[0m   
        Enable detailed logging of the extraction process.
    
    \033[1;32m--no-color\033[0m      
        Disable colored output in the terminal.
    
    \033[1;32m--log-file=FILE\033[0m
        Specify a log file to save the verbose output.

    \033[1;32m--pattern=PATTERN\033[0m
        Process files matching a specific pattern.

\033[1;33mExamples:\033[0m
    \033[1;32mA.\033[0m Using the tool as a command line utility:
        \033[1;34m1.\033[0m Extract sprites from a specific image:
            
            \033[1;35msprite_extractor_love2d sample-image\033[0m

        \033[1;34m2.\033[0m Extract sprites from a specific image with verbose logging:
            
            \033[1;35msprite_extractor_love2d --verbose sample-image\033[0m

        \033[1;34m3.\033[0m Extract sprites from all images in the current directory:
            
            \033[1;35msprite_extractor_love2d all\033[0m

    \033[1;32mB.\033[0m Using the tool as a Python module:
        \033[1;34m1.\033[0m Extract sprites from a specific image:
            
            \033[1;35mfrom love_2d_unpacker.sprite_love_2d import unpack_love2d\033[0m
            \033[1;35munpack_love2d("sample-image")\033[0m

        \033[1;34m2.\033[0m Extract sprites from a specific image with verbose logging:
            
            \033[1;35mfrom love_2d_unpacker.sprite_love_2d import unpack_love2d\033[0m
            \033[1;35munpack_love2d("sample-image", verbose=True)\033[0m

    \033[1;32mC.\033[0m Using the tool with python -m:
        \033[1;34m1.\033[0m Extract sprites from a specific image:

            \033[1;35mpython -m love_2d_unpacker sample-image\033[0m

        \033[1;34m2.\033[0m Extract sprites from a specific image with verbose logging:
        
            \033[1;35mpython -m love_2d_unpacker --verbose sample-image\033[0m
"""
    print(help_message)
