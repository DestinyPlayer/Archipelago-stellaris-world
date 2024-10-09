techStart = '''@progressive_cost_0 = 9999999
@progressive_cost_1 = 1000
@progressive_cost_2 = 4000
@progressive_cost_3 = 10000
@progressive_cost_4 = 24000
@progressive_cost_5 = 40000

@tier0weight1 = 0
'''

techProgCost = "@progressive_cost_"

techTemplate = '''
tech_{type}_{num} = {{
    cost = {cost}
    area = {area}
    is_rare = yes
    potential = {{
        is_ai = no
    }}
    tier = {tier}
    category = {{ {category} }}
    weight = @tier{weight}weight1{weight_null}
}}
'''
weightNull = '''
    weight_modifier = {
		factor = 0
	}'''