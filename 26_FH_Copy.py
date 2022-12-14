"""
# import module
import shutil

# use copyfile()
shutil.copyfile('first.txt','second.txt')

"""
with open('first.txt','r') as firstfile, open('second.txt','w') as secondfile:
	for line in firstfile:
			secondfile.write(line)

