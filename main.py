import argparse, validators
from colorama import Fore

from core.libssh_auth_bypass import LibSSHAuthBypass

BANNER = r'''
       __________ __  __
      / ___/ ___// / / /
      \__ \\__ \/ /_/ / 
     ___/ /__/ / __  /  
    /____/____/_/ /_/   
                    
'''

if __name__ == "__main__":
    print(BANNER)

    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="Target ip/host.")
    parser.add_argument("port", help="Target port.")
    args = parser.parse_args()

    print(f"[*] Validating user input.")
    if validators.ipv4(args.host) and args.port.isdigit():
        print("[*] Validated host,port.")
    else:
        print("[!] Error validating user input.")
        exit()


    print(f"[*] Starting testing on {args.host}:{args.port}.")


    if LibSSHAuthBypass.Exploit(args.host, args.port):
        print(f"[!] Target is {Fore.GREEN}vulnerable{Fore.RESET} to LibSSH Auth Bypass.")
    else:
        print(f"[*] Target is {Fore.RED}not vulnerable{Fore.RESET} to LibSSH Auth Bypass.")

    # kinda getting lazy here ngl
    