"""
Purpose: Creates global variables
"""

import datetime


def init(startDt, outputNm, exit, runLocally):
    """Creates global variables: startDate, outputName, exitSys, runLocal"""
    global startDate
    startDate = startDt
    auto_log.write(str(datetime.datetime.now()) + ' INFO: Global variable startDate set as ' + str(startDate) + '\n')
    global outputName
    outputName = outputNm
    auto_log.write(str(datetime.datetime.now()) + ' INFO: Global variable outputName set as ' + outputName + '\n')
    global exitSys
    exitSys = exit
    auto_log.write(str(datetime.datetime.now()) + ' INFO: Global variable exitSys set as ' + str(exitSys) + '\n')
    global runLocally
    runLocally = runLocal
    auto_log.write(str(datetime.datetime.now()) + ' INFO: Global variable runLocally set as ' + runLocally + '\n')
