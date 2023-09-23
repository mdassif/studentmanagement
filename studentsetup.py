import sys
from cx_Freeze import setup, Executable

includefiles = ["student-cap-books_icon-icons.com_49273.ico"]
excludes = []
packages = []
base = None

if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table = [
    ("DesktopShortcut",  # Shortcut
     "DesktopFolder",   # Directory_
     "Student Management System",  # Name
     "TARGETDIR",       # Component_
     "[TARGETDIR]main.exe",
     None,              # Arguments
     "Student Management System",  # Description
     None,              # Hotkey
     None,              # Icon
     None,              # IconIndex
     None,              # ShowCmd
     "TARGETDIR",       # WkDir
     )
]

msi_data = {"shortcut": shortcut_table}

bdist_msi_options = {
    "data": msi_data,
    "install_icon": "student-cap-books_icon-icons.com_49273.ico",
}

setup(
    name="StudentManagementSystem",
    version="0.1",
    description="Student Management System developed by Assif",
    author="Assif",
    options={
        "build_exe": {
            "include_files": includefiles,
        },
        "bdist_msi": bdist_msi_options,
    },
    executables=[
        Executable(
            script="main.py",
            base=base,
            icon="student-cap-books_icon-icons.com_49273.ico",
        )
    ]
)
