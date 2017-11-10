#This file is for testing one by one 
#Written by TienVo
import sys, os, re

input_mdr = sys.argv[1]
input_pcm = sys.argv[2]

def CompareMDR_PCM(mdr, pcm):
  open_pcm = open(pcm, "r")
  open_mdr = open(mdr, "r")
  temp_file = open("temp_file.txt", "w")
  output_result = open("output.txt","w")
  for line in open_pcm:
	items2 = line.split()
	temp_file.write(items2[1]+"\n")
  temp_file.close()
  temp_file = open("temp_file.txt", "r")
  for line in temp_file:
    print "ahihi"
  #Convert line into string!!! Then prepare string with other string in mdr
  #for line in open_pcm:
   # for line_mdr in open_mdr:
	#  if line.find(line_mdr) >= 0:
	 #   output_result.write(line_mdr)
  #os.remove("temp_file.txt")	
  temp_file.close()
  output_result.close()		
  open_mdr.close()
  open_pcm.close()
  
CompareMDR_PCM(input_mdr, input_pcm)