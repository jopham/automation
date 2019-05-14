####################
#	IMPORT
####################

import datetime


def init(reg, stack, tenant, acc, tenantIntId, outputNm, bucket, key, startDt, runLocal, exit, status, comment, l, awsExe='', awsProf='', emailAddr=''):
    global startDate
    startDate = startDt
    l.write(str(datetime.datetime.now()) + ' INFO: Global variable startDate set as ' + str(startDate) + '\n')
    global outputName
    outputName = outputNm
    l.write(str(datetime.datetime.now()) + ' INFO: Global variable outputName set as ' + outputName + '\n')
    global exitSys
    exitSys = exit
    l.write(str(datetime.datetime.now()) + ' INFO: Global variable exitSys set as ' + str(exitSys) + '\n')
