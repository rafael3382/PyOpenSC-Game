import subprocess

'''
import PlatformConfig
if PlatformConfig.IS_ANDROID:
    print("No need on Android")
    input("Press enter to close")
'''
try:
    import pyglet
except ImportError:
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyglet"])
     except CalledProcessError:
         print("Fail, :(")
         print("You must ask for support at SCC #nome-opensc")
         input()
