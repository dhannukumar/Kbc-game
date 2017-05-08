# Yeh exercise hai
# Har line of code se pehle aapko ek line mei comment mei daal kar likhna hai, ki uss line of code ka matlab kya hai
# Aap jyada comments bhi likh sakte hai, jitne jyada comments likhenge, utna aapkya fayda hoga

# Aap yeh code execute karke dekho

# Question 1
# Ab hum ek flag variable ka use karenge apne program ko control karne ke liye.
# flag koi bhi normal variable and iska naam kuch bhi rakh sakte ho.

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
	print "Yeh flag ke bahar hai", index


# Humne toh loop 10 baar chalane ko kaha tha, toh loop sirf 8 baar kyu execute hua?
# Flag variable ke vajah se.

# Issi concept ka use karke apne KBC game ko aise modify karo jisse ki ----
# Agar user galat answer karta hai toh aap wahi par loop se bahar nikal jaye aur print karein - "KBC Khatam. Phir kheliyega!"

flag=True
questions_list = ["Which of these sounds would you associate with the heart ?","Who is the 'Bharat Ka Veer Putra Aaccording to the title of a 2013 TV Series?","In 2013, where did the natural calamity known as Himalayan tsunami occur?","Which film is this song from ?","In the Ramayana, Which demon impersonated Rama's voice, screaming, 'Lakshman! Help me'?","Who is the only leader to be elected Prime Minister of Pakistan three times ?","The black widow, which eats the male counterpart after mating, as a female species of which animal?","Douglas Engelbert, who passed away in 2013, is credited as the inventor of which of these products?","In 1850, the first experimental electric telegraph line in India was set up between Calcutta and which place?","Which of these persons has not walked on the Moon?","With Which of these states do Chhattisgarh, Jharkhand and Andhra Pradesh all share their borders?","The first world championship in what sport is planned to be held in 2017, though the game has been played since 1877?","Which is the largest living species of tortoise in the world, which may weigh about 400 kg?","According to legend, which of these Rishis regained his youth by a celestial favor ?","On a restaurant menu, which of these items is often listed as 'Jeera', 'Curd', 'Boiled' or 'Fried'?"]
# ek question list banaya hai usme aur 15 question dale hain.
option1_list = ["Tring Tring", "Tipu Sultan",         "Uttrakhand",        "Mere Dad Ki Maruti",  "Surpanakha",  "Syed Yousaf Raza Gillani",  "Sloth",   "Mobile Phone",    "Diamond Harbour",   "Charles Duke",      "Madhya Pradesh",      "Test Cricket",          "Sulcata Tortoise",       "Agastya",        "Manchurian"]
# ek option1_list banaya hain aur usme sare question ke pehle option dale hain.
option2_list = ["Tap Tap",     "Chandragupta Maurya", "Arunachal Pradesh", "Chennai Express",     "Khara",       "Benazir Bhutto",            "Ant",     "Computer Mouse",  "Darjeeling",        "James A Lovell",    "Odisha",              "Rugby Union",           "Grenada Tortoise",       "Durvasa",        "Burger"]
# ek option2_list banaya hain aur usme sare question ke doosre option dale hain.
option3_list = ["Click Click", "Maharana Pratap",     "Jammu and Kashmir", "Ghanchakkar",         "Maricha",     "Liaqat Ali Khan",           "Spider",  "Bluetooth Mouse", "Murshidabad",       "Alan Bean",         "Bihar",               "Kabaddi",               "Golden Greek Tortoise",  "Chyavana",       "Rice"]
# ek option3_list banaya hain aur usme sare question ke teesre option dale hain.
option4_list = ["Dhak Dhak",   "Ashoka",              "Sikkim",            "Race 2",              "Dushana",     "Nawaz Sharif",              "Termite", "Digital camera",  "Dhaka",             "Pete Conrad",       "Uttar Pradesh",       "Carrom",                "Galapagos Tortoise",     "Charaka",        "Pasta"]
# ek option4_list banaya hain aur usme sare question ke chautha option dale hain.
answer_list = (4,3,1,2,3,4,3,4,4,2,2,1,3,3,3)
# ab hamne answer list banaya hain aur usme sare question ke sahi answer dale hain.
prize  = (1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,"25lakh","50lakh","1cr")
# ab hamne ek prize list banai hain usme hamne 1000 se lekar 1cr tak ki prize dali hain.
for index in range(15):
    if flag:
        print "apka question yeh hai"
        print "q-",questions_list[index]
        print "1-",option1_list[index]
        print "2-",option2_list[index]
        print "3-",option3_list[index]
        print "4-",option4_list[index]
        var1 = int(raw_input("enter your answer\n"))
        if var1 == answer_list[index]:
           print "congrats, sahi jawaab"
           print "aap",prize[index], "jeet chuke hai"
        elif var1!=answer_list[index]:
            flag=False
            print "aapne galat ans diya hai aapka game khatam hua"
        if prize[index]==10000:
            print "aapka pehla padav pura huaa"
        if prize[index]==320000:
            print "aapka dusra padav pura huaa"
        if prize[index]=="1cr":
            print "Congrats aap 1 crore jeet chuke ho"






