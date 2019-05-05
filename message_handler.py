import thread
from osd_messenger.connect import OSDConnect

con = OSDConnect()
reading_thread = thread.start_new_thread(con.update_osd, ("Hello world"))
