eventStart = 'namespace = archipelago_dynamic\n'

eventTemplate = '''
country_event = {{
	id = archipelago_dynamic.{num}
	hide_window = yes
	trigger = {{
		resource_stockpile_compare = {{
			resource = {resource}
			value {equalmore} {value}
		}}{outResearch}
	}}
	immediate = {{
		add_resource = {{
			{resource} = {postValue}
		}}{action}
	}}
}}
'''

eventAction = '''
        {elseif} = {{
            limit = {{                {conditions} 
            }}{result}
        }}'''
eventIfTech    = '''\n		        has_technology = {has}'''
eventNotIfTech = '''\n		        NOT = {{ has_technology = "{hasnot}" }}'''
eventGiveTech  = '''\n		    give_technology = {{ tech = "{name}" }}'''
eventIfOutTech = '''\n		has_technology = {has}'''
eventUnsetVar  = '''\n		NOT = {{ is_variable_set = {varname} }}'''
eventSetVar    = '''\n        set_variable = {{ which = {varname} value = 1 }}'''
