import os, sys

schemas = {}

schemas["BA"] = [("GMT","GMT time"),  ("RNC","name of RNC"),  ("VENDOR","RNC vendor"),  ("TECHNOLOGY","RNC technology"),  ("TMZ","RNC Time Zone"),  ("NDC","NDC"),  ("REGION","Region"),  ("EDMARKET","E.D. market"),  ("SUBMARKET","sub-market"),  ("DEVICE_TYPE","Device type (See Appendix A.)"),  ("ITEM_ID","Device item id"),  ("NETWORK_TYPE","network capability for device (3G, 2G, NA)"),  ("UL_CAT","UL category 1 (see appendix E)"),  ("DL_CAT","DL category 1 (see appendix D)"),  ("NET_ID","network indicator (N = ATT, R = roaming)"),  ("APN","name of APN"),  ("RAT_TYPE","network on which traffic was seen (0 = other, 1= 3G, 2 = 2G)"),  ("SERVICE_CATEGORY_ID","top level service category (See appendix B)"),  ("DOMAIN_ID","domain id from domains list (see appendix C)"),  ("UL_QOS","indicates throttling in uplink (see appendix F)"),  ("DL_QOS","indicates throttling in downlink (see appendix F)"),  ("DL_BYTES","downlink bytes"),  ("UL_BYTES","uplink bytes"),  ("DL_PKTS","downlink packets"),  ("UL_PKTS","uplink packets "),  ("DL_FLOW_CNT","downlink flow count"),  ("UL_FLOW_CNT","uplink flow count"),  ("UL_DATA_LENGTH","uplink data length (used for loss calculation)"),  ("UL_SEQ_RANGE","uplink sequence range (used for loss calculation)"),  ("DL_DATA_LENGTH","downlink data length (used for loss calculation)"),  ("DL_SEQ_RANGE","downlink sequence range (used for losscalculation)"),  ("DL_HTTP_200_CNT","count of downlink HTTP 200 codes (success)"),  ("DL_HTTP_300_CNT","count of downlink HTTP 300 codes (redirection)"),  ("DL_HTTP_400_CNT","count of downlink HTTP 400 codes (client error)"),  ("DL_HTTP_500_CNT","count of downlink HTTP 500 codes (server error)"),  ("DL_HTTP_OTHER_CNT","count of downlink HTTP other codes"),  ("DL_TCP_OUTOFORDER_CNT","count of out of order tcp packets (downlink)"),  ("UL_TCP_OUTOFORDER_CNT","count of out of order tcp packets (uplink)"),  ("DL_TCP_RETRANSMISSION_CNT","count of re-transmitted packets (downlink)"),  ("UL_TCP_RETRANSMISSION_CNT","count of re-transmitted packets (uplink)"),]


