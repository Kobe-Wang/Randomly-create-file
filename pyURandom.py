#Testing time
import os, time, hashlib, md5, random, sys, getopt
import ArgumFunc

#For vertifying files from restoring
def md5sum(file_name): 
    if os.path.isfile(file_name):  
        f = open(file_name,'rb')  
        #import hashlib  
        md5 = hashlib.md5(f.read()).hexdigest()  
        f.close()  
        return md5  
    else:  
        return 0 

#Use urandom to randomly generate file
def randomFile(filename, bs, count):
    filePath = "/dev/urandom"
    fr = open(filePath, "r")
    fw = open(filename, "w")
    for i in range(1,count+1):  #count
       bytes = fr.read(bs)
       fw.write(bytes)
       #print bytes
    fr.close()
    fw.close()

#Check user input argument about error handing
def checkInput(arguList):
    flag = True
    try:
       if(int(arguList[0]) >= int(arguList[1])) or (arguList[2] == '') or (int(arguList[0]) <= 0) or (int(arguList[1]) <= 0) or (int(arguList[3]) <= 0) or (int(arguList[4]) <= 0) :
          flag = False
       else:
          flag = True
    except:
       flag = False
    return flag

if __name__=='__main__': 
    arguList = [] # list of argument parameters values 
    ArgumFunc.main(sys.argv[1:], arguList)
    flag = checkInput(arguList)
    
    if flag == True:
       rangeBegin = int(arguList[0]) #begin range of random
       rangeEnd = int(arguList[1])  #end range of random
       
       fileUpDIR = arguList[2]
       diskCap = str(rangeBegin) + "k"+ "-" + str(rangeEnd) + "k"
       try:
         os.makedirs(fileUpDIR)
         os.makedirs(fileUpDIR + "md5/") # md5 folder
       except:
         pass
       fw_md5 = open(fileUpDIR + "md5/" + diskCap + "_md5.txt", "w")  #write md5 of file for vertifying
	     
       dir1_path = fileUpDIR + diskCap
       os.makedirs(dir1_path) # First folder
       countSID = 1
       for dir2 in range(1, (int(arguList[3])+1)):
          dir2_path = dir1_path + "/" + str(dir2)
          os.makedirs(dir2_path) #Second folder
          for dir3 in range(1, (int(arguList[3])+1)):
             dir3_path = dir2_path + "/" + str(dir3)
             os.makedirs(dir3_path)  #Third folder
             for i in range(1, (int(arguList[4])+1)):  #Write 50 files in third folder
	      		 file_path_name = dir3_path + "/"  + str(i) +".bin"
	      		 randomFile(file_path_name, 1024, random.randrange(rangeBegin,rangeEnd))
          	     #uid, filepath name, md5 file
	      		 fw_md5.write( str(countSID) +"\t" + file_path_name + "\t" + md5sum(file_path_name))
	      		 fw_md5.write("\n")
	      		 countSID = countSID + 1
       fw_md5.close()
       print "Succeeded..."
    else:
	    print "Input Failed..."

