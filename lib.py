import os, sys

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
	if filter == []:
		return l_
	for k, v in filter.iteritems():
		if len(l_) <= k:
			return []
		if l_[k] != v:
			return []
	return l_

def printf(f, s):
	print s
	f.write(s + "\n")

def scp_and_plot(f_name):
	os.system("scp %s xing@68.181.99.224:research/SQM/plot/"%(f_name))
	os.system("ssh xing@68.181.99.224 'cd research/SQM/plot; python plot.py \
	%s'"%(f_name))
	if f_name.find("CATEGORY_ID") == -1:
		os.system("ssh xing@68.181.99.224 'cd research/SQM/plot; python \
		plot_combine.py %s'"%(f_name))

def scp_and_plot_separate(f_name):
	os.system("scp %s xing@68.181.99.224:research/SQM/plot/"%(f_name))
	os.system("ssh xing@68.181.99.224 'cd research/SQM/plot; python plot_sep\
arate.py %s'"%(f_name))

schemas = {}

schemas["RNC_BA"] = [("GMT","GMT time"),  ("RNC","name of RNC"),  ("VENDOR","RNC\
 vendor"),  ("TECHNOLOGY","RNC technology"),  ("TMZ","RNC Time Zone"),  ("NDC","\
NDC"),  ("REGION","Region"),  ("EDMARKET","E.D. market"),  ("SUBMARKET","sub-mar\
ket"),  ("DEVICE_TYPE","Device type (See Appendix A.)"),  ("ITEM_ID","Device ite\
m id"),  ("NETWORK_TYPE","network capability for device (3G, 2G, NA)"),  ("UL_CA\
T","UL category 1 (see appendix E)"),  ("DL_CAT","DL category 1 (see appendix D)\
"),  ("NET_ID","network indicator (N = ATT, R = roaming)"),  ("APN","name of APN\
"),  ("RAT_TYPE","network on which traffic was seen (0 = other, 1= 3G, 2 = 2G)")\
,  ("SERVICE_CATEGORY_ID","top level service category (See appendix B)"),  ("DOM\
AIN_ID","domain id from domains list (see appendix C)"),  ("UL_QOS","indicates t\
hrottling in uplink (see appendix F)"),  ("DL_QOS","indicates throttling in down\
link (see appendix F)"),  ("DL_BYTES","downlink bytes"),  ("UL_BYTES","uplink by\
tes"),  ("DL_PKTS","downlink packets"),  ("UL_PKTS","uplink packets "),  ("DL_FL\
OW_CNT","downlink flow count"),  ("UL_FLOW_CNT","uplink flow count"),  ("UL_DATA\
_LENGTH","uplink data length (used for loss calculation)"),  ("UL_SEQ_RANGE","up\
link sequence range (used for loss calculation)"),  ("DL_DATA_LENGTH","downlink \
data length (used for loss calculation)"),  ("DL_SEQ_RANGE","downlink sequence r\
ange (used for losscalculation)"),  ("DL_HTTP_200_CNT","count of downlink HTTP 2\
00 codes (success)"),  ("DL_HTTP_300_CNT","count of downlink HTTP 300 codes (red\
irection)"),  ("DL_HTTP_400_CNT","count of downlink HTTP 400 codes (client error\
)"),  ("DL_HTTP_500_CNT","count of downlink HTTP 500 codes (server error)"),  ("\
DL_HTTP_OTHER_CNT","count of downlink HTTP other codes"),  ("DL_TCP_OUTOFORDER_C\
NT","count of out of order tcp packets (downlink)"),  ("UL_TCP_OUTOFORDER_CNT","\
count of out of order tcp packets (uplink)"),  ("DL_TCP_RETRANSMISSION_CNT","cou\
nt of re-transmitted packets (downlink)"),  ("UL_TCP_RETRANSMISSION_CNT","count \
of re-transmitted packets (uplink)"),]\


