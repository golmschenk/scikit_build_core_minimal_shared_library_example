import errno
import os
from ctypes import CDLL, c_int
from pathlib import Path
import platform

module_parent_directory = Path(__file__).parent.parent
library_directory = module_parent_directory

platform_system_name = platform.system()
if platform_system_name == 'Darwin':
    library_path = library_directory.joinpath('liblibrary_example.dylib')
    if not library_path.exists():
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), str(library_path.absolute()))
    c_library = CDLL(str(library_path))
elif platform_system_name == 'Linux':
    library_path = library_directory.joinpath('liblibrary_example.so')
    if not library_path.exists():
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), str(library_path.absolute()))
    c_library = CDLL(str(library_path))
elif platform_system_name == 'Windows':
    library_path = library_directory.joinpath('library_example.dll')
    if not library_path.exists():
        library_path = library_directory.joinpath('liblibrary_example.dll')
    if not library_path.exists():
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), str(library_path.absolute()))
    c_library = CDLL(str(library_path))
else:
    raise ValueError(f'Platform system {platform_system_name} is not supported.')

library_function = c_library.library_function
library_function.return_type = c_int

