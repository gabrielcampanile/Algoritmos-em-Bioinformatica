import requests as r
from Bio import SeqIO
from io import StringIO

cID='P04637'

baseUrl="http://www.uniprot.org/uniprot/"
currentUrl=baseUrl+cID+".fasta"
response = r.post(currentUrl)
cData=''.join(response.text)

Seq=StringIO(cData)
pSeq=list(SeqIO.parse(Seq,'fasta'))