#!/usr/bin/python

print("\033[31mtrapped\033[0m at 0x000001");
while (True):
	com = input("! ");
	if not com:
		pass;
	elif com == "h":
		print("LastOS CLI Command Help 1/1 Page");
		print("  h - help");
		print("  t - show trap codes");
		print("  q - exit from cli");
	elif com == "t":
		print("0x000001 - command trap test or start cli");
	elif com == "q":
		exit();
	else:
		print("Bad command.");
