"""Module for parsing the student's checkboxes and
generating a summary plot of class progress"""

from choochoo import management
import matplotlib.pyplot as plt
import numpy as np
import re

issue_template_path = "./.github/ISSUE_TEMPLATE/choochoo-student-thread.md"
output_file_path = "./plots/summary_plot.png"

def parse_tickboxes():
"""Parse issue data and sum up the number of ticked boxes for each objective.
Return as a dictionary with each objective as the key and number of ticks as the value."""

	issue_template_content = management.Repository.pygh_repo.get_contents(issue_template_path).decoded_content.decode()
	objectives = re.findall(r'\[ ] (.*)\n', issue_template_content)
	student_issues = repo.student_issues(labels=[issue_template_label])
    tick_count = dict.fromkeys(objectives,0)

	for issue in student_issues:
	    body = issue.body
	    for objective in tick_count.keys():
	        if objective in body:
	            splits = body.split(objective,maxsplit=2)
	            if splits[0][-4:-1] == '[x]':
	                tick_count[objective] += 1
	        else:
	            print("problem: '{}' not in string in issue # {}".format(task, issue.number))

	return tick_count

def create_plot(tick_count):
	""" Create a bar chart to summarise class progress. Lists objectives and the number
	of instances where that objective has been ticked """

	num_objectives = len(tick_count)
	fig, ax = plt.subplots(1,1,figsize=(20,num_objectives))

	ax.barh(np.arange(num_objectives),tick_count.values(), align='center')
	ax.set_yticks(np.arange(num_objectives))
	ax.set_xticks(np.arange(issue_count+0.1))
	ax.set_yticklabels(tick_count.keys())
	ax.invert_yaxis()
	ax.set_xlabel('# of checked boxes')

	for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
	             ax.get_xticklabels() + ax.get_yticklabels()):
	    item.set_fontsize(20)

	plt.tight_layout()
	plt.savefig(output_file_path,dpi=250)

