try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json
import sys
import getopt
import time

import minibig_jmx_engine as mje
import minibig_jmx_hbase_def as mjhbase
import minibig_jmx_hbase_master_def as mjhbm
import minibig_jmx_jvm_cms_def as mjjcms

def usage():
	print sys.argv[0],"-h[elp] -r[egion server name] -t[ime]"

def main():
	epoch_time = int(time.time())
	port = "60030"
	context = "/jmx"

	if len(sys.argv[1:]) < 1:
		usage()
		sys.exit(3)
	try:
		opts, args = getopt.getopt(sys.argv[1:], "htc:p:s:", ["help","time", "server="])
	except getopt.GetoptError as err:
		print str(err)
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		elif opt in ("-t"):
			epoch_time = int(time.time())
			print epoch_time
			sys.exit(1)
		elif opt in ("-s", "--server"):
			server = arg
		elif opt in ("-p", "--port"):
			port = arg
		elif opt in ("-c", "--context"):
			context = arg

	jsonbeansdata = mje.load_jmx("http://"+str(server)+":"+str(port)+str(context))

	mjhbase.get_ugi(jsonbeansdata,server,epoch_time)
	mjhbase.get_jvm(jsonbeansdata,server,epoch_time)
	mjhbase.get_hbsys(jsonbeansdata,server,epoch_time)
	mjhbase.get_ipc(jsonbeansdata,server,epoch_time)
	mjhbm.get_assignmentManger(jsonbeansdata,server,epoch_time)
	mjhbm.get_master(jsonbeansdata,server,epoch_time)
	mjjcms.get_marksweep(jsonbeansdata,server,epoch_time)
	mjjcms.get_eden(jsonbeansdata,server,epoch_time)
	mjjcms.get_perm(jsonbeansdata,server,epoch_time)
	mjjcms.get_survivor(jsonbeansdata,server,epoch_time)
	mjjcms.get_oldgen(jsonbeansdata,server,epoch_time)
	mjjcms.get_codecache(jsonbeansdata,server,epoch_time)
	mjjcms.get_new(jsonbeansdata,server,epoch_time)

if __name__ == "__main__":
    main()
