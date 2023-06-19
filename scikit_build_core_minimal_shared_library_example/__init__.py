import errno
import os
from ctypes import CDLL, POINTER, c_int
from pathlib import Path

module_parent_directory = Path(__file__).parent.parent
library_directory = module_parent_directory
library_path = library_directory.joinpath('liblibrary_example.dylib')
if not library_path.exists():
    library_path = library_directory.joinpath('liblibrary_example.so')
if not library_path.exists():
    library_path = library_directory.joinpath('liblibrary_example.dll')
if not library_path.exists():
    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT),
                            str(library_path.absolute().stem) + '.(dylib|so|dll)')

c_library = CDLL(str(library_path))
library_function = c_library.library_function
library_function.return_type = c_int
