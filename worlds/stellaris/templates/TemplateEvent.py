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
	    set_country_flag = {thisflag}_1
	    if = {{
	        limit = {{
	            AND = {{
	                OR = {{{eventflags}
	                }}
	                NOT = {{ has_country_flag = {thisflag}_2 }}
	            }}
	        }}
	        set_country_flag = {thisflag}_2
	        country_event = {{ id = {thisevent} days = 1 }}
	    }} else {{
            add_resource = {{
                {resource} = {postValue}
            }}{action}
        }}
	}}
}}

country_event = {{
    id = {thisevent1}
    is_triggered_only = yes
    immediate = {{
        remove_country_flag = {thisflag}_1
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
eventIfTech     = '''\n		        has_technology = "{has}"'''
eventNotIfTech  = '''\n		        NOT = {{ has_technology = "{hasnot}" }}'''
eventGiveTech   = '''\n		    give_technology = {{ tech = "{name}" }}'''
eventIfOutTech  = '''\n		{extratab}has_technology = "{has}"'''
eventUnsetVar   = '''\n		{extratab}NOT = {{ is_variable_set = {varname} }}'''
eventSetVar     = '''\n        {extratab}set_variable = {{ which = {varname} value = 1 }}'''
eventEventFlags = '''\n        {extratab}has_country_flag = {eventflag}_1'''
eventUnsetFlag  = '''\n        {extratab}country_event = {{ id = {thisevent}1 days = 1}}'''