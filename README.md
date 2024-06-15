# GradeDistVis
<p align="center">
	<img alt="GitHub latest commit" src="https://img.shields.io/github/last-commit/gsoni1/GradeDist">
	<br>
	<span>A free tool to help you plan your courses based on grade distribution and other metrics</span><br><br>
	<span>For Virginia Tech</span><br><br>
	<small>Made by <a href="https://www.linkedin.com/in/gsoni16/">Gautam Soni</a></small>
</p>

## About

GradeDistVis is a tool that helps plan your courses based on metrics including

- Overall GPA and grade distribution (%)
- Sorts professors by average GPA and shows their best grade distribution (%)
- Enrollment and Withdraws
- Professors who teach the course

## Versions
- Terminal/CLI/IDE (.py)
- Jupyter Notebook (.ipynb)
- Web version https://www.kaggle.com/code/gsoni16/gradedistvis

## Installation
Requirements:
- Python 3.9.12+
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook (optional)
- IDE to run the python file (optional)
  
Process:
- Download the grade_dist_vis.py or grade_dist_vis.ipynb and gradeddistriubtion.csv files
- Install python, matplotlib, seaborn, and jupyter notebook (if using the .ipynb version)

## How to use
Run grade_dist_vis.py from the terminal (cmd for Windows):
```sh
cd ... #directory containing the grade_dist_vis.py and gradeddistriubtion.csv files
python grade_dist_vis.py
```
or through an IDE (I recommend Visual Studio Code)

- Enter subject name (required) eg. BIOL
- Enter course number (optional) eg. 1105
- Enter course title (optional) eg. Principles of Biology

## Example Output
ARCH 1044 - Life in the Built Environment (3 Credits)

Average GPA: 3.65

Grade distribution:

![alt text](https://github.com/gsoni1/GradeDist/blob/main/output.png)

Top Professors by GPA:

Professor Tew, GPA: 3.67, Above average

Enrollment: 1183, Withdraws: 10

Grade distribution:

![alt text](https://github.com/gsoni1/GradeDist/blob/main/output2.png)

Professors who teach Life in the Built Environment:

['Tew']
## Data

Data is from the Virginia Tech University DataCommons Database (Spring 2022 to Fall 2023, chosen to exclude grades that might be inflated due to online school)

- https://udc.vt.edu/irdata/data/courses/grades

## Analytics
![Alt](https://repobeats.axiom.co/api/embed/1df85e0eedd5a0f5eb87cb1f703ccdce58b9c47f.svg "Repobeats analytics image")
