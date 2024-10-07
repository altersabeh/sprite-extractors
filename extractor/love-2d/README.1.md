# SPRITE EXTRACTOR FOR 2D TOOLKIT

This is a simple tool to extract sprites from a 2D Toolkit sprite sheet. It will
detect the format automatically and extract to a given output folder.

## Prerequisites

- Java Development Kit (JDK) 8 or higher
- Gradle

## Building

Using `gradle`:
```sh
gradle build
```

The jar file will be generated in `app/build/libs`.

## Usage

You can run the tool as a standalone executable JAR file or using `java -jar`.

### Running as a Standalone Executable JAR File

```sh
sprite_extractor_2dtk ${SPRITE_SHEET}
```

### Running with `java -jar`

```sh
java -jar sprite_extractor_2dtk.jar ${SPRITE_SHEET}
```

Replace `${SPRITE_SHEET}` with the base name of your sprite sheet files. For
example, if your sprite sheet files are `${SPRITE_SHEET}.bytes` and
`${SPRITE_SHEET}.png`, use `${SPRITE_SHEET}` as the base name.

### Example

#### Standalone Executable JAR File

```sh
sprite_extractor_2dtk image
```

#### Using `java -jar`

```sh
java -jar sprite_extractor_2dtk.jar image
```

This will look for `image.bytes` and `image.png` in the current directory and
extract the sprites to a folder named `image`.

## Sample Image

A sample sprite sheet is provided in the `example` directory. You can use this
sample to test the tool.

### Using the Sample Image

1. Navigate to the `example` directory:
    ```sh
    cd example
    cp ../app/build/libs/sprite_extractor_2dtk-1.0.0.jar sprite_extractor_2dtk.jar
    ```

2. Run the tool with the sample image:
    ```sh
    # Using the standalone executable JAR file
    ./sprite_extractor_2dtk.jar sample_image
    ```
    or
    ```sh
    # Using java -jar
    java -jar sprite_extractor_2dtk.jar sample_image
    ```

3. The sprites will be extracted to a folder named `sample_image`.

This will look for `sample_image.bytes` and `sample_image.png` in the `example`
directory and extract the sprites to a folder named `sample_image`.