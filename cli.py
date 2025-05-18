#!/usr/bin/python3

import os;

def cli(c: int):
	print(f"\033[91mtrapped\033[0m at 0x{hex(c)[2:]:0>8}");
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
			print("  0x000000\tUnexpected error");
			print("  0x000001\tTrap");
			print("  0x000002\tDivision by zero");
			print("  0x000003\tSystem error");
		elif com == "c":
			print("\033[H\033[2J", end="\r");
		elif com == "r":
			os.system("python boot_manager lastos.py");
			exit();
		elif com == "q":
			exit();
		else:
			print("Bad command.");
