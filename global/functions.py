#--GLOBAL FUNCTIONS--#

##SETUP##
{{ ARGS = [a.lower() for a in ARGS ] }}
{{ PARGS = argparse(ARGS) }}
{{ NL = '\n' }}
{{ TB = '\t' }}
{{ RAW = get_raw() }}
#misc modifiers
{{ HALFLING = True if RAW.race.lower().find('halfling') != -1 else PARGS.last('half',False) }}
{{ LUCKY = PARGS.last('luck',False) }}
{{ TEST = PARGS.last('test',False) }}
{{ ADV = PARGS.adv() }}
#activity selection
{{ activity = ARGS.pop(0) if len(ARGS) > 0 else '' }}
{{ activity = activity.lower() }}
{{ activity = int(activity) if activity.isdigit() else max([ a.index if activity == a.title.lower() else 0 for a in ACTS ]) }}
#set title and description
{{ title = ACTS[activity].title }}
{{ desc = ACTS[activity].desc }}
{{ fields = [f'Resources|{ACTS[activity].resources}',f'Resolution|{ACTS[activity].resolution}',f'Usage|!downtime \'{title.lower()}\' {ACTS[activity].usage}'] }}
{{ footer = f"COMMAND USED: !downtime \'{title.lower()}\' {' '.join(ARGS)}" }}

##CLEANUP AND DISPLAY##
{{ f'-title "{title}"' }}
{{ f'-desc "{desc}"' }}
{{ ''.join([f'-f "{field}"{NL}' for field in fields]) }}
{{ f' -footer "{footer}"' }}

#--ACTIVITY FUNCTIONS--#

##USE CONTACT##
{{ ARGS = [a.lower() for a in ARGS ] }}

{{ classArg = ARGS[2] if len(ARGS) > 2 else '?' }}
{{ classVar = classArg if classArg == 'middle' or classArg == 'upper' else 'lower' }}
{{ showusage = classArg == '?' }}

{{ set_uvar_nx('uvar_contacts',dump_json([])) }}
{{ contacts = load_json(uvar_contacts) }}
{{ potentialContacts = [] }}
{{ [ potentialContacts.append(contact) if contact != allied  for contact in contacts ] }}
{{ set_uvar('uvar_contacts',dump_json(contacts)) if not showusage else False }}

{{ title = 'Use Contact' }}
{{ desc = 'This command will is for spending a favour from a contact. Once a favour is spent, the contact is removed and you will need to carouse again.' }}
{{ footer = f"COMMAND USED: !usecontact {' '.join(ARGS)}" }}

{{ f'-title "{title}"' }}
{{ f'-desc "{desc}"' }}
{{ ''.join([f'-f "{field}"{NL}' for field in fields]) }}
{{ f' -footer "{footer}"' }}


##HELP##
{{ activities = ''.join([f'{a.index}. {a.title}{NL}' for a in ACTS]) }}
{{ fields.append(f'**Activities:**|{activities}') }}



##CAROUSING##
{{ persuasionArg = ARGS[0] if len(ARGS) > 0 else '?' }}
{{ persuasion = int(persuasionArg.lstrip('+-')) if persuasionArg.lstrip('+-').isdigit() else -1 }}
{{ persuasion = persuasion * -1 if persuasionArg[0] == '-' else persuasion }}

{{ showusage = persuasionArg == '?' }}

{{ chaArg = ARGS[1] if len(ARGS) > 1 else '?' }}
{{ chaLimit = int(chaArg.lstrip('+-')) if chaArg.lstrip('+-').isdigit() else -1 }}
{{ chaLimit = chaLimit * -1 if chaArg[0] == '-' else chaLimit }}
{{ chaLimit = 1 if chaLimit < 1 else 1 + chaLimit }}

{{ classArg = ARGS[2] if len(ARGS) > 2 else '?' }}
{{ classVar = classArg if classArg == 'middle' or classArg == 'upper' else 'lower' }}

{{ weeks = ARGS[3] if len(ARGS) > 3 else '?' }}
{{ weeks = int(weeks) if weeks.isdigit() else 1 }}
{{ weeks = 1 if weeks < 1 else weeks }}
{{ weeks = 50 if weeks > 50 else weeks }}

{{ resources = 250 if classVar == 'upper' else 50 if classVar == 'middle' else 10 }}
{{ resources = resources * weeks }}

