import argparse
import requests
from urllib.parse import urljoin

def scan_directories(base_url, wordlist, extension=None):
    found_dirs = []
    
    for word in wordlist:
        if extension:
            word = f"{word}.{extension}"
        url = urljoin(base_url, word)
        
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"[+] Found: {url}")
                found_dirs.append(url)
        except requests.RequestException as e:
            print(f"[!] Error scanning {url}: {e}")
    
    return found_dirs

def main():
    parser = argparse.ArgumentParser(description="Simple Directory Scanner")
    parser.add_argument("url", help="Base URL to scan")
    parser.add_argument("wordlist", help="Path to the wordlist file")
    parser.add_argument("-e", "--extension", help="Add a file extension to each word (e.g., 'html')")
    
    args = parser.parse_args()
    
    try:
        with open(args.wordlist, 'r') as f:
            wordlist = [line.strip() for line in f]
    except FileNotFoundError:
        print(f"Error: Wordlist file '{args.wordlist}' not found.")
        return
    
    print(f"Scanning {args.url} with {len(wordlist)} words...")
    found = scan_directories(args.url, wordlist, args.extension)
    
    print(f"\nScan complete. Found {len(found)} directories/files.")

if __name__ == "__main__":
    main()