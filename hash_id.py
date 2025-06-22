import sys
import re

def identify_hash(hash_str):
    hash_patterns = {
        "MD5": r"^[a-fA-F0-9]{32}$",
        "SHA1": r"^[a-fA-F0-9]{40}$",
        "SHA224": r"^[a-fA-F0-9]{56}$",
        "SHA256": r"^[a-fA-F0-9]{64}$",
        "SHA384": r"^[a-fA-F0-9]{96}$",
        "SHA512": r"^[a-fA-F0-9]{128}$",
        "NTLM": r"^[a-fA-F0-9]{32}$",
        "LM": r"^[a-fA-F0-9]{32}$",
        "MySQL (old)": r"^[a-fA-F0-9]{16}$",
        "MySQL5+": r"^[a-fA-F0-9]{40}$"
    }

    print(f"\n[~] Analyzing: {hash_str}\n")

    found = False
    for name, pattern in hash_patterns.items():
        if re.fullmatch(pattern, hash_str):
            print(f"[+] Possible match: {name}")
            found = True

    if not found:
        print("[-] Unknown hash type or unsupported format.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    input_hash = sys.argv[1]
    identify_hash(input_hash)