schemas["RNC_BS"] = [("GMT","GMT time"),  ("RNC","name of RNC"),  ("VENDOR","RNC\
 vendor"),  ("TECHNOLOGY","RNC technology"),  ("TMZ","RNC Time Zone"),  ("NDC","\
NDC"),  ("REGION","Region"),  ("EDMARKET","E.D. market"),  ("SUBMARKET","sub-mar\
ket"),  ("DEVICE_TYPE","Device type (See Appendix A.)"),  ("ITEM_ID","Device ite\
m id"),  ("NETWORK_TYPE","network capability for device (3G, 2G, NA)"),  ("UL_CA\
T","UL category 1 (see appendix E)"),  ("DL_CAT","DL category 1 (see appendix D)\
"),  ("NET_ID","network indicator (N = ATT, R = roaming)"),  ("APN","name of APN\
"),  ("RAT_TYPE","network on which traffic was seen (0 = other,1 = 3G, 2 = 2G)")\
,  ("SERVICE_CATEGORY_ID","top level service category (See appendix B)"),  ("DOM\
AIN_ID","domain id from domains list (see appendix C)"),  ("UL_QOS","indicates t\
hrottling in uplink (see appendix F)"),  ("DL_QOS","indicates throttling in down\
link (see appendixF)"),  ("COMP_DL_BYTES","bytes from complete flows (downlink)"\
),  ("COMP_UL_BYTES","bytes from complete flows (uplink)"),  ("COMP_DL_BYTES_SEQ\
_RANGE","sum of sequence range for complete flows(downlink)"),  ("COMP_UL_BYTES_\
SEQ_RANGE","sum of sequence range for complete flows(uplink)"),  ("COMP_DL_FLOWS\
","count of complete flows (downlink)"),  ("COMP_UL_FLOWS","count of complete fl\
ows (uplink)"),  ("COMP_DL_CREATE_DURATION","sum of duration for complete flows \
(downlink)"),  ("COMP_UL_CREATE_DURATION","sum of duration for complete flows (u\
plink)"),  ("COMP_DL_CREATE_FLOW_CNT","count of complete flows (downlink)"),  ("\
COMP_UL_CREATE_FLOW_CNT","count of complete flows (uplink)"),  ("DL_INDEX1_BYTES\
","sum of bytes for 1 MB TI filter (downlink)"),  ("UL_INDEX1_BYTES","sum of byt\
es for 1 MB TI filter (uplink)"),  ("DL_INDEX1_SEQ_RANGE","sum of sequence range\
 for 1 MB TI filter(downlink)"),  ("UL_INDEX1_SEQ_RANGE","sum of sequence range \
for 1 MB TI filter(uplink)"),  ("DL_INDEX1_DATA_LENGTH","sum of data length for \
1 MB TI filter(downlink)"),  ("UL_INDEX1_DATA_LENGTH","sum of data length for 1 \
MB TI filter (uplink)"),  ("DL_INDEX1_PKTS","count of packets for 1 MB TI filter\
 (downlink)"),  ("UL_INDEX1_PKTS","count of packets for 1 MB TI filter (uplink)"\
),  ("DL_INDEX1_FLOW_CNT","count of flows for 1 MB TI filter (downlink)"),  ("UL\
_INDEX1_FLOW_CNT","count of flows for 1 MB TI filter (uplink)"),  ("DL_INDEX1_DU\
RATION","sum of flow duration for 1 MB TI filter(downlink)"),  ("UL_INDEX1_DURAT\
ION","sum of flow duration for 1 MB TI filter (uplink)"),  ("DL_INDEX1_SUM_THROU\
GHPUT","sum of throughput for 1 MB TI filter (downlink)"),  ("UL_INDEX1_SUM_THRO\
UGHPUT","sum of throughput for 1 MB TI filter (uplink)"),  ("DL_INDEX2_BYTES","s\
um of bytes for 2 MB TI filter (downlink)"),  ("UL_INDEX2_BYTES","sum of bytes f\
or 2 MB TI filter (uplink)"),  ("DL_INDEX2_SEQ_RANGE","sum of sequence range for\
 2 MB TI filter(downlink)"),  ("UL_INDEX2_SEQ_RANGE","sum of sequence range for \
2 MB TI filter(uplink)"),  ("DL_INDEX2_DATA_LENGTH","sum of data length for 2 MB\
 TI filter(downlink)"),  ("UL_INDEX2_DATA_LENGTH","sum of data length for 2 MB T\
I filter (uplink)"),  ("DL_INDEX2_PKTS","count of packets for 2 MB TI filter (do\
wnlink) "),  ("UL_INDEX2_PKTS","count of packets for 2 MB TI filter (uplink)"), \
 ("DL_INDEX2_FLOW_CNT","count of flows for 2 MB TI filter (downlink)"),  ("UL_IN\
DEX2_FLOW_CNT","count of flows for 2 MB TI filter (uplink)"),  ("DL_INDEX2_DURAT\
ION","sum of flow duration for 2 MB TI filter(downlink)"),  ("UL_INDEX2_DURATION\
","sum of flow duration for 2 MB TI filter (uplink)"),  ("DL_INDEX2_SUM_THROUGHP\
UT","sum of throughput for 2 MB TI filter (downlink)"),  ("UL_INDEX2_SUM_THROUGH\
PUT","sum of throughput for 2 MB TI filter (uplink)"),  ("INCOMP_DL_BYTES","sum \
of bytes for incomplete flows (downlink)"),  ("INCOMP_UL_BYTES","sum of bytes fo\
r incomplete flows (uplink)"),  ("INCOMP_DL_SEQ_RANGE","sum of sequence range fo\
r incomplete flows(downlink)"),  ("INCOMP_UL_SEQ_RANGE","sum of sequence range f\
or incomplete flows(uplink)"),  ("INCOMP_DL_PKTS","count of packets for incomple\
te flows(downlink)"),  ("INCOMP_UL_PKTS","count of packets for incomplete flows \
(uplink)"),  ("INCOMP_DL_FLOW_CNT","count of flows for incomplete flows (downlin\
k)"),  ("INCOMP_UL_FLOW_CNT","count of flows for incomplete flows (uplink)"),  (\
"INCOMP_DL_DURATION","sum of flow duration for incomplete flows(downlink)"),  ("\
INCOMP_UL_DURATION","sum of flow duration for incomplete flows(uplink)"),  ("DL_\
TCP_ESTABLISHMENT_ERR","count of TCP flows with only SYN bit set(downlink)"),  (\
"UL_TCP_ESTABLISHMENT_ERR","count of TCP flows with only SYN bit set(uplink)"), \
 ("UL_TCP_SYN_ACK_FLOWS","count of TCP flows with both syn and ack bitsset (upli\
nk)"),  ("UL_TCP_INCOMP_CONN_ERR","count of TCP flows with both syn and ack bits\
set, fin and rst bits not set (uplink)"),  ("DL_TCP_SYN_FLOWS","count of TCP flo\
ws with both syn bit set(downlink)"),  ("UL_TCP_SYN_FLOWS","count of TCP flows w\
ith both syn bit set(uplink)"),  ("DL_TCP_RST_FLOWS","count of TCP flows with bo\
th Ack bit set(downlink)"),  ("UL_TCP_RST_FLOWS","count of TCP flows with both A\
ck bit set(uplink) "),]\

