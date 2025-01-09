#!/usr/bin/env python

import argparse
import skeys
import http.client
import json
import os
import urllib.parse
import openai
from os import listdir
from os.path import isfile, join


client = openai.OpenAI()

# Get OpenAI API key from environment variable
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

if not OPENAI_API_KEY:
    raise ValueError("No OpenAI API key found in environment variables.")

# Add your OpenAI API key
openai.api_key = OPENAI_API_KEY

ALLOWED_IMAGE_EXTENSIONS = ['.jpeg', '.jpg', '.png']


def is_exists(path):
    if os.path.exists(path):
        return True
    else:
        print("Could not find the given file - ", path)
        return False


def get_all_images(directory):
    if is_exists(directory):
        files = [f for f in listdir(directory) if isfile(join(directory, f))]
        images = [f for f in files for ext in ALLOWED_IMAGE_EXTENSIONS if f.lower().endswith(ext.lower())]
        return images


def get_extension(file):
    file, ext = os.path.splitext(file)
    return ext


def find_available_filename(base_dir, new, ext):
    # Define the initial filename
    filename = os.path.join(base_dir, f"{new}{ext}")
    
    # Check if the file already exists
    if os.path.isfile(filename):
        # If it exists, increment the filename until an available one is found
        i = 1
        while True:
            new_filename = os.path.join(base_dir, f"{new}_{i}{ext}")
            if not os.path.isfile(new_filename):
                return new_filename
            i += 1
    else:
        # If the file doesn't exist, return the original filename
        return filename


def rename_img(old, new, base_dir): #old, join(base_dir, new + ext)
    if is_exists(old):
        ext = get_extension(old).lower()
        if ext is not None:
            # os.rename(old, join(base_dir, new + ext))
            os.rename(old, find_available_filename(base_dir, new, ext))
            print("Renaming ", old, "to ", new + ext)
        else: 
            print("File extension is type None. Skipping.")

def get_caption(image_file):
    with open(image_file, 'rb') as img:
        image_data = img.read()
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What's in this image?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_data,
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )

    caption_text = response.choices[0]['message']['content']
    print(caption_text)
    caption_text = caption_text.replace(",", "").replace(" ", "_")
    print(caption_text)
    return caption_text


def full_path(base, file):
    return base + "/" + file


def init(directory):
    images = get_all_images(directory)
    for image in images:
        file = full_path(directory, image)
        print("Processing image - ", image)
        new_name = get_caption(file)
        rename_img(file, new_name, directory)


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', help="Absolute path of image directory", type=str)
    args = parser.parse_args()

    try:
        init(args.dir)
    except ValueError:
        print("Try again")


if __name__ == '__main__':
    arg_parser()
