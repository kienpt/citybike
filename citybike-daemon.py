import daemon
import time
import logging
from logging.handlers import TimedRotatingFileHandler
import libcitybike

def run():
	#Get configuration
	config = {}
	execfile("daemon.conf", config) 
	logfile = config["logfile"] + "." + config["network"]
	
	#Use pre_log to check duplication
	pre_log = ""
	with daemon.DaemonContext():
		#Set up logging
		logHandler = TimedRotatingFileHandler(logfile,when="D") #Create a new log daily
		logFormatter = logging.Formatter('%(asctime)s %(message)s')
		logHandler.setFormatter( logFormatter )
		logger = logging.getLogger( "CitiBikeLogger" )
		logger.addHandler( logHandler )
		logger.setLevel( logging.INFO )
		while True:
			try:
				cur_log = libcitybike.getStationStatus(config["network"])
				if cur_log != pre_log:
					logger.info(cur_log)
					pre_log = cur_log
		        	time.sleep(config["frequency"])
			except:
				logger.error("Unexpected Error")

if __name__ == "__main__":
	run()
