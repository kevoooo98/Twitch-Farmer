from TwitchRunner import TwitchRunner
import sys
from pyvirtualdisplay import Display


display = Display(visible=0, size=(800, 600))
display.start()

sys.stdout.flush()
tr = TwitchRunner()
tr.start()
