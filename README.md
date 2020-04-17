# OCR EXPERIMENTS
This is a repository containing my experiments related to OCR technology.


## Introduction 

Tesseract is an open source [text recognition (OCR)](https://en.wikipedia.org/wiki/Optical_character_recognition) Engine, available under the [Apache 2.0 license.](http://www.apache.org/licenses/LICENSE-2.0) It can be used directly, or (for programmers) using an [API](https://github.com/tesseract-ocr/tesseract/blob/master/include/tesseract/baseapi.h) to extract printed text from images. It supports a wide variety of languages.

Tesseract doesn't have a built-in GUI, but there are several available from the [3rdParty](User-Projects-%E2%80%93-3rdParty.md) page.

## Installation

There are two parts to install, the engine itself, and the python libraries required for bot or web API service if you intend to deploy that.

### Linux

Tesseract is available directly from many Linux distributions. The package is generally called **'tesseract'** or **'tesseract-ocr'** - search your distribution's repositories to find it.
Thus you can install Tesseract 4.x and its developer tools on Ubuntu 18.x bionic by simply running:
```
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
```

**Note for Ubuntu users**: In case ```apt``` is unable to find the package try adding ```universe``` entry to the ```sources.list``` file as shown below. 
```
sudo vi /etc/apt/sources.list

Copy the first line "deb http://archive.ubuntu.com/ubuntu bionic main" and paste it as shown below on the next line.
If you are using a different release of ubuntu, then replace bionic with the respective release name.

deb http://archive.ubuntu.com/ubuntu bionic universe
```

### Telegram Bot

```
pip3 install -r requirements.txt
python3 bot.py <your-token-here>
```

### Flask based web API service

```
pip3 install -r requirements.txt
python3 api.py
```

That's all.

## Support

Firstly, Try to figure out on your own using web search engine which you prefer. But, if you still can't find what you need, please ask me on Telegram, [@Lulzx](https://t.me/lulzx)
