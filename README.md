# Requirements
Python Version: `3.9`
Pipenv

# Subdomain/IP Finder
This is a simple script in charge of finding the subdomains of a giving domain.

- Enter a domain without `http` or `https` like this `apple.com`
- The script then iterates over the `subdomains.txt` content and uses requests to try and verify if a giving subdomain exists
- If it exists is saved to `discovered_subdomains.txt` file (if doesnt exists it will be created)
- It then uses `socket` to get the IP of the found subdomains and save the IP's to the `ips.txt` file
-

# Start the script
To start the script just clone this repository, enter the folder and then `pipenv shell`, once the virtualenv is done starting `pipenv install`, this will use the `Pipfile.lock` to install the required packages for the script to work. After this just run:

```
python main.py
```

This will run the script and generate the files with the discovered subdomains and ip's
