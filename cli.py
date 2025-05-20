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
  print(f"\033[91mtrapped\033[0m at 0x{hex(c)[2:]:0>8}");
  print(f"\033[91mError:\033[0m {errors[c]}");
  while (True):
    com = input("! ");
    if not com:
      pass;
    elif com == "h":
      print("lastos cli help:");
      print("  h      help");
      print("  t      show trap codes");
      print("  c      clear screen");
      print("  r      run lastos");
      print("  q      exit from cli");
    elif com == "t":
      for i in errors:
        print(f"  0x{hex(i)[2:]:0>8}\t{errors[i]}");
    elif com == "c":
      print("\033[H\033[2J", end="\r");
    elif com == "r":
      os.system("python boot_manager lastos.py");
      exit();
    elif com == "q":
      exit();
    else:
      print("Bad command.");
