# google_translator

## Description

Console python script that can be used for translating text from different languages.
It sends requests to google translate servers and saves it results in `results.txt` file.

## Installation

Clone the repository:

    git clone git@github.com:FolloW12587/google_translator.git

This app needs only `requests` lib, that isn't included in default packages.
You might have already installed it, but if you don't, you can run: 

    pip install -r requirements.txt

## Usage

You can start scrpit by:

    python3 main.py

* Input language of text to translate. You skip this by pressing `Enter` if you want to auto detect the language.

* Input language that you want text to translate. If you skip this `en` will be chosen by default.

* Input string to translate. If you print a single sentence, you can see a different options of the translated text.

* To end translations input empty string or `/q`.

* To change languages settings input `/l`.