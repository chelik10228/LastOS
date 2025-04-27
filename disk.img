#!/usr/bin/python

import time;

print("\033[H\033[2J", end="\r");
welcome = "Welcome to \033[32mLastOS\033[0m"
print(welcome);
while (True):
	cmd_line = input("$ ").split();
	if not cmd_line:
                pass;
	elif (cmd_line[0] == "help"):
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
                def divide(a, b):
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
                        result = divide(num1, num2);
                        print("Result: ", result);
                else:
                        print("Incorrent input");
	elif cmd_line[0] == "linux":
                print("You are found secret!");
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
	elif cmd_line[0] == "hexcnv":
		print("Hex Converter 0.2");
		print("Select the mode: ");
		print("1 = Numbers to Hex");
		print("2 = Hex to Numbers");
		selectmode = input("Select mode: ");
		if selectmode == "1":
			print("Numbers to Hex");
			print("Enter numbers for convert to Hex");
			hex_convert = input("Input: ");
			convert = hex(int(hex_convert));
			print("Result: ", convert);
		elif selectmode == "2":
			print("Hex to Numbers");
			print("Enter hex for convert to Numbers");
			hex_convert = input("Input: ");
			convert = int(hex_convert, 16);
			print("Result:", convert);
		else:
			print("Incorrent Input");
	elif cmd_line[0] == "hello":
		def print_chars(msg, t):
			for i in msg:
				print(end=i, flush=True);
				time.sleep(t);
		print_chars("Hello World!\n", 0.1);
	elif cmd_line[0] == "octcnv":
		print("Octal Converter 0.1");
		print("Select mode:");
		print("1 = Number to Octal");
		print("2 = Octal to Number");
		selectmode = input("Select mode: ");
		if selectmode == "1":
			print("Numbers to Octal");
			print("Enter numbers for convert to Octal");
			oct_convert = input("Input: ");
			convert = oct(int(oct_convert));
			print("Result:", convert);
		elif selectmode == "2":
			print("Octal to Numbers");
			print("Enter Octal for convert to Numbers");
			oct_convert = input("Input: ");
			convert = int(oct_convert, 8);
			print("Result:", convert);
		else:
			print("Incorrect Input");
	elif cmd_line[0] == "aboutlastre":
		print("============================================================================================");
		print("=    LastRE is a fork of LastOS - a pseudo-OS written on Python.                           =");
		print("= LastRE contains new commands and fixes, and some of OG LastOS's programs were rewritten. =");
		print("=                                        v0.1                                              =");
		print("============================================================================================");
	else:
		print("Bad Command.");
