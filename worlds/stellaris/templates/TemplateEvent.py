eventStart = 'namespace = archipelago_dynamic\n'

eventTemplate = '''
country_event = {{
	id = archipelago_dynamic.{num}
	hide_window = no
	trigger = {{
	    AND = {{
	        resource_stockpile_compare = {{
	            resource = {resource}
	            value = {value}
	        }}{outResearch}{varCheck}
        }}
	}}
	immediate = {{
		add_resource = {{
			{resource} = {postValue}
		}}{action}
	}}
}}
'''

eventTemplateReceive = '''
country_event = {{
	id = archipelago_dynamic.{num}
	hide_window = yes
	trigger = {{
	    AND = {{
	        OR = {{
                resource_stockpile_compare = {{
                    resource = {resource}
                    value {equalmore} {value}
                }}
            }}{varcheck}
        }}
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
eventIfOutTech = '''\n		{extratab}has_technology = "{has}"'''
eventUnsetVar  = '''\n		{extratab}NOT = {{ is_variable_set = {varname} }}'''
eventSetVar    = '''\n        {extratab}set_variable = {{ which = {varname} value = 1 }}'''
