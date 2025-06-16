from lasutil import *;
from lastoconfig import *;

def lasfetch(settings):
  freemem = "/".join(shell_call("free -h").split()[7:9][::-1]).replace("Gi", "GiB");
  freedsk = "/".join(shell_call("df -h /").split()[8:10][::-1]);
  print(f"\033[94m  _    \033[94m{settings['username']}\033[0m@\033[94m{settings['hostname']}\033[0m");
  print("\033[94m ('=   \033[0m--------------");
  print(f"\033[94m /_)   \033[94mOS Name\033[0m: LastOS {LASTO_VERSION}");
  print("\033[94m /||   \033[94mLang\033[0m: Python");
  print("\033[94m       \033[94mDevelopers\033[0m: Luxidev & Xi816");
  print(f"\033[94m       \033[94mRelease Date\033[0m: {LASTO_RELEASE_DATE[0]}");
  print(f"\033[94m       \033[94mMemory\033[0m: {freemem}");
  print(f"\033[94m       \033[94mDisk space\033[0m: {freedsk}\n");
  print(end="       ");
  for i in range(0,8):
    print(end=f"\033[4{i}m  ");
  print(end="\033[0m\n       ");
  for i in range(0,8):
    print(end=f"\033[10{i}m  ");
  print("\033[0m\n");