schemas["RNC_PA"] = [("GMT","GMT time"),  ("RNC","name of RNC"),  ("VENDOR","RNC\
 vendor"),  ("TECHNOLOGY","RNC technology"),  ("TMZ","RNC Time Zone"),  ("NDC","\
NDC"),  ("REGION","Region"),  ("EDMARKET","E.D. market"),  ("SUBMARKET","sub-mar\
ket"),  ("DEVICE_TYPE","Device type (See Appendix A.)"),  ("ITEM_ID","Device ite\
m id"),  ("NETWORK_TYPE","network capability for device (3G, 2G, NA)"),  ("UL_CA\
T","UL category 1 (see appendix E)"),  ("DL_CAT","DL category 1 (see appendix D)\
"),  ("NET_ID","network indicator (N = ATT, R = roaming)"),  ("APN","name of APN\
"),  ("RAT_TYPE","network on which traffic was seen (0 = other, 1 = 3G, 2 = 2G)"\
),  ("SERVICE_CATEGORY_ID","top level service category (See appendix B)"),  ("DO\
MAIN_ID","domain id from domains list (see appendix C)"),  ("UL_QOS","indicates \
throttling in uplink (see appendix F)"),  ("DL_QOS","indicates throttling in dow\
nlink (see appendix F)"),  ("SUM_RTT_NETWORK","sum of RTT values (network side)"\
),  ("RTT_NETWORK_CNT","sum of RTT count (network side)"),  ("SUM_RTT_INTERNET",\
"sum of RTT values (internet side)"),  ("RTT_INTERNET_CNT","sum of RTT count (in\
ternet side)"),  ("LG_SUM_RTT_NETWORK","sum of large packet RTT values (network \
side)"),  ("LG_RTT_NETWORK_CNT","sum of large packet RTT count (network side)"),\
  ("LG_SUM_RTT_INTERNET","sum of large packet RTT values (internet side)"),  ("L\
G_RTT_INTERNET_CNT","sum of large packet RTT count (internet side)"),  ("SUM_TTF\
B_NETWORK","sum of time-to-first-byte values (network side)"),  ("TTFB_NETWORK_C\
NT","sum of time-to-first-byte counts (network side)"),  ("SUM_TTFB_INTERNET","s\
um of time-to-first-byte values (internet side)"),  ("TTFB_INTERNET_CNT","sum of\
 time-to-first-byte counts (internet side)"),  ("SUM_TTFBST_NETWORK","sum of tim\
e-to-first-byte values with statetransition (network side)"),  ("TTFBST_NETWORK_\
CNT","sum of time-to-first-byte counts with state transition (network side)"),  \
("SUM_TTFBST_INTERNET","sum of time-to-first-byte values with state transition (\
internet side) "),  ("TTFBST_INTERNET_CNT","sum of time-to-first-byte counts wit\
h state transition (internet side)"),  ("RTT_CNT","sum of network and internet R\
TT values (total RTT value)"),  ("SUM_RTT","sum of network and internet RTT coun\
ts (total RTT count)"),]

