#!/usr/bin/python3

import time;
import os;
import cli;

from lastofs import *;

from os import system;
from pygame import mixer;

import subprocess;

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
  print("Loading filesystem...");
  disk = FS_DirCreate(disk, "L/bin");
  disk = FS_DirCreate(disk, "L/usr");
  disk = FS_DirCreate(disk, "L/lasto");
  disk = FS_DirCreate(disk, "L/lasto/Documents");
  disk = FS_DirCreate(disk, "L/lasto/Pictures");
  disk = FS_DirCreate(disk, "L/lasto/Downloads");
  disk = FS_FileCreate(disk, "L/lasto/Downloads/file1.txt");
  disk = FS_FileCreate(disk, "L/lasto/Downloads/file2.txt");

disk = FS_DiskInit("L");
FS_Load(disk);
cwd = "L/lasto/";
lasto_username = "lasto";

print("\033[H\033[2J", end="\r");
welcome = "Welcome to \033[94mLastOS\033[0m"
print(welcome);
while (True):
  cmd_line = input("> ").split();
  if not cmd_line:
    pass;
  if cmd_line[0] == "help":
    print("\033[34m+--------------------------------------------+");
    print("|\033[94mLastOS Command Help 1/1 Page\033[34m                |");
    print("|\033[32m  aboutlastre   \033[93mlastre\033[34m                      |");
    print("|\033[32m  calc          \033[93mopen calculator\033[34m             |");
    print("|\033[32m  cd            \033[93mchange directory\033[34m            |");
    print("|\033[32m  cls           \033[93mclear screen\033[34m                |");
    print("|\033[32m  dateandtime   \033[93mshow date and time\033[34m          |");
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
    def print_chars(msg, t):
      for i in msg:
        print(end=i, flush=True);
        time.sleep(t);
    print("\033[H\033[2J", end="\r");
    time.sleep(2);
    print_chars("-------------------\n", 0.01);
    print_chars("\033[31mSYSTEM ERROR\033[0m\n", 0.01);
    print_chars("-------------------\n", 0.01);
    print_chars("\033[32mSystem crash\033[0m\n", 0.01);
    print_chars("Log: \n", 0.01);
    print_chars("EXECUTE_AT_ROOT com syserr\n", 0.01);
    print_chars("call 0x000001\n", 0.01);
    print_chars("EXECUTE_SYSTEM_REBOOT\n", 0.01);
    print_chars("ERROR_OF_SYSTEM_REBOOT\n", 0.01);
    print_chars("SYSERR\n", 0.01);
    print_chars("Error code: 0x000001\n", 0.01);
    time.sleep(2);
    cli.cli();
    exit();
  elif cmd_line[0] == "lasfetch":
    print(f"\033[94m      \033[0m| \033[94m{lasto_username}\033[0m@\033[94m{shell_call('hostname')[:-1]}\033[0m");
    print("\033[94m  _   \033[0m| \033[94mOS Name\033[0m: LastOS 1.1");
    print("\033[94m ('=  \033[0m| \033[94mLang\033[0m: Python");
    print("\033[94m /_)  \033[0m| \033[94mDeveloper\033[0m: Luxidev & Xi816");
    print("\033[94m /||  \033[0m| \033[94mRelease Date\033[0m: 2025-05-18");
  elif cmd_line[0] == "echo":
    print(" ".join(cmd_line[1:]));
  elif cmd_line[0] == "exit":
    exit();
  elif cmd_line[0] == "cls":
                print("\033[H\033[2J", end="\r");
  elif cmd_line[0] == "dateandtime":
    print(time.ctime());
  elif cmd_line[0] == "calc":
    choice = input("Operation (+,-,*,/): ");

    num1 = float(input("Enter first number: "));
    num2 = float(input("Enter second number: "));

    if choice == "+":
      result = num1 + num2
      print("Result: ", result);
    elif choice == "-":
      result = num1 - num2;
      print("Result: ", result);
    elif choice == "*":
      result = num1 * num2;
      print("Result: ", result);
    elif choice == "/":
      try:
        result = num1 / num2;
        print("Result: ", result);
      except ZeroDivisionError:
        cli.cli();
    else:
      print("Incorrent input");
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
  elif cmd_line[0] == "aboutlastre":
    print("============================================================================================");
    print("=    LastRE is a fork of LastOS - a pseudo-OS written on Python.                           =");
    print("= LastRE contains new commands and fixes, and some of OG LastOS's programs were rewritten. =");
    print("=                                        v0.1                                              =");
    print("============================================================================================");
    print("lastre by metohoru");
  elif cmd_line[0] == "info":
    print("\033[94mVersion: 1.1\033[0m");
    print("\033[94m(C) Release: 2025-05-18\033[0m");
    print("\033[94mDeveloper: Luxidev & Xi816\033[0m");
  elif cmd_line[0] == "cat":
    print("nya");
    print("  /\_/\\");
    print(" ( o.o )");
    print("  > ^ <");
  elif cmd_line[0] == "latutor":
    print("Welcome to \033[33mLasto\033[0m Tutorial!");
    print("\033[32mPress enter to start tutorial...\033[0m");
    input();
    print("\033[H\033[2J");
    print("Okay, start from commands.");
    print("Wait 3 seconds for show other commands");
    print("lasfetch - this command is outputing information of system lastos, example fastfetch or neofetch");
    time.sleep(3);
    print("echo - all know's this command, this command is printing text on screen which you typed");
    time.sleep(3);
    print("cls - this command is clearing terminal");
    time.sleep(3);
    print("date - command is printing date in terminal");
    time.sleep(3);
    print("calc - this command is opening terminal calculator");
    time.sleep(3);
    print("hexcnv - this command is can convert any number to hex or hex to number");
    time.sleep(3);
    print("octcnv - this command is can convert any number to octal or octal to number");
    time.sleep(3);
    print("aboutlastre - it's info of lastos by teaxdev");
    time.sleep(3);
    print("syserr - it's command is test of system error");
    time.sleep(3);
    print("info - it's other info of lastos");
    time.sleep(3);
    print("help - show all commands");
    time.sleep(3);
    print("exit - exit with os");
    time.sleep(1);
    print("\033[H\033[2J");
    print("Okay, now you know all commands, and now...");
    time.sleep(1);
    print("Let's learn using of commands!");
    time.sleep(1);
    print("1. calc");
    time.sleep(1);
    print("Using calc easy!");
    time.sleep(1);
    print("Select operation, +, -, * or /");
    time.sleep(1);
    print("Next, type 1 any numbers");
    time.sleep(1);
    print("And press enter, and type 2 any numbers");
    time.sleep(1);
    print("Done! You learned how to using calculator in lastos!");
    time.sleep(1);
    print("2. hexcnv");
    time.sleep(1);
    print("Using hexcnv too easy!");
    time.sleep(1);
    print("You need select number 1 or 2, 1 = number to hex, 2 = hex to number");
    time.sleep(1);
    print("Next select any number");
    time.sleep(1);
    print("And... Result!");
    time.sleep(1);
    print("Good! Now you know how to using hexcnv!");
    time.sleep(1);
    print("3. octcnv");
    time.sleep(1);
    print("Using octcnv it's copy of hex but not hex, a octal");
    time.sleep(1);
    print("Cool bro! You know how to using LastOS now!!!");
    time.sleep(1);
    print("Good bye bro!!!!!");
  elif cmd_line[0] == "music-test":
    mixer.init();
    mixer.music.load("sceptrum.mp3");
    mixer.music.play();
  elif cmd_line[0] == "music-play":
    mixer.init();
    music = input("Enter music name (with format): ");
    mixer.music.load(music);
    mixer.music.play();
  elif cmd_line[0] == "music-stop":
    mixer.music.stop();
  elif cmd_line[0] == "music-pause":
    mixer.music.pause();
  elif cmd_line[0] == "music-unpause":
    mixer.music.unpause();
  elif cmd_line[0] == "music-list":
    system("find . -name \"*.mp3\" | cut -b 3-");
  elif cmd_line[0] == "cd":
    if (cmd_line[1] == ".."):
      cwd = "/".join(cwd[:-1].split("/")[:-1])+"/";
    else:
      cwd += cmd_line[1]+"/";
    print(cwd);
  elif cmd_line[0] == "ls":
    print(FS_ListDirs(disk, cwd) + FS_ListFiles(disk, cwd));
  else:
    print("Bad Command.");

