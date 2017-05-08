# Yeh exercise hai
# Har line of code se pehle aapko ek line mei comment mei daal kar likhna hai, ki uss line of code ka matlab kya hai
# Aap jyada comments bhi likh sakte hai, jitne jyada comments likhenge, utna aapkya fayda hoga

# Aap yeh code execute karke dekho

# Question 1
# Ab hum ek flag variable ka use karenge apne program ko control karne ke liye. flag koi bhi normal variable and
# iska naam kuch bhi rakh sakte ho.

flag=True
for index in range(10):
	# if flag likhne se, jaise hi flag False set ho jayega, toh yeh sab execute nahi hoga
	if flag:
		# Yaha par aap woh saara kaam karenge jo aap chahte hai na ho jab flag False set ho jaye

		# Yeh condition batati hai flag kab False set karna hai. Aap iss condition ke jagah apne hisaab se koi bhi
		# condition likh sakte hai, jab aap chahte ki Flag false set ho jaye
		if index>6:
			flag=False

		print "Yeh flag ke andar hai", index

	# Yeh flag ke bahar hai toh yeh toh execute hoga hi, chahe flag ki value kuch bhi ho
	# print "Yeh flag ke bahar hai", index


# Humne toh loop 10 baar chalane ko kaha tha, toh loop sirf 8 baar kyu execute hua?
# Flag variable ke vajah se.

# Issi concept ka use karke apne KBC game ko aise modify karo jisse ki ----
# Agar user galat answer karta hai toh aap wahi par loop se bahar nikal jaye aur print karein -
# "KBC Khatam. Phir kheliyega!"


#aur iss program mei ek aur kam karna hai
# Ab aap issi program ko aise modify karo ki loop ke bahar aane ke baad bhi jo index ki value hai usse use karke aap user ko batao woh kitne paise
#  jeeta hai. User apne pichle padav ke paise hi jeetega. Toh agar user ne 12th question galat kiya toh aap user ko doosre padaav ke paise doge.


# User answer mei option dene ki jagah - user quit likh kar game se withdraw bhi kar sakta hai
# But ismei user ko jis question par quit kiya hai, utne paise dene hai
# Socho isse logically kaise karoge. Pehle pen and paper ka use karke sochna. Uske baad karna.
# Jaise humne flag ke baarei mei socha tha, kya aap aisa kuch yaha soch sakte hai?
# Flag ek tareeke se ek temporary variable tha jo kuch information store kar raha tha



questions = ["Which of these sounds would you associate with the heart ?"," Who is the 'Bharat Ka Veer Putra Aaccording to the title of a 2013 TV Series ?",
			"In 2013 where did the natural calamity known as Himalayan tsunami occur?"," In the Ramayana Which demon impersonated Ramas voice screaming 'Lakshman! Help me' ?",
			"Who is the only leader to be elected Prime Minister of Pakistan three times ?",
			"The black widow, which eats the male counterpart after mating, as a female species of which animal ?",
			" Douglas Engelbert, who passed away in 2013, is credited as the inventor of which of these products ?","Which of these persons has not walked on the Moon ?",
			"The 'sasural' of which of these international sports person from India is in Pakistan ?","Which team retained the ashes Trophy in 2013 ?",

			"With Which of these cards would you associate the phrase 'Aam Aadmi ka Adhikaar'?"," Which of these words or phrases was famously used in many of his dialogues by actor Pran?",
			"who is the CEO of google","To respect whose word did the five Pandavas marry Draupadi?",
			"From which country did India buy an aircraft carrier which was renamed as INS Vikramaditya?"]




				# 1						2						3					4					5						6				7
pehla_option = [" Tring Tringc",  " Tipu Sultan",        " Uttrakhand",       " Surpanakha",   " Syed Yousaf Raza Gillani"," Sloth",        " Mobile Phone",
					# 8					9						10					11				12							13				14						15
				" Charles Duke",  " Saina Nehwal",       " Australia",        " PAN Card",     " Khamosh",                 " satya nadela", " krishna",          " france"]


			# 1						2						3					4					5						6				7
dusra_option = [" Tap Tap"     ,  " Chandragupta Maurya"," Arunachal Pradesh"," Khara"   ,     " Benazir Bhutto" ,         " Ant"   ,       " Computer Mouse" ,
				# 8                    9                        10                    11                12                      13                14                        15
				" James A Lovell"," Saina Mirza"        ," South Africa"     ," Voter ID Card"," Barkhurdaar",             " sunder pichai"," indra"      ,      " russia"]


				# 1						2						3					4					5						6				7
