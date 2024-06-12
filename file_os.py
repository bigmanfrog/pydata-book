
path_ = 'C:\\Test_Data\\python_data.txt'
print(path_)

file_ = open(path_, encoding = 'utf-8')

#files should always be closed after done with it to free
##up memory
for line in file_:
    print(line)
file_.close() #explicitly closing the file with code

#a file can be automatically closed using 'with'
with open(path_, encoding = 'utf-8') as file_:
    lines = [x.rstrip() for x in file_]
##no explicit file.close() needed.
print(lines)

#.read(n) returns n characters or characters representing n raw bytes
with open(path_, encoding = 'utf-8') as file_:
    print(file_.read(10)) #read(0) is null, no characters
    print(file_.tell())  #at read(0), tell() returns 0 position
##tell() is based on number of bytes to decode read(n)
##so tell() can return different values based off of encoding value

##default encoding value
import sys
print(sys.getdefaultencoding())

##setting file position can be done with seek()
with open(path_, encoding='utf-8') as file_:
    file_.seek(9)
    print(file_.read(1))

print(path_)

#writelines can write whole lines to a file
#sink path
path_sink = 'C:\\Test_Data\\tmp2.txt'
print(path_sink)
#with open(path_sink, mode='w') as sink:
#    sink.writelines(x for x in open(path_) if len(x) > 1)

