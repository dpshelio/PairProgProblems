#(NR%11 != 1)
BEGIN {
    FS = "\n"
    RS ="#"
    ORS = ""
}
{
    x=1
    while (x<=NF) {
	print $x ","
	x++
    }
    print "\n"
}
