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
{{ vOutStr1 = ''.join([ f'{":warning:" if r[1].total % 10 == 1 else ""}{str(r[0])}. Alter Laws ({r[1].total}):[1/1] Law {"Passed" if r[3] else "Rejected"}, Law: {vLaws[r[0]-1]}, Offence: {vOffenses[r[0]-1]}, Punishment: {vPunishments[r[0]-1]}{", Complication::warning:" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[0:10] ]) }}
{{ vOutStr2 = ''.join([ f'{":warning:" if r[1].total % 10 == 1 else ""}{str(r[0])}. Alter Laws ({r[1].total}):[1/1] Law {"Passed" if r[3] else "Rejected"}, Law: {vLaws[r[0]-1]}, Offence: {vOffenses[r[0]-1]}, Punishment: {vPunishments[r[0]-1]}{", Complication::warning:" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[10:20] ]) }}
{{ vOutStr3 = ''.join([ f'{":warning:" if r[1].total % 10 == 1 else ""}{str(r[0])}. Alter Laws ({r[1].total}):[1/1] Law {"Passed" if r[3] else "Rejected"}, Law: {vLaws[r[0]-1]}, Offence: {vOffenses[r[0]-1]}, Punishment: {vPunishments[r[0]-1]}{", Complication::warning:" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[20:30] ]) }}
{{ vOutStr4 = ''.join([ f'{":warning:" if r[1].total % 10 == 1 else ""}{str(r[0])}. Alter Laws ({r[1].total}):[1/1] Law {"Passed" if r[3] else "Rejected"}, Law: {vLaws[r[0]-1]}, Offence: {vOffenses[r[0]-1]}, Punishment: {vPunishments[r[0]-1]}{", Complication::warning:" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[30:40] ]) }}
{{ vOutStr5 = ''.join([ f'{":warning:" if r[1].total % 10 == 1 else ""}{str(r[0])}. Alter Laws ({r[1].total}):[1/1] Law {"Passed" if r[3] else "Rejected"}, Law: {vLaws[r[0]-1]}, Offence: {vOffenses[r[0]-1]}, Punishment: {vPunishments[r[0]-1]}{", Complication::warning:" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[40:50] ]) }}
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
{{ vOutStr1 = ''.join([ f'{":warning:" if r[1].total % 10 == 1 else ""}{str(r[0])}. Apply for a Position ({r[1].total}):[1/1] Position {"Claimed" if r[3] else "Unclaimed"}, Position: {vPositions[r[0]-1]}{":warning:" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[0:10] ]) }}
{{ vOutStr2 = ''.join([ f'{":warning:" if r[1].total % 10 == 1 else ""}{str(r[0])}. Apply for a Position ({r[1].total}):[1/1] Position {"Claimed" if r[3] else "Unclaimed"}, Position: {vPositions[r[0]-1]}{":warning:" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[10:20] ]) }}
{{ vOutStr3 = ''.join([ f'{":warning:" if r[1].total % 10 == 1 else ""}{str(r[0])}. Apply for a Position ({r[1].total}):[1/1] Position {"Claimed" if r[3] else "Unclaimed"}, Position: {vPositions[r[0]-1]}{":warning:" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[20:30] ]) }}
{{ vOutStr4 = ''.join([ f'{":warning:" if r[1].total % 10 == 1 else ""}{str(r[0])}. Apply for a Position ({r[1].total}):[1/1] Position {"Claimed" if r[3] else "Unclaimed"}, Position: {vPositions[r[0]-1]}{":warning:" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[30:40] ]) }}
{{ vOutStr5 = ''.join([ f'{":warning:" if r[1].total % 10 == 1 else ""}{str(r[0])}. Apply for a Position ({r[1].total}):[1/1] Position {"Claimed" if r[3] else "Unclaimed"}, Position: {vPositions[r[0]-1]}{":warning:" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[40:50] ]) }}
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
{{ vOutStr1 = ''.join([ f'{":warning:" if r[1].total % 10 == 1 else ""}{str(r[0])}. Arrange Marriage ({r[1].total}):[1/1] Proposal {"accepted" if r[3] else "rejected"}, Contact who\'s favour was spent: {vContact}{", Dowry to be payed: 100 GP" if r[3] and vClass == 1 else "Dowry to be payed: 500 GP" if r[3] and vClass == 2 else "Dowry to be payed: 2500 GP" if r[3] and vClass == 3 else ""}{":warning:" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults ]) }}
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
{{ vOutStr1 = ''.join([ f'{":warning:" if r[1].total % 10 == 1 else ""}{str(r[0])}. Arrange Tutor ({r[1].total}):[1/1] Tutor {"found" if r[3] else "not found"} for learning {vSkill}, Contact who\'s favour was spent: {vContact}{":warning:" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults ]) }}
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
{{ vOutStr1 = ''.join([ f'{":warning:" if r[1].total % 10 == 1 else ""}{str(r[0])}. Buy a Magic Item ({r[1].total}):[{vWeeks}/{vWeeks}] Gold spent searching for a buyer: {vMoney} GP, Available items: {r[3].total}{":warning:" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults ]) }}
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
{{ vOutStr1 = ''.join([ f'{":warning:" if r[1].total % 10 == 1 else ""}{str(r[0])}. Carouse ({r[1].total}):[1/1] Gold spent carousing: {"10" if vClass == "lower" else "50" if vClass == "middle" else "250"} GP, Contacts({r[2].total}): {"1 Hostile" if r[2].total < 6 else "None" if r[2].total < 11 else "1 Allied" if r[2].total < 16 else "2 Allied" if r[2].total < 21 else "3 Allied"}{":warning:" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[0:10] ]) }}
{{ vOutStr2 = ''.join([ f'{":warning:" if r[1].total % 10 == 1 else ""}{str(r[0])}. Carouse ({r[1].total}):[1/1] Gold spent carousing: {"10" if vClass == "lower" else "50" if vClass == "middle" else "250"} GP, Contacts({r[2].total}): {"1 Hostile" if r[2].total < 6 else "None" if r[2].total < 11 else "1 Allied" if r[2].total < 16 else "2 Allied" if r[2].total < 21 else "3 Allied"}{":warning:" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[10:20] ]) }}
{{ vOutStr3 = ''.join([ f'{":warning:" if r[1].total % 10 == 1 else ""}{str(r[0])}. Carouse ({r[1].total}):[1/1] Gold spent carousing: {"10" if vClass == "lower" else "50" if vClass == "middle" else "250"} GP, Contacts({r[2].total}): {"1 Hostile" if r[2].total < 6 else "None" if r[2].total < 11 else "1 Allied" if r[2].total < 16 else "2 Allied" if r[2].total < 21 else "3 Allied"}{":warning:" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[20:30] ]) }}
{{ vOutStr4 = ''.join([ f'{":warning:" if r[1].total % 10 == 1 else ""}{str(r[0])}. Carouse ({r[1].total}):[1/1] Gold spent carousing: {"10" if vClass == "lower" else "50" if vClass == "middle" else "250"} GP, Contacts({r[2].total}): {"1 Hostile" if r[2].total < 6 else "None" if r[2].total < 11 else "1 Allied" if r[2].total < 16 else "2 Allied" if r[2].total < 21 else "3 Allied"}{":warning:" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[30:40] ]) }}
{{ vOutStr5 = ''.join([ f'{":warning:" if r[1].total % 10 == 1 else ""}{str(r[0])}. Carouse ({r[1].total}):[1/1] Gold spent carousing: {"10" if vClass == "lower" else "50" if vClass == "middle" else "250"} GP, Contacts({r[2].total}): {"1 Hostile" if r[2].total < 6 else "None" if r[2].total < 11 else "1 Allied" if r[2].total < 16 else "2 Allied" if r[2].total < 21 else "3 Allied"}{":warning:" if r[1].total % 10 == 1 else ""}{nl}' for r in vResults[40:50] ]) }}
{{ vOutput.append(f'-f "Log|{vOutStr1}"{nl}') if vThis else ''}}
{{ vOutput.append(f'-f "Log|{vOutStr2}"{nl}' if vThis and len(vResults) > 10 else '') }}
{{ vOutput.append(f'-f "Log|{vOutStr3}"{nl}' if vThis and len(vResults) > 20 else '') }}
{{ vOutput.append(f'-f "Log|{vOutStr4}"{nl}' if vThis and len(vResults) > 30 else '') }}
{{ vOutput.append(f'-f "Log|{vOutStr5}"{nl}' if vThis and len(vResults) > 40 else '') }}
# - Adding activity output if activity called
{{ vOut[2] = vOutput if vMod != '?' and vThis else vOut[2] }}
