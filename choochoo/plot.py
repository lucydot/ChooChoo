"""Module for 
generating summary plots"""

import matplotlib.pyplot as plt
from choochoo import student_issue_template_path, output_plot_path

def create_plot(repository,tick_count):
	""" Create a bar chart to summarise class progress. Lists objectives and the number
	of instances where that objective has been ticked """

	num_objectives = len(tick_count)
	fig, ax = plt.subplots(1,1,figsize=(20,num_objectives))
	
	issue_count = repository.student_issues().totalCount 

    # prob a neater way to do the below
	tick_count_list = []
	for value in tick_count.values():
		tick_count_list.append(value["select"])

	ax.barh(range(num_objectives),tick_count_list, align='center')
	ax.set_yticks(range(num_objectives))
	ax.set_xticks(range(issue_count+1))
	ax.set_yticklabels(tick_count.keys())
	ax.invert_yaxis()
	ax.set_xlabel('# completed')

	for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
	             ax.get_xticklabels() + ax.get_yticklabels()):
	    item.set_fontsize(20)

	plt.tight_layout()
	plt.savefig(output_plot_path,dpi=250)

