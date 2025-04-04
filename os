#!/usr/bin/python

import os;
import time;
import tkinter as tk;

root = tk.Tk();
root.title("Lasto Display");
root.minsize(640, 480);
root.geometry("640x480");
root.configure(background="blue");

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
                print("   jokegame - start joke game");
                print("   help - show all commands");
                print("   exit - shutdown os");
	elif cmd_line[0] == "echo":
		print(" ".join(cmd_line[1:]));
	elif cmd_line[0] == "exit":
		exit();
	elif cmd_line[0] == "lasfetch":
                print("\033[36m _\033[0m  | OS Name: LastOS 0.2");
                print("\033[36m('=\033[0m | Lang: Python");
                print("\033[36m/_)\033[0m | Developer: FedouM & Xi816");
                print("\033[36m/||\033[0m | Release Date: 2025-04-02");
	elif cmd_line[0] == "cls":
                os.system("clear");
	elif cmd_line[0] == "date":
		os.system("date +%D");
	elif cmd_line[0] == "time":
		os.system("date +%T");
	elif cmd_line[0] == "jokegame":
                sosal = input("Введи да: ");
                print("\033[A Сосал?: ", sosal);
	else:
		print("Bad Command.");
