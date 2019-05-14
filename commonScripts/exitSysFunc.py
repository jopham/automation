"""
Purpose: Exits system if there are errors
"""
####################
#	IMPORT
####################

import datetime

####################
#	EXIT FUNCTION
####################
def exitSysFunc(auto_log):
    """Exits system if there are errors"""
    auto_log.write(str(datetime.datetime.now()) + " INFO: Check exitSys flag\n")
    auto_log.write(str(datetime.datetime.now()) + " INFO: exitSys flag = " + str(globalVars.exitSys) + "\n")
    if globalVars.exitSys == 1:
        if globalVars.runLocally == "1":
            try:
                auto_log.write(str(datetime.datetime.now()) + ' INFO: Running locally, get AWS Keys\n')
                expAwsKeyTime, exitSys = get_awskeytemp(l)
            except:
                auto_log.write(str(datetime.datetime.now()) + ' ERROR: Cannot get aws key\n')
                auto_log.write(str(datetime.datetime.now()) + ' ERROR: This is required, exiting system\n')