schemas["LTE_BA"] = [("GMT","GMT time"),  ("ENODEB","name of ENODEB"),  ("USID",\
"USID of enodeb"),  ("SGW","Name of SGW"),  ("VENDOR","EnodeB vendor"),  ("TECHN\
OLOGY","EnodeB technology"),  ("TMZ","EnodeB Market Time Zone"),  ("NDC","NDC"),\
  ("REGION","Region"),  ("EDMARKET","E.D. market"),  ("SUBMARKET","sub-market"),\
  ("DEVICE_TYPE","Device type (See Appendix A.)"),  ("ITEM_ID","Device item id")\
,  ("NETWORK_TYPE","network capability for device (4G)"),  ("UL_CAT","UL categor\
y 1 (LTE_Cat3)"),  ("DL_CAT","DL category 1 (LTE_Cat3)"),  ("NET_ID","network in\
dicator (N = ATT, R = roaming)"),  ("APN","name of APN"),  ("RAT_TYPE","network \
on which traffic was seen (6 = LTE)"),  ("SERVICE_CATEGORY_ID","top level servic\
e category (See appendix B)"),  ("DOMAIN_ID","domain id from domains list (see a\
ppendix C)"),  ("UL_QOS","indicates throttling in uplink (see appendix F)"),  ("\
DL_QOS","indicates throttling in downlink (see appendix F)"), ("unknown1", "unkn\
own1"), ("QOS", "NUMBER"), ("DL_BYTES","downlink bytes"),  ("UL_BYTES","uplink b\
ytes"),  ("DL_PKTS","downlink packets"),  ("UL_PKTS","uplink packets"),  ("DL_FL\
OW_CNT","downlink flow count"),  ("UL_FLOW_CNT","uplink flow count"),  ("UL_DATA\
_LENGTH","uplink data length (used for loss calculation)"),  ("UL_SEQ_RANGE","up\
link sequence range (used for loss calculation)"),  ("DL_DATA_LENGTH","downlink \
data length (used for loss calculation)"),  ("DL_SEQ_RANGE","downlink sequence r\
ange (used for loss calculation)"),  ("DL_HTTP_200_CNT","count of downlink HTTP \
200 codes (success)"),  ("DL_HTTP_300_CNT","count of downlink HTTP 300 codes (re\
direction)"),  ("DL_HTTP_400_CNT","count of downlink HTTP 400 codes (client erro\
r)"),  ("DL_HTTP_500_CNT","count of downlink HTTP 500 codes (server error)"),  (\
"DL_HTTP_OTHER_CNT","count of downlink HTTP other codes"),  ("DL_TCP_OUTOFORDER_\
CNT","count of out of order tcp packets (downlink)"),  ("UL_TCP_OUTOFORDER_CNT",\
"count of out of order tcp packets (uplink)"),  ("DL_TCP_RETRANSMISSION_CNT","co\
unt of re-transmitted packets (downlink)"),  ("UL_TCP_RETRANSMISSION_CNT","count\
 of re-transmitted packets (uplink)"),]\

