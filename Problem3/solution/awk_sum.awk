{FS = ","}
{for (i=1; i<= NF; i++) { sum[i] += $i }}
END { 
    a = ""
    for (i=2; i<NF; i++) {
	if ((i-1)%25 == 0) {
	    a = (a""$i)
	    print a
	    a = ""
	}
	else {
	    a = (a""$i"\t")
	}
    }
}
