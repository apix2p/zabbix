# MiniBIG zabbix collectors

It's a collection of templates and scripts (Python) to collect metrics from Big Data softwares components (Hadoop, Hbase, MongoDB, etc.)

The collector simply use the json documents provided by the software interfaces (using JMX). The script will format the json entries to send it on zabbix by using the zabbix_sender utility.

The zabbix item type is globally zabbix_trapper.


##Requirements

Zabbix 2.x server, agents, etc. well configured and running.
  
On the collector node (Zabbix server or proxy might be good) :  
- Python  
- zabbix_sender binary 



##Overview
Choose a node as the zabbix server of proxy server, to run the collecting scripts (Python). Why we suggest the server or proxy? It's to limit the FW opening constraint. Cause the scripts collectors will send the data to the server. It's a pushing mode and not a pulling mode. If you can't install it on server or proxy, it's not a big deal, but don't forget the FireWall if you have some. The scripts collectors will need to get access to the JMX/JSON URLs to your interfaces, so don't forget to put in place all necessary access (FW,auth,etc.).  
You'll need to autorised external scripts on the collectors nodes at the zabbix level.
It's a special item that triggers all metrics gathering. This item just collect the script run return code. 
This special item will run the python script, and this script will gather metrics and send the results by using zabbix_sender binary.
The zabbix templates need be imported and associated to each supervised nodes.

##Install

- Import templates (following your needs).  
- On the collectors nodes :  
  * Untar the package in the externalscripts zabbix directory (usually /usr/local/share/zabbix/externalscripts)  
  * Be sure that all collectors files owner and group are set to zabbix:zabbix. 
  * 
@TODO
		
##Limitations
The collectors scripts are probably not compatible with a secured environment. They don't take in account the possibility to provide a user/password to get access to a securised JMX/JSON interfaces. It's in the roadmap.

