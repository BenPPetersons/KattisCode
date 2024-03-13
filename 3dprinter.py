stats = int(input())

printers = 1
days=0
#Maximize the number of printers, then add a day
while (printers<stats):
    printers = printers *2
    #printer prints another printer
    days+=1
    #end of day, add day

#days +1 is needed bc it always takes 1 more day to print out 
# the remaining statues between current printers and printers *2
print(days+1)
