# Tool
netscaner.py
	writing style: python3 netscaner.py ip 
	where ip is your target ip


dir_enum.py
	writing style: python3 dir_enum.py http://example.com wordlist.txt
	where wordlist.txt is just a text file where each line is one path/directory/file that the script will check on the server.	

Example contents of wordlist.txt

	admin
	login
	dashboard
	uploads
	config
	secret
	robots.txt
	backup


subdomain.py
	writing style: python3 subdomain_enum.py example.com subdomains.txt
	where subdomains.txt is a simple text file containing one potential subdomain per line that the script will try to resolve.

Example contents of subdomains.txt:
	
	www
	mail
	ftp
	dev
	test
	shop


ssh_brutforce.py 
	usage: python3 ssh_brutforce.py  <IP> <username> <password_list.txt>
	where password_list.txt is a simple text file containing one password per line that the script will try for the given username on the target SSH server.

Example contents of password_list.txt:

	123456
	password
	admin123
	letmein
	qwerty



hash_id.py  
	usage: python3 hash_id.py <hash>  
	where <hash> is a single hash string (e.g., MD5, SHA1, SHA256, etc.) that you want to identify.  
	The script will try to match the input against known hash patterns based on length and character set.

Example inputs:

	e99a18c428cb38d5f260853678922e03      → MD5 / NTLM / LM  
	5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8 → SHA1  
	cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e → SHA512  

log_analyzer.py
	usage: python3 log_analyzer.py <logfile>
	where <logfile> is a path to a system log file (e.g., /var/log/auth.log, /var/log/syslog)
	The script scans the log file for important keywords like "error", "fail", "denied", "sudo", and "authentication"
	and provides a summary of how many times these keywords appear along with sample matching lines.
