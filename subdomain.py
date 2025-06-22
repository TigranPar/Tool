import requests
import sys

def discover_subdomains(domain, wordlist):
    print(f"[~] Starting subdomain discovery on {domain}\n")
    for sub in wordlist:
        subdomain = f"http://{sub.strip()}.{domain}"
        try:
            response = requests.get(subdomain, timeout=2)
            if response.status_code < 400:
                print(f"[+] Found: {subdomain} (Status: {response.status_code})")
        except requests.RequestException:
            continue

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    domain = sys.argv[1]
    wordlist_path = sys.argv[2]

    try:
        with open(wordlist_path, 'r') as f:
            words = f.readlines()
    except FileNotFoundError:
        print(f"[!] Wordlist not found: {wordlist_path}")
        sys.exit(1)

    discover_subdomains(domain, words)
