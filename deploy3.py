#!/u01/app/oracle/middleware/wl12c/oracle_common/common/bin/wlst.sh
print "connecting to weblogic domain"
connect('weblogic','weblogic1','t3://192.168.56.101:8001')
print "deploying the application"
deploy('timeoff','/u01/app/oracle/middleware/application/timeoff.war',targets='Cluster1')
disconnect()
exit()
