# zSMBrute
Example Command
``` bash
python3 zSMBrute.py -d 1 -i 192.168.0.143 -u username.txt -p passwords.txt
```
Help...
``` bash
-[~/Desktop]$ python3 zSMBrute.py 
usage: zSMBrute.py [-h] [-d DELAY] [-i HOST] [-u USERNAMESFILE] [-p PASSWORDSFILE] [-o OUTPUTFILE]

User credentials brute force script

options:
  -h, --help            show this help message and exit
  -d DELAY, --delay DELAY
                        Delay in minutes between each password attempt
  -i HOST, --host HOST  Host/DC IP address
  -u USERNAMESFILE, --usernamesfile USERNAMESFILE
                        Path to the file containing the usernames
  -p PASSWORDSFILE, --passwordsfile PASSWORDSFILE
                        Path to the file containing the passwords
  -o OUTPUTFILE, --outputfile OUTPUTFILE
                        Output file for the valid credentials
```

# zLdapBrute
Example Command
``` bash
python3 zLdapBrute.py  -d 1 -i 10.11.1.1 -u username.txt -p passwords.txt -t ldap -n DC=test,DC=labs -ds test
```
Help...
``` bash
-[~/Desktop]$ python3 zLdapBrute.py
usage: zLdapBrute.py [-h] [-d DELAY] [-i HOST] [-u USERNAMESFILE] [-p PASSWORDSFILE] [-t {ldap}] [-o OUTPUTFILE] [-n NAMINGCONTEXT] [-ds DOMAIN_SHORTNAME]

User credentials brute force script

options:
  -h, --help            show this help message and exit
  -d DELAY, --delay DELAY
                        Delay in minutes between each password attempt
  -i HOST, --host HOST  Host/DC IP address
  -u USERNAMESFILE, --usernamesfile USERNAMESFILE
                        Path to the file containing the usernames
  -p PASSWORDSFILE, --passwordsfile PASSWORDSFILE
                        Path to the file containing the passwords
  -t {ldap}, --protocol {ldap}
                        Protocol to use for login (only LDAP available)
  -o OUTPUTFILE, --outputfile OUTPUTFILE
                        Output file for the valid credentials
  -n NAMINGCONTEXT, --namingcontext NAMINGCONTEXT
                        LDAP naming context
  -ds DOMAIN_SHORTNAME, --domain-shortname DOMAIN_SHORTNAME
                        Domain short name for the LDAP server

```
