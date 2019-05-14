"""
Purpose: Creates global variables
"""
####################
#	IMPORT
####################

import datetime


def init(startDt, outputNm, exit, runLocally):
    """Creates global variables: startDate, outputName, exitSys, runLocal"""
    global startDate
    startDate = startDt
    l.write(str(datetime.datetime.now()) + ' INFO: Global variable startDate set as ' + str(startDate) + '\n')
    global outputName
    outputName = outputNm
    l.write(str(datetime.datetime.now()) + ' INFO: Global variable outputName set as ' + outputName + '\n')
    global exitSys
    exitSys = exit
    l.write(str(datetime.datetime.now()) + ' INFO: Global variable exitSys set as ' + str(exitSys) + '\n')
    global runLocally
    runLocally = runLocal
    l.write(str(datetime.datetime.now()) + ' INFO: Global variable runLocally set as ' + runLocally + '\n')
