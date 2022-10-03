#!/usr/bin/env python3
from art import *
import time
import sys
from termcolor import colored


def banner():
    print(""" 
                             .
                           .    GIF
                    /^\     .
               /\   "V"
              /__\   I      PDF  o
             //..\\\  I     .
             \].`[/  I
             /l\/j\  (]    .  docx
            /. ~~ ,\/I     o    .
            \\L__j^\//I       mp4
             \/--v}  I     jpg   .
             |    |  I   _________
             |    |  I c(`       ')o
             |    l  I   \.     ,/
           _/j  L l\_!  _//^---^\\_  
                                                                                              
 ------------------- Twitter -------------------
  ----- @z5jt4 @unknownamd_ @Pho1yalfuhaid -----""")

    text = text2art("Byte Wizard")
    print(text)


def loading():
    print("Changing file signature: ")
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()


def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        # f.write(line + content)
        f.write(line.rstrip('\r\n') + '\n' + content)


def file_header(filename, filetype):
    with open(filename, 'rb+') as f:
        f.seek(0, 0)
        f.write(filetype)
        f.close()


def file_changer():
    print("""Select the filetype that you want to convert to:
    1- PDF   2- MP3 (audio)   3- jpg    4- pcapng
    5- GIF   6- tar           7- Word/Office
    
              
    Insert q to Quit 
-------------------------------------------------""")

    try:
        user_input = input("choose a filetype:")
    except ValueError:
        err = colored("ERROR: Only Numbers are Accepted", 'red')
        print(err)
        time.sleep(1)
        file_changer()

    options = ["1", "2", "3", "4", "5","6","7","q"]
    while user_input in options:
        if user_input == "1":
            file_type = b'\x25\x50\x44\x46\x2D'
            file_newline = "AAAAA\n"
        elif user_input == "2":
            file_type = b'\x49\x44\x33'
            file_newline = "AAA\n"
        elif user_input == "3":
            file_type = b'\xFF\xD8\xFF\xE0'
            file_newline = "AAAA\n"
        elif user_input == "4":
            file_type = b'\xD4\xC3\xB2\xA1'
            file_newline = "AAAA\n"
        elif user_input == "5":
            file_type = b'\x47\x49\x46\x38\x39\x61'
            file_newline = "AAAAAA\n"
        elif user_input == "6":
            file_type = b'\x1F\x9D'
            file_newline = "AA\n"
        elif user_input == "7":
            file_type = b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1'
            file_newline = "AAAAAAAA\n"
        elif user_input == "q":
            print("\nQUITTING!!")
            sys.exit()
        
        try:
            file = input("Enter a file name : ")
            line_prepender(file, file_newline)
            file_header(file, file_type)
            loading()
            success = colored(" \n✔ Your file {} type have been changed successfully by Byte Wizard.", 'green')
            print(success.format(file))
            exit()
        except FileNotFoundError:
            err = colored("ERROR 404: File {} not found", 'red')
            print(err.format(file))
    else:
        err = colored("\nERROR: Choose a filetype from the list :)", 'red')
        print(err)
        return file_changer()


banner()
try:
    file_changer()
except KeyboardInterrupt:
    print("\nQUITTING!!")
    sys.exit()