schemas["LTE_BS"]  = [("GMT","GMT time"),  ("ENODEB","name of enodeb"),  ("USID"\
,"USID of enodeb"),  ("SGW","Name of SGW"),  ("VENDOR","enodeb vendor"),  ("TECH\
NOLOGY","enodeb technology"),  ("TMZ","Enodeb market Time Zone"),  ("NDC","NDC")\
,  ("REGION","Region"),  ("EDMARKET","E.D. market"),  ("SUBMARKET","sub-market")\
,  ("DEVICE_TYPE","Device type (See Appendix A.)"),  ("ITEM_ID","Device item id"\
),  ("NETWORK_TYPE","network capability for device (4G)"),  ("UL_CAT","UL catego\
ry 1 (LTE_Cat3)"),  ("DL_CAT","DL category 1 (LTE_Cat3)"),  ("NET_ID","network i\
ndicator (N = ATT, R = roaming)"),  ("APN","name of APN"),  ("RAT_TYPE","network\
 on which traffic was seen (6 = LTE)"),  ("SERVICE_CATEGORY_ID","top level servi\
ce category (See appendix B)"),  ("DOMAIN_ID","domain id from domains list (see \
appendix C)"),  ("UL_QOS","indicates throttling in uplink (see appendix F)"),  (\
"DL_QOS","indicates throttling in downlink (see appendixF)"),  ("COMP_DL_BYTES",\
"bytes from complete flows (downlink)"),  ("COMP_UL_BYTES","bytes from complete \
flows (uplink)"),  ("COMP_DL_BYTES_SEQ_RANGE","sum of sequence range for complet\
e flows(downlink)"),  ("COMP_UL_BYTES_SEQ_RANGE","sum of sequence range for comp\
lete flows(uplink)"),  ("COMP_DL_FLOWS","count of complete flows (downlink)"),  \
("COMP_UL_FLOWS","count of complete flows (uplink)"),  ("COMP_DL_CREATE_DURATION\
","sum of duration for complete flows (downlink)"),  ("COMP_UL_CREATE_DURATION",\
"sum of duration for complete flows (uplink)"),  ("COMP_DL_CREATE_FLOW_CNT","cou\
nt of complete flows (downlink)"),  ("COMP_UL_CREATE_FLOW_CNT","count of complet\
e flows (uplink)"),  ("DL_INDEX1_BYTES","sum of bytes for 1 MB TI filter (downli\
nk)"),  ("UL_INDEX1_BYTES","sum of bytes for 1 MB TI filter (uplink)"),  ("DL_IN\
DEX1_SEQ_RANGE","sum of sequence range for 1 MB TI filter(downlink)"),  ("UL_IND\
EX1_SEQ_RANGE","sum of sequence range for 1 MB TI filter(uplink)"),  ("DL_INDEX1\
_DATA_LENGTH","sum of data length for 1 MB TI filter(downlink)"),  ("UL_INDEX1_D\
ATA_LENGTH","sum of data length for 1 MB TI filter (uplink)"),  ("DL_INDEX1_PKTS\
","count of packets for 1 MB TI filter (downlink)"),  ("UL_INDEX1_PKTS","count o\
f packets for 1 MB TI filter (uplink)"),  ("DL_INDEX1_FLOW_CNT","count of flows \
for 1 MB TI filter (downlink)"),  ("UL_INDEX1_FLOW_CNT","count of flows for 1 MB\
 TI filter (uplink)"),  ("DL_INDEX1_DURATION","sum of flow duration for 1 MB TI \
filter(downlink)"),  ("UL_INDEX1_DURATION","sum of flow duration for 1 MB TI fil\
ter (uplink)"),  ("DL_INDEX1_SUM_THROUGHPUT","sum of throughput for 1 MB TI filt\
er (downlink)"),  ("UL_INDEX1_SUM_THROUGHPUT","sum of throughput for 1 MB TI fil\
ter (uplink)"),  ("DL_INDEX2_BYTES","sum of bytes for 4 MB TI filter (downlink)"\
),  ("UL_INDEX2_BYTES","sum of bytes for 4 MB TI filter (uplink)"),  ("DL_INDEX2\
_SEQ_RANGE","sum of sequence range for 4 MB TI filter(downlink)"),  ("UL_INDEX2_\
SEQ_RANGE","sum of sequence range for 4 MB TI filter(uplink)"),  ("DL_INDEX2_DAT\
A_LENGTH","sum of data length for 4 MB TI filter(downlink)"),  ("UL_INDEX2_DATA_\
LENGTH","sum of data length for 4 MB TI filter (uplink)"),  ("DL_INDEX2_PKTS","c\
ount of packets for 4 MB TI filter (downlink)"),  ("UL_INDEX2_PKTS","count of pa\
ckets for 4 MB TI filter (uplink)"),  ("DL_INDEX2_FLOW_CNT","count of flows for \
4 MB TI filter (downlink)"),  ("UL_INDEX2_FLOW_CNT","count of flows for 4 MB TI \
filter (uplink)"),  ("DL_INDEX2_DURATION","sum of flow duration for 4 MB TI filt\
er(downlink)"),  ("UL_INDEX2_DURATION","sum of flow duration for 4 MB TI filter \
(uplink)"),  ("DL_INDEX2_SUM_THROUGHPUT","sum of throughput for 4 MB TI filter (\
downlink)"),  ("UL_INDEX2_SUM_THROUGHPUT","sum of throughput for 4 MB TI filter \
(uplink)"),  ("INCOMP_DL_BYTES","sum of bytes for incomplete flows (downlink)"),\
  ("INCOMP_UL_BYTES","sum of bytes for incomplete flows (uplink)"),  ("INCOMP_DL\
_SEQ_RANGE","sum of sequence range for incomplete flows(downlink)"),  ("INCOMP_U\
L_SEQ_RANGE","sum of sequence range for incomplete flows(uplink)"),  ("INCOMP_DL\
_PKTS","count of packets for incomplete flows(downlink)"),  ("INCOMP_UL_PKTS","c\
ount of packets for incomplete flows (uplink)"),  ("INCOMP_DL_FLOW_CNT","count o\
f flows for incomplete flows (downlink)"),  ("INCOMP_UL_FLOW_CNT","count of flow\
s for incomplete flows (uplink)"),  ("INCOMP_DL_DURATION","sum of flow duration \
for incomplete flows(downlink)"),  ("INCOMP_UL_DURATION","sum of flow duration f\
or incomplete flows(uplink)"),  ("DL_TCP_ESTABLISHMENT_ERR","count of TCP flows \
with only SYN bit set(downlink)"),  ("UL_TCP_ESTABLISHMENT_ERR","count of TCP fl\
ows with only SYN bit set(uplink)"),  ("UL_TCP_SYN_ACK_FLOWS","count of TCP flow\
s with both syn and ack bitsset (uplink)"),  ("UL_TCP_INCOMP_CONN_ERR","count of\
 TCP flows with both syn and ack bitsset, fin and rst bits not set (uplink)"),  \
("DL_TCP_SYN_FLOWS","count of TCP flows with both syn bit set(downlink)"),  ("UL\
_TCP_SYN_FLOWS","count of TCP flows with both syn bit set(uplink)"),  ("DL_TCP_R\
ST_FLOWS","count of TCP flows with both Ack bit set(downlink)"),  ("UL_TCP_RST_F\
LOWS","count of TCP flows with both Ack bit set(uplink)"),]\

