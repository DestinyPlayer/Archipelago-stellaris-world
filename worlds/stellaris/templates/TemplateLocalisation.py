localisationStart = 'l_{lang}:\n'

localisationEventTemplate = '''
archipelago_dynamic.{num}.name: "Item {receivedSent}!"
archipelago_dynamic.{num}.desc: "§M{desc}§! was {receiveSend} the Archipelago Server."
'''

localisationTechTemplate = '''
tech_{type}_{num}: "{name}"
tech_{type}_{num}_desc: "This technology unlocks the next tier of {desc} technology."
'''

localisationExternalTechTemplate = '''
tech_{type}_{num}: "{name}"
tech_{type}_{num}_desc: "This technology sends the {name} item to another player."
'''