# HINT
# Iske liye aap flag use karoge. Chaliye iss variable ko flagRightAnswer kehte hai
# Galat answer karne par aap flagRightAnswer ko False set kar do
# Loop mei aate hi check karo and dekho agar flagRightAnswer True hai tab hi loop ke andar ka code execute karo

# Ab aap issi program ko aise modify karo ki loop ke bahar aane ke baad bhi jo index ki value hai usse use karke
# aap user ko batao woh kitne paise jeeta hai. User apne pichle padav ke paise hi jeetega.
# Toh agar user ne 12th question galat kiya toh aap user ko doosre padaav ke paise doge.
flag=True
questions_list = ["Which of these sounds would you associate with the heart ?","Who is the 'Bharat Ka Veer Putra Aaccording to the title of a 2013 TV Series?","In 2013, where did the natural calamity known as Himalayan tsunami occur?","Which film is this song from ?","In the Ramayana, Which demon impersonated Rama's voice, screaming, 'Lakshman! Help me'?","Who is the only leader to be elected Prime Minister of Pakistan three times ?","The black widow, which eats the male counterpart after mating, as a female species of which animal?","Douglas Engelbert, who passed away in 2013, is credited as the inventor of which of these products?","In 1850, the first experimental electric telegraph line in India was set up between Calcutta and which place?","Which of these persons has not walked on the Moon?","With Which of these states do Chhattisgarh, Jharkhand and Andhra Pradesh all share their borders?","The first world championship in what sport is planned to be held in 2017, though the game has been played since 1877?","Which is the largest living species of tortoise in the world, which may weigh about 400 kg?","According to legend, which of these Rishis regained his youth by a celestial favor ?","On a restaurant menu, which of these items is often listed as 'Jeera', 'Curd', 'Boiled' or 'Fried'?"]
# ek question list banaya hai usme aur 15 question dale hain.
option1_list = ["Tring Tring", "Tipu Sultan",         "Uttrakhand",        "Mere Dad Ki Maruti",  "Surpanakha",  "Syed Yousaf Raza Gillani",  "Sloth",   "Mobile Phone",    "Diamond Harbour",   "Charles Duke",      "Madhya Pradesh",      "Test Cricket",          "Sulcata Tortoise",       "Agastya",        "Manchurian"]
# ek option1_list banaya hain aur usme sare question ke pehle option dale hain.
option2_list = ["Tap Tap",     "Chandragupta Maurya", "Arunachal Pradesh", "Chennai Express",     "Khara",       "Benazir Bhutto",            "Ant",     "Computer Mouse",  "Darjeeling",        "James A Lovell",    "Odisha",              "Rugby Union",           "Grenada Tortoise",       "Durvasa",        "Burger"]
# ek option2_list banaya hain aur usme sare question ke doosre option dale hain.
option3_list = ["Click Click", "Maharana Pratap",     "Jammu and Kashmir", "Ghanchakkar",         "Maricha",     "Liaqat Ali Khan",           "Spider",  "Bluetooth Mouse", "Murshidabad",       "Alan Bean",         "Bihar",               "Kabaddi",               "Golden Greek Tortoise",  "Chyavana",       "Rice"]
# ek option3_list banaya hain aur usme sare question ke teesre option dale hain.
option4_list = ["Dhak Dhak",   "Ashoka",              "Sikkim",            "Race 2",              "Dushana",     "Nawaz Sharif",              "Termite", "Digital camera",  "Dhaka",             "Pete Conrad",       "Uttar Pradesh",       "Carrom",                "Galapagos Tortoise",     "Charaka",        "Pasta"]
# ek option4_list banaya hain aur usme sare question ke chautha option dale hain.
answer_list = (4,3,1,2,3,4,3,4,4,2,2,1,3,3,3)
# ab hamne answer list banaya hain aur usme sare question ke sahi answer dale hain.
prize  = (1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,"25lakh","50lakh","1cr")
# ab hamne ek prize list banai hain usme hamne 1000 se lekar 1cr tak ki prize dali hain.
padav = [0,0,0,0,10000,10000,10000,10000,10000,320000,320000,320000,320000,320000,"1cr"]
for index in range(16):
    if flag:
        print "apka question yeh hai"
        print "q-",questions_list[index]
        print "1-",option1_list[index]
        print "2-",option2_list[index]
        print "3-",option3_list[index]
        print "4-",option4_list[index]
        var1 = int(raw_input("enter your answer\n"))
        if var1 == answer_list[index]:
           print "congrats, sahi jawaab"
           print "aap",prize[index], "jeet chuke hai"
        elif var1!=answer_list[index]:
            flag=False
            print "aapne galat ans diya hai aapka game khatam hua"
            print "aaj app ",padav[index], "rupey jeet chuke ho"
        if padav[index]==10000:
            print "aapka pehla padav pura huaa"
        if padav[index]==320000:
            print "aapka dusra padav pura huaa"
        if padav[index]=="1cr":
            print "Congrats aap 1 crore jeet chuke ho"






