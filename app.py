import gradio as gr
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

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
        val = []
        for letter in (lettergrades):
            i = 0
            while i < internal_grades.GPA.size:
                letter = letter + internal_grades.iloc[i][letterchar[j]]
                i += 1
            letter = letter / internal_grades.GPA.size
            val.append(letter)
            gradedistribution = gradedistribution + str("{}: {:.3}%".format(letterchar[j], letter))
            gradedistribution = gradedistribution + str(', ')
            j += 1
        data = {'labels': ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'],
            'values': val}
        df = pd.DataFrame(data)
        # plt.style.use('dark_background')
        sns.set_style("whitegrid")
        plt.figure(figsize=(10,10))
        plt.pie(df['values'], labels=df['labels'], autopct='%1.1f%%')
        plt.title('Average Grade Distribution for ' + subject + ' ' + str(internal_grades.iloc[0]['Course_Number']) + ' - ' + internal_grades.iloc[0]['Course_Title'])
        #plt.show()
        plot = plt

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
                sortedprofgradedist = sortedprofgradedist + str(" ")
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
                # vals = []
                for letter in (lettergrades):
                    i = 0
                    while i < internal_grades.A.size:
                        letter = letter + internal_grades.iloc[k][letterchar[j]]
                        i += 1
                    letter = letter / internal_grades.A.size
                    sortedprofgradedist = sortedprofgradedist + str("{}: {:.3}%".format(letterchar[j], letter))
                    sortedprofgradedist = sortedprofgradedist + str(', ')
                    # vals.append(letter)
                    j += 1
                sortedprofgradedist = sortedprofgradedist + str('\n')
                # data = {'labels': ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'],
                #         'values': vals}
                # df = pd.DataFrame(data)
                # sns.set_style("whitegrid")
                # plt.figure(figsize=(10,10))
                # plt.pie(df['values'], labels=df['labels'], autopct='%1.1f%%')
                # plt.title('Best Grade Distribution for ' + "Professor " + internal_grades.iloc[k]['Instructor'] + "'s class")
                # plt.show()
            k += 1

        # professors who teach the class
        profswhoteach = ''
        profswhoteach = profswhoteach + str('\n')
        profswhoteach = profswhoteach + str("Professors who teach {}:".format(internal_grades.iloc[0]['Course_Title']))
        profswhoteach = profswhoteach + str('\n')
        profswhoteach = profswhoteach + str(internal_grades.Instructor.unique())

        # enrollment and withdraws
        print('')
        return (subject + ' ' + str(internal_grades.iloc[0]['Course_Number']) + ' - ' + internal_grades.iloc[0]['Course_Title'] + ' (' + str(internal_grades.iloc[0]['Credits']) + ' Credits)') + ("\nAverage GPA: {:.3}".format(GPA)) + profswhoteach, gradedistribution, plot, sortedprofgradedist 

# gradio interface
demo = gr.Interface(
    fn=greet,
    inputs=[gr.Textbox(label="Subject (Eg. ECON)"), gr.Number(label="Course Number (Eg. 2005)"), gr.Textbox(label="Course Title (Eg. Principles of Economics)")],
    outputs=[gr.Textbox(label="Course Information"), gr.Textbox(label="Average Grade Distribution", lines=2), gr.Plot(label="Average Distribution Plot"), gr.Textbox(label="Grade Distributions by Professors", lines=3)],
    title="GradeDistVis",
    description="For Virginia Tech students, by Gautam Soni: \n\n A free tool to help you plan your courses based on grade distribution and other metrics",
    article="My Github: https://github.com/gsoni1/ My Linkedin: https://www.linkedin.com/in/gsoni16/",
    examples = [["ECON", 2005, ''], ["CHEM", '',"General Chemistry"]],
    cache_examples=True,
).queue(default_concurrency_limit=10000)

demo.launch()