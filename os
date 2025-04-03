#!/usr/bin/python

import os;

os.system("clear");
print("Welcome to \033[32mLastOS\033[0m");
while (True):
	cmd_line = input("# ").split();
	if cmd_line[0] == "help":
                print("Using:");
                print("   lasfetch - show info of the system");
                print("   echo - output text on display");
                print("   cls - clear screen");
                print("   date - show date");
                print("   time - show time");
                print("   help - show all commands");
                print("   exit - shutdown os");
	elif cmd_line[0] == "echo":
		print(" ".join(cmd_line[1:]));
	elif cmd_line[0] == "exit":
		exit();
	elif cmd_line[0] == "lasfetch":
                print("\033[36m _\033[0m  | OS Name: LastOS 0.1");
                print("\033[36m('=\033[0m | Lang: Python");
                print("\033[36m/_)\033[0m | Developer: FedouM & Xi816");
                print("\033[36m/||\033[0m | Release Date: 2025-04-02");
	elif cmd_line[0] == "cls":
                os.system("clear");
	elif cmd_line[0] == "date":
		os.system("date +%D");
	elif cmd_line[0] == "time":
		os.system("date +%T");
	else:
		print("Bad Command.");
