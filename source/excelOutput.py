#!/usr/bin/env python
#_*_coding:utf-8_*_
import staticValue as static_value
import logger
import xlwt
import time
import os
import calculation
#get logger
log = logger.log
log.propagate = False

class ExcelOutput(object):

	#generate file pre_name
	pre_fileName = 'ATT_Trends_'

	#generate files' folder
	generate_folder = 'generated_files'
	
	def __init(self):
		pass
	#iterate the python dict data
	def write_to_meta_sheet(self,data,sheet):
		row=0
		team_name_col=-1
		log.debug('dic length:',len(data))
		for iteration in data:
			column=0
			"""V1.2 update the iteration method to adapt display field change"""
			for v in static_value._output_field:
				for key,value in v.iteritems():
					if row == 0:
						#write header
						"""V1.2 update the print value to adapt display field change"""
						sheet.write(row,column,value)
					#write value
					if key == 'teamId':
						team_name=static_value.team_dic[data[row].get(key)]
						sheet.write(row+1,column,team_name)
						"""v1.1 begin added Sub-domain,Tribe field by Calvin"""
					elif key == 'Sub-domain':
						sheet.write(row+1,column,static_value.team_dic[data[row].get('teamId') + 'Sub-domain'])
					elif key == 'Tribe':
						sheet.write(row+1,column,static_value.team_dic[data[row].get('teamId') + 'Tribe'])
						"""v1.1 end"""
					else:
						sheet.write(row+1,column,data[row].get(key))
				column=column+1
			row=row+1

	#write data to statistics sheet
	#data format:{'yyyy-mm-dd':{'Velocity':value,'Squads':value1...}}
	def write_to_stat_sheet(self,data,sheet):
		sorted_date = calculation.sort_dict(data)
		row_start = 1
		col_start = 1
		for i,v in enumerate(static_value._result_fields):
			sheet.write(row_start+i+1,col_start,v)
		col_start += 1
		row = 0
		# log.info(sorted_date)
		for item in sorted_date:
			#print 'date key:'+k
			for k,v in item.iteritems():
			
				mon = static_value.month_dic.get(str(calculation.transformStrToDate(k).month))
				sheet.write(row_start+row,col_start,mon)
				for i,value in enumerate(static_value._result_fields):
					sheet.write(row_start+i+1,col_start,v.get(value))
				col_start += 1
			

	#write data to specific sheet
	def write_data_to_sheet(self,data,meta_sheet,static_sheet):
		self.write_to_meta_sheet(data,meta_sheet)
		stat_data = calculation.get_group_data(data)
		self.write_to_stat_sheet(stat_data,static_sheet)
		
		
	#write data to excel file
	def write_data_to_execel(self,data):
		log.info('prepare to write data to excel')
		# instance the Workbook(excel file)
		wbk = xlwt.Workbook()
		static_sheet = wbk.add_sheet('sheet 1',cell_overwrite_ok=True)
		meta_sheet = wbk.add_sheet('meta sheet',cell_overwrite_ok=True)
		#write data to excel
		self.write_data_to_sheet(data,meta_sheet,static_sheet)
		
		timeTsp = time.strftime("%Y%m%d%H%M%S",time.localtime())
		#debug point
		#pdb.set_trace()
		if os.path.exists(self.generate_folder) == False:
			os.mkdir(self.generate_folder)
		filename = self.generate_folder+'/'+self.pre_fileName+timeTsp+'.xls'
		wbk.save(filename)
		log.info('excel file has been generated successfully')
		return True