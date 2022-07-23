### Initial Scans

nmap -sC -sV -oA nmap/initial 'IP"
nmap -p- -oA nmap/allports 'IP'
nmap -A -p 'open port' 'IP'

gobuster dir -u 'IP or website'  -w /usr/share/wordlists/directory-list-2.3-medium.txt -o gobuster_scan.txt
enum4linux -a 'IP'

### Hydra

hydra -t 4 -l 'Username' -P 'wordlist' -vV 'IP' ftp

### SQL

' " AND 1 -- -

### SMB

smbclient //IP/ username -U password -p PORT
smbclient //IP/ Anonymous -U -p PORT     (use this to see if Anonymous access is allowed / may need to see what directory is available for SMB)

### Manual

-uname -a
-find /-perm -4000 -ls 2>/dev/null
-ss -lntp (netstat -alntp)
-dpkg -l, rpm -qa
-find /-ls 2>/dev/null

### Scripts

LinEnum.sh
LinuxPrivChecker.py
Smnart Linux Enumeration
LinPEAS

### Favicon

curl 'IP'/favicon.ico | md5sum
must run with a known favicon
(search through <https://wiki.owasp.org/index.php/OWASP_favicon_database>)

### http Headers

curl "IP' -v

### ffuf

ffuf -w /usr/share/wordlists/seclists/Discovery/DNS/namelist.txt -H "Host: FUZZ.'header to call your shot'" -u 'IP' -fs 2395  
setting a file size will not show those results

ffuf -w /usr/share/wordlists/SecLists/Usernames/Names/names.txt -X POST -d "username=FUZZ&email=x&password=x&cpassword=x" -H "Content-Type: application/x-www-form-urlencoded" -u 'IP'/customers/signup -mr "username already exists"
enumerate usernames / assuming customers/signup

ffuf -w valid_usernames.txt:W1,/usr/share/wordlists/SecLists/Passwords/Common-Credentials/10-million-password-list-top-100.txt:W2 -X POST -d "username=W1&password=W2" -H "Content-Type: application/x-www-form-urlencoded" -u 'IP'/customers/login -fc 200
enumerate passwords / assuming customers/login

### dirb

dirb 'IP' /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
dirbuster is used to brute force directories and filenames on web/application servers

### gobuster

gobuster dir --url 'IP' -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
gobuster is used to brute force directories, filenames and DNS subdomains