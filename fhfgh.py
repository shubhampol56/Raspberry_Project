from PIL import Image
from thermalprinter import *

with ThermalPrinter(port='/dev/ttyUSB0', baudrate = 9600, timeout = 5) as printer:
    # Picture
    #printer.image(Image.open('gnu.png'))

    # Bar code

    # Styles
    printer.out('Bold')
    printer.out('Double height', double_height=True)
    printer.out('Double width', double_width=True)
    printer.out('Inverse', inverse=True)
    printer.out('Rotate 90°', rotate=True, codepage=CodePage.ISO_8859_1)
    printer.out('Strike', strike=True)
    printer.out('Underline', underline=1)
    printer.out('Upside down', upside_down=True)

    # Chinese (almost all alphabets exist)
  
    printer.feed(2)
