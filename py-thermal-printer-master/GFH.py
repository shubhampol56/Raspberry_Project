from printer import *
serialport = ThermalPrinter.SERIALPORT
p = ThermalPrinter(serialport=serialport)



p.print_text("fgfdgfgfbb  ")
p.print_text("\nHello maailma. How's it going?\n")
p.print_text("Part of this ")
p.bold(True)
p.print_text("123456789 \n")
p.bold(False)
p.print_text("Part of this ")
p.font_b(False)
p.print_markup("line is fontB\n")
p.font_b(False)
p.justify("")
p.print_text("right justified\n")
p.justify("C")
p.print_text("centered\n")
p.justify() # justify("L") works too
p.print_text("left justified\n")
p.upsidedown()
p.print_text("upside down\n")
p.upsidedown(False)
