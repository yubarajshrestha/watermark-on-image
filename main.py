import os
import sys

from PIL import Image

letter = Image.open('assets/application.png')

letterWidth = letter.width
letterHeight = letter.height


confedential = Image.open('assets/confedential.png')
confedentialWidth = confedential.width
confedentialHeight = confedential.height

size = 500, 500
watermark = confedential.resize(size)

try:
    letter.paste(watermark, (int(letterHeight / 2 - 250), int(letterWidth / 2 - 250)), watermark)
    letter.save('assets/copy-letter.png')
except Exception as e:
    print(e)
    pass