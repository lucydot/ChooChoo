"""Module for 
generating summary plots"""

import matplotlib.pyplot as plt
from choochoo import repository

issue_template_path = "./.github/ISSUE_TEMPLATE/choochoo-student-thread.md"
output_plot_path = "./plots/summary_plot.png"

def create_plot(tick_count):
	""" Create a bar chart to summarise class progress. Lists objectives and the number
	of instances where that objective has been ticked """

	num_objectives = len(tick_count)
	fig, ax = plt.subplots(1,1,figsize=(20,num_objectives))
	
	issue_count = repository.Repository().student_issues().totalCount 

	ax.barh(range(num_objectives),tick_count.values(), align='center')
	ax.set_yticks(range(num_objectives))
	ax.set_xticks(range(issue_count+0.1))
	ax.set_yticklabels(tick_count.keys())
	ax.invert_yaxis()
	ax.set_xlabel('# of checked boxes')

	for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
	             ax.get_xticklabels() + ax.get_yticklabels()):
	    item.set_fontsize(20)

	plt.tight_layout()
	plt.savefig(output_plot_path,dpi=250)

