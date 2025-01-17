# Auto-image-renamer
forked from [sanjujosh/auto-image-renamer](https://github.com/sanjujosh/auto-image-renamer)  
Rename images using deep learning

![Image for demo](images/gif.gif)

Auto-image-renamer automates the task of renaming images with meaningful names. It uses OpenAI Vision API within chat completion to rename the images

## Update Jan 2025
Using OpenAI instead.

## Update Jan 2023
Microsoft changed the old API, so I have updated the same in here. Also removed python2 support.

## Dependencies

- Python 3 (Tested under Windows Python 3.10.2) 

## Usage 

### 1) ~~Get a Microsoft API Key for Free~~

~~[Sign Up](https://azure.microsoft.com/en-gb/products/cognitive-services/computer-vision/)~~

### 2) Create a computer vision

Store the OpenAI key as an environment variable.

## Usage

```
python renamer.py path_to_images_dir
```

EXAMPLE `python3 renamer.py /home/sanju/images`

NOTICE: Do not use a trailing slash in dir

## 4) Enjoy!

All the images in the given directory will be renamed with meaningful names now. 


## How It was Built

1. Find all the images in the given directory
2. Images will be sent to OpenAI, they process the image and send back a caption.
3. Rename the files with new name from the API


## Disclaimer

It uploads the images to OpenAI servers, use it with caution.

## Credits

Originally inspired from https://github.com/ParhamP/altify  
forked from [sanjujosh/auto-image-renamer](https://github.com/sanjujosh/auto-image-renamer)