teesre_option = [" Click Click" ,  " Maharana Pratap",    " Jammu and Kashmir"," Maricha"      ," Liaqat Ali Khan",         " Spider",       " Bluetooth Mouse",
				 # 8                    9                        10                    11                12            13                14                        15
				 " Alan Bean"," Anisa Sayyed",  " West Indies",        " AADHAR Card",      " Jaani" ,       " ambani" ,                 " kunti",        " england"]



				# 1						2						3					4					5						6				7
chauthe_option = [" Dhak Dhak",     " Ashoka",             " Sikkim",           " Dushana",      " Nawaz Sharif",            " Termite",      " Digital camera",
				  # 8                    9                        10                    11                12              13                14                        15
				  " Pete Conrad"," Anjum Chopra",  " England",            " Ration Card",      " Babu Moshai",  " modi"         ,           " madri",        " germany" ,]

index = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
answer_list = [4,4,1,3,4,3,2,3,2,  4,3,2,2,3,2]
answer_list1 =[" Dhak Dhak"," Ashoka"," Uttrakhand"," Maricha"," Nawaz Sharif"," Spider", " Computer Mouse"," Alan Bean"," Saina Mirza",
			   " England", " AADHAR Card"," Barkhurdaar"," sunder pichai"," kunti"," russia"]
prize =[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
count =0
padaav = [0,0,0,0,10000,10000,10000,10000,10000,320000,320000,320000,320000,320000,10000000]
import random

lifeline_counter = 0


flag =True
for p in range(15):
	if flag:
		print "'''"
		print "apka",index[p],"question hai yeh"
		print questions[p]
		print "1 --" + pehla_option[p]
		print "2 --" + dusra_option[p]
		print "3 --" + teesre_option[p]
		print "4 --" + chauthe_option[p]
		user_input =raw_input("can you select correct answer,what you think about it--: \n"+'you can quite game by typing "quit":-\n'+"you can use lifeline "+"service by typing 'lifeline';'''\n")
		list_list = [pehla_option[p], dusra_option[p], teesre_option[p], chauthe_option[p]]
		number_times = 2

		if ("lifeline" ==user_input):
			random_items =random.sample(list_list,number_times)
			print "1--" +answer_list1[p]
			if lifeline_counter == 0:
				if random_items[0] == answer_list1[p]:
					print "2--" + random_items[1]
				else:
					print "2--" + random_items[0]
				user_input1 = raw_input("enter a answer''\n")
				if "quit" == user_input1:  # yha humne ye chek kiya hai agar user quit likhta hai to game khatam
					flag = False  # karne k liye humne flag ko false kar kiya hai isse game quit ho jayegi
					print "Aap ne game se quit kar liya hai"  # yha kuch quote print kiya hia
				elif 1 == int(user_input1):  # yha humne ye dekha hai agar user 1 likhta hai to uska answer sahi hoga kyuki
					# upper humne pehle number option pe har bar sahi answer hi print kiya hai
					count = count + 1  # yha sahi jawab dene par counter 1 plus kar diya hai isse number of sahi question pta chl jayenge
					print "Congrats, Sahi jawaab!"  # yha kuch quotes print kiya hai
				else:  # agar user ne fir se galat jawab de diya to ussse kuch aur quotes print karne k liye hai
					print "Afsos, par yeh galat jawaab hai!"
					print "lekin ajj aap ", padaav[p], " rupees ghr lekar ja rhe hai"
					flag = False
			else:
				print "you lost your game because you are using your lifeline 2 times.\n"
				print "lekin ajj aap rupees ", padaav[p], "ghr lekar ja rhe hai"
				flag = False
			lifeline_counter = lifeline_counter - 1

		elif ("quit" == user_input):
			print "Aaap ne game se quit kar diya ,matlab apki fatt ke hath mei aa gyi hai ,,KBC Khatam. Phir kheliyega!\n"
			print "lekin ajj aap", padaav[p]," rupees ghr lekar ja rhe hai"
			flag = False
		elif (answer_list[p]) ==int(user_input):
			print "Congrats, Sahi jawaab!"
			print "aap",prize[p] ," rupess jeet chuke hai "
			count =count +1
		else:
			print "Afsos, par yeh galat jawaab hai!"
			print "KBC Khatam. Phir kheliyega!"
			print "jeete hai" ,padaav[p],
			flag =False

		if (prize[p] ==10000):
			print "Congrats! Aapka padaav pura ho gaya hai."
		elif (prize[p] ==320000):
			print "Congrats! Aapka doosra padaav pura ho gaya hai."
		elif (prize[p] ==10000000):
			print "Congrats! Aap ek crore rupye jeet gaye hai."


print "apke " +str(len(questions))+" questions mei se "+str(count) +" question sahi hai"

# Finally, aapka aisa message print hona chahiye.
# "Aap ne game se quit kar liya hai. Par aaj aap ghar le kar ja rahe hai 320000 rupees." (320000 ko user ki jeeti hue paise se badloge)
