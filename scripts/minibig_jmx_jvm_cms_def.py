import minibig_jmx_engine as mje

def get_marksweep(jsonbeansdata,hostsource,epoch_time):
	pointer_id = mje.get_metricscategory_position(jsonbeansdata, 'java.lang:type=GarbageCollector,name=ConcurrentMarkSweep')
	try:
		print hostsource+" marksweep_CollectionCount "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('CollectionCount'))
		print hostsource+" marksweep_CollectionTime "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('CollectionTime'))
		print hostsource+" marksweep_lastgcinfo_GcThreadCount "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo'].get('GcThreadCount'))
		print hostsource+" marksweep_lastgcinfo_duration "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo'].get('duration'))
		print hostsource+" marksweep_lastgcinfo_endTime "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo'].get('endTime'))
		print hostsource+" marksweep_lastgcinfo_id "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo'].get('id'))
		print hostsource+" marksweep_lastgcinfo_startTime "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo'].get('startTime'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageAfterGc_perm_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][0]['value'].get('committed'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageAfterGc_perm_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][0]['value'].get('init'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageAfterGc_perm_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][0]['value'].get('max'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageAfterGc_perm_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][0]['value'].get('used'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageAfterGc_eden_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][1]['value'].get('committed'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageAfterGc_eden_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][1]['value'].get('init'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageAfterGc_eden_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][1]['value'].get('max'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageAfterGc_eden_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][1]['value'].get('used'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageAfterGc_codecache_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][2]['value'].get('committed'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageAfterGc_codecache_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][2]['value'].get('init'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageAfterGc_codecache_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][2]['value'].get('max'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageAfterGc_codecache_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][2]['value'].get('used'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageAfterGc_survivor_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][3]['value'].get('committed'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageAfterGc_survivor_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][3]['value'].get('init'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageAfterGc_survivor_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][3]['value'].get('max'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageAfterGc_survivor_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][3]['value'].get('used'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageAfterGc_oldgen_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][4]['value'].get('committed'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageAfterGc_oldgen_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][4]['value'].get('init'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageAfterGc_oldgen_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][4]['value'].get('max'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageAfterGc_oldgen_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][4]['value'].get('used'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageBeforeGc_perm_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][0]['value'].get('committed'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageBeforeGc_perm_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][0]['value'].get('init'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageBeforeGc_perm_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][0]['value'].get('max'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageBeforeGc_perm_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][0]['value'].get('used'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageBeforeGc_eden_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][1]['value'].get('committed'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageBeforeGc_eden_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][1]['value'].get('init'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageBeforeGc_eden_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][1]['value'].get('max'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageBeforeGc_eden_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][1]['value'].get('used'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageBeforeGc_codecache_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][2]['value'].get('committed'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageBeforeGc_codecache_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][2]['value'].get('init'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageBeforeGc_codecache_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][2]['value'].get('max'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageBeforeGc_codecache_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][2]['value'].get('used'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageBeforeGc_survivor_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][3]['value'].get('committed'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageBeforeGc_survivor_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][3]['value'].get('init'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageBeforeGc_survivor_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][3]['value'].get('max'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageBeforeGc_survivor_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][3]['value'].get('used'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageBeforeGc_oldgen_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][4]['value'].get('committed'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageBeforeGc_oldgen_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][4]['value'].get('init'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageBeforeGc_oldgen_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][4]['value'].get('max'))
		print hostsource+" marksweep_lastgcinfo_memoryUsageBeforeGc_oldgen_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][4]['value'].get('used'))
	except AttributeError:
		missingdata=1
	else:
		missingdata=1

def get_eden(jsonbeansdata,hostsource,epoch_time):
	pointer_id = mje.get_metricscategory_position(jsonbeansdata, 'java.lang:type=MemoryPool,name=Par Eden Space')
	try:
		print hostsource+" eden_usage_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['Usage'].get('committed'))
		print hostsource+" eden_usage_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['Usage'].get('init'))
		print hostsource+" eden_usage_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['Usage'].get('max'))
		print hostsource+" eden_usage_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['Usage'].get('used'))
		print hostsource+" eden_peakusage_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['PeakUsage'].get('committed'))
		print hostsource+" eden_peakusage_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['PeakUsage'].get('init'))
		print hostsource+" eden_peakusage_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['PeakUsage'].get('max'))
		print hostsource+" eden_peakusage_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['PeakUsage'].get('used'))
		print hostsource+" eden_collectionusage_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['CollectionUsage'].get('committed'))
		print hostsource+" eden_collectionusage_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['CollectionUsage'].get('init'))
		print hostsource+" eden_collectionusage_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['CollectionUsage'].get('max'))
		print hostsource+" eden_collectionusage_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['CollectionUsage'].get('used'))
	except AttributeError:
		missingdata=1
	else:
		missingdata=1

