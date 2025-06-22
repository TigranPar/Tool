import requests
import sys


def enumerate_directories(base_url, wordlist):
    print(f"[~] Scanning: {base_url}\n")
    for word in wordlist:
        url = f"{base_url}/{word.strip()}"
        try:
            response = requests.get(url)
            if response.status_code in [200, 301, 403]:
                print(f"[+] Found: {url} (status {response.status_code})")
        except requests.exceptions.RequestException:
            continue


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 dir_enum.py <URL> <wordlist>")
        sys.exit(1)

    target_url = sys.argv[1].rstrip('/')
    wordlist_path = sys.argv[2]

    try:
        with open(wordlist_path, 'r') as file:
            words = file.readlines()
    except FileNotFoundError:
        print(f"[!] Wordlist not found: {wordlist_path}")
        sys.exit(1)

    enumerate_directories(target_url, words)
