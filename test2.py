import subprocess, shlex

user = "cristiano"
command_line = "/opt/homebrew/bin/awk '/{user}/ {print $2}' log.txt"
args = shlex.split(command_line)
out = subprocess.check_output(args, encoding="utf-8")
print(args)
for f in out.split():
    print(f)
