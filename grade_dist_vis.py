# jupyter notebook
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

grades = pd.read_csv("gradedist.csv")

# import data as csv file
grades = grades.rename(columns={'Course No.': 'Course_Number', 
                                'Course Title': 'Course_Title',
                                'Graded Enrollment': 'Enrollment', 
                                'A (%)': 'A', 
                                'A- (%)': 'A-', 
                                'B+ (%)': 'B+', 
                                'B (%)': 'B', 
                                'B- (%)': 'B-', 
                                'C+ (%)': 'C+', 
                                'C (%)': 'C',
                                'C- (%)': 'C-',
                                'D+ (%)': 'D+',
                                'D (%)': 'D',
                                'D- (%)': 'D-',
                                'F (%)': 'F'})
grades = grades.sort_values(by='Course_Number')
# print(grades.head())
internal_grades = grades

# user interface
while True:

    # subject input
    subject = input("Enter subject name to search (or type 'exit' to quit): ")
    subject = subject.upper()
    if (subject == 'EXIT'):
        break

    # invalid subject check
    sub_found = False
    for sub in (grades.Subject.unique()):
        if (subject == sub):
            sub_found = True
    while (not subject == 'EXIT' and (not subject.isalpha() or not sub_found)):
        subject = input("Enter subject name to search (or type 'exit' to quit): ")
        subject = subject.upper()
        for sub in (grades.Subject.unique()):
            if (subject == sub):
                sub_found = True
    if (subject == 'EXIT'):
        break
    
    # course number input
    course_number = input("Enter course number (optional, press Enter to skip): ")
    if (course_number != '' and not course_number.isalpha()):
        course_number = int(course_number)
    else:
        while (course_number.isalpha()):
            course_number = input("Enter course number (optional, press Enter to skip): ")
        if (course_number != '' and not course_number.isalpha()):
            course_number = int(course_number)

    # course title input
    course_title = input("Enter course title (optional, press Enter to skip): ")
    while (course_title != '' and course_title.isnumeric()):
        course_title = input("Enter course title (optional, press Enter to skip): ")

    # invalid course title check
    true_course_title = ''
    if (course_title != ''):
        course_title = course_title.lower()
        title_found = False
        for name in (grades.Course_Title.unique()):
            if (course_title == name.lower()):
                title_found = True
                true_course_title = name
                break
        while (course_title.isnumeric() or not title_found):
            course_title = input("Enter course title (optional, press Enter to skip): ")
            while (course_title != '' and course_title.isnumeric()):
                course_title = input("Enter course title (optional, press Enter to skip): ")
            course_title = course_title.lower()
            for name in (grades.Course_Title.unique()):
                if (course_title == name.lower()):
                    title_found = True
                    true_course_title = name
        if (true_course_title != ''):
            course_title = true_course_title

    # invalid course number check
    invalid_course_num = True
    if (course_number != ''):
        while (invalid_course_num):
            try:
                internal_grades = grades.loc[(grades.Subject == subject) & ((grades.Course_Number == course_number) | (grades.Course_Title == course_title))]
                ( subject + ' ' + str(internal_grades.iloc[0]['Course_Number']) + ' - ' + internal_grades.iloc[0]['Course_Title'] + ' (' + str(internal_grades.iloc[0]['Credits']) + ' Credits)')
                internal_grades = grades
                invalid_course_num = False
            except:
                course_number = input("Enter course number (optional, press Enter to skip): ")
                if (course_number != '' and not course_number.isalpha()):
                    course_number = int(course_number)
                else:
                    while (course_number.isalpha()):
                        course_number = input("Enter course number (optional, press Enter to skip): ")
                    if (course_number != '' and not course_number.isalpha()):
                        course_number = int(course_number)

    # index the csv for the subject and class number/title selected
    if ((course_number == '') and (course_title == '')):
        internal_grades = grades.loc[(grades.Subject == subject)]
        # add logic to print every single class out?
    elif ((course_number != '') and (course_title == '')):
        internal_grades = grades.loc[(grades.Subject == subject) & (grades.Course_Number == course_number)]
    else:
        internal_grades = grades.loc[(grades.Subject == subject) & (grades.Course_Title == course_title)]
    internal_grades = internal_grades.sort_values(by='GPA', ascending=False)
    # print(internal_grades.head())

    # class information label
    print('')
    print( subject + ' ' + str(internal_grades.iloc[0]['Course_Number']) + ' - ' + internal_grades.iloc[0]['Course_Title'] + ' (' + str(internal_grades.iloc[0]['Credits']) + ' Credits)')

    
    # gpa calculation
