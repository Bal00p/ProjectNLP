import random
import json

def q(numd, loc, x, t):
	return f'''Give me the sum of {numd} digits from the {loc} of result of repeating multiply 1 by {x} {t} times.'''

def prompt(loc, x, t):
	if loc == 'middle':
		return r'''To find the sum of two digits from the middle of repeating the multiplication of 1 by 0.1 ten times:

1. Start by performing the multiplication of 1 by 0.1:

   1 * 0.1 = 0.1

2. Repeat this process ten times.

3. After repeating the multiplication, the resulting number will have a single digit after the decimal point.

4. From this resulting number, extract two digits from the middle and sum them.

Let's compute this multiplication:

0.1 (1st multiplication)  
0.01 (2nd multiplication)  
0.001 (3rd multiplication)  
0.0001 (4th multiplication)  
0.00001 (5th multiplication)  
0.000001 (6th multiplication)  
0.0000001 (7th multiplication)  
0.00000001 (8th multiplication)  
0.000000001 (9th multiplication)  
0.0000000001 (10th multiplication)

After ten multiplications, the result would be 0.0000000001.

From this result, the middle two digits are "0" and "0". Summing them up:

0 + 0 = 0

So, the sum of the two digits from the middle of the result is 0.
'''
	if loc == 'right':
		if x == "0.1":
			return r'''To find the sum of three thousand digits from the right of the result of repeating the multiplication of 1 by 0.1 ten billion times, we can reason that after so many multiplications, the result will be very close to 0. 

However, let's calculate the number of digits and the sum to confirm:

After multiplying 1 by 0.1 ten billion times, we'll have a number with 10,000,000,001 digits before the decimal point, followed by 10 billion zeros after the decimal point, and then a single digit. 

The sum of the last three thousand digits will depend on the digits right before the decimal point. Since all the digits after the decimal point are zeros, the sum will be determined by the digits before the decimal point.

Let's find the last three thousand digits:  

1. We'll take the last three digits before the decimal point.

2. Sum them up.

Given that we're multiplying 1 by 0.1 repeatedly, the last three digits before the decimal point will be from the initial value of 1, which is 001. 

So, the sum of the last three thousand digits will be:

\(0 + 0 + 1 = 1\).

Therefore, the sum of the last three thousand digits of the result is 1.'''
		if x == "0.5":
			return r'''To find the sum of the two digits from the right of the result of repeating the multiplication of 1 by 0.5 thirteen times, let's compute the result:

1. Start by performing the multiplication of 1 by 0.5:

   \(1 \times 0.5 = 0.5\)

2. Repeat this process twelve more times:

   \(0.5\) (2nd multiplication)
   \(0.25\) (3rd multiplication)
   \(0.125\) (4th multiplication)
   \(0.0625\) (5th multiplication)
   \(0.03125\) (6th multiplication)
   \(0.015625\) (7th multiplication)
   \(0.0078125\) (8th multiplication)
   \(0.00390625\) (9th multiplication)
   \(0.001953125\) (10th multiplication)
   \(0.0009765625\) (11th multiplication)
   \(0.00048828125\) (12th multiplication)
   \(0.000244140625\) (13th multiplication)

After thirteen multiplications, the result is \(0.000244140625\).

From this result, the two digits from the right are "2" and "5". Summing them up:

\(2 + 5 = 7\)

So, the sum of the two digits from the right of the result is \(7\).'''

def genSum():
	numd = ['two', 'nine', 'two thousands']
	t = ['one', 'ten', 'three thousands', 'ten billions']
	samples = []
	for i in range(100):
		loc = random.choice(['middle', 'right'])
		j = random.randrange(len(numd))
		k = random.randrange(j, len(t))
		if loc == 'right':
			x = random.choice(['0.1', '0.5'])
			if x == '0.1':
				ans = '1'
			else:
				ans = '7'
				j = 0
		else:
			x = '0.1'
			if k == 0:
				ans = '1'
			else:
				ans = '0'

		samples.append({"question":q(numd[j], loc, x, t[k]), "prompt":prompt(loc, x, t[k]), "answer":ans})
	with open("task5.json", "w") as fout:
		fout.write(json.dumps(samples))

genSum()
