import pandas as pd

# import data as csv file
grades = pd.read_csv("gradedistriubtion.csv")
grades = grades.rename(columns={'Course No.': 'Course_Number', 'Course Title': 'Course_Title'})
grades = grades.sort_values(by='Course_Number')
print(grades.head())
internal_grades = grades

# user interface
while True:
    subject = input("Enter subject name to search (or type 'exit' to quit): ")
    if (subject == 'exit'):
        break
    
    course_number = input("Enter course number (optional, press Enter to skip): ")
    if (course_number != ''):
        course_number = int(course_number)
    course_title = input("Enter course title (optional, press Enter to skip): ")
    if ((course_number == '') and (course_title == '')):
        internal_grades = grades.loc[(grades.Subject == subject)]
    else:
        internal_grades = grades.loc[(grades.Subject == subject) & ((grades.Course_Number == course_number) | (grades.Course_Title == course_title))]
    internal_grades = internal_grades.sort_values(by='GPA', ascending=False)
    # print(internal_grades.head())

    # GUI
    print( subject + ' ' + str(internal_grades.iloc[0]['Course_Number']) + ' - ' + internal_grades.iloc[0]['Course_Title'] + ' (' + str(internal_grades.iloc[0]['Credits']) + ' Credits)')

    print('')
    # grade calculations
    GPA = 0.00
    i = 0
    while i < internal_grades.GPA.size:
        GPA = GPA + internal_grades.iloc[i]['GPA']
        i += 1
    GPA = GPA / internal_grades.GPA.size
    print("Average GPA: {:.3}".format(GPA))

    print('')
    # best professors
    print("Top 3 Professors by GPA:")
    print("Professor with Highest GPA: " + internal_grades.iloc[0]['Instructor'] + ', ' + str(internal_grades.iloc[0]['GPA']))
    
    # # print(internal_grades.Instructor.unique().size)
    # if (internal_grades.Instructor.unique().size > 1):
    #     j = 1
    #     while (internal_grades.iloc[j]['Instructor'] == internal_grades.iloc[0]['Instructor']):
    #         j += 1
    #     # print (j)
    #     print("Professor " + internal_grades.iloc[j]['Instructor'] + ', ' + str(internal_grades.iloc[j]['GPA']))
    
    # if (internal_grades.Instructor.unique().size > 2):
    #     k = j
    #     while ((internal_grades.iloc[j]['Instructor'] == internal_grades.iloc[k]['Instructor']) | (internal_grades.iloc[j]['Instructor'] == internal_grades.iloc[0]['Instructor'])):
    #         j += 1
    #     # print (j)
    #     print("Professor " + internal_grades.iloc[j]['Instructor'] + ', ' + str(internal_grades.iloc[j]['GPA']))

    j = 1
    profs = [internal_grades.iloc[0]['Instructor']] # list stores the professors already shown
    for j in range(internal_grades.Instructor.unique().size): # iterates over all the professors
        print (profs)
        k = 0
        for k in range(len(profs)):
            while (internal_grades.iloc[j]['Instructor'] == internal_grades.iloc[k]['Instructor']): # while a prof has already been shown, iterate to the next prof
                j += 1
            k += 1
        profs.append(internal_grades.iloc[j]['Instructor'])
        # print (profs)
        # print (j)
        print("Professor " + internal_grades.iloc[j]['Instructor'] + ', ' + str(internal_grades.iloc[j]['GPA']))
        j += 1

    # # show all profs
    # k = 0
    # for k in range (internal_grades.Instructor.unique().size):
    #     res = internal_grades.Instructor == internal_grades.Instructor.unique()[k]
    #     print("Professor " + internal_grades.loc[0][res] + ', ' + str(internal_grades.iloc[0]['GPA']))
    #     k += 1
    # print(internal_grades.Instructor.unique()[1])

    print('')
    # professors who teach
    print("Professors who teach {}:".format(internal_grades.iloc[0]['Course_Title']))
    print(internal_grades.Instructor.unique())
    print('')