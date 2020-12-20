
import sys

from cx_Freeze import setup, Executable

executables = [Executable('main.py')]

options = {
    'build_exe': {
        'include_msvcr': True
    }
}

setup(name='SPDel',
      version='1.0.0',
      description='SPDel',
      executables=executables,
      options=options)
