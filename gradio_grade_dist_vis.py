import gradio as gr
import pandas as pd
def greet(subject, course_number, course_title):
    # modify the inputs
    subject = subject.upper()

    # import data as csv file
    grades = pd.read_csv("gradedist.csv")
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
    internal_grades = grades

    # user interface
    while True:
        # filter the csv file by the input subject and course number/title
        if ((course_number != '') and (course_title == '')):
            internal_grades = grades.loc[(grades.Subject == subject) & (grades.Course_Number == course_number)]
        else:
            internal_grades = grades.loc[(grades.Subject == subject) & (grades.Course_Title == course_title)]
        internal_grades = internal_grades.sort_values(by='GPA', ascending=False)

        # class information label
        print('')
        print( subject + ' ' + str(internal_grades.iloc[0]['Course_Number']) + ' - ' + internal_grades.iloc[0]['Course_Title'] + ' (' + str(internal_grades.iloc[0]['Credits']) + ' Credits)')

        
        # gpa calculation
        print('')
        GPA = 0.00
        i = 0
        while i < internal_grades.GPA.size:
            GPA = GPA + internal_grades.iloc[i]['GPA']
            i += 1
        GPA = GPA / internal_grades.GPA.size
        print("Average GPA: {:.3}".format(GPA))

        gradedistribution = ''
        print('')
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
        for letter in (lettergrades):
            i = 0
            while i < internal_grades.GPA.size:
                letter = letter + internal_grades.iloc[i][letterchar[j]]
                i += 1
            letter = letter / internal_grades.GPA.size
            
            gradedistribution = gradedistribution + str("{}: {:.3}%".format(letterchar[j], letter))
            gradedistribution = gradedistribution + str('\n')
            j += 1
        

        # sort professors
        sortedprofgradedist = ''
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
                sortedprofgradedist = sortedprofgradedist + str("\nProfessor " + internal_grades.iloc[k]['Instructor'] + ', GPA: ' + str(internal_grades.iloc[k]['GPA']) + ',')
                if (internal_grades.iloc[k]['GPA'] > GPA):
                    sortedprofgradedist = sortedprofgradedist + str(" Above average")
                elif (internal_grades.iloc[k]['GPA'] == GPA):
                    sortedprofgradedist = sortedprofgradedist + str(" Average")
                else:
                    sortedprofgradedist = sortedprofgradedist + str(" Below average")
                sortedprofgradedist = sortedprofgradedist + str("\nEnrollment: {}".format(internal_grades.iloc[k]['Enrollment']) + ', Withdraws: {}'.format(internal_grades.iloc[k]['Withdraws']))
                sortedprofgradedist = sortedprofgradedist + str("\nGrade distribution:")
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
                for letter in (lettergrades):
                    i = 0
                    while i < internal_grades.A.size:
                        letter = letter + internal_grades.iloc[k][letterchar[j]]
                        i += 1
                    letter = letter / internal_grades.A.size
                    sortedprofgradedist = sortedprofgradedist + str("\n{}: {:.3}%".format(letterchar[j], letter))
                    j += 1
                sortedprofgradedist = sortedprofgradedist + str('\n')
            k += 1

        # professors who teach the class
        profswhoteach = ''
        profswhoteach = profswhoteach + str("Professors who teach {}:".format(internal_grades.iloc[0]['Course_Title']))
        profswhoteach = profswhoteach + str('\n')
        profswhoteach = profswhoteach + str(internal_grades.Instructor.unique())

        # enrollment and withdraws
        print('')
        return (subject + ' ' + str(internal_grades.iloc[0]['Course_Number']) + ' - ' + internal_grades.iloc[0]['Course_Title'] + ' (' + str(internal_grades.iloc[0]['Credits']) + ' Credits)'), ("Average GPA: {:.3}".format(GPA)), gradedistribution, sortedprofgradedist, profswhoteach

# gradio interface
demo = gr.Interface(
    fn=greet,
    inputs=["text", "number", "text"],
    outputs=["text", "text", "text", "text", "text"],
    title="GradeDistVis",
    description="By Gautam Soni",
)
demo.launch()