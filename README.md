# GradeDist
<p align="center">
	<img alt="GitHub latest commit" src="https://img.shields.io/github/last-commit/gsoni1/GradeDist">
	<br>
	<span>A free tool to help you plan your courses based on grade distribution and other metrics</span><br><br>
	<small>Made by <a href="https://www.linkedin.com/in/gsoni16/">Gautam Soni</a></small>
</p>

## About

GradeDist is a tool that helps plan your courses based on metrics including

- Overall GPA and grade distribution (%)
- Sorts professors by average GPA and shows their grade distribution (%)
- Enrollment and Withdraws
- Professors who teach the course

## Screenshot
![Example screenshot](https://imgur.com/gallery/cli-bvXLqcK.png)

## Installation
Requirements:
- Python 3.9.12+
- Pandas
- IDE to run the python file (optional)
  
Process:
- Download the grade_dist.py and gradeddistriubtion.csv files
- Install python and pandas

## How to use
Run grade_dist.py from the terminal (cmd for Windows) or through an IDE (I recommend Visual Studio Code):
```sh
cd ... #directory containing the grade_dist.py and gradeddistriubtion.csv files
python grade_dist.py
```
- Enter subject name (required) eg. BIOL
- Enter course number (optional) eg. 1105
- Enter course title (optional) eg. Principles of Biology

## Example Output
BIOL 1105 - Principles of Biology (3 Credits)

Average GPA: 2.5

Grade distribution:

A: 18.8%

A-: 0.0%

B+: 0.0%

B: 33.7%

B-: 0.0%

C+: 0.0%

C: 30.7%

C-: 0.0%

D+: 0.0%

D: 12.6%

D-: 0.0%

F: 4.21%

Top Professors by GPA:

Professor Rosenzweig, GPA: 2.93, Above average

Enrollment: 230, Withdraws: 9

Grade distribution:

A: 35.2%

A-: 0.0%

B+: 0.0%

B: 34.3%

B-: 0.0%

C+: 0.0%

C: 23.0%

C-: 0.0%

D+: 0.0%

D: 3.5%

D-: 0.0%

F: 3.9%


Professor Hogan, GPA: 2.77, Above average

Enrollment: 180, Withdraws: 8

Grade distribution:

A: 26.7%

A-: 0.0%

B+: 0.0%

B: 40.6%

B-: 0.0%

C+: 0.0%

C: 21.1%

C-: 0.0%

D+: 0.0%

D: 6.7%

D-: 0.0%

F: 5.0%

Professors who teach Principles of Biology:

['Rosenzweig' 'Hogan' 'Emori' 'Bretz' 'Walker' 'Braswell' 'Lipscomb' 'Watkinson']

## Distributions

- Terminal/CLI/Python File
- Website (coming soon)

## Data

Data is from the Virginia Tech University DataCommons Database (Spring 2022 to Fall 2023, chosen to exclude grades that might be inflated due to online school)

- https://udc.vt.edu/irdata/data/courses/grades

## Analytics
![Alt](https://repobeats.axiom.co/api/embed/1df85e0eedd5a0f5eb87cb1f703ccdce58b9c47f.svg "Repobeats analytics image")
