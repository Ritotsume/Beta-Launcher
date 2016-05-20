	
#functions for luncher main


#read default values on startup for later use

import configparser
defaultsConfig = configparser.ConfigParser()
customConfig = configparser.ConfigParser()

#set the return value to 0 to make it behave like in installed mode or to 1 to start from anjuta

def anjuta():
	VALUE = False
	return VALUE

def readdefaults():

	if anjuta() == True:
		
		global defaultsConfig
		defaultsConfig.read('defaults.conf')
		
		
		global customConfig
		customConfig.read('settings.conf')		
	else:
		
		global defaultsConfig
		defaultsConfig.read('/etc/Beta-Launcher/defaults.conf')
		
		
		global customConfig
		customConfig.read('/etc/Beta-Launcher/settings.conf')

#_______________________________________________________________________________

def name():
	name = "Beta Launcher"
	return name 

def version():
	version = 0.1
#_______________________________________________________________________________

def readconf(option):
	
	global defaultsConfig
	global customConfig
	
	if not option in customConfig['main']:
		return defaultsConfig['main'][option]
	else:
		return customConfig['main'][option]

#_____________________________________________________________________________
#create new list which gets apended to file


def newdi(option, newinput):

	global customConfig

	#create new dict entry

	customConfig['main'][option]=str(newinput)
	


def writefile():
	global customConfig
	
	if anjuta() == True:
		confile = open("settings.conf", "w")
	else:
		confile = open("/etc/Beta-Launcher/settings.conf", "w")

	customConfig.write(confile)


	confile.close()

def termlength(command):
	length = len(command) + 1
	return length

def termcommand(command):
	final = command + '\n'
	return final
