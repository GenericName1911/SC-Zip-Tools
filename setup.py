# Installs Pip
import subprocess, sys
subprocess.run([sys.executable, "-m", "pip", "install", "sc-compression==0.6.1"])
input()