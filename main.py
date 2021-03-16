from concurrent.futures.thread import ThreadPoolExecutor
import requests
import time
import socket

print('Enter the main url - like example.com:')
domain = input()
discovered_subdomains = []

print('Running script...')
# init the status bar

def get_subdomains(subdomain):
    url = f"https://{subdomain}.{domain}"
    try:
        res = requests.get(url)
        if res.status_code != 404:
            print(f'{url} subdomain discovered!!')
            discovered_subdomains.append(url)
            save_subdomains(url)
    except requests.ConnectionError:
        pass

def save_subdomains(subdomain):
    with open('discovered_subdomains.txt', 'w') as f:
        print(subdomain, file=f)

def save_ips(subomains):
    print('Getting and saving ips...')
    with open('ips.txt', 'w') as f:
        for subdomain in subomains:
            ip = socket.gethostbyname(subdomain.split('https://')[1])
            print(f'{ip} for {subdomain} saved sucessfully!')
            print(ip, file=f)
    
def main():
    print('Multithread starting...\n')
    with ThreadPoolExecutor() as executor:
        subdomains_db = open('subdomains.txt')
        subdomains_db_content = subdomains_db.read()
        subdomains = subdomains_db_content.splitlines()
        for subdomain in subdomains:
            executor.submit(get_subdomains, subdomain)
    print(f'{len(discovered_subdomains)} found in {domain} in {time.perf_counter()}')
    save_ips(discovered_subdomains)

if __name__ == '__main__':
    main()

