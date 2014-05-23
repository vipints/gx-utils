#!/bin/bash 
# 
# Can interact with the Galaxy server instance 
# 
# Usage
#
# $ bash server-daemon.sh start|stop|restart 
# 

# Make sure that below path point to your Galaxy installation 
GALAXY_ROOT_DIR=`pwd`

# check the input arguments 
if [ $# -eq 0 ] ; then
    echo 'Please mention the service operation like start|stop|restart'
    exit 1 
fi 
#
# check the run.sh file in GALAXY_ROOT_DIR 
if [ ! -f run.sh ] ; then
    echo 'No run.sh file here. Please check the GALAXY_ROOT_DIR'
    exit 1 
fi 
# 
# check the universe.ini file for Galaxy service 
if [ ! -f universe_wsgi.ini ]; then  
    echo 'No universe_wsgi.ini Galaxy configuration file here. Please check the GALAXY_ROOT_DIR'
    exit 1 
fi 
#
# do the operations
if [ "$1" == "start" ] ; then
    echo Starting the Galaxy Server 
    bash $GALAXY_ROOT_DIR/run.sh --daemon --log-file=$GALAXY_ROOT_DIR/galaxy_instance_run.log 

elif [ "$1" == "stop" ] ; then 
    echo Stopping the Galaxy Server 
    bash $GALAXY_ROOT_DIR/run.sh --stop-daemon 

elif [ "$1" == "restart" ] ; then 
    echo Restarting the Galaxy Server 
    bash $GALAXY_ROOT_DIR/run.sh --stop-daemon 
    bash $GALAXY_ROOT_DIR/run.sh --daemon --log-file=$GALAXY_ROOT_DIR/galaxy_instance_run.log 
fi 
#
echo DONE
