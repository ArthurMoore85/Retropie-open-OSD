from subprocess import Popen, PIPE, check_output, check_call
import logging
import sys
import time
import signal
import os

HOME = os.path.expanduser("~")

class OSDConnect(object):
    def __init__(self, *args, **kwargs):
        self.debug = kwargs['debug'] if kwargs.get('debug') else False
        self.bin_dir = os.path.join(HOME, 'Retropie-open-OSD')
        self.osd_proc = None
        self.osd_in = None

        self.set_up_osd()

    @property
    def osd_path(self):
        if not self.debug:
            return os.path.join(self.bin_dir, 'osd', 'osd')
        else:
            return '/home/arthur/Projects/retropie-osd/Retropie-open-OSD/osd/osd'

    def set_up_osd(self):
        """
        Sets up the OSD service
        """
        try:
            self.osd_proc = Popen(
                self.osd_path, shell=False, stdin=PIPE, 
                stdout=None, stderr=None
            )
            self.osd_in = self.osd_proc.stdin
            time.sleep(1)
            osd_poll = self.osd_proc.poll()
            if (osd_poll):
                error_msg = "ERROR: Failed to start OSD, error: {error_msg}".format(
                    error_msg=osd_poll
                )
                logging.error(error_msg)
                sys.exit(1)
        except Exception:
            logging.exception("ERROR: Failed start OSD binary")
            sys.exit(1)

    def update_osd(self, message):
        """
        Updates the OSD

        :param message: Message to be passed to the OSD
        """
        self.osd_proc.send_signal(signal.SIGUSR1)
        self.osd_in.write(message)
        self.osd_in.flush()