#rolls
{{ rolltable = [ [n+1] for n in range(weeks) ] }} #column 0
{{ rollstr = f'{"2" if LUCKY or ADV != 0 else "1"}d20{"kh1" if LUCKY or ADV == 1 else "kl1" if ADV == -1 else ""}{"ro1" if HALFLING else ""}+{persuasion}' }}
{{ [ row.append(vroll("1d100")) for row in rolltable ] }} #column 1
{{ [ row.append(vroll(rollstr)) for row in rolltable ] }} #column 2

#contacts
{{ set_uvar_nx('uvar_contacts',dump_json([])) }}
{{ contacts = load_json(uvar_contacts) }}

{{ potentialContacts = [] }}
{{ [ potentialContacts.append(f'allied {classVar} class') if row[2].total > 10 and row[2].total < 16 else [ potentialContacts.append(f'allied {classVar} class') for x in range(2) ] if row[2].total > 15 and row[2].total < 21 else [ potentialContacts.append(f'allied {classVar} class') for x in range(3) ] if row[2].total > 20 else False for row in rolltable ] }}
{{ [ contacts.append(contact) if len(contacts) < chaLimit else False for contact in potentialContacts ] }}

{{ set_uvar('uvar_contacts',dump_json(contacts)) if not showusage else False }}

#format output
{{ output1 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Carousing ({row[1].total}):[1/1] Gold spent: {"10" if classVar == "lower" else "50" if classVar == "middle" else "250"} GP, Contacts({row[2].total}): {"1 Hostile" if row[2].total < 6 else "None" if row[2].total < 11 else "1 Allied" if row[2].total < 16 else "2 Allied" if row[2].total < 21 else "3 Allied"}{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[0:10] ]) }}
{{ output2 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Carousing ({row[1].total}):[1/1] Gold spent: {"10" if classVar == "lower" else "50" if classVar == "middle" else "250"} GP, Contacts({row[2].total}): {"1 Hostile" if row[2].total < 6 else "None" if row[2].total < 11 else "1 Allied" if row[2].total < 16 else "2 Allied" if row[2].total < 21 else "3 Allied"}{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[10:20] ]) }}
{{ output3 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Carousing ({row[1].total}):[1/1] Gold spent: {"10" if classVar == "lower" else "50" if classVar == "middle" else "250"} GP, Contacts({row[2].total}): {"1 Hostile" if row[2].total < 6 else "None" if row[2].total < 11 else "1 Allied" if row[2].total < 16 else "2 Allied" if row[2].total < 21 else "3 Allied"}{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[20:30] ]) }}
{{ output4 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Carousing ({row[1].total}):[1/1] Gold spent: {"10" if classVar == "lower" else "50" if classVar == "middle" else "250"} GP, Contacts({row[2].total}): {"1 Hostile" if row[2].total < 6 else "None" if row[2].total < 11 else "1 Allied" if row[2].total < 16 else "2 Allied" if row[2].total < 21 else "3 Allied"}{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[30:40] ]) }}
{{ output5 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Carousing ({row[1].total}):[1/1] Gold spent: {"10" if classVar == "lower" else "50" if classVar == "middle" else "250"} GP, Contacts({row[2].total}): {"1 Hostile" if row[2].total < 6 else "None" if row[2].total < 11 else "1 Allied" if row[2].total < 16 else "2 Allied" if row[2].total < 21 else "3 Allied"}{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[40:50] ]) }}
{{ outputContacts = ''.join([ f'{contact}{NL}' for contact in contacts ]) }}

#load output for display
{{ fields = [] if not showusage else fields }}
{{ fields.append(f'Carousing Class|{classVar}') if not showusage else False }}
{{ fields.append(f'Resources|{resources} GP{" and access to the local nobility" if classVar == "upper" else "" }') if not showusage else False }}
{{ fields.append(f'Rolling|Luck:1d100{NL}Persuasion:{rollstr}') if not showusage else False }}
{{ fields.append(f'Log|{output1}') if not showusage else False }}
{{ fields.append(f'Log|{output2}') if output2 != '' and not showusage else False }}
{{ fields.append(f'Log|{output3}') if output3 != '' and not showusage else False }}
{{ fields.append(f'Log|{output4}') if output4 != '' and not showusage else False }}
{{ fields.append(f'Log|{output5}') if output5 != '' and not showusage else False }}
{{ fields.append(f'Contacts|{outputContacts}') if not showusage else False }}



##CRIME##
{{ dc = ARGS[0] if len(ARGS) > 0 else '?' }}
{{ dc = int(dc) if dc.isdigit() else '?' }}

