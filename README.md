# Company-Cleaner
At my position as a starter data operations manager ( cleaning excel spreadsheets ) i needed to clean company names removing superfluous information ( LLC, PLC and Etc.). Instead of spending 8 hours cleaning the sheet, i decided to create this script.


#HOW TO USE#

1.Inside the csv folder put your .csv file with company names and rename it to "to_Clean.csv" ( /csv/toClean ) 
2.make sure it's the correct format ( First Name,Last Name,Title,Company Name,Email ...... )
3.Your cleaned file will come out as "Cleaned.csv"

#EXPLANATION AND MY REASONING#
The best way to check the "actual" name of the company is looking at the domain of the email, so that's what i did. i got the specific part of the row that is considered the email and i split it by the "@", from jimi@amazon to jimi , amazon. And from then there are 3 main cases, 1 where everything is the same with the domain and it remains untouched in the cleaned, 2 where i added a "@@@ " so that i can manually clean it later for this case maybe 1 or 2 words in the company match the domain and 3 where nothing matches so i added a "!!! ". From the type of csv files i dealt with there still had to be a lot of manual work because there weren't any concrete rules set in place when i got the csv file.

PS. it also normalizes and turns the company names into Camel Case. And it removes the "useless information" for example "Green Company 'by' Jimmy", everything after 'by' will get removed leaving "Green Company", The reason being when you send a formal email to jimmy, the email would look like "Hello Jimmy from Green Company" instead of "Hello Jimmy from Green Company by Jimmy" the only reason being it makes it sound more human. 
