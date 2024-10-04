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
		}}
	}}
	immediate = {{
		add_resource = {{
			{resource} = -99999999
		}}{action}
	}}
}}
'''

eventAddTech = '''
        {elseif} = {{
            limit = {{                {conditions} 
            }}
            give_technology = {{ tech = "{name}" }}
        }}'''
eventIfTech = '''\n		        has_technology = "{has}"'''
eventNotIfTech = '''\n		        NOT = {{ has_technology = "{hasnot}" }}'''