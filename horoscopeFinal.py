"""Horoscope reader. This program asks the user for their birth month and birth day.
Based on the users answer, it tells them what their zodiac sign is.
The program then uses this information to gather their personalized
horoscope, mood, compatibility, color,lucky number and lucky time
from the aztro API imported after installing pip intall requests in terminal.
It then gives the user their gemstone and the gemstone meaning
based on the month they were born in.
Lastly, it asks the user for their birth year and presents their Chinese zodiac sign."""

import logging
#file for logging
logging.basicConfig(filename='myProgramLog.txt',
                    level=logging.DEBUG,
                    format=' %(asctime)s -  %(levelname)s -  %(message)s') 
import sys
import time
#try and except for importing the 3rd party package
try:
    import requests
except:
    logging.critical('Missing requests')
    print('Missing requests! Program is closing.')
    sys.exit()

#asking the user their birth month and day, which are the parameters, and input validationfor API
months = ["march", "mar", "april", "apr", "may", "june", "jun" ,"july", "jul", "august", "aug",
          "september", "sep", "sept", "october", "oct", "november", "nov", "december", "dec",
          "january", "jan", "february", "feb"]
while True:
    print("What month were you born in?")
    userMonth = input("> ").lower()
    if userMonth in months:
        break
    else:
        print("That is invalid input! Please try again!")
while True:
    print("What day were you born on?(number)")
    userDay = input("> ").lower()
    try:
        userDay = int(userDay)
        if userDay > 0 and userDay <= 31:
            break
        else:
            print("That is invalid input! Please try again!")
    except:
        logging.warning('Invalid input')
        print("That is invalid input! Please try again!")
        continue


#function to assign the users Zodiac based on their input for month and day
def zodiacSign(month, day):
    if month == "december" or month == "dec":
        if (day <= 21):
            sign = "sagittarius"
            print("Your sign is Sagittarius!")
        else:
            sign = "capricorn"
            print("Your sign is Capricorn!")
    elif month == "january" or month == "jan":
        if (day <= 19):
            sign = "capricorn"
            print("Your sign is Capricorn!")
        else:
            sign = "aquarius"
            print("Your sign is Aquarius!")
    elif month == "february" or month == "feb":
        if (day <= 18):
            sign = "aquarius"
            print("Your sign is Aquarius!")
        else:
            sign = "pisces"
            print("Your sign is Pisces!")
    elif month == "march" or month == "mar":
         if (day <= 20):
            sign = "pisces"
            print("Your sign is Pisces!")
         else:
            sign = "aries"
            print("Your sign is Aries!")
    elif month == "april" or month == "apr":
        if (day <= 19):
            sign = "aries"
            print("Your sign is Aries!")
        else:
            sign = "taurus"
            print("Your sign is Taurus!")
    elif month == "may":
        if (day <= 20):
            sign = "taurus"
            print("Your sign is Taurus!")
        else:
            sign = "gemini"
            print("Your sign is Gemini!")
    elif month == "june" or month == "jun":
        if (day <= 20):
            sign = "gemini"
            print("Your sign is Gemini!")
        else:
            sign = "cancer"
            print("Your sign is Cancer!")
    elif month == "july" or month == "jul":
        if (day <= 22): 
            sign = "cancer"
            print("Your sign is Cancer!")
        else:
            sign = "leo"
            print("Your sign is Leo!")
    elif month == "august" or month == "aug":
        if (day <= 22):
            sign = "leo"
            print("Your sign is Leo!")
        else:
            sign = "virgo"
            print("Your sign is Virgo!")
    elif month == "september"or month == "sep" or month == "sept":
        if (day <= 22):
            sign = "virgo"
            print("Your sign is Virgo!")
        else:
            sign = "libra"
            print("Your sign is Libra!")
    elif month == "october"or month == "oct":
        if (day <= 22):
            sign = "libra"
            print("Your sign is Libra!")
        else:
            sign = "scorpio"
            print("Your sign is Scorpio!")
    elif month == "november" or month == "nov":
        if (day <= 21):
            sign = "scorpio"
            print("Your sign is Scorpio!")
        else:
            sign = "sagittarius"
            print("Your sign is Sagittarius!")
    return sign

