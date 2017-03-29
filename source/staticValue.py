#coding=utf-8
from xml.dom.minidom import parse
import xml.dom.minidom

#field list for output
"""v1.1 added Sub-domain,Tribe by Calvin"""
_output_field=['teamId','name','startDate','endDate','deliveredStories','storyPointsDelivered',
'committedStoryPoints','deployments','defects','cycleTimeInBacklog','cycleTimeWIP','memberCount','teamSatisfaction','clientSatisfaction','comment','createdBy','createDate','Sub-domain','Tribe']

#field result show in the statistics 
_result_fields=['Velocity','     Squads','     Iterations','Throughput','Deployments','Defects','Backlog','WIP','     %Iteration','     #Iteration','     Teams with 5-12 member','     Team with <5 members','     Team with >12 members','     Team Sat','     Client Sat']

#month dict
month_dic = {'1':'Jan','2':'Feb','3':'Mar','4':'Apr','5':'May','6':'Jun','7':'Jul','8':'Agu','9':'Sep','10':'Oct','11':'Nov','12':'Dec'}

iteration_url = 'https://agiletool.mybluemix.net/api/iteration/searchTeamIteration?id='

"""get static value from properties.txt file"""
def parseFromTxt(file_path):
	f = open(file_path, 'r')
	dic = {}
	
	for line in f:
		p_tmp = line.strip().split('=')
		if len(p_tmp) > 1:
			dic[p_tmp[0]] = p_tmp[1]
		else:
			t_temp = p_tmp[0].split('@')
			"""get team ID&name dic"""
			dic[t_temp[0]] = t_temp[1]
			"""v1.1 begin added Sub-domain,Tribe by Calvin"""
			if len(t_temp) > 3:
				dic[t_temp[0]+'Tribe'] = t_temp[2]
				dic[t_temp[0]+'Sub-domain'] = t_temp[3]
			else:
				dic[t_temp[0]+'Tribe'] = 'None'
				dic[t_temp[0]+'Sub-domain'] = t_temp[2]
			"""v1.1 end"""
	return dic

"""v1.2 begin get static value from properties.xml file"""
def parseFromXml(file_path):
	dic = {}
	data = parse(file_path).documentElement
	dic['geckodriver_path'] = data.getElementsByTagName('geckodriver_path')[0].childNodes[0].data
	dic['att_login_url'] = data.getElementsByTagName('att_login_url')[0].childNodes[0].data

	for sub_domain in data.getElementsByTagName('sub-domain'):
		for tribe in sub_domain.getElementsByTagName('tribe'):
			for squad in tribe.getElementsByTagName('squad'):
				team_id = squad.getElementsByTagName('id')[0].childNodes[0].data
				dic[team_id] = squad.getAttribute('name')
				dic[team_id+'Tribe'] = tribe.getAttribute('name')
				dic[team_id+'Sub-domain'] = sub_domain.getAttribute('name')

	return dic
"""v1.2 end"""

# dic = parseFromTxt('properties.txt')
dic = parseFromXml('properties.xml')