leg = {}

leg["SERVICE_CATEGORY_ID"] = {"apple_appstore": 16,"apple_push_jabber": 28,"att_mms": 27,"att_navigation": 8,"Email": 10,"ftp": 4,"Gaming": 12,"Im": 5,"Misc": 2,"optimization_bytemobile": 21,"p2p": 7,"smartphone_apps": 29,"Streaming": 30,"Unknown": 6,"Voip": 11,"Vpn": 9,"web_browsing": 3,"NA": 0,"ALL":-1}

leg["DOMAIN_ID"] = {" youtube.com ": 12 , " apple.com ": 1 , " pandora.com ": 2 , " google.com ": 7 , " fbcdn.net ": 6 , " facebook.com ": 13 , " llnwd.net ": 9 , " xvideos.com ": 140 , " pornhub.com ": 4 , " yahoo.com ": 5 , " edgesuite.net ": 43 , " nflximg.com ": 258 , " mzstatic.com ": 8500 , " icloud.com ": 8510 , " cingular.com ": 949 , " gmail.com ": 3646 , " phncdn.com ": 5810 , " live.com ": 128 , " amazonaws.com ": 19 , " akamaistream.net ": 61 , " youporn.com ": 72 , " youjizz.com ": 363 , " akamai.net ": 32 , " gstatic.com ": 38 , " tube8.com ": 8 , " twitter.com ": 166 , " llnwd.net:netflix.vo ": 20008 , " edgesuite.net:nflximg.com ": 10258 , " llnwd.net:directvnfl.vo ": 20001 , " edgesuite.net:apple.com ": 10001 , " llnwd.net:listen.vo ": 20002 , " windowsupdate.com:au.download.windowsupdate.com ": 30001 , " llnwd.net:wdigespmms.vo ": 20003 , " llnwd.net:brightcove.vo ": 20004 , " llnwd.net:navigon.vo ": 20005 , " windowsupdate.com:download.windowsupdate.com ": 30002 , " edgesuite.net:starbucks.com ": 10806 , " llnwd.net:ustream.vo ": 20006 , " llnwd.net:amazon.hs ": 20007 , " edgesuite.net:netflix.com ": 10547 , " Unknown ": -1 , " All_other_domains ": 0 ,}

def get_legend(key, val):
	x = leg[key]
	for xx in x:
		if x[xx] == val:
			return xx
	return "-1"
