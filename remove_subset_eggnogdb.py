Subsystem="M"

funccat = open("/data/Zohaib/GitHubRepositories/CoMW/databases/all.funcat.eggnogv3.txt",'r')
lines=funccat.readlines()
funccat.close()

funccat_OG={}
for line in lines:
	line=line.strip()
	funccat_OG[line.split("\t")[0]]=line.split("\t")[1]

list_OG([k for k,v in funccat_OG.items() if v == 'M'])


db=open("/data/Zohaib/GitHubRepositories/CoMW/databases/eggNOG.md52id2ont","r")
lines=db.readlines()
db.close()
for line in lines:
	cog=line.split("\t")[1]
	if cog in list_OG:
		print line.split("\t")[0]


