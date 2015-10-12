#!/bin/bash 
#
# Program to delete the unfinished or broken jobs 
# 
# check the input arguments 
if [ $# -eq 0 ] ; then
    echo 'error: Please mention the Job ID to be deleted'
    echo 'Usage: cluster_job_del.sh <JOB_ID>'
    exit 1 
fi 

# check the job number
JOB_NUM='^[0-9]+$' 
if ! [[ ${1} =~ $JOB_NUM ]] ; then 
    echo 'error: Job ID NOT a number'
    exit 1 
fi

# get the job id
JOB_NUM_START=${1}
shift 

# check is there a second argument 
if [ "$1" = "" ]; then
    JOB_NUM_STOP=${JOB_NUM_START}
else 
    if ! [[ ${1} =~ $JOB_NUM ]] ; then 
        echo 'error: Job ID NOT a number'
        exit 1 
    fi
    JOB_NUM_STOP=${1}
fi     

# check the job range 
if ! [[ "${JOB_NUM_STOP}" -ge ${JOB_NUM_START} ]] ; then 
    echo error: Range value should be in ascending order $JOB_NUM_START $JOB_NUM_STOP
    exit 1 
fi 

# delete the jobs
for JOB_ID in `seq ${JOB_NUM_START} 1 ${JOB_NUM_STOP}`
do 
    echo deleting job $JOB_ID
    qdel $JOB_ID ## depends on the job scheduler the deleting function will be different
done 

