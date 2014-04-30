ip.dansysadm.com
================

What is powering `ip.dansysadm.com`

Why?
====

We had an issue today, when traffic from our crappy Telstra 4G router was showing different source IP's depending on the destination ports.
We started to use this to find out the ip's...

    $ curl ip.dansysadm.com
	{
	  "ip": "11.45.13.21"
	}

	$ curl ip.dansysadm.com:5000
	{
	  "ip": "58.17.13.21"
	}

json

	$ curl ip.dansysadm.com?json
	{
	  "ip": "58.17.13.21"
	}
	
yaml

	$ curl ip.dansysadm.com?yaml
	---
	ip: 1.2.3.4
	
plain, txt

	$ curl ip.dansysadm.com?{plain,txt,text}
	1.2.3.4
	
bash, zsh, ksh

	$ curl ip.dansysadm.com?{bash,zsh,ksh}
	IP=1.2.3.4


Getting started
===============

    $ sudo apt-get install python-pip git
	$ git clone git@github.com:daniellawrence/ip.dansysadm.com.git
	$ pip install -r requirements.txt
	$ cd ip.dansysadm.com
	$ ./main.py


Getting started production, lawls 
=================================

DON'T

    $ sudo apt-get install python-pip git nginx
	$ git clone git@github.com:daniellawrence/ip.dansysadm.com.git
	$ sudo pip install -r requirements.txt
	$ cd ip.dansysadm.com
	$ sudo cp ./main.py /usr/local/bin/
	$ sudo cp ./ip-upstart.conf /etc/init/ip.conf
	$ sudo cp ./ip-nginx.conf /etc/nginx/sites-enabled/ip.conf
	$ sudo start ip
	$ sudo start nginx
