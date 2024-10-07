# SPRITE EXTRACTOR FOR LÖVE2D

This is a simple tool to extract sprites from a LÖVE2D sprite sheet. It will
detect the format automatically and extract to a given output folder.

## Prerequisites

- Python 3.x
- Poetry

## Setting Up

Using `poetry`:
```sh
poetry install
```

## Building

Using `poetry`:
```sh
poetry build
```

The wheel file will be generated in the `dist` directory.

```sh
pip install dist/love_2d_unpacker-1.0.0-py3-none-any.whl
```

## Usage

You can run the tool directly or using the `python -m` module option.

### Running the Script Directly

```sh
sprite_extractor_love2d ${SPRITE_SHEET}
```

### Running with `-m` Module Option

```sh
python -m love_2d_unpacker ${SPRITE_SHEET}
```

Replace `${SPRITE_SHEET}` with the base name of your sprite sheet files. For
example, if your sprite sheet files are `${SPRITE_SHEET}.lua` and
`${SPRITE_SHEET}.png`, use `${SPRITE_SHEET}` as the base name.


### Example

#### Running the Script Directly

```sh
sprite_extractor_love2d image
```

#### Running with `-m` Module Option

```sh
python -m love_2d_unpacker image
```

This will look for `image.lua` and `image.png` in the current directory and
extract the sprites to a folder named `image`.

## Sample Image

A sample sprite sheet is provided in the `example` directory. You can use this
sample to test the tool.

### Using the Sample Image

1. Navigate to the `example` directory:
    ```sh
    cd example
    ```

2. Run the tool with the sample image:
    ```sh
    # Running the Script Directly
    sprite_extractor_love2d sample_image
    ```
    or
    ```sh
    # Running with -m module Option
    python -m love_2d_unpacker sample_image
    ```

3. The sprites will be extracted to a folder named `sample_image`.

This will look for `sample_image.lua` and `sample_image.png` in the `example`
directory and extract the sprites to a folder named `sample_image`.