schemas["LTE_PA"] = [("GMT","GMT time"),  ("ENODEB","name of enodeb"),  ("USID",\
"USID of enodeb"),  ("SGW","Name of SGW"),  ("VENDOR","enodeb vendor"),  ("TECHN\
OLOGY","enodeb technology"),  ("TMZ","Enodeb market Time Zone"),  ("NDC","NDC"),\
  ("REGION","Region"),  ("EDMARKET","E.D. market"),  ("SUBMARKET","sub-market"),\
  ("DEVICE_TYPE","Device type (See Appendix A.)"),  ("ITEM_ID","Device item id")\
,  ("NETWORK_TYPE","network capability for device (4G)"),  ("UL_CAT","UL categor\
y 1 (LTE_Cat3)"),  ("DL_CAT","DL category 1 (LTE_Cat3)"),  ("NET_ID","network in\
dicator (N = ATT, R = roaming)"),  ("APN","name of APN"),  ("RAT_TYPE","network \
on which traffic was seen (6 = LTE)"),  ("SERVICE_CATEGORY_ID","top level servic\
e category (See appendix B)"),  ("DOMAIN_ID","domain id from domains list (see a\
ppendix C)"),  ("UL_QOS","indicates throttling in uplink (see appendix F)"),  ("\
DL_QOS","indicates throttling in downlink (see appendix F)"),  ("SUM_RTT_NETWORK\
","sum of RTT values (network side)"),  ("RTT_NETWORK_CNT","sum of RTT count (ne\
twork side)"),  ("SUM_RTT_INTERNET","sum of RTT values (internet side)"),  ("RTT\
_INTERNET_CNT","sum of RTT count (internet side)"),  ("LG_SUM_RTT_NETWORK","sum \
of large packet RTT values (network side)"),  ("LG_RTT_NETWORK_CNT","sum of larg\
e packet RTT count (network side)"),  ("LG_SUM_RTT_INTERNET","sum of large packe\
t RTT values (internet side)"),  ("LG_RTT_INTERNET_CNT","sum of large packet RTT\
 count (internet side)"),  ("SUM_TTFB_NETWORK","sum of time-to-first-byte (no st\
ate transition)values"),  ("TTFB_NETWORK_CNT","sum of time-to-first-byte (no sta\
te transition)counts"),  ("SUM_TTFB_INTERNET","sum of time-to-first-byte values \
(with statetransition)"),  ("TTFB_INTERNET_CNT","sum of time-to-first-byte count\
s (with statetransition)"),  ("SUM_TTFBST_NETWORK","NULL"),  ("TTFBST_NETWORK_CN\
T","NULL"),  ("SUM_TTFBST_INTERNET","NULL"),  ("TTFBST_INTERNET_CNT","NULL"),  (\
"RTT_CNT","sum of network and internet RTT values (totalRTT value)"),  ("SUM_RTT\
","sum of network and internet RTT counts (totalRTT count)"),]
