import subprocess, shlex

command_line = "/opt/homebrew/bin/awk '{print $2}' log.txt"
args = shlex.split(command_line)
subprocess.Popen(args)
