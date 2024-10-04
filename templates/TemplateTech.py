techStart = '@progressive_cost = 9999999\n'

techTemplate = '''
tech_progressive_{type}_{num} = {{
    cost = @progressive_cost
    area = {area}
    is_rare = yes
    tier = 5
    category = {{ {category} }}
    weight = 0
    weight_modifier = {{
		factor = 0
	}}
}}
'''
