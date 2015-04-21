import os

enb = open("enbs.out").readlines()

for xx in enb[1:20]:
	print xx
	x = xx[:-1]
	print x
	os.system("python data_aggre.py LTE_BA 11 24-30 DL_BYTES ENODEB=%s,SERVICE_CATEGORY_ID=3"%(x))
	os.system("python data_aggre.py LTE_BA 11 24-30 DL_BYTES ENODEB=%s,SERVICE_CATEGORY_ID=30"%(x))
	os.system("python data_aggre.py LTE_BA 11 24-30 DL_BYTES ENODEB=%s,SERVICE_CATEGORY_ID=29"%(x))
	os.system("python data_aggre.py LTE_BA 11 24-30 DL_BYTES ENODEB=%s"%(x))
