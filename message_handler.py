import thread
from osd_messenger.connect import OSDConnect

con = OSDConnect(debug=True)
reading_thread = thread.start_new_thread(con.update_osd, ("Hello world"))