{{ mod1arg = ARGS[1] if len(ARGS) > 1 else '?' }}
{{ mod1 = int(mod1arg.lstrip('+-')) if mod1arg.lstrip('+-').isdigit() else -1 }}
{{ mod1 = mod1 * -1 if mod1arg[0] == '-' else mod1 }}

{{ mod2arg = ARGS[2] if len(ARGS) > 2 else '?' }}
{{ mod2 = int(mod2arg.lstrip('+-')) if mod2arg.lstrip('+-').isdigit() else -1 }}
{{ mod2 = mod2 * -1 if mod2arg[0] == '-' else mod2 }}

{{ mod3arg = ARGS[3] if len(ARGS) > 3 else '?' }}
{{ mod3 = int(mod3arg.lstrip('+-')) if mod3arg.lstrip('+-').isdigit() else -1 }}
{{ mod3 = mod3 * -1 if mod3arg[0] == '-' else mod3 }}

{{ weeks = ARGS[4] if len(ARGS) > 4 else '?' }}
{{ weeks = int(weeks) if weeks.isdigit() else 1 }}
{{ weeks = 1 if weeks < 1 else weeks }}
{{ weeks = 50 if weeks > 50 else weeks }}

{{ showusage = dc == '?' }}
{{ dc = 10 if showusage else dc }}

{{ val = 50 if dc == 10 else 100 if dc == 15 else 200 if dc == 20 else 1000 if dc == 25 else 0 }}

#rolls
{{ rolltable = [ [n+1] for n in range(weeks) ] }} #column 0
{{ modFeat = 1 if min(mod1,mod2,mod3) == mod1 else 2 if min(mod1,mod2,mod3) == mod2 else 3 }}
{{ modDie = f'{"2" if LUCKY or ADV != 0 else "1"}d20{"kh1" if LUCKY or ADV == 1 else "kl1" if ADV == -1 else ""}' }}
{{ rollstr1 = f'{modDie if modFeat == 1 else "1d20"}{"ro1" if HALFLING else ""}+{mod1}' }}
{{ rollstr2 = f'{modDie if modFeat == 2 else "1d20"}{"ro1" if HALFLING else ""}+{mod2}' }}
{{ rollstr3 = f'{modDie if modFeat == 3 else "1d20"}{"ro1" if HALFLING else ""}+{mod3}' }}
{{ [ row.append(vroll("1d100")) for row in rolltable ] }} #column 1
{{ [ row.append(vroll(rollstr1)) for row in rolltable ] }} #column 2
{{ [ row.append(vroll(rollstr2)) for row in rolltable ] }} #column 3
{{ [ row.append(vroll(rollstr3)) for row in rolltable ] }} #column 4

#results
{{ [ row.append(sum([row[2].total >= dc, row[3].total >= dc, row[4].total >= dc])) for row in rolltable ] }} #column 5: passes
{{ [ row.append(round(val if row[5] == 3 else val / 2 if row[5] == 2 else 0 if row[5] == 1 else -val)) for row in rolltable ] }} #column 6: net
{{ [ row.append(round(((-row[6]/25) % 7)+1) if row[6] < 0 and (-row[6]/25) > 7 else 1) for row in rolltable ] }} #column 7: duration
{{ [ [ rolltable.pop(len(rolltable)-1) if n > 0 else False for n in range(row[7]) ] for row in rolltable ] }}

