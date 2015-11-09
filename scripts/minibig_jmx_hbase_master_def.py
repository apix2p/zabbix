import minibig_jmx_engine as mje

def get_assignmentManger(jsonbeansdata,hostsource,epoch_time):
    pointer_id = mje.get_metricscategory_position(jsonbeansdata, 'Hadoop:service=HBase,name=Master,sub=AssignmentManger')
    print hostsource+" assignmentManger_ritCount "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('ritCount'))
    print hostsource+" assignmentManger_ritOldestAge "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('ritOldestAge'))
    print hostsource+" assignmentManger_BulkAssign_num_ops "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('BulkAssign_num_ops'))
    print hostsource+" assignmentManger_BulkAssign_min "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('BulkAssign_min'))
    print hostsource+" assignmentManger_BulkAssign_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('BulkAssign_max'))
    print hostsource+" assignmentManger_BulkAssign_mean "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('BulkAssign_mean'))
    print hostsource+" assignmentManger_BulkAssign_median "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('BulkAssign_median'))
    print hostsource+" assignmentManger_Assign_num_ops "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('Assign_num_ops'))
    print hostsource+" assignmentManger_ritCountOverThreshold "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('ritCountOverThreshold'))

def get_master():
    pointer_id = mje.get_metricscategory_position(jsonbeansdata, 'Hadoop:service=HBase,name=Master,sub=Server')
    print hostsource+" master_averageLoad "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('averageLoad'))
    print hostsource+" master_numRegionServers "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('numRegionServers'))
    print hostsource+" master_numDeadRegionServers "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('numDeadRegionServers'))
    print hostsource+" master_clusterRequests "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('clusterRequests'))
    print hostsource+" master_masterStartTime "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('masterStartTime'))
    print hostsource+" master_masterActiveTime "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('masterActiveTime'))
