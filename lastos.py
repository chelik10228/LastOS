#!/usr/bin/python3

import os;
import cli;
import time;

from lasutil import *;
from lastofs import *;
from lastoconfig import *;
from lasfetch import lasfetch;
from lassettings import lassettings;
# lassettings();

from os import system, environ;
from time import sleep;

environ["PYGAME_DETECT_AVX2"] = "1";
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1";
from pygame import mixer;
import subprocess;

def FS_Init(disk):
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
  return disk;

disk = None;
cwd = "";
settings = dict();
def Lasto_Init():
  global disk, cwd, settings;

  print("\033[H\033[2J", end="\r");
  sleep(.2);
  print(f"L/: 19,005,422 bytes free, 5 directories, 2 files");
  sleep(.055);
  print(f"Initializing \033[94mLastOS\033[0m {LASTO_VERSION}");
  sleep(.24);
  print("  [0.000000]\tcreating virtual disk filesystem");
  sleep(.1);
  disk = FS_DiskInit("L");
  print("  [0.101992]\tcreating basic filesystem hierarachy");
  disk = FS_Init(disk);
  sleep(.14);
  print("  [0.247918]\tsetting up shell and user settings");
  cwd = "L/lasto/";
  settings["username"] = "lasto";
  settings["date_format"] = "%-m/%d/%y %H:%M:%S";
  sleep(.4);
  print("  [0.681142]\tLastOS is ready to use!");
  sleep(.2);
  print("\n");

Lasto_Init();
print("Welcome to \033[94mLastOS\033[0m");
while (1):
  cmd_line = input(f"\033[94m{cwd}>\033[0m ").split();
  if (not cmd_line):
    continue;
  elif (cmd_line[0] == "help"):
    printff("runtime/preload/help.txt");
  elif (cmd_line[0] == "syserr"):
    cli.cli(0x00000003);
    exit(1);
  elif (cmd_line[0] == "lasfetch"):
    lasfetch(settings["username"]);
  elif (cmd_line[0] == "echo"):
    print(" ".join(cmd_line[1:]));
  elif (cmd_line[0] == "exit"):
    exit();
  elif (cmd_line[0] == "cls"):
    print(end="\033[H\033[2J");
  elif (cmd_line[0] == "var"):
    if (len(cmd_line) < 3):
      print("var: syntax error");
      print("usage: var <varname> <value>");
    else:
      settings[cmd_line[1]] = " ".join(cmd_line[2:]);
  elif (cmd_line[0] == "date"):
    system(f"date +'{settings['date_format']}'");
  elif (cmd_line[0] == "calc"):
    print(f"Calculator for LastOS {LASTO_VERSION}");
    while ((a := input("; ")) not in ["q", "quit", "exit"]):
      print(eval(a));
  elif (cmd_line[0] == "linux"):
    printff("runtime/preload/linux.txt");
  elif (cmd_line[0] == "hexcnv"):
    print("Hex Converter 0.2\nSelect the mode:\n1 = Numbers to Hex\n2 = Hex to Numbers");
    selectmode = input("Select mode: ");
    print(hex(int(input(": "))) if (selectmode == "1") else int(input(": "), base=16));
  elif (cmd_line[0] == "hello"):
    def print_chars(msg, t):
      for i in msg:
        print(end=i, flush=True);
        time.sleep(t);
    print_chars("Hello World!\n", 0.1);
  elif (cmd_line[0] == "octcnv"):
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
    elif (selectmode == "2"):
      print("Octal to Numbers");
      print("Enter Octal for convert to Numbers");
      oct_convert = input("Input: ");
      convert = int(oct_convert, 8);
      print("Result:", convert);
    else:
      print("Incorrect Input");
  elif (cmd_line[0] == "info"):
    printff("runtime/preload/info.txt");
  elif (cmd_line[0] == "latutor"):
    print("Welcome to \033[33mLasto\033[0m Tutorial!");
    print("\033[32mPress enter to start tutorial...\033[0m");
    input();
    print("\033[H\033[2JOkay, let's start from commands.");
    tutor = readff("runtime/preload/tutor.txt").split("\n");
    printd(tutor, d=3);
    sleep(1);
  elif (cmd_line[0] == "music-test"):
    mixer.init();
    mixer.music.load("sceptrum.mp3");
    mixer.music.play();
  elif (cmd_line[0] == "music-play"):
    mixer.init();
    music_fn = input("Enter music name (with format): ");
    FS_FileStream(disk, "L/lasto/Music/"+music_fn, "runtime/tmp/music.mp3");
    mixer.music.load("runtime/tmp/music.mp3");
    mixer.music.play();
  elif (cmd_line[0] == "music-stop"):
    mixer.music.stop();
  elif (cmd_line[0] == "music-pause"):
    mixer.music.pause();
  elif (cmd_line[0] == "music-unpause"):
    mixer.music.unpause();
  elif (cmd_line[0] == "music-list"):
    for i,j in enumerate(FS_ListFilesRaw(disk, "L/lasto/Music/").split(" ")):
      print(f"{i+1}\t{j}");
  elif (cmd_line[0] == "cd"):
    if (cmd_line[1] == ".."):
      if (len(cwd) != 2):
        cwd = "/".join(cwd[:-1].split("/")[:-1])+"/";
    else:
      if (cmd_line[1][-1] != "/"):
        cmd_line[1] += "/";
      cwd += cmd_line[1];
  elif (cmd_line[0] == "pwd"):
    print(cwd);
  elif (cmd_line[0] == "cat"):
    print(FS_FileRead(disk, cwd+cmd_line[1]).decode("utf-8"));
  elif (cmd_line[0] == "changelog"):
    system("less runtime/changelog.txt");
  elif (cmd_line[0] == "ls"):
    if (len(cmd_line) == 1):
      print(FS_ListDirs(disk, cwd) + FS_ListFiles(disk, cwd));
    else:
      if (cmd_line[1][-1] != "/"):
        cmd_line[1] += "/";
      print(FS_ListDirs(disk, cwd+cmd_line[1]) + FS_ListFiles(disk, cwd+cmd_line[1]));
  elif (cmd_line[0] == "lassettings"):
    settings = lassettings(settings);
  else:
    print(f"Bad command or file name {cmd_line[0]}");
