leg = {}

leg["SERVICE_CATEGORY_ID"] = {"apple_appstore": 16,"apple_push_jabber": 28,"att_mms": 27,"att_navigation": 8,"Email": 10,"ftp": 4,"Gaming": 12,"Im": 5,"Misc": 2,"optimization_bytemobile": 21,"p2p": 7,"smartphone_apps": 29,"Streaming": 30,"Unknown": 6,"Voip": 11,"Vpn": 9,"web_browsing": 3,"NA": 0,"ALL":-1}

def get_legend(key, val):
	x = leg[key]
	for xx in x:
		if x[xx] == val:
			return xx
	return "-1"
