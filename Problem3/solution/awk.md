With `awk` we can solve the problem with the two scripts in this directory as:

```shell
awk -f awk_solve.awk ../secret_image.dat | awk -f awk_sum.awk > image.txt
```

which then it can be ploted in `gnuplot` as:

```gnuplot
plot 'image.txt' matrix with image
```
