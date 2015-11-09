def get_memory(jsonbeansdata,hostsource,epoch_time):
    #Get the pointer id (just in case that the json order had changes)
    pointer_id = get_metricscategory_position(jsonbeansdata, 'java.lang:type=Memory')
    print hostsource+" heap_usage_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['HeapMemoryUsage'].get('committed'))
    print hostsource+" heap_usage_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['HeapMemoryUsage'].get('init'))
    print hostsource+" heap_usage_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['HeapMemoryUsage'].get('max'))
    print hostsource+" heap_usage_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['HeapMemoryUsage'].get('used'))
    print hostsource+" nonheap_usage_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['NonHeapMemoryUsage'].get('committed'))
    print hostsource+" nonheap_usage_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['NonHeapMemoryUsage'].get('init'))
    print hostsource+" nonheap_usage_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['NonHeapMemoryUsage'].get('max'))
    print hostsource+" nonheap_usage_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['NonHeapMemoryUsage'].get('used'))

def get_bufferpool(jsonbeansdata,hostsource,epoch_time):
    pointer_id = get_metricscategory_position(jsonbeansdata, 'java.nio:type=BufferPool,name=mapped')
    print hostsource+" bufferpool_TotalCapacity "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('TotalCapacity'))
    print hostsource+" bufferpool_MemoryUsed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('MemoryUsed'))
    print hostsource+" bufferpool_Count "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('Count'))

def get_compilation(jsonbeansdata,hostsource,epoch_time):
    pointer_id = get_metricscategory_position(jsonbeansdata, 'java.lang:type=Compilation')
    print hostsource+" compilation_TotalCompilationTime "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('TotalCompilationTime'))

def get_os(jsonbeansdata,hostsource,epoch_time):
    pointer_id = get_metricscategory_position(jsonbeansdata, 'java.lang:type=OperatingSystem')
    print hostsource+" os_OpenFileDescriptorCount "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('OpenFileDescriptorCount'))
    print hostsource+" os_MaxFileDescriptorCount "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('MaxFileDescriptorCount'))
    print hostsource+" os_CommittedVirtualMemorySize "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('CommittedVirtualMemorySize'))
    print hostsource+" os_TotalSwapSpaceSize "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('TotalSwapSpaceSize'))
    print hostsource+" os_FreeSwapSpaceSize "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('FreeSwapSpaceSize'))
    print hostsource+" os_ProcessCpuTime "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('ProcessCpuTime'))
    print hostsource+" os_FreePhysicalMemorySize "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('FreePhysicalMemorySize'))
    print hostsource+" os_TotalPhysicalMemorySize "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('TotalPhysicalMemorySize'))
    print hostsource+" os_SystemCpuLoad "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('SystemCpuLoad'))
    print hostsource+" os_ProcessCpuLoad "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('ProcessCpuLoad'))
    print hostsource+" os_SystemLoadAverage "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('SystemLoadAverage'))
    print hostsource+" os_AvailableProcessors "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('AvailableProcessors'))

def get_rs_threading(xbeans,hostsource,epoch_time):
    rs_treading_pointer_id = get_metricscategory_position(xbeans, 'java.lang:type=Threading')
    print hostsource+" rs_threading_ThreadCount "+str(epoch_time)+" "+str(xbeans[rs_treading_pointer_id].get('ThreadCount'))
    print hostsource+" rs_threading_TotalStartedThreadCount "+str(epoch_time)+" "+str(xbeans[rs_treading_pointer_id].get('TotalStartedThreadCount'))
    print hostsource+" rs_threading_CurrentThreadCpuTime "+str(epoch_time)+" "+str(xbeans[rs_treading_pointer_id].get('CurrentThreadCpuTime'))
    print hostsource+" rs_threading_CurrentThreadUserTime "+str(epoch_time)+" "+str(xbeans[rs_treading_pointer_id].get('CurrentThreadUserTime'))
    print hostsource+" rs_threading_PeakThreadCount "+str(epoch_time)+" "+str(xbeans[rs_treading_pointer_id].get('PeakThreadCount'))
    print hostsource+" rs_threading_DaemonThreadCount "+str(epoch_time)+" "+str(xbeans[rs_treading_pointer_id].get('DaemonThreadCount'))
