import numpy as np

ANSWERS = [
	" It is certain.",
	"It is decidedly so.",
	"Without a doubt.",
	"Yes definitely.",
	"You may rely on it.",
	"As I see it, yes.",
	"Most likely.",
	"Outlook good.",
	"Yes.",
	"Signs point to yes.",
	"Reply hazy, try again.",
	"Ask again later.",
	"Better not tell you now.",
	"Cannot predict now.",
	"Concentrate and ask again.",
	" Don't count on it.",
	"My reply is no.",
	"My sources say no.",
	"Outlook not so good.",
	"Very doubtful."
]



def eight_ball():
	input("I'm the magic 8 ball man! Ask me a yes or no question.\n")
	answer = np.random.choice(ANSWERS)
	print()
	print(answer)

if __name__ == "__main__":
	eight_ball()
