##SETUP##
{{ ARGS = [a.lower() for a in ARGS ] }}
{{ PARGS = argparse(ARGS) }}
{{ NL = '\n' }}
{{ TB = '\t' }}
#misc modifiers
{{ HALFLING = PARGS.last('half',False) }}
{{ LUCKY = PARGS.last('luck',False) }}
{{ ADV = PARGS.adv() }}
#activity selection
{{ activity = ARGS.pop(0) if len(ARGS) > 0 else '' }}
{{ activity = int(activity) if activity.isdigit() else 0 }}
#set title and description
{{ title = ACTS[activity].title }}
{{ desc = ACTS[activity].desc }}
{{ fields = [f'Resources|{ACTS[activity].resources}',f'Resolution|{ACTS[activity].resolution}',f'Usage|{ACTS[activity].usage}'] }}
{{ footer = f"COMMAND USED: !dt {activity} {' '.join(ARGS)}" }}

##CLEANUP AND DISPLAY##
{{ f'-title "{title}"' }}
{{ f'-desc "{desc}"' }}
{{ ''.join([f'-f "{field}"{NL}' for field in fields]) }}
{{ f' -footer "{footer}"' }}

#--ACTIVITIES--#

##HELP##
{{ activities = ''.join([f'{a.index}. {a.title}{NL}' for a in ACTS]) }}
{{ fields.append(f'**Activities:**|{activities}') }}

##CAROUSING##
{{ persuasionArg = ARGS[0] if len(ARGS) > 0 else '?' }}
{{ persuasion = int(persuasionArg.lstrip('+-')) if persuasionArg.lstrip('+-').isdigit() else -1 }}
{{ persuasion = persuasion * -1 if persuasionArg[0] == '-' else persuasion }}

{{ chaArg = ARGS[1] if len(ARGS) > 1 else '?' }}
{{ chaLimit = int(chaArg.lstrip('+-')) if chaArg.lstrip('+-').isdigit() else -1 }}
{{ chaLimit = chaLimit * -1 if chaArg[0] == '-' else chaLimit }}
{{ chaLimit = 1 if chaLimit < 1 else 1 + chaLimit }}

{{ classArg = ARGS[2] if len(ARGS) > 2 else '?' }}
{{ classVar = classArg if classArg == 'lower' or classArg == 'middle' or classArg == 'upper' else 'lower' }}

{{ weeks = ARGS[3] if len(ARGS) > 3 else '?' }}
{{ weeks = int(weeks) if weeks.isdigit() else 1 }}
{{ weeks = 50 if weeks > 50 else weeks }}
#rolls
{{ table = [ [n+1] for n in range(weeks) ] }}
{{ rollstr = f'{"2" if LUCKY else "1"}d20{"kh1" if (LUCKY and ADV != -1) or (not LUCKY and ADV == 1) else "kl1" if (not LUCKY and ADV == -1) else ""}{"ro1" if HALFLING else ""}+{persuasion}' }}

{{ [ row.append(vroll('1d100')) for row in table ] }}
{{ [ row.append(vroll(rollstr)) for row in table ] }}
#results
{{ set_uvar_nx('uvar_contacts',dump_json([])) }}
{{ contacts = load_json(uvar_contacts) }}
{{ potentialContacts = [] }}

