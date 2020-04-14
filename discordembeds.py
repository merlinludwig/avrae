###SETUP###

{{ vIn = [a.lower() for a in ARGS ] }}
{{ vArgs = argparse(ARGS) }}
{{ vOut = ['title','desc',[],f"COMMAND USED: !downtime {' '.join(vIn)}"] }}
{{ nl = '\n' }}
{{ tb = '\t' }}
{{ vGactivity = load_json(get_gvar('7099e6ad-3f3c-4bc3-a3ef-36f11c39e058')) }}
{{ vResults = [] }}

#misc modifiers
{{ vHalfling = vArgs.last('h',False) }}
{{ vLucky = vArgs.last('l',False) }}

#activity selection
{{ vIn1 = vIn.pop(0) if len(vIn) > 0 else '' }}
{{ vIn1 = int(vIn1) if vIn1.isdigit() else 0 }}

#set title and description
{{ vOut[0] = f'{vGactivity[vIn1].title}' }}
{{ vOut[1] = f'{vGactivity[vIn1].desc}{nl+nl}{vGactivity[vIn1].usage}' }}

###ACTIVITIES###

##Help##
{{ vOut[1] = vOut[1]+f'{nl+nl}**Activities:**'+''.join([f'{nl}{a.index}. {a.title}' for a in vGactivity]) if vIn1 == 0 else vOut[1] }}

