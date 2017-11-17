#This file is for testing one by one 
#Written by TienVo
import sys, os, re
from filecmp import dircmp

input_mdr = sys.argv[1]
input_pcm = sys.argv[2]

def CompareMDR_PCM(mdr, pcm):
  open_pcm = open(pcm, "r")
  open_mdr = open(mdr, "r")
  temp_file = open("output/temp_file.txt", "w")
  output_result = open("output/output.txt","w")
  for line in open_pcm:
	items2 = line.split()
	temp_file.write(items2[1]+"\n")
  temp_file.close()
  temp_file = open("output/temp_file.txt", "r")
  temp = "1.3.6.1.2.1.2.2.1.3"
  regex = re.compile(r'OctetString (\d{1,3}(-\d{1,3})+)')
  searchOids = []
  outTempOids = []
  for line in temp_file:
    for line_mdr in open_mdr:
      match = re.search
  for line in temp_file:
    searchOids.append(line.strip())
  for line in open_mdr:
    current_line = line.split()
    for searchOid in searchOids:
      if searchOid in current_line:
         outTempOids.append(searchOid)
         break
  for line in outTempOids:
    output_result.writelines(line)
  #Convert line into string!!! Then prepare string with other string in mdr	
  #It is possible to use regexp for searching line by line
  #Because of version of python, so we have change approach.
  temp_file.close()
  output_result.close()		
  open_mdr.close()
  open_pcm.close()
  
CompareMDR_PCM(input_mdr, input_pcm)
