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

ffuf -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -u 'IP'/FUZZ
fast word fuzzer

### dirb

dirb 'IP' /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
dirbuster is used to brute force directories and filenames on web/application servers

### gobuster

gobuster dir --url 'IP' -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
gobuster is used to brute force directories, filenames and DNS subdomains