##Alter Laws##
{{ vOutput = [] }}
{{ vMod = vIn[0] if len(vIn) > 0 else '?' }}
{{ vHonorMod = int(vMod.lstrip('+-')) if vMod.lstrip('+-').isdigit() else -1 }}
{{ vHonorMod = vHonorMod * -1 if vMod[0] == '-' else vHonorMod }}
{{ vLaws = vIn[1].split('::') if len(vIn) > 1 else ['Test Law'] }}
{{ vOffenses = vIn[2].split('::') if len(vIn) > 2 else ['Test Offense'] }}
{{ vPunishments = vIn[3].split('::') if len(vIn) > 3 else ['Test Punishment'] }}
# - rolls
{{ vResults = [ [n+1] for n in range(min(len(vLaws),len(vOffenses),len(vPunishments))) ] }}
{{ [ r.append(vroll('1d100')) for r in vResults ] }}
{{ [ r.append(vroll(f'{"2" if vLucky else "1"}d20{"kh1" if vLucky else ""}{"ro1" if vHalfling else ""}+{vHonorMod}')) for r in vResults ] }}
{{ [ r.append(True if r[2].total >= 20 else False) for r in vResults ] }} }}
# - output
{{ vOutput.append(f'-f "Rolling|1d100 and {"2" if vLucky else "1"}d20{"kh1" if vLucky else ""}{"ro1" if vHalfling else ""}+{vHonorMod}"{nl}') }}
{{ vOutStr1 = ''.join([ f'{"**" if r[1].total % 10 == 1 else ""}{str(r[0])}. Alter Laws ({r[1].total}):[1/1] Law {"Passed" if r[3] else "Rejected"}, Law: {vLaws[r[0]-1]}, Offence: {vOffenses[r[0]-1]}, Punishment: {vPunishments[r[0]-1]}{", Complication:**" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[0:10] ]) }}
{{ vOutStr2 = ''.join([ f'{"**" if r[1].total % 10 == 1 else ""}{str(r[0])}. Alter Laws ({r[1].total}):[1/1] Law {"Passed" if r[3] else "Rejected"}, Law: {vLaws[r[0]-1]}, Offence: {vOffenses[r[0]-1]}, Punishment: {vPunishments[r[0]-1]}{", Complication:**" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[10:20] ]) }}
{{ vOutStr3 = ''.join([ f'{"**" if r[1].total % 10 == 1 else ""}{str(r[0])}. Alter Laws ({r[1].total}):[1/1] Law {"Passed" if r[3] else "Rejected"}, Law: {vLaws[r[0]-1]}, Offence: {vOffenses[r[0]-1]}, Punishment: {vPunishments[r[0]-1]}{", Complication:**" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[20:30] ]) }}
{{ vOutStr4 = ''.join([ f'{"**" if r[1].total % 10 == 1 else ""}{str(r[0])}. Alter Laws ({r[1].total}):[1/1] Law {"Passed" if r[3] else "Rejected"}, Law: {vLaws[r[0]-1]}, Offence: {vOffenses[r[0]-1]}, Punishment: {vPunishments[r[0]-1]}{", Complication:**" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[30:40] ]) }}
{{ vOutStr5 = ''.join([ f'{"**" if r[1].total % 10 == 1 else ""}{str(r[0])}. Alter Laws ({r[1].total}):[1/1] Law {"Passed" if r[3] else "Rejected"}, Law: {vLaws[r[0]-1]}, Offence: {vOffenses[r[0]-1]}, Punishment: {vPunishments[r[0]-1]}{", Complication:**" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[40:50] ]) }}
{{ vOutput.append(f'-f "Results|{vOutStr1}"{nl}') }}
{{ vOutput.append(f'-f "Results|{vOutStr2}"{nl}' if len(vResults) > 10 else '') }}
{{ vOutput.append(f'-f "Results|{vOutStr3}"{nl}' if len(vResults) > 20 else '') }}
{{ vOutput.append(f'-f "Results|{vOutStr4}"{nl}' if len(vResults) > 30 else '') }}
{{ vOutput.append(f'-f "Results|{vOutStr5}"{nl}' if len(vResults) > 40 else '') }}
# - errors
{{ vOutput.append(f'-f "Error|Somehow the number of laws, offenses, and punishments don\'t match up.{nl}Please double-check the COMMAND USED in the footer to see what might be wrong."{nl}') if vIn1 == 0 and len(vLaws) != len(vOffenses) or vIn1 == 0 and  len(vLaws) != len(vPunishments) else '' }}
# - Adding activity output if activity called
{{ vOut[2] = vOutput if vMod != '?' and vIn1 == 1 else vOut[2] }}

##Apply for a Position##
{{ vOutput = [] }}
{{ vMod = vIn[0] if len(vIn) > 0 else '?' }}
{{ vHonorMod = int(vMod.lstrip('+-')) if vMod.lstrip('+-').isdigit() else -1 }}
{{ vHonorMod = vHonorMod * -1 if vMod[0] == '-' else vHonorMod }}
{{ vRank = int(vIn[1]) if len(vIn) > 1 and vIn[1].isdigit() else 0 }}
{{ vPositions = vIn[2].split('::') if len(vIn) > 2 else ['Test Position'] }}
{{ vPositionRanks = vIn[3].split(' ') if len(vIn) > 3 else ['0'] }}
{{ vPositionRanks = [ int(r) if r.isdigit() else 0 for r in vPositionRanks] }}
# - rolls
{{ vResults = [ [n+1] for n in range(min(len(vPositions),len(vPositionRanks))) ] }}
{{ [ r.append(vroll('1d100')) for r in vResults ] }}
{{ [ r.append(vroll(f'{"2" if vLucky else "1"}d20{"kh1" if vLucky else ""}{"ro1" if vHalfling else ""}+{vHonorMod}+{vRank}-{vPositionRanks[vResults.index(r)]}')) for r in vResults ] }}
{{ [ r.append(True if r[2].total >= 10 else False) for r in vResults ] }} }}
# - output
{{ vOutput.append(f'-f "Rolling|1d100 and {"2" if vLucky else "1"}d20{"kh1" if vLucky else ""}{"ro1" if vHalfling else ""}+{vHonorMod}+{vRank}-{vPositionRanks[vResults.index(r)]}"{nl}') }}
{{ vOutStr1 = ''.join([ f'{"**" if r[1].total % 10 == 1 else ""}{str(r[0])}. Apply for a Position ({r[1].total}):[1/1] Position {"Claimed" if r[3] else "Unclaimed"}, Position: {vPositions[r[0]-1]}{"**" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[0:10] ]) }}
{{ vOutStr2 = ''.join([ f'{"**" if r[1].total % 10 == 1 else ""}{str(r[0])}. Apply for a Position ({r[1].total}):[1/1] Position {"Claimed" if r[3] else "Unclaimed"}, Position: {vPositions[r[0]-1]}{"**" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[10:20] ]) }}
{{ vOutStr3 = ''.join([ f'{"**" if r[1].total % 10 == 1 else ""}{str(r[0])}. Apply for a Position ({r[1].total}):[1/1] Position {"Claimed" if r[3] else "Unclaimed"}, Position: {vPositions[r[0]-1]}{"**" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[20:30] ]) }}
{{ vOutStr4 = ''.join([ f'{"**" if r[1].total % 10 == 1 else ""}{str(r[0])}. Apply for a Position ({r[1].total}):[1/1] Position {"Claimed" if r[3] else "Unclaimed"}, Position: {vPositions[r[0]-1]}{"**" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[30:40] ]) }}
{{ vOutStr5 = ''.join([ f'{"**" if r[1].total % 10 == 1 else ""}{str(r[0])}. Apply for a Position ({r[1].total}):[1/1] Position {"Claimed" if r[3] else "Unclaimed"}, Position: {vPositions[r[0]-1]}{"**" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[40:50] ]) }}
{{ vOutput.append(f'-f "Log|{vOutStr1}"{nl}') if vIn1 == 2 else ''}}
{{ vOutput.append(f'-f "Log|{vOutStr2}"{nl}' if vIn1 == 2 and len(vResults) > 10 else '') }}
{{ vOutput.append(f'-f "Log|{vOutStr3}"{nl}' if vIn1 == 2 and len(vResults) > 20 else '') }}
{{ vOutput.append(f'-f "Log|{vOutStr4}"{nl}' if vIn1 == 2 and len(vResults) > 30 else '') }}
{{ vOutput.append(f'-f "Log|{vOutStr5}"{nl}' if vIn1 == 2 and len(vResults) > 40 else '') }}
# - errors
{{ vOutput.append(f'-f "Error|Somehow the number of positions and ranks don\'t match up.{nl}Please double-check the COMMAND USED in the footer to see what might be wrong."{nl}') if len(vPositions) != len(vPositionRanks) else '' }}
# - Adding activity output if activity called
{{ vOut[2] = vOutput if vMod != '?' and vIn1 == 2 else vOut[2] }}

##Arrange Marriage##
{{ vOutput = [] }}
{{ vMod = vIn[0] if len(vIn) > 0 else '?' }}
{{ vHonorMod = int(vMod.lstrip('+-')) if vMod.lstrip('+-').isdigit() else -1 }}
{{ vHonorMod = vHonorMod * -1 if vMod[0] == '-' else vHonorMod }}
{{ vClass = int(vIn[1]) if len(vIn) > 1 and vIn[1].isdigit() else 0 }}
{{ vContact = vIn[2] if len(vIn) > 2 else ['Test Contact'] }}
# - rolls
{{ vResults = [ [n+1] for n in range(1) ] }}
{{ [ r.append(vroll('1d100')) for r in vResults ] }}
{{ [ r.append(vroll(f'{"2" if vLucky else "1"}d20{"kh1" if vLucky else ""}{"ro1" if vHalfling else ""}+{vHonorMod}')) for r in vResults ] }}
{{ [ r.append(True if r[2].total >= 15 else False) for r in vResults ] }} }}
# - output
{{ vOutput.append(f'-f "Rolling|1d100 and {"2" if vLucky else "1"}d20{"kh1" if vLucky else ""}{"ro1" if vHalfling else ""}+{vHonorMod}"{nl}') }}
{{ vOutStr1 = ''.join([ f'{"**" if r[1].total % 10 == 1 else ""}{str(r[0])}. Arrange Marriage ({r[1].total}):[1/1] Proposal {"accepted" if r[3] else "rejected"}, Contact who\'s favour was spent: {vContact}{", Dowry to be payed: 100 GP" if r[3] and vClass == 1 else "Dowry to be payed: 500 GP" if r[3] and vClass == 2 else "Dowry to be payed: 2500 GP" if r[3] and vClass == 3 else ""}{"**" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults ]) }}
{{ vOutput.append(f'-f "Log|{vOutStr1}"{nl}') if vIn1 == 3 else ''}}
# - Adding activity output if activity called
{{ vOut[2] = vOutput if vMod != '?' and vIn1 == 3 else vOut[2] }}

##Arrange Tutor##
{{ vOutput = [] }}
{{ vMod = vIn[0] if len(vIn) > 0 else '?' }}
{{ vHonorMod = int(vMod.lstrip('+-')) if vMod.lstrip('+-').isdigit() else -1 }}
{{ vHonorMod = vHonorMod * -1 if vMod[0] == '-' else vHonorMod }}
{{ vSkill = vIn[1] if len(vIn) > 1 else ['Test Language/Tool'] }}
{{ vContact = vIn[2] if len(vIn) > 2 else ['Test Contact'] }}
# - rolls
{{ vResults = [ [n+1] for n in range(min(len(vSkill),len(vContact))) ] }}
{{ [ r.append(vroll('1d100')) for r in vResults ] }}
{{ [ r.append(vroll(f'{"2" if vLucky else "1"}d20{"kh1" if vLucky else ""}{"ro1" if vHalfling else ""}+{vHonorMod}')) for r in vResults ] }}
{{ [ r.append(True if r[2].total >= 15 else False) for r in vResults ] }} }}
# - output
{{ vOutput.append(f'-f "Rolling|1d100 and {"2" if vLucky else "1"}d20{"kh1" if vLucky else ""}{"ro1" if vHalfling else ""}+{vHonorMod}"{nl}') }}
{{ vOutStr1 = ''.join([ f'{"**" if r[1].total % 10 == 1 else ""}{str(r[0])}. Arrange Tutor ({r[1].total}):[1/1] Tutor {"found" if r[3] else "not found"} for learning {vSkill}, Contact who\'s favour was spent: {vContact}{"**" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults ]) }}
{{ vOutput.append(f'-f "Log|{vOutStr1}"{nl}') if vIn1 == 4 else ''}}
# - Adding activity output if activity called
{{ vOut[2] = vOutput if vMod != '?' and vIn1 == 4 else vOut[2] }}

##Build a Stronghold##
# - don't really think we need that right now

##Buy/Sell a item##
# - don't really think we need that right now

##Buy a Magic Item##
{{ vOutput = [] }}
{{ vThis = True if vIn1 == 7 else False }}
{{ vMod = vIn[0] if len(vIn) > 0 else '?' }}
{{ vChaMod = int(vMod.lstrip('+-')) if vMod.lstrip('+-').isdigit() else -1 }}
{{ vChaMod = vChaMod * -1 if vMod[0] == '-' else vChaMod }}
{{ vMod2 = vIn[1] if len(vIn) > 1 else '?' }}
{{ vWeeks = int(vMod2) if vMod2.isdigit() else 1 }}
{{ vWeeks = 11 if vWeeks > 11 else vWeeks }}
{{ vBonus = vWeeks-1 }}
{{ vMod2 = vIn[2] if len(vIn) > 2 else '?' }}
{{ vMoney = int(vMod2) if vMod2.isdigit() and int(vMod2) > 99 else 100 }}
{{ vMoney = 100+(100*(10-vBonus)) if vMoney > 100+(100*(10-vBonus)) else vMoney }}
{{ vBonus = int(vBonus + ((vMoney-100)/100)) }}
# - rolls
{{ vResults = [ [n+1] for n in range(1) ] }}
{{ [ r.append(vroll('1d100')) for r in vResults ] }}
{{ [ r.append(vroll(f'{"2" if vLucky else "1"}d20{"kh1" if vLucky else ""}{"ro1" if vHalfling else ""}+{vChaMod}+{vBonus}')) for r in vResults ] }}
{{ [ r.append(vroll(f'{"1d6" if r[1].total < 6 else "1d4"}')) for r in vResults ] }}
# - output
{{ vOutput.append(f'-f "Rolling|1d100, {"2" if vLucky else "1"}d20{"kh1" if vLucky else ""}{"ro1" if vHalfling else ""}+{vChaMod}+{vBonus}, {"1d6" if r[1].total < 6 else "1d4"}"{nl}') }}
{{ vOutStr1 = ''.join([ f'{"**" if r[1].total % 10 == 1 else ""}{str(r[0])}. Buy a Magic Item ({r[1].total}):[{vWeeks}/{vWeeks}] Gold spent searching for a buyer: {vMoney} GP, Available items: {r[3].total}{"**" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults ]) }}
{{ vOutput.append(f'-f "Log|{vOutStr1}"{nl}') if vThis else ''}}
# - Adding activity output if activity called
{{ vOut[2] = vOutput if vMod != '?' and vThis else vOut[2] }}

##Carouse##
{{ vOutput = [] }}
{{ vThis = True if vIn1 == 8 else False }}
{{ vMod = vIn[0] if len(vIn) > 0 else '?' }}
{{ vChaMod = int(vMod.lstrip('+-')) if vMod.lstrip('+-').isdigit() else -1 }}
{{ vChaMod = vChaMod * -1 if vMod[0] == '-' else vChaMod }}
{{ vMod2 = vIn[1] if len(vIn) > 1 else '?' }}
{{ vClass = vMod2 if vMod2 == 'lower' or vMod2 == 'middle' or vMod2 == 'upper' else 'lower' }}
{{ vMod2 = vIn[2] if len(vIn) > 2 else '?' }}
{{ vWeeks = int(vMod2) if vMod2.isdigit() else 1 }}
{{ vWeeks = 50 if vWeeks > 50 else vWeeks }}
# - rolls
{{ vResults = [ [n+1] for n in range(vWeeks) ] }}
{{ [ r.append(vroll('1d100')) for r in vResults ] }}
{{ [ r.append(vroll(f'{"2" if vLucky else "1"}d20{"kh1" if vLucky else ""}{"ro1" if vHalfling else ""}+{vChaMod}')) for r in vResults ] }}
# - output
{{ vOutput.append(f'-f "Rolling|1d100, {"2" if vLucky else "1"}d20{"kh1" if vLucky else ""}{"ro1" if vHalfling else ""}+{vChaMod}"{nl}') }}
{{ vOutStr1 = ''.join([ f'{"**" if r[1].total % 10 == 1 else ""}{str(r[0])}. Carouse ({r[1].total}):[1/1] Gold spent carousing: {"10" if vClass == "lower" else "50" if vClass == "middle" else "250"} GP, Contacts({r[2].total}): {"1 Hostile" if r[2].total < 6 else "None" if r[2].total < 11 else "1 Allied" if r[2].total < 16 else "2 Allied" if r[2].total < 21 else "3 Allied"}{"**" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[0:10] ]) }}
{{ vOutStr2 = ''.join([ f'{"**" if r[1].total % 10 == 1 else ""}{str(r[0])}. Carouse ({r[1].total}):[1/1] Gold spent carousing: {"10" if vClass == "lower" else "50" if vClass == "middle" else "250"} GP, Contacts({r[2].total}): {"1 Hostile" if r[2].total < 6 else "None" if r[2].total < 11 else "1 Allied" if r[2].total < 16 else "2 Allied" if r[2].total < 21 else "3 Allied"}{"**" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[10:20] ]) }}
{{ vOutStr3 = ''.join([ f'{"**" if r[1].total % 10 == 1 else ""}{str(r[0])}. Carouse ({r[1].total}):[1/1] Gold spent carousing: {"10" if vClass == "lower" else "50" if vClass == "middle" else "250"} GP, Contacts({r[2].total}): {"1 Hostile" if r[2].total < 6 else "None" if r[2].total < 11 else "1 Allied" if r[2].total < 16 else "2 Allied" if r[2].total < 21 else "3 Allied"}{"**" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[20:30] ]) }}
{{ vOutStr4 = ''.join([ f'{"**" if r[1].total % 10 == 1 else ""}{str(r[0])}. Carouse ({r[1].total}):[1/1] Gold spent carousing: {"10" if vClass == "lower" else "50" if vClass == "middle" else "250"} GP, Contacts({r[2].total}): {"1 Hostile" if r[2].total < 6 else "None" if r[2].total < 11 else "1 Allied" if r[2].total < 16 else "2 Allied" if r[2].total < 21 else "3 Allied"}{"**" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[30:40] ]) }}
{{ vOutStr5 = ''.join([ f'{"**" if r[1].total % 10 == 1 else ""}{str(r[0])}. Carouse ({r[1].total}):[1/1] Gold spent carousing: {"10" if vClass == "lower" else "50" if vClass == "middle" else "250"} GP, Contacts({r[2].total}): {"1 Hostile" if r[2].total < 6 else "None" if r[2].total < 11 else "1 Allied" if r[2].total < 16 else "2 Allied" if r[2].total < 21 else "3 Allied"}{"**" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[40:50] ]) }}
{{ vOutput.append(f'-f "Log|{vOutStr1}"{nl}') if vThis else ''}}
{{ vOutput.append(f'-f "Log|{vOutStr2}"{nl}' if vThis and len(vResults) > 10 else '') }}
{{ vOutput.append(f'-f "Log|{vOutStr3}"{nl}' if vThis and len(vResults) > 20 else '') }}
{{ vOutput.append(f'-f "Log|{vOutStr4}"{nl}' if vThis and len(vResults) > 30 else '') }}
{{ vOutput.append(f'-f "Log|{vOutStr5}"{nl}' if vThis and len(vResults) > 40 else '') }}
# - Adding activity output if activity called
{{ vOut[2] = vOutput if vMod != '?' and vThis else vOut[2] }}

###CLEANUP AND DISPLAY###

{{ f'-title "{vOut[0]}"' }}
{{ f'-desc "{vOut[1]}"' }}
{{ ''.join(vOut[2]) }}
{{ f' -footer "{vOut[3]}"' }}

########################################################################

[
	{"index":0,
	"title":"Help",
	"desc":"To do a downtime activity, type __!downtime <n> <arguments>__\n<n> the number corresponding to the downtime activity from the list below\n<arguments> the arguments for the downtime activity\n\nFor additional help with a specific downtime activity and to see its usage, select it without any additional arguments.",
	"usage":""},
	{"index":1,
	"title":"Altar Laws",
	"desc":"Req: N/A\nWW: 1\n\nA ruler can spend time trying to change the edicts and punishments of their kingdom, though navigating through the precarious legal system is sure to incite opposition. In order for a new law to be passed, edited, or removed, the ruler must pass a DC 20 Honor Check. A law must include an offence, and a proportional punishment.",
	"usage":"**Usage:** !downtime 1 <Honor Mod> '<Law>' '<Offense>' '<Punishment>'\n<Honor Mod> This is the modifier to pass to the honor check\n<Law> The name of the law to pass. This must be surrounded in quotes. If you wish to pass multiple laws, you can seperate them like with '::' like so... 'Law 1::Law 2::Law 3'\n<Offense> The offense that recieves the punishment. This must be surrounded in quotes. If attempting to pass multiple laws, you must incorporate multiple offenses the same way, 'Offense 1::Offense 2::Offense 3'\n<Punishment> The punishment for the offense. This must be surrounded in quotes. If attempting to pass multiple laws, you must incorporate multiple punishments the same way, 'Punishment 1::Punishment 2::Punishment 3'"},	
	{"index":2,
	"title":"Apply for a Position",
	"desc":"Req: N/A\nWW: 1\n\nWhen a council position becomes vacant, all players may apply for the post. The highest position is resolved first. To win a position, each player rolls an Honor Check, adds their current rank and deducts the rank of the vacant position. If the player's total is 10 or more they moves into the new position. If two or more players achieve the score, the highest total moves into the position. If no players score 10 or more, an NPC fills the position.\n",
	"usage":"**Usage:** !downtime 2 <Honor Mod> <Rank> '<Position>' '<Position Rank>'\n<Honor Mod> This is the modifier to pass to the honor check\n<Rank> Your current rank to add to the roll.\n<Position> The position applying for. This must be surrounded in quotes. If attempting to apply for multiple positions, you can seperate them like with '::' like so... 'Figurehead::Spymaster::Royal Enforcer'\n<Position Rank> The rank of the position to which your are applying. This must be surrounded in quotes. If attempting to apply for multiple positions, you must incorporate multiple ranks seperated by spaces like so, '1 2 3'"},	
	{"index":3,
	"title":"Arrange Marriage",
	"desc":"Req: ??\nWW: 1\n\nBy spending a favour from an Allied contact, a character can spend time navigating the complex courting system of the kingdom in order to secure relations familial relations with a person related to that contact. The character must succeed a DC 15 Honor Check to be successful in their proposal attempt. Pass or fail, the favour is spent.\n\nIf the proposal is successful, the proposer is expected to pay a Dowry based on the wealth of the person they are proposing to.\n\nLower Class - 100 GP\nMiddle Class - 500 GP\nUpper Class - 2500 GP (Req: Position of Privilege, Disguise Kit, or Deception Skill) \n\nProposals between PC's are obviously expected to be handled between players",
	"usage":"**Usage:** !downtime 3 <Honor Mod> <Class> '<Contact>'\n<Honor Mod> This is the modifier to pass to the honor check\n<Class> This is the class of the person proposing to. 1,2, or 3 for lower, middle, and upper class.\n<Contact> The name of the contact who's favour you are spending. Must be surrounded by quotes like so... 'Joe Shmoe'"},	
	{"index":4,
	"title":"Arrange Tutor",
	"desc":"Req: N/A\nWW: 1\n\nBy spending a favour from an Allied contact, a character can spend time locating a teacher related to that contact. The player must declare what language or tool they wish to learn. The character must then succeed a DC 15 Honor Check to be successful in finding and persuading a teacher into passing on their skill. Pass or fail, the favour is spent. Once found, a teacher is prepared to teach (via the Train Downtime), but will leave if mistreated.",
	"usage":"**Usage:** !downtime 4 <Honor Mod> '<Skill>' '<Contact>'\n<Honor Mod> This is the modifier to pass to the honor check\n<Skill> This is the language or tool skill for which you are seeking a tutor. Must be surrounded by quotes like so... 'Common Language'\n<Contact> The name of the contact who's favour you are spending. Must be surrounded by quotes like so... 'Joe Shmoe'"},	
	{"index":5,
	"title":"Build a Stronghold",
	"desc":"Req: N/A\nWW: 1\n\nA character can spend time between adventures building a stronghold. Before work can begin, the character must acquire a plot of land. If the estate lies within a kingdom or similar domain, the character will need a grant (a legal document that serves as proof of ownership). Land grants are usually given by the crown as a reward for faithful service, although they can also be bought or inherited. A character can obtain a grant by spending the favour of a contact in the Upper Class (via Carousing).\n\nOnce the estate is secured, a character needs access to building materials and labourers. The Building a Stronghold table shows the cost of building the stronghold (including materials and labour) and the amount of time it takes, provided that the character is using downtime to oversee construction.\n\nAbbey: 50000 GP, 80 Workweeks\nGuildhall, town or city: 5000 GP, 12 Workweeks\nKeep or small castle: 50000 GP, 80 Workweeks\nNoble estate with manor: 25000 GP, 30 Workweeks\nOutpost or fort: 15000 GP, 20 Workweeks\nPalace or large castle: 500000 GP, 240 Workweeks\nTemple: 50000 GP, 80 Workweeks\nTower, fortified: 15000 GP, 20 Workweeks\nTrading post: 5000 GP, 12 Workweeks",
	"usage":"***NOT YET IMPLEMENTED***"},	
	{"index":6,
	"title":"Buy/Sell a item",
	"desc":"Req: N/A\nWW: 1\n\nA character seeking to sell or purchase mundane items does not need to make a check to find a buyer. Instead, this workweek is simply a way of formal way of logging any sales or purchases your character has made throughout the year. Use the prices in the PHB for adventure-gear prices where appropriate, and ask a DM if unsure about a price. When selling a mundane item, unless it has a value listed in it's name, it's value is always half of it's retail price (rounded down).This downtime still requires a complication roll as normal.",
	"usage":"***NOT YET IMPLEMENTED***"},	
	{"index":7,
	"title":"Buy a Magic Item",
	"desc":"Req: 100 GP\nWW: 1+\n\nA character seeking to buy a magic item makes a Charisma (Persuasion) check to determine the quality of the seller found. The Character gains a +1 bonus on the check for every workweek beyond the first that is spent seeking a seller and a +1 bonus for every additional 100 gp spent on the search, up to a maximum bonus of +10. The monetary cost includes a wealthy lifestyle, for a buyer must impress potential business partners.\n\n1-5: Roll 1d6, Ping a DM to generate available items\n6-40+: Roll 1d4, Ping a DM to generate available items \n\nIf the characters seek a specific magic item, first include the desired item among the items for sale on a check total of 10 or higher if the item is common, 15 or higher if it is uncommon, 20 or higher if it is rare, 25 or higher if it is very rare: and 30 or higher if it is legendary.\n\nPrices will be determined for the player by the DM generating the items.",
	"usage":"**Usage:** !downtime 7 <Cha Mod> <Weeks> <Money>\n<Cha Mod> Your cha mod\n<Weeks> How many weeks to spend attracting a seller\n<Money> How much money to spend attracting a seller"},	
	{"index":8,
	"title":"Carouse",
	"desc":"Req: ??\nWW: 1\n\nLower Class - 10 GP\nMiddle Class - 50 GP\nUpper Class - 250 GP (Req: Position of Privilege, Disguise Kit, or Deception Skill) \n\nAfter a workweek of carousing, a character stands to make contacts within the selected social class. The character makes a Charisma (Persuasion) check using the Carousing table.\n\n1-5: Character has made a hostile contact\n6-10: Character has made no new contacts\n11-15: Character has made an allied contact\n16-20: Character has made two allied contacts\n21+: Character has made three allied contacts. \n\nContacts are NPCs who now share a bond with the character. Each one either owes the character a favor or has some reason to bear a grudge. A hostile contact works against the character, placing obstacles but stopping short of committing a crime or a violent act. Allied contacts are friends who will render aid to the character, but not at the risk of their lives.\n\nOnce a contact has helped or hindered a character, the character needs to carouse again to get back into the NPC’s good graces. A contact provides help once, not help for life.\n\nAt any time, a character can have a maximum number of unspecified allied contacts equal to 1 + the character’s Charisma modifier (minimum of 1). While contacts can be used purely for narrative, they can be spent as a resource towards other downtime events- or be used to negate the effect of one complication.",
	"usage":"**Usage:** !downtime 8 <Persuasion Mod> '<Class>'\n<Persuasion Mod> Your persuasion mod\n<Class> Which class of people you are carousing with. This must be surrounded in quotes. It must be 'lower', 'middle', or 'upper'."},	
	{"index":9,
	"title":"Craft an Item",
	"desc":"Req: ??\nWW: ??\n\nIn addition to the appropriate tools for the item to be crafted, a character needs raw materials worth half of the item’s selling cost. To determine how many workweeks it takes to create an item, divide its gold piece cost by 50. A character can complete multiple items in a workweek if the items combined cost is 50 gp or lower. Multiple characters can combine their efforts. Divide the time needed to create an item by the number of characters working on it. Everyone who collaborates needs to have the appropriate tool proficiency.\n\nThe result of the process is an item of the desired sort. A character can sell an item crafted in this way at its listed price.",
	"usage":"***NOT YET IMPLEMENTED***"},	
	{"index":10,
	"title":"Craft a Magic Item",
	"desc":"Req: ??\nWW: ??\n\nTo start with, a character needs a formula for a magic item in order to create it. The formula is like a recipe, and can be obtained via Research. It lists the materials needed and steps required to make the item. An item invariably requires an exotic material to complete it. This material can range from the skin of a yeti to a vial of water taken from a whirlpool on the Elemental Plane of Water. Finding that material should take place as part of an adventure. The Magic ltem Ingredients table suggests the challenge rating of a creature that the characters need to face to acquire the materials for an item. Note that facing a creature does not necessarily mean that the characters must collect items from its corpse. Rather, the creature might guard a location or a resource that the characters need access to. A DM will generate a combat encounter based on the rarity of the Ingredient.\n\nIn addition to facing a specific creature, creating an item comes with a gold piece cost covering other materials, tools, and so on, based on the item’s rarity. Halve the listed price and creation time for any consumable items.\n\nTo complete a magic item, a character also needs whatever tool proficiency is appropriate, as for crafting a nonmagical object, or proficiency in the Arcana skill.\n\nCommon: 1 Workweek, 50 GP\nUncommon: 2 Workweeks, 200 GP\nRare: 10 Workweeks, 2000 GP.\nVery Rare: 25 Workweeks, 20000 GP\nLegendary: 50 Workweeks, 100000 GP \n\nHealth Potions: A character who has proficiency with the herbalism kit can create health potions without a schematic.\n\nHealing, 1 day, 25 gp\nGreater healing, 1 workweek, 100 gp\nSuperior healing, 3 workweeks, 1,000 gp\nSupreme healing, 4 workweeks, 10,000 gp \n\nBullets & Bombs: A character who has proficiency with the Gunsmithing tools can create bullets without a schematic.\n\nRenaissance Bullets (10), 1 workweek, 50 gp\nBomb, 1 workweek, 100 gp\nModern Bullets (10), 2 workweeks, 500 gp\nDynamite, 2 workweeks, 500 gp",
	"usage":"***NOT YET IMPLEMENTED***"},	
	{"index":11,
	"title":"Crime",
	"desc":"Req: 25 GP\nWW: 1\n\nThe PC must make a series of checks, with the DC for all the checks chosen by the PC according to the amount of profit sought from the crime. The chosen DC can be 10, 15, 20, or 25. Successful completion of the crime yields a number of gold pieces.\n\n10: 50 GP, robbery of a struggling merchant\n15: 100 GP, robbery of a prosperous merchant\n20: 200 GP, robbery of a noble\n25: 1,000 GP, robbery of the richest figures in town\n\nTo attempt a crime, the PC makes three checks: Dexterity (Stealth), Dexterity using thieves' tools, and the player's choice of Intelligence (Investigation), Wisdom (Perception), or Charisma (Deception). \n\n0 Successes: the PC is caught and jailed. The PC must pay a fine equal to the profit the crime would have earned and must spend one day in jail for each 25 GP of the fine. \n1 Successes: the heist fails but the PC escapes.\n2 Successes: the heist is a partial success, netting the PC half the payout.\n3 Successes: the PC earns the full value of the loot.",
	"usage":"***NOT YET IMPLEMENTED\n(for now, use !crime)***"},	
	{"index":12,
	"title":"Discover Schematic",
	"desc":"Req: N/A\nWW: 5\n\nBy spending a favor from an Allied contact or temple, a character can consult their ally for access to their collections or extensive networks, to gather scientific papers or ancient lore.\n\nThe character makes a Honor check using the Schematic table. \n\n1-10: Character finds an Unidentified common schematic\n11-15: Character finds an Unidentified uncommon schematic \n16-20: Character finds an Unidentified rare schematic\n20-25: Character finds an Unidentified very rare schematic \n26+: Character finds an Unidentified Legendary schematic\n\nThese Unidentified Schematics can encompass the mechanical fundamentals necessary for blueprinting a specific Magic Item design of the Researchers choice (See Research).",
	"usage":"***NOT YET IMPLEMENTED***"},	
	{"index":13,
	"title":"Gain Renown",
	"desc":"Req: N/A\nWW: 10\n\nDuring the turn, all characters can compete for the affection of the realms Councils. This is done by investing extended time working alongside with them. Each character has a pool of social points equal to their Honor Modifier (Min 1), and secretly tells the Ruler how many points they are going to spend on each Council. Each kingdoms councils are divided as follows: Ports, Citadels, Marketplaces, Temples, Walls and Shanty Towns. At the end of the Turn the ruler declares who invested the most points in a council, earning that councils approval for the next turn. Ties between players are settled by an Honor Check Contest, as councils can only approve of one character at a time.\n\nIf a character is approved by the Shanty Town, in the next social phase they can use bribes to gain the affections of other Councils. The bribe counts as as giving three points of social time to a Council but cannot be used on the Shanty Town itself. The same rules apply to a character approved by the Citadel, except that the militia use physical threats instead of bribes.\n\nThis Downtime Activity can only be used once per Turn.",
	"usage":"***NOT YET IMPLEMENTED***"},	
	{"index":14,
	"title":"Gambling",
	"desc":"Req: 10-1000 GP\nWW: 1\n\nThe PC declares a bet and then makes a series of checks, with a DC determined at random based on the quality of the competition that the PC runs into. Part of the risk of gambling is that one never knows who might end up sitting across the table. The PC makes three checks: Wisdom (Insight), Charisma (Deception), and Charisma (Intimidation). If the PC has proficiency with an appropriate gaming set, that tool proficiency can replace the relevant skill in any of the checks. The DC for each of the checks is 5 + 2d10; generate a separate DC for each one. Consult the Gambling Results table to see how the PC did.\n\n[PCs may not use trick dice or cards for downtime gambling advantage but they may use them for flavour.]\n\n0 successes: Lose all the money you bet and accrue a debt equal to that amount.\n1 success: Lose half the money you bet.\n2 successes: Gain the amount you bet plus half again more.\n3 successes: Gain double the amount you bet.",
	"usage":"***NOT YET IMPLEMENTED\n(for now, use !gambling)***"},	
	{"index":15,
	"title":"Compel Honor Duel",
	"desc":"Req: N/A\nWW: 1\n\nGenerals and characters liked by the Citadels have the power to formally compel other council leaders or the Ruler into a 1 on 1 duel. If the player being challenged refuses or loses the duel, they must resign from their position. If the player being challenged wins, the challenger is required to pay them 1D6 * 100 GP in compensation. Duels are typically overseen by a third party, such as a High Priest. Duels are typically fought until one side concedes, and duels to the death are extremely rare. If an agreement is reached, the two can change the terms of the duel to accommodate the needs of the combatants.\n\nInformal duels between characters do not require downtime.\n\nThis Downtime Activity can only be used once per Turn.",
	"usage":"***NOT YET IMPLEMENTED***"},	
	{"index":16,
	"title":"Perform Duty",
	"desc":"Req: N/A\nWW: 10\n\nPC's in an office must spend time to carry out their duties. How well an officer performs in their office depends upon whether he has the support of his council or not. If an officer is liked by his staff, they perform well and the character gains 1000 GP. If the council like an opposing player, that player can persuade them to work slowly and cause trouble for their officer. The affected officer must succeed a DC 13 Honor Saving Throw or make 0 GP that turn.\n\nThis Downtime Activity can only be used once per Turn.",
	"usage":"***NOT YET IMPLEMENTED***"},	
	{"index":17,
	"title":"Pit Fighting",
	"desc":"Req: N/A\nWW: 1\n\nThe character makes a series of checks, with a DC determined at random based on the quality of the opposition that the character runs into.  A big part of the challenge in pit fighting lies in the unknown nature of a character’s opponents.\n\nThe character makes three checks: Strength (Athletics), Dexterity (acrobatics), and a special constitution check that has a bonus equal to a roll of the character’s largest Hit Die (this roll doesn’t spend that die).  If desired, the character can replace one of these skill check with an attack roll using one of the character’s weapons. The DC for each check is 5 + 2d10; generate a separate DC for each one. Consult the Pit Fighting Results table to see how the character did.\n\n0 successes: Lose your bouts, earning nothing\n1 success: Win 50 GP\n2 successes: Win 100 GP\n3 successes: Win 200 GP",
	"usage":"***NOT YET IMPLEMENTED\n(for now, use !pitfighting)***"},	
	{"index":18,
	"title":"Produce Letter of Recommendation",
	"desc":"Req: N/A\nWW: 1\n\nBy spending a favor from an Allied contact or temple (see Carousing & Religious Service), a characters benefactor can provide them with a letter of recommendation. Usually enclosed in a case, or scroll tube for safe transport, and bears the signature and seal of whoever wrote it. A letter of recommendation from a person of Lower, Middle, or Higher Class reputation can grant adventurers access to NPCs of a similar demographic, such as Sailors, Merchants, and Nobles.\n\nCarrying a recommendation on one's person can also help clear up \"misunderstandings\" with local authorities who might not otherwise take the adventurers at their word, assuming the contact has influence over the security.\n\nA character can use a Letter of Recommendation to contact establishments for aid and specialist supplies. This effectively halves the GP and Downtime Cost (min 1) for Crafting Magic Items, and Scribing Spell Scrolls. Once a Letter of Recommendation has been used this way, it loses it's inherent value and cannot be used again in the same way.\n\nA letter of recommendation is worth only as much as the person who wrote it and offer no benefit in places outside where its writer holds sway.",
	"usage":"***NOT YET IMPLEMENTED***"},	
	{"index":19,
	"title":"Relaxation",
	"desc":"Req: N/A\nWW: 1\n\nPCs who maintain at least a modest lifestyle while relaxing gain several benefits. While relaxing, a PC gains advantage on saving throws to recover from long-acting diseases and poisons. In addition, at the end of the week, a PC can end one effect that keeps the PC from regaining hit points or can restore one ability score that has been reduced to less than its normal value. This benefit cannot be used if the harmful effect was caused by a spell or some other magical effect with an ongoing duration.",
	"usage":"***NOT YET IMPLEMENTED***"},	
	{"index":20,
	"title":"Religous Service",
	"desc":"Req: 25 GP\nWW: 1\n\nThe PC chooses to make either an Intelligence (Religion) check or a Charisma (Persuasion) check. The total of the check determines the benefits of service, as shown on the Religious Service table.\n\n1-10:Your efforts fail to make a lasting impression.\n11-20: You earn one favour.\n21+: You earn two favours \n\nFavour, in broad terms, is a promise of future assistance from a representative of the temple. It can be expended to ask the temple for help in dealing with a specific problem, for general political or social support, or to reduce the cost of cleric spellcasting by 50%. Favour could also take the form of a deity's intervention, such as an omen, a vision, or a minor miracle provided at a key moment. This latter sort of favour is determined by the DM and the Admins, who also determine its nature. Favours earned need not be expended immediately, but only a certain number can be stored up. A PC can have a maximum number of unused favors equal to 1 + the PC's Charisma modifier (1 minimum).",
	"usage":"***NOT YET IMPLEMENTED***"},	
	{"index":21,
	"title":"Research",
	"desc":"Req: 50 GP\nWW: 1\n\nThe PC declares the focus of the research—a specific person, place, item formula or thing. After one week, the PC makes an Intelligence check with a +1 bonus per 100 gp spent beyond the initial 50 gp, to a maximum of +6. In addition, a PC who has access to a particularly well-stocked library or knowledgeable sages gains advantage on this check.\n\n1-5: No effect.\n6-10: You learn one piece of lore.\n11-20: You learn two pieces of lore.\n21+: You learn three pieces of lore \n\nIn this setting, you can spend lore to draw up a schematic of a magic item in your possession, but the process requires dissembling the item to the point where it beyond reuse.\n\nAdditionally, a character can spend lore on analysing unidentified schematics. If the characters is seeking a specific magic item, the formula for the desired item is found on a check total of 10 or higher if the item is common, 15 or higher if it is uncommon, 20 or higher if it is rare, 25 or higher if it is very rare: and 30 or higher if it is legendary. Otherwise, ping a DM to generate a magic item schematic that the character identifies.",
	"usage":"***NOT YET IMPLEMENTED***"},	
	{"index":22,
	"title":"Run a Business",
	"desc":"Req: 50\nWW: 6\n\nAdventurers who build or buy their own stronghold can end up running a businesses that have nothing to do with delving into dungeons or saving the world. A character might start a smithy, or a group might decide to work on a farmland or a tavern. A character running a business rolls an Honor Check with a +1 bonus per 100 gp spent beyond the initial 50 gp, to a maximum of +6, then compares the total to the Running a Business table to determine what happens.\n\n1-5: The business makes a loss of 1D6 x 50 GP\n6-10: The business covers it's own cost, but makes no profit\n11-15: The business earns a profit of 1D6 x 50 GP\n16-20: The business earns a profit of 2D8 x 50 GP\n21+: The business earns a profit of 3D10 x 50 GP ",
	"usage":"***NOT YET IMPLEMENTED***"},	
	{"index":23,
	"title":"Scribe a Spell Scroll",
	"desc":"Req: 15-250000 GP\nWW: ??\n\nScribing a spell scroll takes an amount of time and money related to the level of the spell the PC wants to scribe, as shown in the Spell Scroll Costs table. In addition, the PC must have proficiency in the Arcana skill and must provide any material components required for the casting of the spell. Moreover, the PC must have the spell prepared, or it must be among the PC's known spells, in order to scribe a scroll of that spell.\n\nCantrip: 1 day, 15 gp\n1st: 1 day, 25 gp\n2nd: 3 days, 250 gp\n3rd: 1 workweek, 500 gp\n4th: 2 workweeks, 2,500 gp\n5th: 4 workweeks, 5,000 gp\n6th: 8 workweeks, 15,000 gp\n7th: 16 workweeks, 25,000 gp\n8th: 32 workweeks, 50,000 gp\n9th: 48 workweeks, 250,000 gp",
	"usage":"***NOT YET IMPLEMENTED***"},	
	{"index":24,
	"title":"Sell a Magic Item",
	"desc":"Req: 25 GP\nWW: 1\n\nA PC who wants to sell an item must make a Charisma (Persuasion) check to determine what kind of offer comes in. The PC can always opt not to sell, instead of forfeiting the downtime week of effort and trying again later. Use the Magic Item Base Prices and Magic Item Offer tables to determine the sale price.\n\n1-10: 50% of base price\n11-20: 100% of base price\n21+: 150% of base price \n\nCommon: 100 gp\nUncommon: 400 gp\nRare: 4,000 gp\nVery rare: 40,000 gp\nLegendary: 200,000 gp\n\n*Halved for a consumable item like a potion or scroll*",
	"usage":"***NOT YET IMPLEMENTED***"},	
	{"index":25,
	"title":"Sow Rumours",
	"desc":"Req: N/A\nWW: 10\n\nIf a player is liked by a council, they can spend Downtime to try and destabilise the current leader of that council. The Officer must succeed on DC 15 Honor Save or be forced to resign from their position.\n\nThis Downtime Activity can only be used once per Turn. ",
	"usage":"***NOT YET IMPLEMENTED***"},	
	{"index":26,
	"title":"Spell Persistance",
	"desc":"Req: ??\nWW: ??\n\nIf you cast this spell in the same area every day for a year, the spell lasts until dispelled.\n\nDruid Grove: 50 workweeks\nForbiddance: 5 workweeks, 1000 GP\nGuards and Wards: 50 workweeks\nNystuls Magic Aura: 5 workweeks\nPrivate Sanctum: 50 workweeks\nTeleportation Circle: 50 workweeks, 2500 GP\nTemple of the Gods: 50 workweeks",
	"usage":"***NOT YET IMPLEMENTED***"},	
	{"index":27,
	"title":"Train",
	"desc":"Req: Tutor + ?? GP\nWW: 10 - int mod\n\nGiven enough free time and the services of an instructor, a character can learn a language or pick up proficiency with a tool. Training costs 25 gp per workweek. A PC proficient in a tool or language may act as a tutor for the student, but this does not reduce the training cost.",
	"usage":"***NOT YET IMPLEMENTED***"},	
	{"index":28,
	"title":"Travel the World",
	"desc":"Req: ??\nWW: 1+\n\nOver the course of a year, a character can move a great deal of distance around the world. For this reason, moving within the confines of a kingdom is classified as free movement. A character only needs to spend Downtime travelling when they travel between kingdoms.\n\nTo calculate the amount of Workweeks needed to make the trip, the player will first need to open up the World Map and use the Ruler tool. Unless the character is capable of flying 8 hours per day, the player will need to plot a path between two points using the existing road network. This road reflects bridges, safe resting places, and essential landmarks to prevent the character from getting lost. The initial starting point must be a Burg inside the kingdom the player is currently residing, and the final end point must be a Burg inside the kingdom the character wishes to travel to.\n\nOnce the distance in miles has been established, a character will then need to choose their mode of transport. Travelling on foot is always an option over land, but a player may be able to decrease their travel time if they have access to a mount or vehicle. A character may choose to spend a favour from an allied contact (see Carousing) to temporarily borrow a horse or gain access onto a ship. A character with the Ship's Passage feature can always procure passage on ship without payment.\n\nBy Foot: 120 Miles per workweek, 1 GP per workweek \nBy Riding Horse: 200 Miles per workweek, 2 GP per workweek\nBy Sailing Ship: 240 Miles per workweek, 2 GP per workweek ",
	"usage":"***NOT YET IMPLEMENTED***"},	
	{"index":29,
	"title":"Try for an Heir",
	"desc":"Req: N/A\nWW: 50\n\nA married character who decides to continue their families lineage may decide to produce an offspring. Doing so means navigating the complex courting rituals to ensure the child's legitimacy, and providing support to the mother until the childs birth. The character must make a DC 10 Honor Check. On a success, a legitimate heir is born (or adopted into the family).\n\nProducing heirs between PC's is obviously expected to be handled between players ",
	"usage":"***NOT YET IMPLEMENTED***"},
	{"index":30,
	"title":"Work",
	"desc":"Req: N/A\nWW: 1\n\nWhen all else fails, an adventurer can turn to an honest trade to earn a living. This activity represents a character's attempt to find temporary work, the quality and wages of which are difficult to predict. To determine how much money a character earns, the character makes an ability check: Strength (Athletics), Dexterity (Acrobatics), Intelligence using a set of tools, Charisma (Performance), or Charisma using a musical instrument.\n\n9-: 10 GP\n10-14: 20 GP\n15-20: 30 GP\n21+: 50 GP",
	"usage":"***NOT YET IMPLEMENTED\n(for now, use !work)***"}
]