#format output
{{ output1 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Crime ({row[1].total}):[{row[7]}/1], DC{dc}, Stealth:{row[2].total}, Thieve\'s Tools:{row[3].total}, Misc Mod:{row[4].total}, Passes:{row[5]}, Net:{row[6]} GP{" & "+str(round(-row[6]/25))+" days in jail" if row[6] < 0 else ""}{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[0:5] ]) }}
{{ output2 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Crime ({row[1].total}):[{row[7]}/1], DC{dc}, Stealth:{row[2].total}, Thieve\'s Tools:{row[3].total}, Misc Mod:{row[4].total}, Passes:{row[5]}, Net:{row[6]} GP{" & "+str(round(-row[6]/25))+" days in jail" if row[6] < 0 else ""}{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[5:10] ]) }}
{{ output3 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Crime ({row[1].total}):[{row[7]}/1], DC{dc}, Stealth:{row[2].total}, Thieve\'s Tools:{row[3].total}, Misc Mod:{row[4].total}, Passes:{row[5]}, Net:{row[6]} GP{" & "+str(round(-row[6]/25))+" days in jail" if row[6] < 0 else ""}{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[10:15] ]) }}
{{ output4 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Crime ({row[1].total}):[{row[7]}/1], DC{dc}, Stealth:{row[2].total}, Thieve\'s Tools:{row[3].total}, Misc Mod:{row[4].total}, Passes:{row[5]}, Net:{row[6]} GP{" & "+str(round(-row[6]/25))+" days in jail" if row[6] < 0 else ""}{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[15:20] ]) }}
{{ output5 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Crime ({row[1].total}):[{row[7]}/1], DC{dc}, Stealth:{row[2].total}, Thieve\'s Tools:{row[3].total}, Misc Mod:{row[4].total}, Passes:{row[5]}, Net:{row[6]} GP{" & "+str(round(-row[6]/25))+" days in jail" if row[6] < 0 else ""}{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[20:25] ]) }}
{{ output6 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Crime ({row[1].total}):[{row[7]}/1], DC{dc}, Stealth:{row[2].total}, Thieve\'s Tools:{row[3].total}, Misc Mod:{row[4].total}, Passes:{row[5]}, Net:{row[6]} GP{" & "+str(round(-row[6]/25))+" days in jail" if row[6] < 0 else ""}{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[25:30] ]) }}
{{ output7 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Crime ({row[1].total}):[{row[7]}/1], DC{dc}, Stealth:{row[2].total}, Thieve\'s Tools:{row[3].total}, Misc Mod:{row[4].total}, Passes:{row[5]}, Net:{row[6]} GP{" & "+str(round(-row[6]/25))+" days in jail" if row[6] < 0 else ""}{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[30:35] ]) }}
{{ output8 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Crime ({row[1].total}):[{row[7]}/1], DC{dc}, Stealth:{row[2].total}, Thieve\'s Tools:{row[3].total}, Misc Mod:{row[4].total}, Passes:{row[5]}, Net:{row[6]} GP{" & "+str(round(-row[6]/25))+" days in jail" if row[6] < 0 else ""}{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[35:40] ]) }}
{{ output9 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Crime ({row[1].total}):[{row[7]}/1], DC{dc}, Stealth:{row[2].total}, Thieve\'s Tools:{row[3].total}, Misc Mod:{row[4].total}, Passes:{row[5]}, Net:{row[6]} GP{" & "+str(round(-row[6]/25))+" days in jail" if row[6] < 0 else ""}{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[40:45] ]) }}
{{ output10 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Crime ({row[1].total}):[{row[7]}/1], DC{dc}, Stealth:{row[2].total}, Thieve\'s Tools:{row[3].total}, Misc Mod:{row[4].total}, Passes:{row[5]}, Net:{row[6]} GP{" & "+str(round(-row[6]/25))+" days in jail" if row[6] < 0 else ""}{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[45:50] ]) }}
{{ profits = sum([ row[6] for row in rolltable ]) }}

#load output for display
{{ fields = [] if not showusage else fields }}
{{ fields.append(f'DC|{dc}') if not showusage else False }}
{{ fields.append(f'Rolling|Luck:1d100{NL}Stealth:{rollstr1}{NL}Tools:{rollstr2}{NL}Misc:{rollstr3}') if not showusage else False }}
{{ fields.append(f'Log|{output1}') if not showusage else False }}
{{ fields.append(f'Log|{output2}') if output2 != '' and not showusage else False }}
{{ fields.append(f'Log|{output3}') if output3 != '' and not showusage else False }}
{{ fields.append(f'Log|{output4}') if output4 != '' and not showusage else False }}
{{ fields.append(f'Log|{output5}') if output5 != '' and not showusage else False }}
{{ fields.append(f'Log|{output6}') if output6 != '' and not showusage else False }}
{{ fields.append(f'Log|{output7}') if output7 != '' and not showusage else False }}
{{ fields.append(f'Log|{output8}') if output8 != '' and not showusage else False }}
{{ fields.append(f'Log|{output9}') if output9 != '' and not showusage else False }}
{{ fields.append(f'Log|{output10}') if output10 != '' and not showusage else False }}
{{ fields.append(f'Profits|{profits}') if not showusage else False }}


##GAMBLING##
{{ bet = ARGS[0] if len(ARGS) > 0 else '?' }}
{{ bet = int(bet) if bet.isdigit() else '?' }}

{{ mod1arg = ARGS[1] if len(ARGS) > 1 else '?' }}
{{ mod1 = int(mod1arg.lstrip('+-')) if mod1arg.lstrip('+-').isdigit() else -1 }}
{{ mod1 = mod1 * -1 if mod1arg[0] == '-' else mod1 }}

{{ mod2arg = ARGS[2] if len(ARGS) > 2 else '?' }}
{{ mod2 = int(mod2arg.lstrip('+-')) if mod2arg.lstrip('+-').isdigit() else -1 }}
{{ mod2 = mod2 * -1 if mod2arg[0] == '-' else mod2 }}

{{ mod3arg = ARGS[3] if len(ARGS) > 3 else '?' }}
{{ mod3 = int(mod3arg.lstrip('+-')) if mod3arg.lstrip('+-').isdigit() else -1 }}
{{ mod3 = mod3 * -1 if mod3arg[0] == '-' else mod3 }}

{{ weeks = ARGS[4] if len(ARGS) > 4 else '?' }}
{{ weeks = int(weeks) if weeks.isdigit() else 1 }}
{{ weeks = 1 if weeks < 1 else weeks }}
{{ weeks = 50 if weeks > 50 else weeks }}

{{ showusage = bet == '?' }}
{{ bet = 10 if showusage else bet }}

#rolls
{{ rolltable = [ [n+1] for n in range(weeks) ] }} #column 0
{{ modFeat = 1 if min(mod1,mod2,mod3) == mod1 else 2 if min(mod1,mod2,mod3) == mod2 else 3 }}
{{ modDie = f'{"2" if LUCKY or ADV != 0 else "1"}d20{"kh1" if LUCKY or ADV == 1 else "kl1" if ADV == -1 else ""}' }}
{{ rollstr1 = f'{modDie if modFeat == 1 else "1d20"}{"ro1" if HALFLING else ""}+{mod1}' }}
{{ rollstr2 = f'{modDie if modFeat == 2 else "1d20"}{"ro1" if HALFLING else ""}+{mod2}' }}
{{ rollstr3 = f'{modDie if modFeat == 3 else "1d20"}{"ro1" if HALFLING else ""}+{mod3}' }}
{{ [ row.append(vroll("1d100")) for row in rolltable ] }} #column 1
{{ [ row.append(vroll(rollstr1)) for row in rolltable ] }} #column 2
{{ [ row.append(vroll(rollstr2)) for row in rolltable ] }} #column 3
{{ [ row.append(vroll(rollstr3)) for row in rolltable ] }} #column 4
{{ [ row.append(vroll('5+2d10')) for row in rolltable ] }} #column 5
{{ [ row.append(vroll('5+2d10')) for row in rolltable ] }} #column 6
{{ [ row.append(vroll('5+2d10')) for row in rolltable ] }} #column 7

#results
{{ [ row.append(sum([row[2].total >= row[5].total, row[3].total >= row[6].total, row[4].total >= row[7].total])) for row in rolltable ] }} #column 8: passes
{{ [ row.append(round(bet) if row[8] == 3 else round(.5*bet) if row[8] == 2 else -round(.5*bet) if row[8] == 1 else -bet) for row in rolltable ] }} #column 9: net

#format output
{{ output1 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Gambling ({row[1].total}):[1/1], Insight:{row[2].total} DC{row[5].total}, Deception:{row[3].total} DC{row[6].total}, Intimidation:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[0:5] ]) }}
{{ output2 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Gambling ({row[1].total}):[1/1], Insight:{row[2].total} DC{row[5].total}, Deception:{row[3].total} DC{row[6].total}, Intimidation:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[5:10] ]) }}
{{ output3 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Gambling ({row[1].total}):[1/1], Insight:{row[2].total} DC{row[5].total}, Deception:{row[3].total} DC{row[6].total}, Intimidation:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[10:15] ]) }}
{{ output4 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Gambling ({row[1].total}):[1/1], Insight:{row[2].total} DC{row[5].total}, Deception:{row[3].total} DC{row[6].total}, Intimidation:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[15:20] ]) }}
{{ output5 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Gambling ({row[1].total}):[1/1], Insight:{row[2].total} DC{row[5].total}, Deception:{row[3].total} DC{row[6].total}, Intimidation:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[20:25] ]) }}
{{ output6 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Gambling ({row[1].total}):[1/1], Insight:{row[2].total} DC{row[5].total}, Deception:{row[3].total} DC{row[6].total}, Intimidation:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[25:30] ]) }}
{{ output7 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Gambling ({row[1].total}):[1/1], Insight:{row[2].total} DC{row[5].total}, Deception:{row[3].total} DC{row[6].total}, Intimidation:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[30:35] ]) }}
{{ output8 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Gambling ({row[1].total}):[1/1], Insight:{row[2].total} DC{row[5].total}, Deception:{row[3].total} DC{row[6].total}, Intimidation:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[35:40] ]) }}
{{ output9 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Gambling ({row[1].total}):[1/1], Insight:{row[2].total} DC{row[5].total}, Deception:{row[3].total} DC{row[6].total}, Intimidation:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[40:45] ]) }}
{{ output10 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Gambling ({row[1].total}):[1/1], Insight:{row[2].total} DC{row[5].total}, Deception:{row[3].total} DC{row[6].total}, Intimidation:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[45:50] ]) }}
{{ profits = sum([ row[9] for row in rolltable ]) }}

