import random
import json
words_with_in = [
    "Paint",
    "Faint",
    "Saint",
    "Saintly",
    "Quinoa",
    "Vintage",
    "Painting",
    "Paining",
    "Painter",
    "Sprinter",
    "Sprinting",
    "Rescind",
    "Minty",
    "Minted",
    "Hinted",
    "Hinting",
    "Inter",
    "Intern",
    "Intersect",
    "Pint",
    "Printing",
    "Printer",
    "Printed",
    "Pointing",
    "Pointe",
    "Jointing",
    "Jointed",
    "Quintet",
    "Quinto",
    "Quintuplet",
    "Quintessential",
    "Quintuple",
    "Pintle",
    "Pint-sized",
    "Splinter",
    "Spinter",
    "Splint",
    "Splinted",
    "Splinting",
    "Feint",
    "Taint",
    "Vintner",
    "Vintaged",
    "Vintaging",
    "Reprint",
    "Printing",
    "Imprint",
    "Unprint",
    "Coinage",
    "Rejoined"
]
words_with_on = [
    "Monitor",
    "Condom",
    "Concede",
    "Condone",
    "Control",
    "Convoy",
    "Convex",
    "Convict",
    "Convince",
    "Confine",
    "Confide",
    "Conflict",
    "Conflate",
    "Conform",
    "Confound",
    "Contour",
    "Contort",
    "Context",
    "Content",
    "Contain",
    "Contact",
    "Consist",
    "Console",
    "Consult",
    "Consume",
    "Consign",
    "Confirm",
    "Connect",
    "Conjoin",
    "Concert",
    "Concise",
    "Concoct",
    "Conform",
    "Conquer",
    "Control",
    "Convene",
    "Converge",
    "Convert",
    "Conserve",
    "Confound",
    "Consider",
    "Condemn",
    "Condone",
    "Conduct",
    "Confess",
    "Confuse",
    "Conceal",
    "Conceive",
    "Conclude",
    "Concrete"
]
N = min(len(words_with_in), len(words_with_on))
def q_in(x1, x2):
	return f"Solve rebus. There is a picture. The green cube is in the white one. The letter {x1} is carved on the green cube, letter {x2} on white. What is this picture about?"
def q_inside(x1, x2):
	return f"Solve rebus. There is a picture. The green cube is inside the white one. The letter {x1} is carved on the green cube, letter {x2} on white. What is this picture about?"
def q_on(x1, x2):
	return f"Solve rebus. There is a picture. The yellow cube is on the blue one. The letter {x2} is carved on the blue cube, letter {x1} on yellow. What is this picture about?"
def q_under(x1, x2):
	return f"Solve rebus. There is a picture. The yellow cube is under the blue one. The letter {x1} is carved on the blue cube, letter {x2} on yellow. What is this picture about?"

def prompt_on(x1, x2):
	return f'''1. **Visual Description**: 
   - The blue cube has the letter "{x1}" carved on it.
   - The yellow cube has the letter "{x2}" carved on it.
   - The blue cube (with "{x1}") is on top of the yellow cube (with "{x2}").

2. **Interpretation**: 
   - When you put the letter "{x1}" on top of the letter "{x2}," it forms the phrase "{x1} on {x2}."

3. **Phonetic Connection**: 
   - The phrase "{x1} on {x2}" sounds like the English word "{x1}on{x2}."

4. **Conclusion**: 
   - Therefore, the rebus is representing the word "{x1}on{x2}."

So, "{x1}on{x2}" is the correct answer because the rebus uses a clever visual and phonetic play to combine the letters and their positions into a recognizable word.'''


def prompt_under(x1, x2):
	return f'''1. **Visual Description**: 
   - The blue cube has the letter "{x1}" carved on it.
   - The yellow cube has the letter "{x2}" carved on it.
   - The blue cube (with "{x2}") is under the yellow cube (with "{x1}").

2. **Interpretation**: 
   - When you put the letter "{x1}" on top of the letter "{x2}," it forms the phrase "{x1} on {x2}."

3. **Phonetic Connection**: 
   - The phrase "{x1} on {x2}" sounds like the English word "{x1}on{x2}."

4. **Conclusion**: 
   - Therefore, the rebus is representing the word "{x1}on{x2}."

So, "{x1}on{x2}" is the correct answer because the rebus uses a clever visual and phonetic play to combine the letters and their positions into a recognizable word.'''

def prompt_in(x1,x2):
	return f'''To solve this rebus, let's break down the elements step-by-step:

	1. **Visual Description**:
	   - The white cube has the letter "{x2}" carved on it.
	   - The green cube has the letter "{x1}" carved on it.
	   - The green cube (with "{x1}") is in the white cube (with "{x2}").

	2. **Interpretation**:
	   - When you see the letter "{x1}" in the letter "{x2}," it forms the phrase "{x1} in {x2}."

	3. **Phonetic Connection**:
	   - The phrase "{x1} in {x2}" sounds like the word "{x1}in{x2}."

	4. **Conclusion**:
	   - Therefore, the rebus is representing the word "{x1}in{x2}."

	So, the rebus puzzle is depicting the word "{x1}in{x2}."'''

def prompt_inside(x1,x2):
	return f'''To solve this rebus, let's break down the elements step-by-step:

	1. **Visual Description**:
	   - The white cube has the letter "{x2}" carved on it.
	   - The green cube has the letter "{x1}" carved on it.
	   - The green cube (with "{x1}") is inside the white cube (with "{x2}").

	2. **Interpretation**:
	   - When you see the letter "{x1}" inside the letter "{x2}," it forms the phrase "{x1} in {x2}."

	3. **Phonetic Connection**:
	   - The phrase "{x1} in {x2}" sounds like the word "{x1}in{x2}."

	4. **Conclusion**:
	   - Therefore, the rebus is representing the word "{x1}in{x2}."

	So, the rebus puzzle is depicting the word "{x1}in{x2}."'''
def mkquestion(prep, index):
	if prep == "on":
		x = words_with_on[index].split("on")
		x1, x2 = x[0], "".join(x[1:])
		return q_on(x1, x2), prompt_on(x1, x2), words_with_on[index]
	if prep == "under":
		x = words_with_on[index].split("on")
		x1, x2 = x[0], "".join(x[1:])
		return q_under(x1, x2), prompt_under(x1, x2), words_with_on[index]
	if prep == "in":
		x = words_with_in[index].split("in")
		x1, x2 = x[0], "".join(x[1:])
		return q_in(x1, x2), prompt_in(x1, x2), words_with_in[index]
	x = words_with_in[index].split("in")
	x1, x2 = x[0], "".join(x[1:])
	return q_inside(x1, x2), prompt_inside(x1, x2), words_with_in[index]

def rebus():
	preps = ["on", "under", "in", "inside"]
	samples = []
	for i in range(N):
		prep = random.choice(preps)
		q, prompt, ans = mkquestion(prep, i)
		print(q)
		samples.append({"question":q, "prompt":prompt, "answer":ans})
	with open("task4.json", "w") as fout:
		fout.write(json.dumps(samples))

words_with_in = [i.lower() for i in words_with_in]
words_with_on = [i.lower() for i in words_with_on]
rebus()