import sys
from cx_Freeze import setup, Executable

if sys.platform == "win32":
    base = "Win32GUI"

options = {"include_files":["Icon.ico"]}

setup(
  name = "Calculator",
  version = "0.1",
  description = "A calculator program",
  options = {"build_exe": options},
  executables = [Executable("main.py", base=base, icon="Icon.ico")]
)
