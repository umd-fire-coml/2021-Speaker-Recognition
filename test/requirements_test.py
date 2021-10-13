
from pip._internal.utils.misc import get_installed_distributions 

def check():
    
    lst = get_installed_distributions()
    flat_installed_packages = [package.project_name for package in lst]
        
    checked = False
    
    if "jupyterlab" in flat_installed_packages:
        checked = True
        
    assert(checked == True)

check()
