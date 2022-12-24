import time
import random

string_dict = {1 : "A teacher's professional duties may extend beyond formal teaching. Outside of the classroom teachers may accompany students on field trips, help with the organization of school functions, and serve as supervisors for extracurricular activities.",
			   2 : "Scolding is something common in student life. Being a naughty boy, I am always scolded by my parents. But one day I was severely scolded by my English teacher. But that day, I could not resist the temptation that an adventure of Nancy Drew offered.",
			   3 : "Days are not of equal value in one’s life. Some bring happiness while others bring sadness. Sadness and happiness both are equally important to man’s life, since they are the two sides of a coin. As we cannot forget the happiest day, we are unable to forget the saddest day of our life too.",
			   4 : "Studying is the main source of knowledge. Books are indeed never failing friends of man. For a mature mind, reading is the greatest source of pleasure and solace to distressed minds. The study of good books ennobles us and broadens our outlook.",
			   5 : "Recently, an exhibition ‘Building A New India’ was held in the capital. It was organized by the Ministry of Information and Broadcasting, Government of India. The exhibition was set up in the Triveni Kala Sangam.",
			   6 : "A teacher is called builder of the nation. The profession of teaching needs men and women with qualities of head and heart. There are many teachers in our school and a large number of teachers among them are highly qualified. I have great respect for all of them."
			  }

#print(string_dict)
while True:
	key, string = random.choice(list(string_dict.items()))
	print("TYPE THE BELOW CONTEXT TO KNOW YOUR TYPING SPEED.....\n",string)
	wc = len(string.split())
	print('-----------------------------------------')
	in_time = time.time()
	inputtext = str(input('Enter the Sentence: \n'))
	st_time = time.time()
	timetaken = st_time - in_time
	wpm = wc/timetaken
	print('-----------------------------------------')
	print('No. OF WORDS - ',wc)
	print('WPM - ',round(wpm*100))
	print('TIME TAKEN - ',timetaken)
	print('-----------------------------------------')
	opt = input('Want to continue (Y/n) ?')
	if(opt == 'Y' or opt == 'y'):
		continue
	elif(opt == 'N' or opt == 'n'):
		break
	else:
		print('You choose the wrong option ...')
		break