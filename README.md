# Subdomain/IP Finder
This is a simple script in charge of finding the subdomains of a giving domain.

- Enter a domain without `http` or `https` like this `apple.com`
- The script then iterates over the `subdomains.txt` content and uses requests to try and verify if a giving subdomain exists
- If it exists is saved to `discovered_subdomains.txt` file (if doesnt exists it will be created)
- It then uses `socket` to get the IP of the found subdomains and save the IP's to the `ips.txt` file

# Start the script
To start the script just clone this repository, enter the folder and then `pipenv shell`, once the virtualenv is done starting `pip install` this is just gonna install the requests library
