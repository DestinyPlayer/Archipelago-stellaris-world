eventStart = 'namespace = archipelago_dynamic\n'

eventTemplate = '''
country_event = {{
	id = archipelago_dynamic.{num}
	title = "archipelago_dynamic.{num}.name"
	desc = "archipelago_dynamic.{num}.desc"
	picture = GFX_evt_archipelago_start
	trigger = {{
		resource_stockpile_compare = {{
			resource = {resource}
			value = {value}
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
eventIfTech    = '''\n		        has_technology = "{has}"'''
eventNotIfTech = '''\n		        NOT = {{ has_technology = "{hasnot}" }}'''
eventGiveTech  = '''\n		    give_technology = {{ tech = "{name}" }}'''
eventIfOutTech = '''\n		has_technology = "{has}"'''