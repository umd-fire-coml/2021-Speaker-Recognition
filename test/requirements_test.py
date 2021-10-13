
import os

def check():

    ccfile = open("requirements.txt", "r")
    atPackages = False
    isHere = False
    isInstalled = True
    env_packages = []
    installed_packages = []

    for aline in ccfile:
        values = aline.split()
        env_packages.append(values[0])
    ccfile.close()

    out = []
    out = os.popen('pip3 list').read().split()

    for name in env_packages:
        if "=" in name:
            terminator = name.index('=')
            name = name[:terminator]
        for line in out:
            if name in line:
                isHere = True
                break
        if isHere is False:
            print(f"{name} is not installed!")
            isInstalled = False
        isHere = False
    
    if isInstalled is True:
        return True
    else:
        return False

def test_check_env():
     assert(check() == True)
     
