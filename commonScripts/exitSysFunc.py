"""
Purpose: Exits system if there are errors
"""

import datetime


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
        end = datetime.datetime.now()

        auto_log.write(str(datetime.datetime.now()) + " INFO: End time = " + str(end) + "\n")
        print("End time: "+str(end)+"\n")

        # Get the time elapsed and convert it to seconds
        elapsedTimeSecsOG = (end - globalVars.startDate).seconds

        # Get the number of whole hours elapsed
        elapsedTimeHours = elapsedTimeSecsOG // 3600

        # Subtract the number of whole hours, get the number of whole minutes elapsed
        elapsedTimeMins = (elapsedTimeSecsOG % 3600) // 60

        # Get the number of seconds passed after subtracting the whole number of hours and minutes
        elapsedTimeSecs = elapsedTimeSecsOG % 60

        runTimeStr = "Run time: " + str(elapsedTimeHours) + " hours, " + str(elapsedTimeMins) + " mins, and " + str(elapsedTimeSecs) + " secs\n"
        auto_log.write(str(datetime.datetime.now()) + " INFO: Run Time = " + runTimeStr)
        print("Run Time = " + runTimeStr)
        auto_log.close()
