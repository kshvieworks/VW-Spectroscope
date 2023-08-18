import os
from pathlib import Path
def configure_path():

    try:
        os.add_dll_directory('C:/opencv/build/x64/vc16/bin')
        os.add_dll_directory('C:/Vieworks Imaging Solution 7/SDK/CPP/DLL/x64')

    except AttributeError or FileNotFoundError:
        pass

    relative_path_to_dlls = os.sep + 'build' + os.sep + 'Debug'
    os.environ['PATH'] = f"{Path.cwd().parent}" + relative_path_to_dlls + os.pathsep + os.environ['PATH']

    try:
        os.add_dll_directory(f"{Path.cwd().parent}" + relative_path_to_dlls)

    except AttributeError or FileNotFoundError:
        pass

    del relative_path_to_dlls