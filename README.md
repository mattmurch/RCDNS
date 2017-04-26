# RCDNS

## DNS Server basics

* Our local machine looks inside the /etc/resolv.conf file to get the IP
  of the nameserver
* Whenever we lookup an IP, it queries the nameserve for resolution
* The query is sent to the port 53 of the nameserver as UDP packets
* Command line utilities to help learn about DNS lookups: dig, tcpdump,
  whois
* The nameserver does something called the Recursive lookup, where it
  splits the entire hostname based on the dots and recursively query
different servers for right hits
* Command line utilities to help learn about DNS lookups: dig, tcpdump, whois

* The structure of a DNS message:
    Header/Question/Answer/Authority/Additional stuff
