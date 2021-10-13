
import sys

def check():
    checked = False
    if "jupyterlab" in sys.modules:
        checked = True
        
    assert(checked == True)

check()