# User answer mei option dene ki jagah - user quit likh kar game se withdraw bhi kar sakta hai
# But ismei user ko jis question par quit kiya hai, utne paise dene hai
# Socho isse logically kaise karoge. Pehle pen and paper ka use karke sochna. Uske baad karna.
# Jaise humne flag ke baarei mei socha tha, kya aap aisa kuch yaha soch sakte hai?
# Flag ek tareeke se ek temporary variable tha jo kuch information store kar raha tha

# Finally, aapka aisa message print hona chahiye.
# "Aap ne game se quit kar liya hai. Par aaj aap ghar le kar ja rahe hai 320000 rupees."
# (320000 ko user ki jeeti hue paise se badloge)
flag=True
questions_list = ["Which of these sounds would you associate with the heart ?","Who is the 'Bharat Ka Veer Putra Aaccording to the title of a 2013 TV Series?","In 2013, where did the natural calamity known as Himalayan tsunami occur?","Which film is this song from ?","In the Ramayana, Which demon impersonated Rama's voice, screaming, 'Lakshman! Help me'?","Who is the only leader to be elected Prime Minister of Pakistan three times ?","The black widow, which eats the male counterpart after mating, as a female species of which animal?","Douglas Engelbert, who passed away in 2013, is credited as the inventor of which of these products?","In 1850, the first experimental electric telegraph line in India was set up between Calcutta and which place?","Which of these persons has not walked on the Moon?","With Which of these states do Chhattisgarh, Jharkhand and Andhra Pradesh all share their borders?","The first world championship in what sport is planned to be held in 2017, though the game has been played since 1877?","Which is the largest living species of tortoise in the world, which may weigh about 400 kg?","According to legend, which of these Rishis regained his youth by a celestial favor ?","On a restaurant menu, which of these items is often listed as 'Jeera', 'Curd', 'Boiled' or 'Fried'?"]
# ek question list banaya hai usme aur 15 question dale hain.
option1_list = ["Tring Tring", "Tipu Sultan",         "Uttrakhand",        "Mere Dad Ki Maruti",  "Surpanakha",  "Syed Yousaf Raza Gillani",  "Sloth",   "Mobile Phone",    "Diamond Harbour",   "Charles Duke",      "Madhya Pradesh",      "Test Cricket",          "Sulcata Tortoise",       "Agastya",        "Manchurian"]
# ek option1_list banaya hain aur usme sare question ke pehle option dale hain.
option2_list = ["Tap Tap",     "Chandragupta Maurya", "Arunachal Pradesh", "Chennai Express",     "Khara",       "Benazir Bhutto",            "Ant",     "Computer Mouse",  "Darjeeling",        "James A Lovell",    "Odisha",              "Rugby Union",           "Grenada Tortoise",       "Durvasa",        "Burger"]
# ek option2_list banaya hain aur usme sare question ke doosre option dale hain.
option3_list = ["Click Click", "Maharana Pratap",     "Jammu and Kashmir", "Ghanchakkar",         "Maricha",     "Liaqat Ali Khan",           "Spider",  "Bluetooth Mouse", "Murshidabad",       "Alan Bean",         "Bihar",               "Kabaddi",               "Golden Greek Tortoise",  "Chyavana",       "Rice"]
# ek option3_list banaya hain aur usme sare question ke teesre option dale hain.
option4_list = ["Dhak Dhak",   "Ashoka",              "Sikkim",            "Race 2",              "Dushana",     "Nawaz Sharif",              "Termite", "Digital camera",  "Dhaka",             "Pete Conrad",       "Uttar Pradesh",       "Carrom",                "Galapagos Tortoise",     "Charaka",        "Pasta"]
# ek option4_list banaya hain aur usme sare question ke chautha option dale hain.
answer_list = (4,3,1,2,3,4,3,4,4,2,2,1,3,3,3)
# ab hamne answer list banaya hain aur usme sare question ke sahi answer dale hain.
prize  = (1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,"25lakh","50lakh","1cr")
# ab hamne ek prize list banai hain usme hamne 1000 se lekar 1cr tak ki prize dali hain.
padav = [0,0,0,0,10000,10000,10000,10000,10000,320000,320000,320000,320000,320000,"1cr"]
for index in range(15):
    if flag:
        print "apka question yeh hai"
        print "q-",questions_list[index]
        print "1-",option1_list[index]
        print "2-",option2_list[index]
        print "3-",option3_list[index]
        print "4-",option4_list[index]
        var1 = (raw_input("enter your answer\n"))
        if var1 == "quit":
            print "Aap ne game se quit kar liya hai. Par aaj aap ghar le kar ja rahe hai",padav[index], "rupees."
            flag = False
        elif int(var1) == answer_list[index]:
           print "congrats, sahi jawaab"
           print "aap",prize[index], "jeet chuke hai"
        else:
            var1!=answer_list[index]
            flag=False
            print "aapne galat ans diya hai aapka game khatam hua"
            print "ajj aap",padav[index],"jeet chuke ho."
        if prize[index]==10000:
            print "aapka pehla padav pura huaa"
        if prize[index]==320000:
            print "aapka dusra padav pura huaa"
        if prize[index]=="1cr":
            print "Congrats aap 1 crore jeet chuke ho"