schemas["BS"] = [("GMT","GMT time"),  ("RNC","name of RNC"),  ("VENDOR","RNC vendor"),  ("TECHNOLOGY","RNC technology"),  ("TMZ","RNC Time Zone"),  ("NDC","NDC"),  ("REGION","Region"),  ("EDMARKET","E.D. market"),  ("SUBMARKET","sub-market"),  ("DEVICE_TYPE","Device type (See Appendix A.)"),  ("ITEM_ID","Device item id"),  ("NETWORK_TYPE","network capability for device (3G, 2G, NA)"),  ("UL_CAT","UL category 1 (see appendix E)"),  ("DL_CAT","DL category 1 (see appendix D)"),  ("NET_ID","network indicator (N = ATT, R = roaming)"),  ("APN","name of APN"),  ("RAT_TYPE","network on which traffic was seen (0 = other,1 = 3G, 2 = 2G)"),  ("SERVICE_CATEGORY_ID","top level service category (See appendix B)"),  ("DOMAIN_ID","domain id from domains list (see appendix C)"),  ("UL_QOS","indicates throttling in uplink (see appendix F)"),  ("DL_QOS","indicates throttling in downlink (see appendixF)"),  ("COMP_DL_BYTES","bytes from complete flows (downlink)"),  ("COMP_UL_BYTES","bytes from complete flows (uplink)"),  ("COMP_DL_BYTES_SEQ_RANGE","sum of sequence range for complete flows(downlink)"),  ("COMP_UL_BYTES_SEQ_RANGE","sum of sequence range for complete flows(uplink)"),  ("COMP_DL_FLOWS","count of complete flows (downlink)"),  ("COMP_UL_FLOWS","count of complete flows (uplink)"),  ("COMP_DL_CREATE_DURATION","sum of duration for complete flows (downlink)"),  ("COMP_UL_CREATE_DURATION","sum of duration for complete flows (uplink)"),  ("COMP_DL_CREATE_FLOW_CNT","count of complete flows (downlink)"),  ("COMP_UL_CREATE_FLOW_CNT","count of complete flows (uplink)"),  ("DL_INDEX1_BYTES","sum of bytes for 1 MB TI filter (downlink)"),  ("UL_INDEX1_BYTES","sum of bytes for 1 MB TI filter (uplink)"),  ("DL_INDEX1_SEQ_RANGE","sum of sequence range for 1 MB TI filter(downlink)"),  ("UL_INDEX1_SEQ_RANGE","sum of sequence range for 1 MB TI filter(uplink)"),  ("DL_INDEX1_DATA_LENGTH","sum of data length for 1 MB TI filter(downlink)"),  ("UL_INDEX1_DATA_LENGTH","sum of data length for 1 MB TI filter (uplink)"),  ("DL_INDEX1_PKTS","count of packets for 1 MB TI filter (downlink)"),  ("UL_INDEX1_PKTS","count of packets for 1 MB TI filter (uplink)"),  ("DL_INDEX1_FLOW_CNT","count of flows for 1 MB TI filter (downlink)"),  ("UL_INDEX1_FLOW_CNT","count of flows for 1 MB TI filter (uplink)"),  ("DL_INDEX1_DURATION","sum of flow duration for 1 MB TI filter(downlink)"),  ("UL_INDEX1_DURATION","sum of flow duration for 1 MB TI filter (uplink)"),  ("DL_INDEX1_SUM_THROUGHPUT","sum of throughput for 1 MB TI filter (downlink)"),  ("UL_INDEX1_SUM_THROUGHPUT","sum of throughput for 1 MB TI filter (uplink)"),  ("DL_INDEX2_BYTES","sum of bytes for 2 MB TI filter (downlink)"),  ("UL_INDEX2_BYTES","sum of bytes for 2 MB TI filter (uplink)"),  ("DL_INDEX2_SEQ_RANGE","sum of sequence range for 2 MB TI filter(downlink)"),  ("UL_INDEX2_SEQ_RANGE","sum of sequence range for 2 MB TI filter(uplink)"),  ("DL_INDEX2_DATA_LENGTH","sum of data length for 2 MB TI filter(downlink)"),  ("UL_INDEX2_DATA_LENGTH","sum of data length for 2 MB TI filter (uplink)"),  ("DL_INDEX2_PKTS","count of packets for 2 MB TI filter (downlink) "),  ("UL_INDEX2_PKTS","count of packets for 2 MB TI filter (uplink)"),  ("DL_INDEX2_FLOW_CNT","count of flows for 2 MB TI filter (downlink)"),  ("UL_INDEX2_FLOW_CNT","count of flows for 2 MB TI filter (uplink)"),  ("DL_INDEX2_DURATION","sum of flow duration for 2 MB TI filter(downlink)"),  ("UL_INDEX2_DURATION","sum of flow duration for 2 MB TI filter (uplink)"),  ("DL_INDEX2_SUM_THROUGHPUT","sum of throughput for 2 MB TI filter (downlink)"),  ("UL_INDEX2_SUM_THROUGHPUT","sum of throughput for 2 MB TI filter (uplink)"),  ("INCOMP_DL_BYTES","sum of bytes for incomplete flows (downlink)"),  ("INCOMP_UL_BYTES","sum of bytes for incomplete flows (uplink)"),  ("INCOMP_DL_SEQ_RANGE","sum of sequence range for incomplete flows(downlink)"),  ("INCOMP_UL_SEQ_RANGE","sum of sequence range for incomplete flows(uplink)"),  ("INCOMP_DL_PKTS","count of packets for incomplete flows(downlink)"),  ("INCOMP_UL_PKTS","count of packets for incomplete flows (uplink)"),  ("INCOMP_DL_FLOW_CNT","count of flows for incomplete flows (downlink)"),  ("INCOMP_UL_FLOW_CNT","count of flows for incomplete flows (uplink)"),  ("INCOMP_DL_DURATION","sum of flow duration for incomplete flows(downlink)"),  ("INCOMP_UL_DURATION","sum of flow duration for incomplete flows(uplink)"),  ("DL_TCP_ESTABLISHMENT_ERR","count of TCP flows with only SYN bit set(downlink)"),  ("UL_TCP_ESTABLISHMENT_ERR","count of TCP flows with only SYN bit set(uplink)"),  ("UL_TCP_SYN_ACK_FLOWS","count of TCP flows with both syn and ack bitsset (uplink)"),  ("UL_TCP_INCOMP_CONN_ERR","count of TCP flows with both syn and ack bitsset, fin and rst bits not set (uplink)"),  ("DL_TCP_SYN_FLOWS","count of TCP flows with both syn bit set(downlink)"),  ("UL_TCP_SYN_FLOWS","count of TCP flows with both syn bit set(uplink)"),  ("DL_TCP_RST_FLOWS","count of TCP flows with both Ack bit set(downlink)"),  ("UL_TCP_RST_FLOWS","count of TCP flows with both Ack bit set(uplink) "),]

