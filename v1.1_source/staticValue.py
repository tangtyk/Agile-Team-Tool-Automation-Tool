
#field list for output
"""v1.1 added Sub-domain,Tribe by Calvin"""
"""v1.2 added defect related column , and the display value"""
_output_field=[{'teamId':'Team id'},{'name':'Team name'},{'startDate':'Iteration start date'},{'endDate':'Iteration end date'},{'deliveredStories':'Stories/Cards/Tickets-Delivered'},{'storyPointsDelivered':'Story points delivered'},{'committedStoryPoints':'Story points - Committed'},{'deployments':'Deployments this iteration'},{'defectsStartBal':'Opening balance'},{'defects':'New this iteration'},{'defectsClosed':'Resolved this iteration'},{'defectsEndBal':'Closing balance'},{'cycleTimeInBacklog':'Cycle time in backlog (days)'},{'cycleTimeWIP':'Cycle time in WIP (days)'},{'memberCount':'Team members this iteration'},{'teamSatisfaction':'Team satisfaction'},{'clientSatisfaction':'Client satisfaction'},{'comment':'Comment about this iteration'},{'createdBy':'Created By'},{'createDate':'Create Date'},{'Sub-domain':'Sub-domain'},{'Tribe':'Tribe'}]

#field result show in the statistics 
_result_fields=['Velocity','     Squads','     Iterations','Throughput','Deployments','Defects','Backlog','WIP','     %Iteration','     #Iteration','     Teams with 5-12 member','     Team with <5 members','     Team with >12 members','     Team Sat','     Client Sat']

#month dict
month_dic = {'1':'Jan','2':'Feb','3':'Mar','4':'Apr','5':'May','6':'Jun','7':'Jul','8':'Agu','9':'Sep','10':'Oct','11':'Nov','12':'Dec'}

iteration_url = 'https://agiletool.mybluemix.net/api/iteration/searchTeamIteration?id='

"""get static value from property file"""
f = open('properties.txt', 'r')
dic = {}
team_dic = {}

for line in f:
	p_tmp = line.strip().split('=')
	if len(p_tmp) > 1:
		p_n = p_tmp[0]
		p_v = p_tmp[1]
		dic[p_n] = p_v
	else:
		t_temp = p_tmp[0].split('@')
		"""get team ID&name dic"""
		team_dic[t_temp[0]] = t_temp[1]
		"""v1.1 begin added Sub-domain,Tribe by Calvin"""
		team_dic[t_temp[0]+'Sub-domain'] = t_temp[2]
		if len(t_temp) > 3:
			team_dic[t_temp[0]+'Tribe'] = t_temp[3]
		else:
			team_dic[t_temp[0]+'Tribe'] = 'None'
		"""v1.1 end"""