#!/usr/bin/python

def cli(errno: error_to_name):
	print("\033[31mtrapped\033[0m");
	while (True):
		com = input("! ");
		if not com:
			pass;
		elif com == "h":
			print("lastos cli help:");
			print("  h      help");
			print("  t      show trap codes");
			print("  c      clear screen");
			print("  q      exit from cli");
		elif com == "t":
			print("0x000001 - command trap test or start cli");
			print("0x000002 - error in python ZeroDivisionError");
		elif com == "c":
			print("\033[H\033[2J", end="\r");
		elif com == "q":
			exit();
		else:
			print("Bad command.");
