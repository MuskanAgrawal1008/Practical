def fraction(num,den):
    if num % den == 0:
        print("Whole number:", num // den)
    else:
        if num < den:
            print(num, "/", den, ", which is an improper fraction")
        else:
            rem = num % den
            mix = (num - rem) // den
            print(mix, "(", rem, "/", den, "), which is a mixed fraction")

num = int(input("Enter numerator:"))
den = input("Enter denominator:")
if len(den) == 0:
    den =1
else:
    den = int(den)

if den == 0:
    print("denominator cannot be 0")
else:
    fraction(num, den)