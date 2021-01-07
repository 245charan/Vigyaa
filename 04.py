# Python program to convert the time in numerals into words

''' Use if else if statement to convert the time into words '''
#Algorithm

# 1. create a wordlist[] consisting of 
        # zero to twentynine
# 2. if minutes = 0 append O' clcok
    # else if minutes  = 1 print one minute past to wordlist[hour]
    # else if minutes = 59 print one minute to wordlist[hour +1]
    # else if minutes = 15 print quater past to wordlist[hour]
    # else if minutes = 45 print half past to wordlist[hour]
    # else if minutes <= 30 print wordlist[minutes] minutes past wordlist[hour]
    # else if minutes > 30 print wordlist[60 - minutes] minutes to wordlist[hour +1]



 
def numeral_to_Words(hours, minutes): 
	wordlist = ["zero", "one", "two", "three", "four", 
			"five", "six", "seven", "eight", "nine", 
			"ten", "eleven", "twelve", "thirteen", 
			"fourteen", "fifteen", "sixteen", 
			"seventeen", "eighteen", "nineteen", 
			"twenty", "twenty one", "twenty two", 
			"twenty three", "twenty four", 
			"twenty five", "twenty six", "twenty seven", 
			"twenty eight", "twenty nine"]
# mod by 12 to use time in 12 hours format	

	if (minutes == 0): 
		print(wordlist[hours], "o' clock")
	elif (minutes == 1):
	    print("one minute past", wordlist[hours])
	elif (minutes == 59):
	    print("one minute to", wordlist[(hours % 12) + 1])
	elif (minutes == 15):
	    print("quarter past", wordlist[hours])
	elif (minutes == 30):
	    print("half past", wordlist[hours])
	elif (minutes == 45):
	    print("quarter to", (wordlist[(hours % 12) + 1]))
	elif (minutes <= 30):
	    print(wordlist[minutes],"minutes past", wordlist[hours])
	elif (minutes > 30):
	    print(wordlist[60 - minutes], "minutes to", wordlist[(hours % 12) + 1])

if __name__ == '__main__':
    hours = int(input()) 
    minutes = int(input())
    numeral_to_Words(hours, minutes); 