#     print('')
    GPA = 0.00
    i = 0
    while i < internal_grades.GPA.size:
        GPA = GPA + internal_grades.iloc[i]['GPA']
        i += 1
    GPA = GPA / internal_grades.GPA.size
    print("Average GPA: {:.3}".format(GPA))

    # grade distribution calculation
#     print('')
    print("Grade distribution:")
    A = 0
    Aminus = 0
    Bplus = 0
    B = 0
    Bminus = 0
    Cplus = 0
    C = 0
    Cminus = 0
    Dplus = 0
    D = 0
    Dminus = 0
    F = 0
    
    j = 0
    letterchar = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']
    lettergrades = [A, Aminus, Bplus, B, Bminus, Cplus, C, Cminus, Dplus, D, Dminus, F]
    val = []
    for letter in (lettergrades):
        i = 0
        while i < internal_grades.GPA.size:
            letter = letter + internal_grades.iloc[i][letterchar[j]]
            i += 1
        letter = letter / internal_grades.GPA.size
#         print("{}: {:.3}%".format(letterchar[j], letter))
        val.append(letter)
        j += 1
    data = {'labels': ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'],
            'values': val}
    df = pd.DataFrame(data)
    sns.set_style("whitegrid")
    plt.figure(figsize=(10,10))
    plt.pie(df['values'], labels=df['labels'], autopct='%1.1f%%')
    plt.title('Average Grade Distribution for ' + subject + ' ' + str(internal_grades.iloc[0]['Course_Number']) + ' - ' + internal_grades.iloc[0]['Course_Title'])
    plt.show()

    # sort professors
    print('')
    print("Top Professors by GPA:")
    k = 1
    for k in range(internal_grades.Instructor.size):
        j = k - 1
        internal_found = False
        while (j >= 0):
            if (internal_grades.iloc[k]['Instructor'] == internal_grades.iloc[j]['Instructor']):
                internal_found = True
            j -= 1
        if (internal_found != True):
            print('')
            print("Professor " + internal_grades.iloc[k]['Instructor'] + ', GPA: ' + str(internal_grades.iloc[k]['GPA']) + ',', end = " ")
            if (internal_grades.iloc[k]['GPA'] > GPA):
                print("Above average")
            elif (internal_grades.iloc[k]['GPA'] == GPA):
                print("Average")
            else:
                print("Below average")
            print("Enrollment: {}".format(internal_grades.iloc[k]['Enrollment']) + ', Withdraws: {}'.format(internal_grades.iloc[k]['Withdraws']))
            print("Grade distribution:")
            A = 0
            Aminus = 0
            Bplus = 0
            B = 0
            Bminus = 0
            Cplus = 0
            C = 0
            Cminus = 0
            Dplus = 0
            D = 0
            Dminus = 0
            F = 0
    
            j = 0
            letterchar = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']
            lettergrades = [A, Aminus, Bplus, B, Bminus, Cplus, C, Cminus, Dplus, D, Dminus, F]
            vals = []
            for letter in (lettergrades):
                i = 0
                while i < internal_grades.A.size:
                    letter = letter + internal_grades.iloc[k][letterchar[j]]
                    i += 1
                letter = letter / internal_grades.A.size
#                 print("{}: {:.3}%".format(letterchar[j], letter))
                vals.append(letter)
                j += 1
            data = {'labels': ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'],
                        'values': vals}
            df = pd.DataFrame(data)
            sns.set_style("whitegrid")
            plt.figure(figsize=(10,10))
            plt.pie(df['values'], labels=df['labels'], autopct='%1.1f%%')
            plt.title('Best Grade Distribution for ' + "Professor " + internal_grades.iloc[k]['Instructor'] + "'s class")
            plt.show()
        k += 1

    # professors who teach the class
    print('')
    print("Professors who teach {}:".format(internal_grades.iloc[0]['Course_Title']))
    print(internal_grades.Instructor.unique())
    print('')

    # enrollment and withdraws
    print('')
    # print()