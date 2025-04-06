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
welcome = "Welcome to \033[32mLastOS\033[0m"
print(welcome);
while (True):
	cmd_line = input("LASTOS -> ").split();
	if cmd_line[0] == "help":
                print("Using:");
                print("   lasfetch - show info of the system");
                print("   echo - output text on display");
                print("   cls - clear screen");
                print("   date - show date");
                print("   time - show time");
                print("   jokegame - start joke game");
                print("   calc - open calculator");
                print("   kernelpanic - lasto kernelpanic");
                print("   help - show all commands");
                print("   exit - shutdown os");
	elif cmd_line[0] == "echo":
		print(" ".join(cmd_line[1:]));
	elif cmd_line[0] == "exit":
		exit();
	elif cmd_line[0] == "lasfetch":
                print("\033[36m _\033[0m  | OS Name: LastOS 0.2");
                print("\033[36m('=\033[0m | Lang: Python");
                print("\033[36m/_)\033[0m | Developer: FedouM");
                print("\033[36m/||\033[0m | Release Date: 2025-04-04");
	elif cmd_line[0] == "cls":
                os.system("clear");
	elif cmd_line[0] == "date":
		os.system("date +%D");
	elif cmd_line[0] == "time":
		os.system("date +%T");
	elif cmd_line[0] == "jokegame":
                sosal = input("Введи да: ");
                print("\033[A Сосал?: ", sosal);
	elif cmd_line[0] == "calc":
                def add(a, b):
                        return a + b;
                def subtract(a, b):
                        return a - b;
                def multiply(a, b):
                        return a * b;
                def devide(a, b):
                        return a / b;

                choice = input("Opearation (+,-,*,/): ");

                num1 = float(input("Enter first number: "));
                num2 = float(input("Enter second number: "));

                if choice == "+":
                        result = add(num1, num2)
                        print("Result: ", result);
                elif choice == "-":
                        result = subtract(num1, num2);
                        print("Result: ", result);
                elif choice == "*":
                        result = multiply(num1, num2);
                        print("Result: ", result);
                elif choice == "/":
                        result = devide(num1, num2);
                        print("Result: ", result);
                else:
                        print("Incorrent input");
	elif cmd_line[0] == "kernelpanic":
                os.system("clear");
                print("         /");
                print(" .      /");
                print("       /  Error code: 0x000001");
                print("      /  Decode error: KernelPanic Command Test");
                print("     /");
                print("     \\");
                print("      \\");
                print("       \\");
                print(" .      \\");
                print("         \\");
                print("Solving error... 1%", end="\r");
                time.sleep(1);
                print("Solving error... 28%", end="\r");
                time.sleep(1);
                print("Solving error... 36%", end="\r");
                time.sleep(1);
                print("Solving error... 47%", end="\r");
                time.sleep(1);
                print("Solving error... 59%", end="\r");
                time.sleep(1);
                print("Solving error... 68%", end="\r");
                time.sleep(1);
                print("Solving error... 98%", end="\r");
                time.sleep(1);
                print("Solving error... 100%", end="\r");
                time.sleep(2);
                print("Rebooting to system...");
                os.system("clear");
                print(welcome);
	else:
		print("Bad Command.");
