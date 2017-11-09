

import os.path
import bs4 as BeautifulSoup
import urllib.request as rq
import urllib.parse as parse
import re
import csv
from urllib.request import urlopen

def main():
    home = "/Users/chengsheng/Desktop/cache/"
    if not os.path.isfile(home + "FacultyDirectory1.html"):
        data = rq.urlopen("http://www.suffolk.edu/college/6578.php").read().decode()
        useableData = re.sub("[\u2013\xa0\u2019]", "", data)
        outfile = open(home + "FacultyDirectory1.html", "w")
        outfile.write(useableData)
        outfile.close()
    with open(home + "FacultyDirectory1.html") as infile:
        soup = BeautifulSoup.BeautifulSoup(infile, "lxml")
    
    links = soup.find_all("a")
    urls = []
    finalNames = []
    for i in range(151, 345):
        urls.append(links[i]["href"])
    
  
    
    finalRanks = []
    finalDegrees = []
    #facCount = 0
    #193 fac members
    for k in range(193):
        if re.match("http://www.suffolk.edu", urls[k]) != None:
            urls[k] = re.sub("http://www.suffolk.edu", "", urls[k])
        with urlopen("http://www.suffolk.edu" + urls[k]) as infile2:
            currentSoup = BeautifulSoup.BeautifulSoup(infile2, "lxml")
            currentFaculty = re.match(".+,", currentSoup.title.string)
            currentRank = re.search(",.*\s-" , currentSoup.title.string)
            contentDiv = currentSoup.find(id="content")
            
            currentDegree = re.search(r"((Education\s?</h3>))(.*?)<h3>", str(contentDiv), re.S)
            
            if currentDegree != None:
                print(currentDegree.group())
                foo = currentDegree.group().split(", ")
                finalDegrees.append(foo)
            else:
                finalDegrees.append("no match")
                print("no match, index: " + str(k) + " name: " + currentFaculty.group()[:-1])
                
            
            
            if not currentFaculty == None:
                finalNames.append(currentFaculty.group()[:-1])
            else:
                finalNames.append(re.sub(" - Suffolk University", "", currentSoup.title.string))
            
            if not currentRank == None:
                finalRanks.append(currentRank.group()[2:-2])
            else:
                finalRanks.append("")
                
    with open("/Users/chengsheng/Desktop/faculty-education.csv", "w") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(('Name','Rank','Degree','Insitution'))
        for i in range(192):
            writer.writerow((finalNames[i], finalRanks[i], finalDegrees[i]))
                

            
            



    
    

main()