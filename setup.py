from cx_Freeze import setup, Executable



setup(name = 'Going Home', 
      version='4.2.0.', 
      description='Get Home',
      executables = [Executable(script = 'Going Home.py', base='Win32GUI')])