#load output for display
{{ fields = [] if not showusage else fields }}
{{ fields.append(f'Rolling|Luck:1d100{NL}Insight:{rollstr1}{NL}Deception:{rollstr2}{NL}Intimidation:{rollstr3}') if not showusage else False }}
{{ fields.append(f'Log|{output1}') if not showusage else False }}
{{ fields.append(f'Log|{output2}') if output2 != '' and not showusage else False }}
{{ fields.append(f'Log|{output3}') if output3 != '' and not showusage else False }}
{{ fields.append(f'Log|{output4}') if output4 != '' and not showusage else False }}
{{ fields.append(f'Log|{output5}') if output5 != '' and not showusage else False }}
{{ fields.append(f'Log|{output6}') if output6 != '' and not showusage else False }}
{{ fields.append(f'Log|{output7}') if output7 != '' and not showusage else False }}
{{ fields.append(f'Log|{output8}') if output8 != '' and not showusage else False }}
{{ fields.append(f'Log|{output9}') if output9 != '' and not showusage else False }}
{{ fields.append(f'Log|{output10}') if output10 != '' and not showusage else False }}
{{ fields.append(f'Profits|{profits}') if not showusage else False }}


##PIT FIGHTING##
{{ attackArg = ARGS[0] if len(ARGS) > 0 else '?' }}
{{ attack = int(attackArg.lstrip('+-')) if attackArg.lstrip('+-').isdigit() else -1 }}
{{ attack = attack * -1 if attackArg[0] == '-' else attack }}

