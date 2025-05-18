#!/usr/bin/python3

import time;
import os;
import cli;

from lastofs import *;

from os import system;
from time import sleep;
from pygame import mixer;

import subprocess;

def print_chars(msg, t):
  for i in msg:
    print(end=i, flush=True);
    time.sleep(t);

def shell_call(command, shell=True, universal_newlines=True):
  try:
    result = subprocess.run(
      command,
      check=True,
      shell=shell,
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE,
      universal_newlines=universal_newlines
    );
    return result.stdout;
  except subprocess.CalledProcessError as e:
    error_output = f"Command failed with exit code {e.returncode}\n";
    error_output += f"Error output:\n{e.stderr}";
    raise subprocess.CalledProcessError(
      e.returncode, e.cmd, error_output
    ) from e;

def FS_Load(disk):
  disk = FS_DirCreate(disk, "L/bin");
  disk = FS_DirCreate(disk, "L/usr");
  disk = FS_DirCreate(disk, "L/lasto");
  disk = FS_DirCreate(disk, "L/lasto/Documents");
  disk = FS_DirCreate(disk, "L/lasto/Pictures");
  disk = FS_DirCreate(disk, "L/lasto/Downloads");
  disk = FS_DirCreate(disk, "L/lasto/Music");
  disk = FS_FileCreate(disk, "L/lasto/Downloads/file1.txt", "runtime/file1.txt");
  disk = FS_FileCreate(disk, "L/lasto/Downloads/file2.txt", "runtime/file2.txt");

  songs = shell_call("find runtime/music/ -type f");
  for i in songs.split("\n")[:-1]:
    i = i.split("/")[-1];
    disk = FS_FileCreate(disk, f"L/lasto/Music/{i}", f"runtime/music/{i}");

print("\033[H\033[2J", end="\r");
sleep(.2);
print(f"L/: 19,005,422 bytes free, 5 directories, 2 files");
sleep(.055);
print("Initializing \033[94mLastOS\033[0m 1.3.3");
sleep(.24);
print("  [0.000000]\tcreating virtual disk filesystem");
sleep(.1);
disk = FS_DiskInit("L");
print("  [0.101992]\tcreating basic filesystem hierarachy");
FS_Load(disk);
sleep(.14);
print("  [0.247918]\tsetting up shell and user settings");
cwd = "L/lasto/";
lasto_username = "lasto";
lasto_setting_date_format = "%Y-%m-%d %H:%M:%S";
sleep(.4);
print("  [0.681142]\tLastOS is ready to use!");
sleep(.2);
print("\n");

