DESCRIPTION
	Create many random files/size for testing performance

python pyURandom.py [-B|-E|-D|-O|-N] [-h|--help]

Parameters: (Arguments)
	[-h|--help]					show help information
	------------------------------------------------------------
   [-B|--BeginSize]        Begin range of file size      (int)
	[-E|--EndSize]			   End range of file size        (int)
   [-D|--FileDIR]          Save file in Folder name      (String)
	[-O|--FileDirNum]       Number of file directory      (int) 
	[-N|--FileNum]          Number of file in final layer (int) 
	------------------------------------------------------------

For example:
	python pyURandom.py -B 1 -E 10 -D /home/delta/test/ -O 5 -N 3
	------------------------------------------------------------------
	Folder location:
		/home/delta/test/1k-10k/... and /home/delta/test/md5/1k-10k_md5.txt
	------------------------------------------------------------------
	Default: Save as third layer. 
		About above example in -O and -N parameters
			- First layer: 5 numbers
			- Second layer: 5 numbers
			- Third later: 3 numers
		Total number of files is 5*5*3 = 75 numbers
	------------------------------------------------------------------
