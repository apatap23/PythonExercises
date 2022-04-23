name = input("Enter file:")
handle = open(name)
dictCount = {}
emails = []

for line in handle: 
    #the program looks for 'From '
    if not line.startswith('From '):
        continue
    #takes the second word from those lines as the person who sent the mail
    words = line.split()
    person = words[1]
    emails.append(person)


    #create a python dict that maps the send email to count of num times appeared
for email in emails: 
    dictCount[email] = dictCount.get(email, 0) + 1

mostEmail = ' '
mostCount = 0 
for email,count in dictCount.items():
    if count > mostCount:
        mostCount = count
        mostEmail = email
print(mostEmail, mostCount)