#parameters for horoscope reader third party package
sign = zodiacSign(userMonth, userDay)
days = ["today", "tomorrow", "yesterday"]
while True:
    print("Enter the day of the horoscope you want (today, tomorrow, or yesterday)")
    day = input("> ",).lower()
    if day in days:
        break
    else:
        print("That is invalid input! Please try again!")


 #parameters for the HTTP request
params = (
    ('sign', sign),
    ('day', day)
    )

#making the HTTP request 
response = requests.post('https://aztro.sameerkumar.website', params=params)

#assigning json as a variable equal to the response we get back
#from the HTTP request
json = response.json()

#statement to keep user engaged
print("Searching the stars for your horoscope...")

#adding some suspense
time.sleep(2.5)

#presenting the user with their horoscope information
print("\nHoroscope for", json.get('current_date'), '\n')
print(json.get('description'), '\n')
print('Compatibility: ', json.get('compatibility'))
print('Mood: ', json.get('mood'))
print('Color: ', json.get('color'))
print('Lucky Number: ', json.get('lucky_number'))
print('Lucky Time: ', json.get('lucky_time'), '\n')

# function for finding the gemstone
def gemstone(month):
    if userMonth == "january" or userMonth == "jan":
        stone = "Your birthstone is Garnet"
        meaning = "and it's meaning is Protection.\n"
        print(stone)
        print(meaning)
    elif userMonth == "february" or userMonth == "feb":
        stone = "Your birthstone is Amethyst"
        meaning = "and it's meaning is Wisdom.\n"
        print(stone)
        print(meaning)
    elif userMonth == "march" or userMonth == "mar":
        stone = "Your birthstone is Aquarmarine"
        meaning = "and it's meaning is Serenity.\n"
        print(stone)
        print(meaning)
    elif userMonth == "april" or userMonth == "apr":
        stone = "Your birthstone is Quartz or Diamond"
        meaning = "and their meaning is Strength.\n"
        print(stone)
        print(meaning)
    elif userMonth == "may":
        stone = "Your birthstone is Emerald"
        meaning = "and it's meaning is Hope.\n"
        print(stone)
        print(meaning)
    elif userMonth == "june" or userMonth == "jun":
        stone = "Your birthstone is Pearl or Alexandrite"
        meaning = "and their meaning is Love.\n"
        print(stone)
        print(meaning)
    elif userMonth == "july" or userMonth == "jul":
        stone = "Your birthstone is Ruby"
        meaning = "and it's meaning is Vitality.\n"
        print(stone)
        print(meaning)
    elif userMonth == "august" or userMonth == "aug":
        stone = "Your birthstone is Peridot"
        meaning = "and it's meaning is Beauty.\n"
        print(stone)
        print(meaning)
    elif userMonth == "september" or userMonth == "sept" or userMonth == "sep":
        stone = "Your birthstone is Sapphire"
        meaning = "and it's meaning is Truth.\n"
        print(stone)
        print(meaning)
    elif userMonth == "october" or userMonth == "oct":
        stone = "Your birthstone is Tourmaline"
        meaning = "and it's meaning is Healing.\n"
        print(stone)
        print(meaning)
    elif userMonth == "november" or userMonth == "nov":
        stone = "Your birthstone is Citrine"
        meaning = "and it's meaning is Joy.\n"
        print(stone)
        print(meaning)
    elif userMonth == "december" or userMonth == "dec":
        stone = "Your birthstone is Turquoise"
        meaning = "and it's meaning is Friendship.\n"
        print(stone)
        print(meaning)
    return stone
    return meaning

#calling the gemstone function and presenting the user their gemstone
gemstone(userMonth)

#asking the user if they want to know their Chinese zodiac and validating their input
while True:
    print("While we're at it, would you like to know your Chinese zodiac? (yes or no)")
    answer = input("> ").lower()
    if answer.isalpha() and answer == "yes":
        break
    elif answer == "no":
        print("No worries! I hope you enjoyed your time here today :)")
        time.sleep(1)
        #exiting the program
        sys.exit("Have a ~magical~ day!!")
    elif answer != "yes" or "no":
        print("That is invalid input! Please try again!")
        continue
    else:
        logging.warning('Invalid input')
        print("That is invalid input! Please try again!")


