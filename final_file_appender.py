#!/usr/bin/env python

import os
import sys

directory_name = sys.argv[1]
#print ("Hello", directory_name, "lol")
cwd = os.getcwd() #gets current directory , aka this program file must be in the same directory as files to append 
#print (os.path.abspath(directory_name))

List_of_reads = []
i = 0

# List all files in  current directory (cwd) using os.listdir
for entry in os.listdir(directory_name): #for every object in the directory
   #print ("I am in directory")
   print (entry)
   if os.path.isfile(os.path.join(directory_name, entry)):#checks if the object is a file 
        #print(entry) #print file name with extension
        #print ("I am a file")
        #i += 1
        #print (i)
        #print(os.path.splitext(os.path.basename(entry))[0]) #gets filename w/o extension
        filename = os.path.splitext(os.path.basename(entry))[0] #stores filename w/o extension into variable filename
        List_of_reads.append(filename) #makes a file of FILENAMES (not the actual file)

List_of_reads.sort()
#print (List_of_reads)
print ()

FinalForward = open("Appended_R1.fastq", "w+")
FinalReverse = open ("Appended_R2.fastq", "w+")

for i in List_of_reads:

	if "R1" in i: 
		filename_with_extension = os.path.abspath(directory_name)+"/"+i+".fastq"
		read = open(filename_with_extension, "r")
		reader = (read.read())
		FinalForward.write(reader)
		#print ("We appended R1")

	if "R2" in i:
		filename_with_extension = os.path.abspath(directory_name)+"/"+i+".fastq"
		read = open(filename_with_extension, "r")
		reader = (read.read())
		FinalReverse.write(reader)
		#print ("We appended R2")

FinalReverse.close()
FinalForward.close()

#how to output a file?