{{ [ potentialContacts.append('hostile') if row[2].total < 6 else potentialContacts.append('allied') if row[2].total > 10 and row[2].total < 16 else [ potentialContacts.append('allied') for x in range(2) ] if row[2].total > 15 and row[2].total < 21 else [ potentialContacts.append('allied') for x in range(3) ] if row[2].total > 20 else False for row in table ] }}
{{ [ contacts.append(contact) if len(contacts) < chaLimit else False for contact in potentialContacts ] }}
{{ set_uvar('uvar_contacts',dump_json(contacts)) }}
#format output
{{ output1 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Carousing ({row[1].total}):[1/1] Gold spent: {"10" if classVar == "lower" else "50" if classVar == "middle" else "250"} GP, Contacts({row[2].total}): {"1 Hostile" if row[2].total < 6 else "None" if row[2].total < 11 else "1 Allied" if row[2].total < 16 else "2 Allied" if row[2].total < 21 else "3 Allied"}{"**" if row[1].total % 10 == 1 else ""}{NL}' for row in table[0:10] ]) }}
{{ output2 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Carousing ({row[1].total}):[1/1] Gold spent: {"10" if classVar == "lower" else "50" if classVar == "middle" else "250"} GP, Contacts({row[2].total}): {"1 Hostile" if row[2].total < 6 else "None" if row[2].total < 11 else "1 Allied" if row[2].total < 16 else "2 Allied" if row[2].total < 21 else "3 Allied"}{"**" if row[1].total % 10 == 1 else ""}{NL}' for row in table[10:20] ]) }}
{{ output3 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Carousing ({row[1].total}):[1/1] Gold spent: {"10" if classVar == "lower" else "50" if classVar == "middle" else "250"} GP, Contacts({row[2].total}): {"1 Hostile" if row[2].total < 6 else "None" if row[2].total < 11 else "1 Allied" if row[2].total < 16 else "2 Allied" if row[2].total < 21 else "3 Allied"}{"**" if row[1].total % 10 == 1 else ""}{NL}' for row in table[20:30] ]) }}
{{ output4 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Carousing ({row[1].total}):[1/1] Gold spent: {"10" if classVar == "lower" else "50" if classVar == "middle" else "250"} GP, Contacts({row[2].total}): {"1 Hostile" if row[2].total < 6 else "None" if row[2].total < 11 else "1 Allied" if row[2].total < 16 else "2 Allied" if row[2].total < 21 else "3 Allied"}{"**" if row[1].total % 10 == 1 else ""}{NL}' for row in table[30:40] ]) }}
{{ output5 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Carousing ({row[1].total}):[1/1] Gold spent: {"10" if classVar == "lower" else "50" if classVar == "middle" else "250"} GP, Contacts({row[2].total}): {"1 Hostile" if row[2].total < 6 else "None" if row[2].total < 11 else "1 Allied" if row[2].total < 16 else "2 Allied" if row[2].total < 21 else "3 Allied"}{"**" if row[1].total % 10 == 1 else ""}{NL}' for row in table[40:50] ]) }}
{{ outputContacts = ''.join([ f'{contact}{NL}' for contact in contacts ]) }}
#load output for display
{{ showusage = persuasionArg == '?' }}
{{ fields = [] if not showusage else fields }}
{{ fields.append(f'Carousing Class|{classVar}') if not showusage else False }}
{{ fields.append(f'Rolling|1d100{NL}{rollstr}') if not showusage else False }}
{{ fields.append(f'Log|{output1}') if not showusage else False }}
{{ fields.append(f'Log|{output2}') if output2 != '' and not showusage else False }}
{{ fields.append(f'Log|{output3}') if output3 != '' and not showusage else False }}
{{ fields.append(f'Log|{output4}') if output4 != '' and not showusage else False }}
{{ fields.append(f'Log|{output5}') if output5 != '' and not showusage else False }}
{{ fields.append(f'Contacts|{outputContacts}') if not showusage else False }}


###ACTIVITIES###

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
	"desc":"Doghouse downtime activities.\nYou will select up to 2 activities, accounting for a maximum of 1 month of time. Some activities take an entire month.",
	"resources":"Each downtime activity will have resources required, depending on the taks.",
	"resolution":"Each downtime activity  will require resolution. This includes resolving any complications that may arise.",
	"usage":"To do a downtime activity, type __!dt <n> <arguments>__\n<n> the number corresponding to the downtime activity from the list below\n<arguments> the arguments for the downtime activity\nFor additional help with a specific downtime activity and to see its usage, select it without any additional arguments."},
	{"index":1,
	"title":"Carousing",
	"desc":"Carousing is a default downtime activity for many characters. Between adventures, who doesn’t want to relax with a few drinks and a group of friends at a tavern?",
	"resources":"A character can carouse with the lower class for 10 gp to cover expenses, or 50 gp for the middle class. Upper class requires 250 gp for the workweek and access to the local nobility.",
	"resolution":"After a workweek of carousing, a character stands to make contacts within the selected social class.\nA Charisma(Persuasion) check must be made.\n	1-5: one hostile contact\n	6-10: no new contacts, 11-15: one allied contact, 16-20: two allied contacts, 21+: three allied contacts.\nAt any time, a character can have a maximum number of unspecified allied contacts equal to 1+Cha mod (minimum 1).",
	"usage":"!dt <> <> <>"},
	{"index":2,
	"title":"Crime",
	"desc":"Sometimes it pays to be bad. This activity gives a character the chance to make some extra cash, at the risk of arrest.",
	"resources":"A character must spend one week carousing - gathering information on potential targets before committing the intended crime.",
	"resolution":"The character must make a series of checks, with the DC for all the checks chosen by the character according to the amount of profit sought from the crime.\nThe chosen DC can be 10, 15, 20, or 25. To attempt a crime, the character makes 3 checks:\nDex(Stealth), Dex using Thieve's Tools, and the player's choice of Int(Investigation), Wis(Perception), or Cha(Deception)",
	"usage":"***NOT YET IMPLEMENTED***"},
	{"index":3,
	"title":"Gambling",
	"desc":"Games of chance are a way to make a fortune — and perhaps a better way to lose one.",
	"resources":"This activity requires one workweek of effort plus a stake of at least 10 gp, to a maximum of 1,000 gp",
	"resolution":"The character must make a series of checks, with a DC determined at random based on the quality of the competition that the character runs into. Part of the risk of gambling is that one never knows who might end up sitting across the table.\nThe character makes 3 checks:\nWis(Insight), Cha(Deception), and Cha(Intimidation)\nIf the character has proficiency with an appropriate gaming set, that tool proficiency can replace the relevant skill in any one of the checks",
	"usage":"***NOT YET IMPLEMENTED***"},
	{"index":4,
	"title":"Pit Fighting",
	"desc":"Pit fighting includes boxing, wrestling, and other nonlethal forms of combat in an organized setting with predetermined matches. Generally this is not-fatal.",
	"resources":"Engaging in this activity requires one workweek of effort from a character.",
	"resolution":"The character must make a series of checks, with a DC determined at random based on the quality of the opposition that the character runs into. A big part of the challenge in pit fighting lies in the unknown nature of a character’s opponents.\nThe character makes 3 checks:\nStr(Athletics), Dex(Acrobatics), and a special Con check that has a bonus equal to a roll of the character's largest Hit Die.",
	"usage":"***NOT YET IMPLEMENTED***"},
	{"index":5,
	"title":"Relaxation",
	"desc":"Whether a character wants a hard-earned vacation or needs to recover from injuries, relaxation is the ideal option for adventurers who need a break.",
	"resources":"Relaxation requires one week. A character needs to maintain at least a modest lifestyle while relaxing to gain the benefit of the activity.",
	"resolution":"Characters who maintain at least a modest lifestyle while relaxing gain several benefits. While relaxing, a character gains advantage on saving throws to recover from long-acting diseases and poisons. The character can restore ability damage. This benefit cannot be used if the harmful effect was caused by a spell or some other magical effect with an ongoing duration.",
	"usage":"***NOT YET IMPLEMENTED***"},
	{"index":6,
	"title":"Religous Service",
	"desc":"Characters with a religious bent might want to spend downtime in service to a temple, either by attending rites or by proselytizing in the community. Someone who undertakes this activity has a chance of winning the favor of the temple’s leaders.",
	"resources":"Performing religious service requires access to, and often attendance at, a temple whose beliefs and ethos align with the character’s.",
	"resolution":"At the end of the required time, the character chooses to make a check that determines the benefits of service:\nInt(Religion) or Cha(Persuasion)",
	"usage":"***NOT YET IMPLEMENTED***"},
	{"index":7,
	"title":"Research",
	"desc":"The research downtime activity allows a character to delve into lore concerning a monster, a location, a magic item, or some other particular topic.",
	"resources":"Typically, a character needs access to a library or a sage to conduct research. Assuming such access is available, conducting research requires one workweek of effort and at least 50 gp spent on materials, bribes, gifts, and other expenses.",
	"resolution":"The character declares the focus of the research — a specific person, place, or thing. After one workweek, the character makes an Int check with a +1 bonus per 100 gp spent beyond the initial 100 gp, to a maximum of +6. In addition, a character who has access to a particularly well-stocked library or knowledgeable sages gains advantage on this check.",
	"usage":"***NOT YET IMPLEMENTED***"},
	{"index":8,
	"title":"Training",
	"desc":"Given enough free time and the services of an instructor, a character can learn a language or pick up proficiency with a tool.",
	"resources":"Receiving training in a language or tool typically takes at least ten workweeks, but this time is reduced by a number of workweeks equal to the character’s Intelligence modifier (an Intelligence penalty doesn’t increase the time needed). Training costs 25 gp per workweek.",
	"resolution":"",
	"usage":"***NOT YET IMPLEMENTED***"},
	{"index":9,
	"title":"Work",
	"desc":"When all else fails, an adventurer can turn to an honest trade to earn a living. This activity represents a character’s attempt to find temporary work, the quality and wages of which are difficult to predict.",
	"resources":"Performing a job requires one workweek of effort.",
	"resolution":"To determine how much money a character earns, the character makes an ability check for the specific work task to determine how much income is made:\nStr(Athletics), Dex(Acrobatics), Int using a set oftools, Cha(Performance), or Cha using an instrument.",
	"usage":"***NOT YET IMPLEMENTED***"}
]
