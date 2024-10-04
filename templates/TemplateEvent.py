eventStart = 'namespace = archipelago_dynamic\n'

eventTemplate = '''
country_event = {{
	id = archipelago_dynamic.{evnum}
	title = "archipelago_dynamic.{evnum}.name"
	desc = "archipelago_dynamic.{evnum}.desc"
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
		}}
	}}
}}
'''