schemas["PA"] = [("GMT","GMT time"),  ("RNC","name of RNC"),  ("VENDOR","RNC vendor"),  ("TECHNOLOGY","RNC technology"),  ("TMZ","RNC Time Zone"),  ("NDC","NDC"),  ("REGION","Region"),  ("EDMARKET","E.D. market"),  ("SUBMARKET","sub-market"),  ("DEVICE_TYPE","Device type (See Appendix A.)"),  ("ITEM_ID","Device item id"),  ("NETWORK_TYPE","network capability for device (3G, 2G, NA)"),  ("UL_CAT","UL category 1 (see appendix E)"),  ("DL_CAT","DL category 1 (see appendix D)"),  ("NET_ID","network indicator (N = ATT, R = roaming)"),  ("APN","name of APN"),  ("RAT_TYPE","network on which traffic was seen (0 = other, 1 = 3G, 2 = 2G)"),  ("SERVICE_CATEGORY_ID","top level service category (See appendix B)"),  ("DOMAIN_ID","domain id from domains list (see appendix C)"),  ("UL_QOS","indicates throttling in uplink (see appendix F)"),  ("DL_QOS","indicates throttling in downlink (see appendix F)"),  ("SUM_RTT_NETWORK","sum of RTT values (network side)"),  ("RTT_NETWORK_CNT","sum of RTT count (network side)"),  ("SUM_RTT_INTERNET","sum of RTT values (internet side)"),  ("RTT_INTERNET_CNT","sum of RTT count (internet side)"),  ("LG_SUM_RTT_NETWORK","sum of large packet RTT values (network side)"),  ("LG_RTT_NETWORK_CNT","sum of large packet RTT count (network side)"),  ("LG_SUM_RTT_INTERNET","sum of large packet RTT values (internet side)"),  ("LG_RTT_INTERNET_CNT","sum of large packet RTT count (internet side)"),  ("SUM_TTFB_NETWORK","sum of time-to-first-byte values (network side)"),  ("TTFB_NETWORK_CNT","sum of time-to-first-byte counts (network side)"),  ("SUM_TTFB_INTERNET","sum of time-to-first-byte values (internet side)"),  ("TTFB_INTERNET_CNT","sum of time-to-first-byte counts (internet side)"),  ("SUM_TTFBST_NETWORK","sum of time-to-first-byte values with statetransition (network side)"),  ("TTFBST_NETWORK_CNT","sum of time-to-first-byte counts with state transition (network side)"),  ("SUM_TTFBST_INTERNET","sum of time-to-first-byte values with state transition (internet side) "),  ("TTFBST_INTERNET_CNT","sum of time-to-first-byte counts with state transition (internet side)"),  ("RTT_CNT","sum of network and internet RTT values (total RTT value)"),  ("SUM_RTT","sum of network and internet RTT counts (total RTT count)"),]


def get_index(s, schema_tag):
	if not (schema_tag in schemas):
		return -1

	schema = schemas[schema_tag]
	for i in range(len(schema)):
		if (schema[i][0] == s):
			return i
	return -1
	
def print_usage():
	print "Usage:    python .py [TIME RANGE] [FIELD NAME] [FILTER]"
	print "    e.g.: python .py 01-07 DL_BYTES RNC=abcde,SERVICE_CATEGORY_ID=4"

def get_date(s):
	return int(s.split("-")[0]), int(s.split("-")[1])

def get_filter(s, schema_tag):
	filter = {}
	filter_ = s.split(",")
	for f in filter_:
		f_ = f.split("=")
		ind = get_index(f_[0], schema_tag)
		if ind != -1:
			filter[ind] = f_[1]
		else:
			print "\t Cannot pass filter: %s"%(f_[0])
	return filter

def get_folder(i):
	if i < 10:
		return "0" + str(i)
	else:
		return str(i)

def get_unzip(f, f_out):
	if f.find(".gz") != -1:
		os.system("gzip -d -c %s > %s"%(f, f_out))

# if it passes the filtering, returns splited fields, otherwise it returns []
def get_filtered(l, filter):
	l_ = l.split("|")
	for k, v in filter.iteritems():
		if l_[k] != v:
			return []
	return l_
		