{{ mod1arg = ARGS[1] if len(ARGS) > 1 else '?' }}
{{ mod1 = int(mod1arg.lstrip('+-')) if mod1arg.lstrip('+-').isdigit() else -1 }}
{{ mod1 = mod1 * -1 if mod1arg[0] == '-' else mod1 }}

{{ mod2arg = ARGS[2] if len(ARGS) > 2 else '?' }}
{{ mod2 = int(mod2arg.lstrip('+-')) if mod2arg.lstrip('+-').isdigit() else -1 }}
{{ mod2 = mod2 * -1 if mod2arg[0] == '-' else mod2 }}

{{ mod3arg = ARGS[3] if len(ARGS) > 3 else '?' }}
{{ mod3 = int(mod3arg.lstrip('+-')) if mod3arg.lstrip('+-').isdigit() else -1 }}
{{ mod3 = mod3 * -1 if mod3arg[0] == '-' else mod3 }}

{{ mod4arg = ARGS[4] if len(ARGS) > 4 else '?' }}
{{ mod4 = int(mod4arg.lstrip('+-')) if mod4arg.lstrip('+-').isdigit() else -1 }}
{{ mod4 = mod4 * -1 if mod4arg[0] == '-' else mod4 }}

{{ weeks = ARGS[5] if len(ARGS) > 5 else '?' }}
{{ weeks = int(weeks) if weeks.isdigit() else 1 }}
{{ weeks = 1 if weeks < 1 else weeks }}
{{ weeks = 50 if weeks > 50 else weeks }}

{{ showusage = attackArg == '?' }}

#rolls
{{ rolltable = [ [n+1] for n in range(weeks) ] }} #column 0
{{ modFeat = 1 if min(mod1,mod2,mod3+((mod4/2)+1)) == mod1 else 2 if min(mod1,mod2,mod3) == mod2 else 3 }}
{{ modDie = f'{"2" if LUCKY or ADV != 0 else "1"}d20{"kh1" if LUCKY or ADV == 1 else "kl1" if ADV == -1 else ""}' }}
{{ rollstr1 = f'{modDie if modFeat == 1 else "1d20"}{"ro1" if HALFLING else ""}+{attack if attack > mod1 and modFeat == 1 else mod1}' }}
{{ rollstr2 = f'{modDie if modFeat == 2 else "1d20"}{"ro1" if HALFLING else ""}+{attack if attack > mod2 and modFeat == 2 else mod2}' }}
{{ rollstr3 = f'{modDie if modFeat == 3 else "1d20"}{"ro1" if HALFLING else ""}+{attack if attack > mod3+((mod4/2)+1) and modFeat == 3 else str(mod3)+"+1d"+str(mod4)}' }}
{{ [ row.append(vroll("1d100")) for row in rolltable ] }} #column 1
{{ [ row.append(vroll(rollstr1)) for row in rolltable ] }} #column 2
{{ [ row.append(vroll(rollstr2)) for row in rolltable ] }} #column 3
{{ [ row.append(vroll(rollstr3)) for row in rolltable ] }} #column 4
{{ [ row.append(vroll('5+2d10')) for row in rolltable ] }} #column 5
{{ [ row.append(vroll('5+2d10')) for row in rolltable ] }} #column 6
{{ [ row.append(vroll('5+2d10')) for row in rolltable ] }} #column 7