def get_perm(jsonbeansdata,hostsource,epoch_time):
	pointer_id = mje.get_metricscategory_position(jsonbeansdata, 'java.lang:type=MemoryPool,name=Par Eden Space')
	try:
		print hostsource+" perm_usage_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['Usage'].get('committed'))
		print hostsource+" perm_usage_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['Usage'].get('init'))
		print hostsource+" perm_usage_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['Usage'].get('max'))
		print hostsource+" perm_usage_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['Usage'].get('used'))
		print hostsource+" perm_peakusage_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['PeakUsage'].get('committed'))
		print hostsource+" perm_peakusage_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['PeakUsage'].get('init'))
		print hostsource+" perm_peakusage_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['PeakUsage'].get('max'))
		print hostsource+" perm_peakusage_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['PeakUsage'].get('used'))
		print hostsource+" perm_collectionusage_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['CollectionUsage'].get('committed'))
		print hostsource+" perm_collectionusage_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['CollectionUsage'].get('init'))
		print hostsource+" perm_collectionusage_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['CollectionUsage'].get('max'))
		print hostsource+" perm_collectionusage_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['CollectionUsage'].get('used'))
	except AttributeError:
		missingdata=1
	else:
		missingdata=1
	
def get_survivor(jsonbeansdata,hostsource,epoch_time):
	pointer_id = mje.get_metricscategory_position(jsonbeansdata, 'java.lang:type=MemoryPool,name=Par Survivor Space')
	try:
		print hostsource+" survivor_usage_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['Usage'].get('committed'))
		print hostsource+" survivor_usage_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['Usage'].get('init'))
		print hostsource+" survivor_usage_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['Usage'].get('max'))
		print hostsource+" survivor_usage_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['Usage'].get('used'))
		print hostsource+" survivor_peakusage_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['PeakUsage'].get('committed'))
		print hostsource+" survivor_peakusage_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['PeakUsage'].get('init'))
		print hostsource+" survivor_peakusage_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['PeakUsage'].get('max'))
		print hostsource+" survivor_peakusage_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['PeakUsage'].get('used'))
		print hostsource+" survivor_collectionusage_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['CollectionUsage'].get('committed'))
		print hostsource+" survivor_collectionusage_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['CollectionUsage'].get('init'))
		print hostsource+" survivor_collectionusage_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['CollectionUsage'].get('max'))
		print hostsource+" survivor_collectionusage_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['CollectionUsage'].get('used'))
	except AttributeError:
		missingdata=1
	else:
		missingdata=1

def get_oldgen(jsonbeansdata,hostsource,epoch_time):
	pointer_id = mje.get_metricscategory_position(jsonbeansdata, 'java.lang:type=MemoryPool,name=CMS Old Gen')
	try:
		print hostsource+" oldgen_usage_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['Usage'].get('committed'))
		print hostsource+" oldgen_usage_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['Usage'].get('init'))
		print hostsource+" oldgen_usage_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['Usage'].get('max'))
		print hostsource+" oldgen_usage_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['Usage'].get('used'))
		print hostsource+" oldgen_peakusage_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['PeakUsage'].get('committed'))
		print hostsource+" oldgen_peakusage_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['PeakUsage'].get('init'))
		print hostsource+" oldgen_peakusage_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['PeakUsage'].get('max'))
		print hostsource+" oldgen_peakusage_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['PeakUsage'].get('used'))
		print hostsource+" oldgen_collectionusage_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['CollectionUsage'].get('committed'))
		print hostsource+" oldgen_collectionusage_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['CollectionUsage'].get('init'))
		print hostsource+" oldgen_collectionusage_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['CollectionUsage'].get('max'))
		print hostsource+" oldgen_collectionusage_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['CollectionUsage'].get('used'))
	except AttributeError:
		missingdata=1
	else:
		missingdata=1

def get_codecache(jsonbeansdata,hostsource,epoch_time):
	pointer_id = mje.get_metricscategory_position(jsonbeansdata, 'java.lang:type=MemoryPool,name=Code Cache')
	try:
		print hostsource+" codecache_usage_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['Usage'].get('committed'))
		print hostsource+" codecache_usage_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['Usage'].get('init'))
		print hostsource+" codecache_usage_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['Usage'].get('max'))
		print hostsource+" codecache_usage_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['Usage'].get('used'))
		print hostsource+" codecache_peakusage_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['PeakUsage'].get('committed'))
		print hostsource+" codecache_peakusage_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['PeakUsage'].get('init'))
		print hostsource+" codecache_peakusage_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['PeakUsage'].get('max'))
		print hostsource+" codecache_peakusage_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['PeakUsage'].get('used'))
	except AttributeError:
		missingdata=1
	else:
		missingdata=1

