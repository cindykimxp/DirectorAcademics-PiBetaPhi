'''
Cindy Kim
Pi Beta Phi Director Academics
Jan 26, 2021
Automating Grade Collection
'''

def main():
    output_doc = open('Missing Grades.txt', 'w') #students with missing grades
    missing_emails = open('Missing Grades Emails.txt', 'w') #collection of all emails from students with missing grades
    grades_organized = open('Organized Grades.txt', 'w') #all grades organized by term_gpa sections

    f = open('Fall 2020 Grades Submitted.txt', 'r') #members that submitted grades
    z = open('Member Roster.txt', 'r') #all members 
    read_submitted = f.readlines()
    read_all = z.readlines()


    first = [] #4.0 or above
    second = [] #3.500-3.999
    third = [] #3.250-3.499
    fourth = [] #3.000-3.249
    fifth = [] #2.750-2.999
    sixth = [] #2.50-2.749
    seventh = [] #2.250-2.499
    eighth = [] #2.000-2.249
    ninth = [] #below 2.000
    
    submitted_count = 1
    submitted_names = [] #includes all the names of members that have submitted grades
    for line in read_submitted:
        column = line.strip().split('\t')
        sub_name = column[0]
        if (sub_name == "First and Last Name"):
            continue
        
        year = column[1]
        try:
            term_gpa = float(column[2])
        except:
            term_gpa = 0.00 #unknown or waiting grades temporarily placed as 0.00
        try:
            cum_gpa = float(column[3])
        except:
            cum_gpa = 0.00 #unknown or waiting grades temporarily placed as 0.00
        submitted_names.append(sub_name)

        #ORGANIZATION BY TERM GPA
        tup = (sub_name, term_gpa)
        if (term_gpa >= 4.0):
            first.append(tup)
            print("first!", first)
        elif (3.500 <= term_gpa <= 3.999):
            second.append(tup)
            print("second", second)
        elif (3.250 <= term_gpa <= 3.499):
            third.append(tup)
            print("third", third)
        elif (3.000 <= term_gpa <= 3.249):
            fourth.append(tup)
            print("fourth", fourth)
        elif (2.750 <= term_gpa <= 2.999):
            fifth.append(tup)
            print("fifth", fifth)
        elif (2.50 <= term_gpa <= 2.749):
            sixth.append(tup)
            print("sixth", sixth)
        elif (2.250 <= term_gpa <= 2.499):
            seventh.append(tup)
            print("seventh", seventh)
        elif (2.000 <= term_gpa <= 2.249):
            eighth.append(tup)
            print("eighth", eighth)
        elif (term_gpa < 2.000):
            ninth.append(tup)
            print("ninth", ninth)

        submitted_count += 1

    missing_dict = {} #includes all names (with number and email) of members that are missing grades
    all_count = 1
    for line in read_all:
        listc = line.strip().split('\t')
        name = listc[0]
        number = listc[1]
        email = listc[3]
        
        if name not in submitted_names:
            missing_dict[name] = (number, email)
        all_count += 1

    #producing missing member info output in 'Missing Grades.txt' of name, number, and email
    count = 1
    for element in missing_dict:
        output_doc.write(str(count) + '\t' + element + '\t' + '{0}'.format(missing_dict.get(element)) + '\n')
        missing_emails.write(missing_dict.get(element)[1] + '\n')
        count += 1     

    grades_organized.write("4.0 or above:" + '\n')
    count = 1
    for member in first:
        grades_organized.write(str(count) + ": " + member[0] + '\t' + str(member[1]) + '\n')
        count += 1


    grades_organized.write("\n3.500-3.999:" + '\n')
    count = 1
    for member in second:
        grades_organized.write(str(count) + ": " + member[0] + '\t' + str(member[1]) + '\n')
        count += 1
    
    grades_organized.write("\n3.250-3.499:" + '\n')
    count = 1
    for member in third:
        grades_organized.write(str(count) + ": " + member[0] + '\t' + str(member[1]) + '\n')
        count += 1
    
    grades_organized.write("\n3.000-3.249:" + '\n')
    count = 1
    for member in fourth:
        grades_organized.write(str(count) + ": " + member[0] + '\t' + str(member[1]) + '\n')
        count += 1
        
    grades_organized.write("\n2.750-2.999" + '\n')
    count = 1
    for member in fifth:
        grades_organized.write(str(count) + ": " + member[0] + '\t' + str(member[1]) + '\n')
        count += 1
    
    grades_organized.write("\n2.50-2.749:" + '\n')
    count = 1
    for member in sixth:
        grades_organized.write(str(count) + ": " + member[0] + '\t' + str(member[1]) + '\n')
        count += 1
        
    grades_organized.write("\n2.250-2.499:" + '\n')
    count = 1
    for member in seventh:
        grades_organized.write(str(count) + ": " + member[0] + '\t' + str(member[1]) + '\n')
        count += 1
        
    grades_organized.write("\n2.000-2.249:" + '\n')
    count = 1
    for member in eighth:
        grades_organized.write(str(count) + ": " + member[0] + '\t' + str(member[1]) + '\n')
        count += 1
        
    grades_organized.write("\nbelow 2.000:" + '\n')
    count = 1
    for member in ninth:
        grades_organized.write(str(count) + ": " + member[0] + '\t' + str(member[1]) + '\n')
        count += 1

    
    f.close()
    z.close()
    output_doc.close()
    missing_emails.close()
    grades_organized.close()
main()
