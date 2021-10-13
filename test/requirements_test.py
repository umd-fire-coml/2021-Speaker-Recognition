
import sys

def check():
    checked = false
    if "jupyterlab" in sys.modules:
        checked = true
        
    assert(true)
