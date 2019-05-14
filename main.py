"""
Purpose: This script drives automation execution.
"""
####################
#	IMPORT
####################

import argparse
import boto3
import datetime
import os
import subprocess
import sys
from shutil import copy

import commonScripts
from commonScripts.exitSysFunc import exitSysFunc

# Set exit system var to 0
exitSys = 0


####################
#	OUTPUT FOLDERS
####################

# Generate unique output folder name based on datetime
dt = datetime.datetime.now()
if dt.month < 10:
    mth = "0" + str(dt.month)
else:
    mth = str(dt.month)

if dt.day < 10:
    dy = "0" + str(dt.day)
else:
    dy = str(dt.day)

if dt.hour < 10:
    hr = "0" + str(dt.hour)
else:
    hr = str(dt.hour)

if dt.minute < 10:
    min = "0" + str(dt.minute)
else:
    min = str(dt.minute)

if dt.second < 10:
    sec = "0" + str(dt.second)
else:
    sec = str(dt.second)

outputName = 'AUTO-' + str(dt.year) + mth + dy + hr + min + sec

# Clear all previous output files
try:
    os.remove('./output/'+outputName)
except OSError:
    pass


####################
#	LOGS
####################

# Create the output directory and logs, print errors
logName = './executionLogs/' + outputName + '/automation-logs/AUTO.log'
logLoc = './executionLogs/' + outputName + '/logs/'

if not os.path.exists(os.path.dirname(logName)):
    try:
        os.makedirs(os.path.dirname(logName))
    except:
        print("ERROR: Issue creating the output directory, log directories, or log file\n")
        exit()

# Record start of an automation run
l = open(logName, 'w')
l.write('*****************************************************************************************\n')
l.write('*****************************************************************************************\n')
l.write('\n')
l.write("~ Let the automation begin! ~\n")
l.write('\n')
l.write('*****************************************************************************************\n')
l.write('*****************************************************************************************\n')

# Record automation start time and folder and directory names
print('Start time: ' + str(dt) + '\n')
l.write('Start time: ' + str(dt) + '\n\n')
l.write(str(datetime.datetime.now()) + ' INFO: Unique output folder name is ' + outputName + '\n')
print('INFO: Unique output folder name is ' + outputName)

# Create input folder for data sets
folder = './executionLogs/' + outputName + '/input/'
if not os.path.exists(os.path.dirname(folder)):
    try:
        l.write(str(datetime.datetime.now()) + ' INFO: Create ' + folder + '\n')
        os.makedirs(os.path.dirname(folder))
        l.write(str(datetime.datetime.now()) + ' INFO: Create ' + folder + 'dataFiles/\n')
        os.makedirs(os.path.dirname(folder+'dataFiles/'))
    except:
        l.write(str(datetime.datetime.now()) + ' ERROR: Creating a folder in the ' + folder + '\n')
        print('ERROR: Issue creating a folder in the ' + folder + '\n')
        exit()

# Create output forlder for each automation run
folder = './executionLogs/' + outputName + '/output/'
if not os.path.exists(os.path.dirname(folder)):
    try:
        l.write(str(datetime.datetime.now()) + ' INFO: Create ' + folder + '\n')
        os.makedirs(os.path.dirname(folder))
    except:
        l.write(str(datetime.datetime.now()) + ' ERROR: Creating ' + folder + '\n')
        print('ERROR: Issue creating ' + folder + '\n')
        exit()
