# this requires that you download or copy the file first and save it to the same directory. 
# it will work on a Ctrl-A, Ctrl-C, Ctrl-V approach, or if you download the source html.
f = open("ppc4.txt", 'r')
allthelines = f.readlines()

countfd = 0
countar = 0

#the trick here would be to search & make up this listoffilters first. we didn't finish this step.
listoffilters = ["00094","00131", "00171"]

numbers = [0] * len(listoffilters) #this makes an array of zero's the same length like [0,0,0]


for line in allthelines:
    if "_fd_" in line:
        countfd = countfd + 1
    if ("_ar_" in line) and ("_small" not in line):
        countar = countar +1
    for i in range(len(listoffilters)):
        if listoffilters[i] in line:
            numbers[i] = numbers[i] + 1

           

print "fd: {}".format(countfd)
print "ar: {}".format(countar)

for i in range(len(listoffilters)):
    print "{} : {}".format(listoffilters[i],numbers[i])

