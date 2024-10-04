techStart = '@progressive_cost = 9999999\n'

techProgCost = "@progressive_cost"

techTemplate = '''
tech_progressive_{type}_{num} = {{
    cost = {cost}
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