welcome = "Welcome to \033[94mLastOS\033[0m"
print(welcome);
while (True):
  cmd_line = input(f"\033[94m{cwd}>\033[0m ").split();
  if not cmd_line:
    continue;
  elif cmd_line[0] == "help":
    print("\033[34m+--------------------------------------------+");
    print("|\033[94mLastOS Command Help 1/1 Page\033[34m                |");
    print("|\033[32m  calc          \033[93mopen calculator\033[34m             |");
    print("|\033[32m  cd            \033[93mchange directory\033[34m            |");
    print("|\033[32m  changelog     \033[93msee change log\033[34m              |");
    print("|\033[32m  cls           \033[93mclear screen\033[34m                |");
    print("|\033[32m  date          \033[93mshow date and time\033[34m          |");
    print("|\033[32m  echo          \033[93moutput text on screen\033[34m       |");
    print("|\033[32m  exit          \033[93mshutdown os\033[34m                 |");
    print("|\033[32m  help          \033[93mshow all commands\033[34m           |");
    print("|\033[32m  hexcnv        \033[93mconvert any number to hex\033[34m   |");
    print("|\033[32m  info          \033[93m2 info of system\033[34m            |");
    print("|\033[32m  lasfetch      \033[93mshow info of the system\033[34m     |");
    print("|\033[32m  latutor       \033[93mlasto tutorial\033[34m              |");
    print("|\033[32m  ls            \033[93mlist files\033[34m                  |");
    print("|\033[32m  music-list    \033[93mlist music\033[34m                  |");
    print("|\033[32m  music-pause   \033[93mpause playing music\033[34m         |");
    print("|\033[32m  music-play    \033[93mplay music with pygame\033[34m      |");
    print("|\033[32m  music-stop    \033[93mstop playing music\033[34m          |");
    print("|\033[32m  music-test    \033[93mmusic test with pygame\033[34m      |");
    print("|\033[32m  music-unpause \033[93munpause playing music\033[34m       |");
    print("|\033[32m  octcnv        \033[93mconvert any number to octal\033[34m |");
    print("|\033[32m  pwd           \033[93mshow current directory\033[34m      |");
    print("|\033[32m  syserr        \033[93msystem error test\033[34m           |");
    print("+--------------------------------------------+\033[0m");
  elif cmd_line[0] == "syserr":
    cli.cli(0x00000003);
    exit(1);
  elif cmd_line[0] == "lasfetch":
    freemem = "/".join(shell_call("free -h").split()[7:9][::-1]);
    freedsk = "/".join(shell_call("df -h /").split()[8:10][::-1]);
    print(f"\033[94m  _    \033[94m{lasto_username}\033[0m@\033[94m{shell_call('hostname')[:-1]}\033[0m");
    print("\033[94m ('=   \033[0m--------------");
    print("\033[94m /_)   \033[94mOS Name\033[0m: LastOS 1.3.3");
    print("\033[94m /||   \033[94mLang\033[0m: Python");
    print("\033[94m       \033[94mDeveloper\033[0m: Luxidev & Xi816");
    print("\033[94m       \033[94mRelease Date\033[0m: 25-05-19");
    print(f"\033[94m       \033[94mMemory\033[0m: {freemem}");
    print(f"\033[94m       \033[94mDisk space\033[0m: {freedsk}\n");
  elif cmd_line[0] == "echo":
    print(" ".join(cmd_line[1:]));
  elif cmd_line[0] == "exit":
    exit();
  elif cmd_line[0] == "cls":
                print("\033[H\033[2J", end="\r");
  elif cmd_line[0] == "var":
    if (len(cmd_line) < 3):
      print("var: syntax error");
      print("usage: var <varname> <value>");
    else:
      exec(f"lasto_setting_{cmd_line[1]} = \"{' '.join(cmd_line[2:])}\"");
  elif cmd_line[0] == "date":
    system(f"date +'{lasto_setting_date_format}'");
  elif cmd_line[0] == "calc":
    print("Calculator for LastOS 1.3.3");
    while ((a := input("; ")) not in ["q", "quit", "exit"]):
      print(eval(a));
  elif cmd_line[0] == "linux":
    print("You found a secret!");
    print("         _nnnn_");
    print("        dGGGGMMb");
    print("       @p~qp~~qMb");
    print("       M|@||@) M|");
    print("       @,----.JM|");
    print("      JS^\__/  qKL");
    print("     dZP        qKRb");
    print("    dZP          qKKb");
    print("   fZP            SMMb");
    print("   HZM            MMMM");
    print("   FqM            MMMM");
    print(" __| \".        |\dS\"qML");
    print(" |    `.       | `' \Zq");
    print("_)      \.___.,|     .'");
    print("\____   )MMMMMP|   .'");
    print("     `-'       `--'");
  elif cmd_line[0] == "hexcnv":
    print("Hex Converter 0.2");
    print("Select the mode: ");
    print("1 = Numbers to Hex");
    print("2 = Hex to Numbers");
    selectmode = input("Select mode: ");
    if selectmode == "1":
      print("Numbers to Hex");
      print("Enter numbers for convert to Hex");
      hex_convert = input("Input: ");
      convert = hex(int(hex_convert));
      print("Result: ", convert);
    elif selectmode == "2":
      print("Hex to Numbers");
      print("Enter hex for convert to Numbers");
      hex_convert = input("Input: ");
      convert = int(hex_convert, 16);
      print("Result:", convert);
    else:
      print("Incorrent Input");
  elif cmd_line[0] == "hello":
    def print_chars(msg, t):
      for i in msg:
        print(end=i, flush=True);
        time.sleep(t);
    print_chars("Hello World!\n", 0.1);
  elif cmd_line[0] == "octcnv":
    print("Octal Converter 0.1");
    print("Select mode:");
    print("1 = Number to Octal");
    print("2 = Octal to Number");
    selectmode = input("Select mode: ");
    if selectmode == "1":
      print("Numbers to Octal");
      print("Enter numbers for convert to Octal");
      oct_convert = input("Input: ");
      convert = oct(int(oct_convert));
      print("Result:", convert);
    elif selectmode == "2":
      print("Octal to Numbers");
      print("Enter Octal for convert to Numbers");
      oct_convert = input("Input: ");
      convert = int(oct_convert, 8);
      print("Result:", convert);
    else:
      print("Incorrect Input");
  elif cmd_line[0] == "info":
    print("\033[94mVersion: 1.3.3\033[0m");
    print("\033[94m(C) Release: 2025-05-18\033[0m");
    print("\033[94mDeveloper: Luxidev & Xi816\033[0m");
  elif cmd_line[0] == "latutor":
    print("Welcome to \033[33mLasto\033[0m Tutorial!");
    print("\033[32mPress enter to start tutorial...\033[0m");
    input();
    print("\033[H\033[2J");
    print("Okay, let's start from commands.");
    print("\033[92mlasfetch\033[0m - this command outputs information of the LastOS operating system");
    sleep(3);
    print("\033[92mecho\033[0m - this command prints text (echoes back) to the screen");
    sleep(3);
    print("\033[92mcls\033[0m - this command clears the terminal");
    sleep(3);
    print("\033[92mdate\033[0m - command prints current date into the terminal");
    sleep(3);
    print("\033[92mcalc\033[0m - this command runs a terminal calculator");
    sleep(3);
    print("\033[92mhexcnv\033[0m - this command converts any decimal number to hexadecimal or vice versa");
    sleep(3);
    print("\033[92moctcnv\033[0m - this command converts any decimal number to octal or vice versa");
    sleep(3);
    print("\033[92maboutlastre\033[0m - LastOS info by metohoru");
    sleep(3);
    print("\033[92msyserr\033[0m - starts up test kernel panic");
    sleep(3);
    print("\033[92minfo\033[0m - shows LastOS release info");
    sleep(3);
    print("\033[92mhelp\033[0m - show help");
    sleep(3);
    print("\033[92mexit\033[0m - exits from the OS");
    sleep(1);
    print("Cool bro! You know how to using LastOS now!!!");
    sleep(1);
  elif cmd_line[0] == "music-test":
    mixer.init();
    mixer.music.load("sceptrum.mp3");
    mixer.music.play();
  elif cmd_line[0] == "music-play":
    mixer.init();
    music_fn = input("Enter music name (with format): ");
    FS_FileStream(disk, "L/lasto/Music/"+music_fn, "runtime/tmp/music.mp3");
    mixer.music.load("runtime/tmp/music.mp3");
    mixer.music.play();
  elif cmd_line[0] == "music-stop":
    mixer.music.stop();
  elif cmd_line[0] == "music-pause":
    mixer.music.pause();
  elif cmd_line[0] == "music-unpause":
    mixer.music.unpause();
  elif cmd_line[0] == "music-list":
    for i,j in enumerate(FS_ListFilesRaw(disk, "L/lasto/Music/").split(" ")):
      print(f"{i+1}\t{j}");
  elif cmd_line[0] == "cd":
    if (cmd_line[1] == ".."):
      if (len(cwd) != 2):
        cwd = "/".join(cwd[:-1].split("/")[:-1])+"/";
    else:
      if (cmd_line[1][-1] != "/"):
        cmd_line[1] += "/";
      cwd += cmd_line[1];
  elif cmd_line[0] == "pwd":
    print(cwd);
  elif cmd_line[0] == "cat":
    print(FS_FileRead(disk, cwd+cmd_line[1]).decode("utf-8"));
  elif cmd_line[0] == "changelog":
    system("less runtime/changelog.txt");
  elif cmd_line[0] == "ls":
    if (len(cmd_line) == 1):
      print(FS_ListDirs(disk, cwd) + FS_ListFiles(disk, cwd));
    else:
      if (cmd_line[1][-1] != "/"):
        cmd_line[1] += "/";
      print(FS_ListDirs(disk, cwd+cmd_line[1]) + FS_ListFiles(disk, cwd+cmd_line[1]));
  else:
    print("Bad Command.");

