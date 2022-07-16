### Common Linux Privesc

IP address 10.10.156.22

user3:password

hostname: polobox

8 users

4 shells

/etc/passwd is rw-

### Finding SUID Binaries

We already know that there is SUID capable files on the system, thanks to our LinEnum scan. However, if we want to do this manually we can
use the command: *find / -perm -u=s -type f 2>/dev/null* to search the file system for SUID/GUID files.