#results
{{ [ row.append(sum([row[2].total >= row[5].total, row[3].total >= row[6].total, row[4].total >= row[7].total])) for row in rolltable ] }} #column 8: passes
{{ [ row.append(200 if row[8] == 3 else 100 if row[8] == 2 else 50 if row[8] == 1 else 0) for row in rolltable ] }} #column 9: net

#format output
{{ output1 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Pitfighting ({row[1].total}):[1/1], Athletics:{row[2].total} DC{row[5].total}, Acrobatics:{row[3].total} DC{row[6].total}, Con Check:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[0:5] ]) }}
{{ output2 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Pitfighting ({row[1].total}):[1/1], Athletics:{row[2].total} DC{row[5].total}, Acrobatics:{row[3].total} DC{row[6].total}, Con Check:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[5:10] ]) }}
{{ output3 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Pitfighting ({row[1].total}):[1/1], Athletics:{row[2].total} DC{row[5].total}, Acrobatics:{row[3].total} DC{row[6].total}, Con Check:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[10:15] ]) }}
{{ output4 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Pitfighting ({row[1].total}):[1/1], Athletics:{row[2].total} DC{row[5].total}, Acrobatics:{row[3].total} DC{row[6].total}, Con Check:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[15:20] ]) }}
{{ output5 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Pitfighting ({row[1].total}):[1/1], Athletics:{row[2].total} DC{row[5].total}, Acrobatics:{row[3].total} DC{row[6].total}, Con Check:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[20:25] ]) }}
{{ output6 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Pitfighting ({row[1].total}):[1/1], Athletics:{row[2].total} DC{row[5].total}, Acrobatics:{row[3].total} DC{row[6].total}, Con Check:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[25:30] ]) }}
{{ output7 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Pitfighting ({row[1].total}):[1/1], Athletics:{row[2].total} DC{row[5].total}, Acrobatics:{row[3].total} DC{row[6].total}, Con Check:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[30:35] ]) }}
{{ output8 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Pitfighting ({row[1].total}):[1/1], Athletics:{row[2].total} DC{row[5].total}, Acrobatics:{row[3].total} DC{row[6].total}, Con Check:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[35:40] ]) }}
{{ output9 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Pitfighting ({row[1].total}):[1/1], Athletics:{row[2].total} DC{row[5].total}, Acrobatics:{row[3].total} DC{row[6].total}, Con Check:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[40:45] ]) }}
{{ output10 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Pitfighting ({row[1].total}):[1/1], Athletics:{row[2].total} DC{row[5].total}, Acrobatics:{row[3].total} DC{row[6].total}, Con Check:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[45:50] ]) }}
{{ profits = sum([ row[9] for row in rolltable ]) }}

#load output for display
{{ fields = [] if not showusage else fields }}
{{ fields.append(f'Rolling|Luck:1d100{NL}Athletics:{rollstr1}{NL}Acrobatics:{rollstr2}{NL}Con Check:{rollstr3}') if not showusage else False }}
{{ fields.append(f'Log|{output1}') if not showusage else False }}
{{ fields.append(f'Log|{output2}') if output2 != '' and not showusage else False }}
{{ fields.append(f'Log|{output3}') if output3 != '' and not showusage else False }}
{{ fields.append(f'Log|{output4}') if output4 != '' and not showusage else False }}
{{ fields.append(f'Log|{output5}') if output5 != '' and not showusage else False }}
{{ fields.append(f'Log|{output6}') if output6 != '' and not showusage else False }}
{{ fields.append(f'Log|{output7}') if output7 != '' and not showusage else False }}
{{ fields.append(f'Log|{output8}') if output8 != '' and not showusage else False }}
{{ fields.append(f'Log|{output9}') if output9 != '' and not showusage else False }}
{{ fields.append(f'Log|{output10}') if output10 != '' and not showusage else False }}
{{ fields.append(f'Profits|{profits}') if not showusage else False }}


