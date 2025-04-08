#!/usr/bin/python

import time;
import pygame;

screen = pygame.display.set_mode((640, 480));
pygame.display.set_caption("Lasto Display");
pygame.display.flip();

running = True;

print("\033[H\033[2J", end="\r");
welcome = "Welcome to \033[32mLastOS\033[0m"
print(welcome);
while (True):
	cmd_line = input(": ").split();
	if cmd_line[0] == "help":
		f = open("commands/1.help", "r");
		content = f.read();
		print(content);
	elif cmd_line[0] == "echo":
		print(" ".join(cmd_line[1:]));
	elif cmd_line[0] == "exit":
		exit();
	elif cmd_line[0] == "lasfetch":
		f = open("commands/lasfetch", "r")
		content = f.read();
		f.close();
		print(content);
	elif cmd_line[0] == "cls":
                print("\033[H\033[2J", end="\r");
	elif cmd_line[0] == "dateandtime":
		print(time.ctime());
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
		while (running):
			time.sleep(1);
