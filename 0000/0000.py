# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

__author__ = 'patrick_psq'

def DrawNumber(FilePath):
    avatar = Image.open(FilePath)
    drawAvatar = ImageDraw.Draw(avatar)

    xSize, ySize = avatar.size
    fontSize = int(min(xSize, ySize) * 0.2)

    myFont = ImageFont.truetype('/Users/patrick_psq/Library/Fonts/Hack-Italic.ttf', fontSize)

    drawAvatar.text([0.9 * xSize, 0.1 * ySize], '4', fill=(255, 0, 0), font=myFont)
    del drawAvatar

    avatar.show()

if __name__ == '__main__':
    DrawNumber('ashe.jpg')
