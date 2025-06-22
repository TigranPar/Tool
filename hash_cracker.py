import hashlib
import sys

def crack_hash(hash_to_crack, wordlist_path, algorithm):
    try:
        with open(wordlist_path, 'r') as f:
            passwords = f.readlines()
    except FileNotFoundError:
        print(f"[!] Wordlist not found: {wordlist_path}")
        return

    print(f"[~] Trying to crack hash using {algorithm.upper()}...\n")

    for password in passwords:
        password = password.strip()
        if algorithm == 'md5':
            hash_candidate = hashlib.md5(password.encode()).hexdigest()
        elif algorithm == 'sha1':
            hash_candidate = hashlib.sha1(password.encode()).hexdigest()
        elif algorithm == 'sha256':
            hash_candidate = hashlib.sha256(password.encode()).hexdigest()
        else:
            print("[!] Unsupported algorithm")
            return

        if hash_candidate == hash_to_crack:
            print(f"[+] Password found: {password}")
            return

    print("[-] Password not found in wordlist.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 hash_cracker.py <hash> <wordlist.txt> <algorithm>")
        print("Supported algorithms: md5, sha1, sha256")
        sys.exit(1)

    hash_input = sys.argv[1]
    wordlist = sys.argv[2]
    algo = sys.argv[3].lower()

    crack_hash(hash_input, wordlist, algo)
