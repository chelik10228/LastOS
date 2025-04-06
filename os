#!/usr/bin/python

import time;
import pygame;

screen = pygame.display.set_mode((640, 480));
pygame.display.set_caption("Lasto Display");
pygame.display.flip();

print("\033[H\033[2J", end="\r");
welcome = "Welcome to \033[32mLastOS\033[0m"
print(welcome);
while (True):
	cmd_line = input(": ").split();
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
                print("\033[36m _\033[0m  | OS Name: LastOS 0.3");
                print("\033[36m('=\033[0m | Lang: Python");
                print("\033[36m/_)\033[0m | Developer: FedouM");
                print("\033[36m/||\033[0m | Release Date: 2025-04-06");
	elif cmd_line[0] == "cls":
                print("\033[H\033[2J", end="\r");
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

                choice = input("Operation (+,-,*,/): ");

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
		def print_chars(msg, t):
			for i in msg:
				print(end=i, flush=True);
				time.sleep(t);
		print("\033[H\033[2J", end="\r");
		print_chars("------------------\n", 0.01);
		print_chars("\033[31mKERNEL PANIC\033[0m\n", 0.01);
		print_chars("------------------\n", 0.01);
		print_chars("\033[32mSystem crash\033[0m\n", 0.01);
		print_chars("Log: \n", 0.01);
		print_chars(": kernelpanic\n", 0.01);
		print_chars("call 0x000001\n", 0.01);
		print_chars("KERNELPANIC\n", 0.01);
		time.sleep(2);
		print("\033[H\033[2J", end="\r");
		print(welcome);
	elif cmd_line[0] == "linux":
                print("Это пасхалка!");
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
	else:
		print("Bad Command.");
