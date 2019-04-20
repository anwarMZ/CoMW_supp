"""

Author: Muhammad Zohaib Anwar
License: GPL v3.0\n\n


Description:
Supplementary script to remove a cerain subsyetm from the m5nr database.

"""

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

def filter_fasta(fastafile, idx_list, subs):
	f=open(fastafile.replace[".fasta",subs+"_.fasta"],"w")
	for record in SeqIO.parse(fastafile,'fasta'):
		if record.id in idx_list:
			f.write(">"+str(record.id)+"\n")
			f.write(str(record.seq)+"\n")
	f.close()

if __name__ == "__main__":	
	##Change the value from the categories /data/Zohaib/GitHubRepositories/CoMW/databases/fun2003-2014.tab in order to remove anyother subsystem
	Subsystem="M"

	funccat = open("/data/Zohaib/GitHubRepositories/CoMW/databases/all.funcat.eggnogv3.txt","r")
	lines=funccat.readlines()
	funccat.close()

	funccat_OG={}
	for line in lines:
		line=line.strip()
		funccat_OG[line.split("\t")[0]]=line.split("\t")[1]

	list_OG=[k for k,v in funccat_OG.items() if v == 'M']


	db=open("/data/Zohaib/GitHubRepositories/CoMW/databases/eggNOG.md52id2ont","r")
	lines=db.readlines()
	db.close()
	m5nr=[]
	for line in lines:
		cog=line.split("\t")[1]
		if cog in list_OG:
			m5nr.append(line.split("\t")[0])

	filter_fasta(fastafile = "/data/Zohaib/GitHubRepositories/CoMW/databases/M5NR_protien.fasta",idx_list = m5nr, subs = subsystem)
