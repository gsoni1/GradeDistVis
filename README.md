# GradeDistVis

<p align="center">
	<img alt="" src="https://github.com/gsoni1/GradeDist/blob/main/highresoutput.jpg">
	<br>
	<span>A free tool to help you plan your courses based on grade distribution and other metrics</span><br><br>
	<span>For Virginia Tech students, by <a href="https://www.linkedin.com/in/gsoni16/">Gautam Soni</a></small> </span><br><br>
</p>

## About

GradeDistVis is a tool that helps plan your courses based on metrics including

- Overall GPA and grade distribution (%)
- Sorts professors by average GPA and shows their best grade distribution (%)
- Enrollment and Withdraws
- Professors who teach the course

### Built with Python, Gradio, Pandas, Hugging Face, Seaborn, Matplotlib, Jupyter Notebook

## Versions
- <a href=https://huggingface.co/spaces/gsoni/GradeDistVis>Web version (Best Experience) </a></small>  
- Terminal/CLI/IDE (.py)
- Jupyter Notebook (.ipynb)

## Installation
Requirements:
- Python 3.9.12+
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook to run the ipynb file (optional)
- IDE to run the python file (optional)
  
Process:
- Download the grade_dist_vis.py or grade_dist_vis.ipynb and gradedist.csv files
- Install python, matplotlib, seaborn, and jupyter notebook (if using the .ipynb version)

## How to use
Run grade_dist_vis.py from the terminal (cmd for Windows):
```sh
cd ... #directory containing the grade_dist_vis.py and gradeddistriubtion.csv files
python grade_dist_vis.py
```
or through an IDE (I recommend Visual Studio Code)

- Enter subject name (required) eg. ECON
- Enter EITHER course number (optional) eg. 2005,
- OR course title (optional) eg. Principles of Economics

## Example Output
ECON 2005 - Principles of Economics (3 Credits)

Average GPA: 3.03

Grade distribution:

![alt text](https://github.com/gsoni1/GradeDist/blob/main/econ2005darkmode.png)

Top Professors by GPA:

Professor Wooten, GPA: 3.19, Above average

Enrollment: 53, Withdraws: 0

Grade distribution:

![alt text](https://github.com/gsoni1/GradeDist/blob/main/wootendarkmode.png)

Professors who teach Principles of Economics:

['Nurmukhametov' 'Perdue' 'Spoon' 'Mun' 'Wagnon' 'Sukhee' 'Wooten' 'Gu'
 'Owusu-Brown' 'Bandyopadhyay' 'Liu' 'Tantihkarnchana' 'Bradley']
## Data

Data is from the Virginia Tech University DataCommons Database (Spring 2022 to Spring 2024, chosen to exclude grades that might be inflated due to online school between 2020 and 2021)

- https://udc.vt.edu/irdata/data/courses/grades
