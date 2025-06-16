#!/usr/bin/python3

import os;

errors = {
  0x00000000: "Unexpected trap",
  0x00000001: "Trap",
  0x00000002: "Division by zero",
  0x00000003: "System error",
  0x00000004: "Not enough space on device",

  0x00000103: "Too big disk label"
};

def cli(c: int):
  print(f"Kernel panic 0,0x{hex(c)[2:]:0>8}: {errors[c]}");
  print("Entering rescue mode...");
  print("  type \"h\" for help");
  while (True):
    com = input("lasto rescue> ");
    if (not com): continueOB;
    elif (com[0] == "h"): print("Lasto Rescue help:\n  h      Show help\n  e      Show error codes\n  c      Clear the screen\n  s      Shutdown");
    elif (com[0] == "e"):
      for i in errors:
        print(f"  0x{hex(i)[2:]:0>8}\t{errors[i]}");
    elif (com[0] == "c"):
      print(end="\033[H\033[2J");
    elif (com[0] == "s"):
      print(end="\033[H\033[2J");
      exit();
    else:
      print("Bad command.");
