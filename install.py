import subprocess
import sys

def install_package(package):
    """Install a package using pip."""
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        print(f"'{package}' has been installed successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to install '{package}'. Please check your internet connection or package name.")

if __name__ == "__main__":
    install_package('docx2txt')
