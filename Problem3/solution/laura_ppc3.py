data = []
onepage = []
with open("../secret_image.dat", 'r') as f:
    for line in f.readlines()[1:]: #Discard first "#"
        if line.startswith("#"): # end of previous one
            data.append(onepage)
            onepage = []
            continue
        line = line.strip()
        onepage = onepage + [float(l) for l in line.split(',')]
data.append(onepage)

list = zip(*data)
summedlist = [sum(l) for l in list]

finalstring = ""
for i in range(625):
     if i%25 == 0: finalstring = finalstring + "\n"
     if summedlist[i] < 100: finalstring = finalstring + "#"
     if summedlist[i] > 100: finalstring = finalstring + " "

print finalstring

finalnoisystring = ""
for i in range(625):
     if i%25 == 0: finalnoisystring = finalnoisystring + "\n"
     if summedlist[i] < 4: finalnoisystring = finalnoisystring + "#"
     if 4 <= summedlist[i] <= 100: finalnoisystring = finalnoisystring + "*"
     if 200 > summedlist[i] > 100: finalnoisystring = finalnoisystring + "."
     if summedlist[i] >= 200: finalnoisystring = finalnoisystring + " "


print finalnoisystring
