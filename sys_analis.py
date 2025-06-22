import sys
from collections import Counter

def analyze_log(filepath, keywords=None):
    if keywords is None:
        keywords = ["error", "fail", "denied", "invalid", "sudo", "authentication"]

    keyword_counter = Counter()
    matching_lines = []

    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                for keyword in keywords:
                    if keyword.lower() in line.lower():
                        keyword_counter[keyword.lower()] += 1
                        matching_lines.append(line.strip())
                        break
    except FileNotFoundError:
        print(f"[!] File not found: {filepath}")
        sys.exit(1)

    print(f"\n[~] Log Analysis for {filepath}")
    print(f"[~] Found {len(matching_lines)} matching lines.\n")

    print("Top keyword matches:")
    for word, count in keyword_counter.most_common():
        print(f"  {word}: {count}")

    print("\nSample matching lines:\n")
    for line in matching_lines[:10]:
        print(f"  {line}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 log_analyzer.py <logfile>")
        sys.exit(1)

    log_file = sys.argv[1]
    analyze_log(log_file)
