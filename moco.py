def filterTags(attrs):
	if not attrs: return

	tags = {}
	tags.update({'name':attrs['PARK_NAME'].strip().replace(" LP"," Local Park").replace(" NP"," Neighborhood Park").replace(" UP"," Urban Park").replace(" SP"," Special Park").replace(" SVU"," Stream Valley Unit").replace(" SVP"," Stream Valley Park").replace(" CP"," Conservation Park").replace(" NCA"," Neighborhood Conservation Area")})
	tags.update({'website':attrs['URL'].strip()})
	tags.update({'owner':attrs['OWNER'].strip()})

	if attrs['STATUS'] == "Proposed":
		tags.update({'proposed':'leisure'})

	#automagically convert type
	if attrs['TYPE_']:
		if attrs['TYPE_'] == "Conservation":
			tags.update({'leisure':'nature_reserve'})
			tags.update({'boundary':'protected_area'})
			tags.update({'protection_title':'Conservation Area'})
			tags.update({'protect_class':'6'})
		elif attrs['TYPE_'] == "Local":
			tags.update({'leisure':'park'})
			tags.update({'boundary':'protected_area'})
			tags.update({'protection_title':'Local Park'})
			tags.update({'protect_class':'5'})
		elif attrs['TYPE_'] == "Misc. Non-Recreational Facility":
			tags.update({'boundary':'protected_area'})
			tags.update({'protection_title':'Miscellaneous Non-Recreational Facility'})
			tags.update({'protect_class':'5'})
		elif attrs['TYPE_'] == "Misc. Recreational Facility":
			tags.update({'boundary':'protected_area'})
			tags.update({'protection_title':'Miscellaneous Recreational Facility'})
			tags.update({'protect_class':'5'})
		elif attrs['TYPE_'] == "Municipal":
			tags.update({'leisure':'park'})
			tags.update({'boundary':'protected_area'})
			tags.update({'protection_title':'Municipal Park'})
			tags.update({'protect_class':'6'})
		elif attrs['TYPE_'] == "Neighborhood":
			tags.update({'leisure':'park'})
			tags.update({'boundary':'protected_area'})
			tags.update({'protection_title':'Neighborhood Park'})
			tags.update({'protect_class':'6'})
		elif attrs['TYPE_'] == "Neighborhood Conservation":
			tags.update({'leisure':'nature_reserve'})
			tags.update({'boundary':'protected_area'})
			tags.update({'protection_title':'Neighborhood Conservation Area'})
			tags.update({'protect_class':'6'})
		elif attrs['TYPE_'] == "Regional":
			tags.update({'leisure':'park'})
			tags.update({'boundary':'protected_area'})
			tags.update({'protection_title':'Regional Park'})
			tags.update({'protect_class':'6'})
		elif attrs['TYPE_'] == "Special":
			tags.update({'leisure':'park'})
			tags.update({'boundary':'protected_area'})
			tags.update({'protection_title':'Special Park'})
			tags.update({'protect_class':'6'})
		elif attrs['TYPE_'] == "State":
			tags.update({'leisure':'park'})
			tags.update({'boundary':'protected_area'})
			tags.update({'protection_title':'State Park'})
			tags.update({'protect_class':'6'})
		elif attrs['TYPE_'] == "Stream Valley":
			tags.update({'leisure':'park'})
			tags.update({'boundary':'protected_area'})
			tags.update({'protection_title':'Stream Valley Park'})
			tags.update({'protect_class':'6'})
		elif attrs['TYPE_'] == "Urban":
			tags.update({'leisure':'park'})
			tags.update({'boundary':'protected_area'})
			tags.update({'protection_title':'Urban Park'})
			tags.update({'protect_class':'6'})
		elif attrs['TYPE_'] == "Water Supply":
			tags.update({'boundary':'protected_area'})
			tags.update({'protection_title':'Water Supply'})
			tags.update({'protect_class':'27'})
		elif attrs['TYPE_'] == "WWTP":
			tags.update({'man_made':'wastewater_plant'})
			tags.update({'boundary':'protected_area'})
			tags.update({'protection_title':'Waste Water Treatment Plant'})
			tags.update({'protect_class':'27'})

	return tags
