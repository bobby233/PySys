r"""A simple system framework based on Python

Author: bobby233<mczsjzsjz@outlook.com>
Version: 0.0.0-alpha0
The first version of PySys

PySys is just like a system, but a simpler one. You can easily use the Python
modules you like in this system framework. Like an operating system, you can
also control the directories and files. PySys offers its own executable file
format, .psy (PySys Python format, or ψ \u03C8). It is much more easier and
safer to write executable files that only run on PySys. Internet connecting,
virtual disk and so on is provided. More methods are provided in PSTerm (PySys
Terminal)
"""
import json

# import PySys Terminal
emergency = False
try:
    import modulename # TODO: write PSTerm
except ImportError:
    # enter enmergency mode
    emergency = True
    print("! PSTerm (PySys Terminal) is not installed, entering enmergency mode")
    from urllib import request, error

def download_file(url: str, dir: str = "."):
    """Download a file and save it to a real directory in your computer.

    Keyword arguments:
    url -- where the file is on the Internet
    dir -- where to save the file (default '.')
    """
    filename = url.split("/")[-1]
    print("Downloading", filename + "...")
    file = request.urlopen(url).read().decode()
    if dir == ".":
        # save into file named filename
        with open(filename, "w", encoding="utf-8") as f:
            f.write(file)
    else:
        import os.path
        if os.path.exists(dir) & os.path.isdir(dir):
            with open(dir + "/" + filename, "w", encoding="utf-8") as f:
                f.write(file)
        else:
            print("! Directory", dir, "doesn't exist!")

if emergency:
    print("\nWelcome to PySys enmergency fixing mode!", end="")

    while True:
        command = input("\n$ ")
        arguments = command.split()
        prefix = arguments[0]

        # exit PySys
        if command == "exit":
            print("Exit PySys...")
            exit()
        
        # download file(s)
        elif prefix == "download":
            if len(arguments) == 2:
                try:
                    download_file(arguments[1])
                # do if the URL is not correct
                except ValueError:
                    print("! This URL isn't a correct one!")
                # do if connection failed (like 404, 403, 503, etc.)
                except error.URLError:
                    print("! Internet connection failed!")
            else:
                try:
                    download_file(arguments[1], arguments[2])
                # like above
                except ValueError:
                    print("! This URL isn't a correct one!")
                except error.URLError:
                    print("! Internet connection failed!")