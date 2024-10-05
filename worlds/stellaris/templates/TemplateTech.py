techStart = '@progressive_cost = 9999999\n'

techProgCost = "@progressive_cost"

techTemplate = '''
tech_progressive_{type}_{num} = {{
    cost = {cost}
    area = {area}
    is_rare = yes
    tier = {tier}
    category = {{ {category} }}
    weight = {weight}{weight_null}
}}
'''
weightNull = '''
    weight_modifier = {
		factor = 0
	}'''