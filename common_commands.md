### Initial Scans
nmap -sC -sV -oA nmap/initial 'IP"
nmap -p- -oA nmap/allports 'IP'
gobuster dir -u 'IP or website'  -w /usr/share/wordlists/directory-list-2.3-medium.txt -o gobuster_scan.txt
enum4linux -A 'IP'




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



