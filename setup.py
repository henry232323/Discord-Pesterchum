from cx_Freeze import setup, Executable
import sys

sys.argv.append("build")

include_files = ["resources", "themes", "README.md", "LICENSE"]

build_exe_options = {
    "includes": ["PyQt5", "os", "json", "asyncio", "types", "discord", "aiohttp",
                 "requests", "contextlib", "io", "inspect", "traceback", "subprocess",
                 "async_timeout"],
    "excludes": ["tkinter", "_tkinter", '_gtkagg', '_tkagg', 'bsddb', 'curses',
                 'pywin.debugger', 'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
                 'unittest', 'idlelib', 'certifi', 'nacl', "_lzma", "_hashlib", "_bz2"],
    "include_files": include_files,
    }

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Pesterchum-Discord",
    version="1.1.1",
    description="A Discord client mimicking the Pesterchum chat client from Homestuck, Uses a lot of code from my Pesterchum Client.",
    options={"build_exe": build_exe_options},
    executables=[Executable("pesterchum.py", base=base, icon="resources/pc_chummy.ico"),
                 Executable("updater.py", base=None, icon="resources/sburb.ico")]
        )