##WORK##
{{ descriptor = ARGS[0] if len(ARGS) > 0 else '?' }}

{{ mod1arg = ARGS[1] if len(ARGS) > 1 else '?' }}
{{ mod1 = int(mod1arg.lstrip('+-')) if mod1arg.lstrip('+-').isdigit() else -1 }}
{{ mod1 = mod1 * -1 if mod1arg[0] == '-' else mod1 }}

{{ weeks = ARGS[2] if len(ARGS) > 2 else '?' }}
{{ weeks = int(weeks) if weeks.isdigit() else 1 }}
{{ weeks = 1 if weeks < 1 else weeks }}
{{ weeks = 50 if weeks > 50 else weeks }}

{{ showusage = descriptor == '?' }}

#rolls
{{ rolltable = [ [n+1] for n in range(weeks) ] }} #column 0
{{ modDie = f'{"2" if LUCKY or ADV != 0 else "1"}d20{"kh1" if LUCKY or ADV == 1 else "kl1" if ADV == -1 else ""}' }}
{{ rollstr1 = f'{modDie}{"ro1" if HALFLING else ""}+{mod1}' }}
{{ [ row.append(vroll("1d100")) for row in rolltable ] }} #column 1
{{ [ row.append(vroll(rollstr1)) for row in rolltable ] }} #column 2

#results
{{ [ row.append(10 if row[2].total < 10 else 20 if row[2].total < 15 else 30 if row[2].total < 21 else 50) for row in rolltable ] }} #column 3

#format output
{{ output1 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Work ({row[1].total}):[1/1], {descriptor}:{row[2].total}, Net:{row[3]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[0:5] ]) }}
{{ output2 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Work ({row[1].total}):[1/1], {descriptor}:{row[2].total}, Net:{row[3]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[5:10] ]) }}
{{ output3 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Work ({row[1].total}):[1/1], {descriptor}:{row[2].total}, Net:{row[3]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[10:15] ]) }}
{{ output4 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Work ({row[1].total}):[1/1], {descriptor}:{row[2].total}, Net:{row[3]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[15:20] ]) }}
{{ output5 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Work ({row[1].total}):[1/1], {descriptor}:{row[2].total}, Net:{row[3]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[20:25] ]) }}
{{ output6 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Work ({row[1].total}):[1/1], {descriptor}:{row[2].total}, Net:{row[3]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[25:30] ]) }}
{{ output7 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Work ({row[1].total}):[1/1], {descriptor}:{row[2].total}, Net:{row[3]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[30:35] ]) }}
{{ output8 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Work ({row[1].total}):[1/1], {descriptor}:{row[2].total}, Net:{row[3]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[35:40] ]) }}
{{ output9 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Work ({row[1].total}):[1/1], {descriptor}:{row[2].total}, Net:{row[3]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[40:45] ]) }}
{{ output10 = ''.join([ f'{"**" if row[1].total % 10 == 1 else ""}{str(row[0])}. Work ({row[1].total}):[1/1], {descriptor}:{row[2].total}, Net:{row[3]} GP{", Complication**" if row[1].total % 10 == 1 else ""}{NL}' for row in rolltable[45:50] ]) }}
{{ profits = sum([ row[3] for row in rolltable ]) }}

#load output for display
{{ fields = [] if not showusage else fields }}
{{ fields.append(f'Rolling|Luck:1d100{NL}{descriptor}:{rollstr1}') if not showusage else False }}
{{ fields.append(f'Log|{output1}') if not showusage else False }}
{{ fields.append(f'Log|{output2}') if output2 != '' and not showusage else False }}
{{ fields.append(f'Log|{output3}') if output3 != '' and not showusage else False }}
{{ fields.append(f'Log|{output4}') if output4 != '' and not showusage else False }}
{{ fields.append(f'Log|{output5}') if output5 != '' and not showusage else False }}
{{ fields.append(f'Log|{output6}') if output6 != '' and not showusage else False }}
{{ fields.append(f'Log|{output7}') if output7 != '' and not showusage else False }}
{{ fields.append(f'Log|{output8}') if output8 != '' and not showusage else False }}
{{ fields.append(f'Log|{output9}') if output9 != '' and not showusage else False }}
{{ fields.append(f'Log|{output10}') if output10 != '' and not showusage else False }}
{{ fields.append(f'Profits|{profits}') if not showusage else False }}




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