def get_new(jsonbeansdata,hostsource,epoch_time):
	pointer_id = mje.get_metricscategory_position(jsonbeansdata, 'java.lang:type=GarbageCollector,name=ParNew')
	try:
		print hostsource+" new_CollectionCount "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('CollectionCount'))
		print hostsource+" new_CollectionTime "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id].get('CollectionTime'))
		print hostsource+" new_lastgcinfo_memoryUsageAfterGc_perm_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][0]['value'].get('committed'))
		print hostsource+" new_lastgcinfo_memoryUsageAfterGc_perm_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][0]['value'].get('init'))
		print hostsource+" new_lastgcinfo_memoryUsageAfterGc_perm_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][0]['value'].get('max'))
		print hostsource+" new_lastgcinfo_memoryUsageAfterGc_perm_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][0]['value'].get('used'))
		print hostsource+" new_lastgcinfo_memoryUsageAfterGc_eden_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][1]['value'].get('committed'))
		print hostsource+" new_lastgcinfo_memoryUsageAfterGc_eden_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][1]['value'].get('init'))
		print hostsource+" new_lastgcinfo_memoryUsageAfterGc_eden_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][1]['value'].get('max'))
		print hostsource+" new_lastgcinfo_memoryUsageAfterGc_eden_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][1]['value'].get('used'))
		print hostsource+" new_lastgcinfo_memoryUsageAfterGc_codecache_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][2]['value'].get('committed'))
		print hostsource+" new_lastgcinfo_memoryUsageAfterGc_codecache_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][2]['value'].get('init'))
		print hostsource+" new_lastgcinfo_memoryUsageAfterGc_codecache_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][2]['value'].get('max'))
		print hostsource+" new_lastgcinfo_memoryUsageAfterGc_codecache_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][2]['value'].get('used'))
		print hostsource+" new_lastgcinfo_memoryUsageAfterGc_survivor_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][3]['value'].get('committed'))
		print hostsource+" new_lastgcinfo_memoryUsageAfterGc_survivor_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][3]['value'].get('init'))
		print hostsource+" new_lastgcinfo_memoryUsageAfterGc_survivor_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][3]['value'].get('max'))
		print hostsource+" new_lastgcinfo_memoryUsageAfterGc_survivor_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][3]['value'].get('used'))
		print hostsource+" new_lastgcinfo_memoryUsageAfterGc_oldgen_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][4]['value'].get('committed'))
		print hostsource+" new_lastgcinfo_memoryUsageAfterGc_oldgen_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][4]['value'].get('init'))
		print hostsource+" new_lastgcinfo_memoryUsageAfterGc_oldgen_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][4]['value'].get('max'))
		print hostsource+" new_lastgcinfo_memoryUsageAfterGc_oldgen_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageAfterGc'][4]['value'].get('used'))
		print hostsource+" new_lastgcinfo_memoryUsageBeforeGc_perm_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][0]['value'].get('committed'))
		print hostsource+" new_lastgcinfo_memoryUsageBeforeGc_perm_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][0]['value'].get('init'))
		print hostsource+" new_lastgcinfo_memoryUsageBeforeGc_perm_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][0]['value'].get('max'))
		print hostsource+" new_lastgcinfo_memoryUsageBeforeGc_perm_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][0]['value'].get('used'))
		print hostsource+" new_lastgcinfo_memoryUsageBeforeGc_eden_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][1]['value'].get('committed'))
		print hostsource+" new_lastgcinfo_memoryUsageBeforeGc_eden_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][1]['value'].get('init'))
		print hostsource+" new_lastgcinfo_memoryUsageBeforeGc_eden_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][1]['value'].get('max'))
		print hostsource+" new_lastgcinfo_memoryUsageBeforeGc_eden_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][1]['value'].get('used'))
		print hostsource+" new_lastgcinfo_memoryUsageBeforeGc_codecache_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][2]['value'].get('committed'))
		print hostsource+" new_lastgcinfo_memoryUsageBeforeGc_codecache_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][2]['value'].get('init'))
		print hostsource+" new_lastgcinfo_memoryUsageBeforeGc_codecache_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][2]['value'].get('max'))
		print hostsource+" new_lastgcinfo_memoryUsageBeforeGc_codecache_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][2]['value'].get('used'))
		print hostsource+" new_lastgcinfo_memoryUsageBeforeGc_survivor_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][3]['value'].get('committed'))
		print hostsource+" new_lastgcinfo_memoryUsageBeforeGc_survivor_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][3]['value'].get('init'))
		print hostsource+" new_lastgcinfo_memoryUsageBeforeGc_survivor_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][3]['value'].get('max'))
		print hostsource+" new_lastgcinfo_memoryUsageBeforeGc_survivor_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][3]['value'].get('used'))
		print hostsource+" new_lastgcinfo_memoryUsageBeforeGc_oldgen_committed "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][4]['value'].get('committed'))
		print hostsource+" new_lastgcinfo_memoryUsageBeforeGc_oldgen_init "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][4]['value'].get('init'))
		print hostsource+" new_lastgcinfo_memoryUsageBeforeGc_oldgen_max "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][4]['value'].get('max'))
		print hostsource+" new_lastgcinfo_memoryUsageBeforeGc_oldgen_used "+str(epoch_time)+" "+str(jsonbeansdata[pointer_id]['LastGcInfo']['memoryUsageBeforeGc'][4]['value'].get('used'))
	except AttributeError:
		missingdata=1
	else:
		missingdata=1
