import thread
from osd_messenger.connect import OSDConnect

con = OSDConnect()
con.update_osd("Hello World!")
