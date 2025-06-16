from readchar import readkey;

from lasutil import *;
from lastoconfig import *;

def lassettings(settings):
  options = ["Date format", "Username", "Hostname", "Exit"];
  current = 0;
  colored = ["\033[44m\033[37m", "\033[47m\033[30m"];
  while (1):
    print("\033[44m\033[H\033[2J\033[47m\033[30mLasto Settings Manager\033[K\033[0m\n");

    for i,j in enumerate(options):
      print(f"\033[44m    {colored[current == i]}{j}\033[K\033[999C\033[4D\033[44m     ");
    print(end="\033[999B\033[104m\033[K\033[44m", flush=True);

    k = readkey();
    if (k in ["\033[A", "\033OA"]):
      current = (current - 1) % len(options);
    elif (k in ["\033[B", "\033OB"]):
      current = (current + 1) % len(options);
    elif (k == "\n"):
      if (current == 0):
        print("\033[10;10H\033[47m\033[30m Enter new date format:    \033[44m\033[37m");
        print("\033[11;10H\033[47m\033[30m \033[44m\033[37m\033[s                         \033[47m\033[30m \033[44m\033[37m");
        print(end="\033[12;10H\033[47m\033[30m                           \033[44m\033[37m\033[u");
        settings["date_format"] = input();
      elif (current == 1):
        print("\033[10;10H\033[47m\033[30m Enter new username:       \033[44m\033[37m");
        print("\033[11;10H\033[47m\033[30m \033[44m\033[37m\033[s                         \033[47m\033[30m \033[44m\033[37m");
        print(end="\033[12;10H\033[47m\033[30m                           \033[44m\033[37m\033[u");
        settings["username"] = input();
      elif (current == 2):
        print("\033[10;10H\033[47m\033[30m Enter new hostname:       \033[44m\033[37m");
        print("\033[11;10H\033[47m\033[30m \033[44m\033[37m\033[s                         \033[47m\033[30m \033[44m\033[37m");
        print(end="\033[12;10H\033[47m\033[30m                           \033[44m\033[37m\033[u");
        settings["hostname"] = input();
      elif (current == 3):
        print(end="\033[0m\033[H\033[2J");
        return settings;