#if their answer is yes, they are asked their birth year and validating their input 
while answer == "yes" :
    print("Okay, cool! What year were you born?")
    year = input("> ")
    try:
        year = int(year)
        if year > 1920 and year <= 2020:
            break
    except:
        print("That is invalid input! Please try again!")
        continue

    

#function to find their Chinese zodiac animal
def chineseZodiac(year):
    if year == int("1924") or year == int("1936") or year == int("1948") \
       or year == int("1960") or year == int("1972")or year == int("1984")\
       or year ==  int("1996") or year == int("2008") or year ==  int("2020"):
        czodiac = "Your Chinese zodiac is a rat!\n"
        print(czodiac)
    elif year == int("1925") or year == int("1937") or year == int("1949") \
         or year == int("1961") or year == int("1973")or year == int("1985")\
         or year ==  int("1997") or year == int("2009") or year ==  int("2021"):
        czodiac = "Your Chinese zodiac is an ox!\n"
        print(czodiac)
    elif year == int("1926") or year == int("1938") or year == int("1950") \
         or year == int("1962") or year == int("1974") or year == int("1986") \
         or year ==  int("1998") or year == int("2010") or year ==  int("2022"):
        czodiac = "Your Chinese zodiac is a tiger!\n"
        print(czodiac)
    elif year == int("1927") or year == int("1939") or year == int("1951") \
         or year == int("1961") or year == int("1973")or year == int("1987")\
         or year ==  int("1999") or year == int("2011"):
        czodiac = "Your Chinese zodiac is a rabbit!\n"
        print(czodiac)
    elif year == int("1928") or year == int("1940") or year == int("1952") \
         or year == int("1964") or year == int("1976")or year == int("1988")\
         or year ==  int("2000") or year == int("2012"):
        czodiac = "Your Chinese zodiac is a dragon!\n"
        print(czodiac)
    elif year == int("1929") or year == int("1941") or year == int("1953")\
         or year == int("1965") or year == int("1977")or year == int("1989")\
         or year ==  int("2001") or year == int("2013"):
        czodiac = "Your Chinese zodiac is a snake!\n"
        print(czodiac)
    elif year == int("1930") or year == int("1942") or year == int("1954") \
         or year == int("1966") or year == int("1978")or year == int("1990") \
         or year ==  int("2002") or year == int("2014"):
        czodiac = "Your Chinese zodiac is a horse!\n"
        print(czodiac)
    elif year == int("1931") or year == int("1943") or year == int("1955") \
         or year == int("1967") or year == int("1979")or year == int("1991") \
         or year ==  int("2003") or year == int("2015"):
        czodiac = "Your Chinese zodiac is a sheep!\n"
        print(czodiac)
    elif year == int("1932") or year == int("1944") or year == int("1956")\
         or year == int("1968") or year == int("1980")or year == int("1992") \
         or year ==  int("2004") or year == int("2016"):
        czodiac = "Your Chinese zodiac is a monkey!\n"
        print(czodiac)
    elif year == int("1933") or year == int("1944") or year == int("1957")\
         or year == int("1969") or year == int("1981")or year == int("1993") \
         or year ==  int("2005") or year == int("2017"):
        czodiac = "Your Chinese zodiac is a rooster!\n"
        print(czodiac)
    elif year == int("1934") or year == int("1945") or year == int("1958")\
         or year == int("1970") or year == int("1982")or year == int("191994") \
         or year ==  int("2006") or year == int("2018"):
        czodiac = "Your Chinese zodiac is a dog!\n"
        print(czodiac)
    elif year == int("1935") or year == int("1947") or year == int("1959") \
         or year == int("19671") or year == int("1983")or year == int("1995") \
         or year ==  int("2007") or year == int("2019"):
        czodiac = "Your Chinese zodiac is a pig!\n"
        print(czodiac)
    return czodiac

#add suspense
time.sleep(1)

#calling the chinese zodiac function
chineseZodiac(year)

#add more suspense
time.sleep(1)
print("I hope you've enjoyed! \n")

#exiting the program
sys.exit("Have a ~magical~ day!!")

