from csv import writer
import csv, operator
import re

runProgram=bool(True)

def printList():
  csvFile = open("movies.csv", "r")
  for line in csvFile.readlines():
    parts = line.split(",")
    movie = parts[0]
    re.sub("`", ",", movie)
    score = str(parts[1])
    category = parts[2]
    re.sub("`", " \\ ", category)
    page = str(parts[3])
    print(movie + "\t" + score + "\t" + category + "\t"+ page)
  csvFile.close()

def listByPageNumAscend():
  csvFile = csv.reader(open('movies.csv'),delimiter=',')
  csvFile = sorted(csvFile, key=operator.itemgetter(3))
  for lines in csvFile:
    for line in lines:
      print(line, end="\t")
    print()

def listByPageNumDescend():
  csvFile = csv.reader(open('movies.csv'),delimiter=',')
  csvFile = sorted(csvFile, key=operator.itemgetter(3), reverse=True)
  for lines in csvFile:
    for line in lines:
      print(line, end="\t")
    print()

def sortAlpahbetically():
  csvFile = csv.reader(open('movies.csv'),delimiter=',')
  csvFile = sorted(csvFile, key=operator.itemgetter(0), reverse=False)
  for lines in csvFile:
    for line in lines:
      print(line, end="\t")
    print()

def listByScore():
  csvFile = csv.reader(open('movies.csv'),delimiter=',')
  csvFile = sorted(csvFile, key=operator.itemgetter(1), reverse=True)
  for lines in csvFile: # is a multi dimensional array. each row has multiple parts in it. strings within lists wtihin list
    for line in lines:
      print(line, end="\t")
    print()
    
def addMovie():
  csvFile = open("movies.csv", "a")
  print("movie name? ")
  movie = input()
  re.sub(",", "`", movie)
  print("score? ")
  score = float(input())
  print("category? ")
  category = input()
  re.sub(",", "`", category)
  print("page number? ")
  page = int(input())
  addto = [movie, score, category, page]
  writer_object = writer(csvFile)
  writer_object.writerow(addto)
  csvFile.close()

def clearMovies():
  print("are you sure you want to delete all movies? ")
  inpt = input()
  if ("yes" == inpt) or ("y" == inpt) or ("Yes" == inpt):
    print("are you absolutely sure? ")
    if ("yes" == inpt) or ("y" == inpt) or ("Yes" == inpt):
      open('movies.csv', 'w').close()
  
def sortByCategory(): # print from sorted category list. add ways to sort by score, name, page num
  print("please list all categories here: ")
  inpt = input()
  csvFile = open("movies.csv", "r")
  sortedCSV = open("sorted.csv", "w")
  if re.search("(a|A)ction", inpt):
    action = bool(True)
  if re.search("(d|D)rama", inpt):
    drama = bool(True)
  if re.search("(c|C)omedy", inpt):
    comedy = bool(True)
  if re.search("(m|M)ystery", inpt):
    mystery = bool(True)
  if re.search("(t|T)hriller", inpt):
    thriller = bool(True)
  if re.search("(a|A)dventure", inpt):
    adventure = bool(True)
  if re.search("(f|F)antasy", inpt):
    fantasy = bool(True)
  if re.search("(h|H)orror", inpt):
    horror = bool(True)
  if re.search("(m|M)usical", inpt):
    musical = bool(True)
  if re.search("(r|R)omance", inpt):
    romance = bool(True)
  if re.search("(s|S)ci(F|f)i", inpt) or (re.search("(s|S)cience", inpt) and re.search("(f|F)iction", inpt)):
    scifi = bool(True)
  if re.search("(s|S)ports", inpt):
    sports = bool(True)
  if re.search("(w|W)estern", inpt):
    western = bool(True)
  for lines in csvFile:
    for line in lines:
      if (re.search("(a|A)ction", lines) and action) or (re.search("(d|D)rama", lines) and drama) or (re.search("(c|C)omedy", lines) and comedy) or (re.search("(m|M)ystery", lines) and mystery) or (re.search("(t|T)hriller", lines) and thriller) or (re.search("(a|A)dventure", lines) and adventure) or (re.search("(f|F)antasy", lines) and fantasy) or (re.search("(h|H)orror", lines) and horror) or (re.search("(m|M)usical", lines) and musical) or (re.search("(r|R)omance", lines) and romance) or ((re.search("(s|S)ci(F|f)i", inpt) or (re.search("(s|S)cience", inpt) and re.search("(f|F)iction", inpt))) and scifi) or (re.search("(s|S)ports", line) and sports) or (re.search("(w|W)estern", line) and western):
        writer_object = writer(sortedCSV)
        writer_object.writerow(line)
    csvFile.close()
    sortedCSV.close()

def searchForMovie(): # finish  
  print("fisns")

def options():
  print("what would you like to do?")
  inpt = input()
  if re.search("(o|O)ptions", inpt):
    print("print list\n")
    print("other options to be added later")
  elif (re.search("(p|P)rint", inpt) and re.search("(l|L)ist", inpt)) and ((re.search("(p|P)age", inpt) or re.search("(n|N)um", inpt)) or re.search("(s|S)core", inpt)) == False:
    print()
    printList()
  elif re.search("(a|A)dd", inpt) and re.search("(m|M)ovie", inpt):
    addMovie()
  elif re.search("(c|C)ategor", inpt):
    sortByCategory()
  elif re.search("(p|P)age", inpt) or re.search("(n|N)um", inpt):
    print()
    if re.search("(d|D)escend", inpt):
      listByPageNumDescend()
    else:
      listByPageNumAscend()
  elif re.search("(s|S)core", inpt):
    print()
    listByScore()
  elif re.search("(a|A)lphabet", inpt):
    sortAlpahbetically()
  else:
    print()
    options()
  

while runProgram == True:  
  options()
  print()
  print("anything else?")
  inpt=input()
  if re.search("(n|N)o", inpt):
    runProgram=False

# add sort categories by score, page num, and alphabetically
# add search for movie and add (something that im blanking on)