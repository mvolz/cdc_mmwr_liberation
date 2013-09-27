from django.db import models


class Disease(models.Model):
	name = models.CharField(max_length = 100, blank = True, null = True,)
	#A disease can have another disease as a super category. For instance,
	#Dengue Hemorrhagic Fever and Dengue Fever are both Dengue Virus Infections
	super_category = models.ForeignKey('self')
	
#In most cases, weekly data is available and should be reported as
#'week' data. In some cases, weekly cumulative data is collected and
#this can also be stored here, but weekly data should be calculated
#from the cumulative the data type should be stored as
#cumulative to indicate that the morbidity_count was calculated. Ideally 
#will be no overlaps in time periods in this set.
class MorbidityData(models.Model):
	dt_choices = (
('year_ch','Calculated from a yearly cumulative'),
('quar_cu','Calculated from a quarterly cumulative'),
('week','Reported over the course of a week'),
)
	data_type = models.CharField(choices = dt_choices, max_length = 20 , blank = True, null = True,)
	disease = models.ForeignKey(Disease)
	from_date = models.DateField(blank = True, null = True)
	to_date = models.DateField(blank = True, null = True)
	morbidity_count = models.IntegerField(blank = True, null=True)
	
#Below is a class that can be used to store the raw data exactly as 
#listed in the MMRW tables- just in case we need to do that.
 
class RawMorbidity(models.Model):
	'''
	Almost every disease has a yearly cumulative ('year').
	Many have also have weekly data ('week').
	Very few have quarterly cumulatives ('quar').
	'''
	disease = models.ForeignKey(Disease)
	per_choices = (('year','Cumulative year'),('quar','Cumulative quarter'), ('week','week'))
	period = models.CharField(choices = per_choices, max_length = 4 , blank = True, null = True,)
	period_value = models.IntegerField(blank = True, null=True)
	week = models.IntegerField(blank = True, null=True)
	morbidity_count = models.IntegerField(blank = True, null=True)
