import sys
from cx_Freeze import setup, Executable



setup(name = 'Going Home', 
      version='1.0.', 
      description='Get Home',
      options = {'build_exe': {'include_files': ['freesansbold.ttf']}
      executables = [Executable(script = 'Going Home.py')])
