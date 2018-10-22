
# coding: utf-8

# In[1]:



import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


# In[ ]:





# In[4]:


def getData(file):
    infile = open(file, 'r')
    infile_string = infile.readlines()
    template = infile_string[0].split(",")
    lst_of_str = infile_string[1:]
    getData_lst = []

    for string in lst_of_str:
        lst = string.split(",")
        d = {template[0]: lst[0], template[1]: lst[1], template[2]:lst[2], template[3]:lst[3], template[4].strip('\n'):lst[4].strip('\n')}
        getData_lst.append(d)

    infile.close()
    return getData_lst




def mySort(data,col):
    dex = sorted(data, key= lambda x : x[col])
    lst = []
    for d in dex:
        string = d['First'] + " " + d["Last"]
        lst.append(string)
    return lst[0]


def classSizes(data):
    dic = {}
    for d in data:
        if d['Class'] not in dic.keys():
            dic[d["Class"]] = 1
        else:
            dic[d["Class"]] = dic[d["Class"]] + 1
    new_dic = sorted(dic.keys(), key=lambda x : dic[x], reverse = True)
    fnal_lst = []
    for ky in new_dic:
        fnal_lst.append((ky, dic[ky]))
    return fnal_lst


def findMonth(a):
    tally_d = {}
    for line in a:
        x = line['DOB'].split('/')
        xx = x[0]
        if xx not in tally_d.keys():
            tally_d[xx] = 1
        else:
            tally_d[xx] = tally_d[xx] + 1
    return int(sorted(tally_d.keys(), key = lambda x : tally_d[x], reverse = True)[0])


def mySortPrint(a,col,fileName):
    outfile = open(fileName, "w")
    sort = sorted(a, key = lambda x : x[col])
    sorted_lines = []
    for line in sort:
        sorted_lines.append([line['First'],line['Last'],line['Email']])
    for lst in sorted_lines:
        outfile.write(lst[0] + ',' + lst[1] + ',' + lst[2] + '\n')
    outfile.close()
    return

def findAge(a):
    current_date = input("Please write todays date in the following format: mm/dd/yyy").split('/')
    dates = []
    for d in a:
        dates.append(d["DOB"].split('/'))
    total_age = 0
    for lst in dates:
        if lst[0] == current_date[0]:
            if int(lst[1]) > int(current_date[1]):
                total_age += (int(current_date[2]) - int(lst[2]) + 1)
            else:
                total_age += int(current_date[2]) - int(lst[2])
        elif int(lst[0]) > int(current_date[0]):
            total_age += (int(current_date[2]) - int(lst[2]) + 1)
        else:
            total_age += int(current_date[2]) - int(lst[2])
    num = len(a)
    avg = total_age // num
    return avg


# In[5]:



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB2.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()


# In[6]:


##my own test for mySortPrint
infile1 = open("outfile.csv", "r")
infile2 = open("results.csv", 'r')
lines1 = infile1.readlines()
lines2 = infile2.readlines()
counter = 0
for i in range(len(lines1)):
    if lines1[i] == lines2[i]:
        counter += 1
    else:
        print(lines1[i])
        print(lines2[i])
print(counter)
infile1.close()
infile2.close()

