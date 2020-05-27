##CAROUSING##
{{ classArg = ARGS.pop(0) if len(ARGS) > 0 else '?' }}
{{ classVar = classArg if classArg == 'middle' or classArg == 'upper' else 'lower' }}

{{ showusage = classArg == '?' }}

{{ weeks = ARGS.pop(0) if len(ARGS) > 0 else '?' }}
{{ weeks = int(weeks) if weeks.isdigit() else 1 }}
{{ weeks = 1 if weeks < 1 else weeks }}
{{ weeks = WEEKLIMIT if weeks > WEEKLIMIT else weeks }}

{{ persuasionArg = ARGS.pop(0) if len(ARGS) > 0 else str(RAW.skills.persuasion) }}
{{ persuasion = int(persuasionArg.lstrip('+-')) if persuasionArg.lstrip('+-').isdigit() else -1 }}
{{ persuasion = persuasion * -1 if persuasionArg[0] == '-' else persuasion }}

{{ chaArg = ARGS.pop(0) if len(ARGS) > 0 else str(charismaMod) }}
{{ chaLimit = int(chaArg.lstrip('+-')) if chaArg.lstrip('+-').isdigit() else -1 }}
{{ chaLimit = chaLimit * -1 if chaArg[0] == '-' else chaLimit }}
{{ chaLimit = 1 if chaLimit < 1 else 1 + chaLimit }}

{{ resources = 250 if classVar == 'upper' else 50 if classVar == 'middle' else 10 }}
{{ resources = resources * weeks }}

#rolls
{{ rolltable = [ [n+1] for n in range(weeks) ] }} #column 0
{{ rollstr = f'{"2" if LUCKY or ADV != 0 else "1"}d20{"kh1" if LUCKY or ADV == 1 else "kl1" if ADV == -1 else ""}{"ro1" if HALFLING else ""}+{persuasion}' }}
{{ [ row.append(vroll("1d100")) for row in rolltable ] }} #column 1
{{ [ row.append(vroll(rollstr)) for row in rolltable ] }} #column 2

#contacts
{{ set_cvar_nx('contacts',dump_json([])) }}
{{ contacts = load_json(contacts) }}
{{ potentialContacts = [] }}

{{ [ potentialContacts.append(f'hostile {classVar} class') if row[2].total < 6 else potentialContacts.append(f'allied {classVar} class') if row[2].total > 10 and row[2].total < 16 else [ potentialContacts.append(f'allied {classVar} class') for x in range(2) ] if row[2].total > 15 and row[2].total < 21 else [ potentialContacts.append(f'allied {classVar} class') for x in range(3) ] if row[2].total > 20 else False for row in rolltable ] }}

{{ [ contacts.append(contact) if (len(contacts) < chaLimit) or ('hostile' in contact) else False for contact in potentialContacts ] }}
{{ set_cvar('contacts',dump_json(contacts)) }}
{{ contacts = load_json(contacts) }}

#format output
{{ output1 = ''.join([ f'{str(row[0])}. Carousing ({row[1].total}{":warning:" if row[1].total % 10 == 1 else ""}):[1/1] Gold spent: {"10" if classVar == "lower" else "50" if classVar == "middle" else "250"} GP, Contacts({row[2].total}): {"1 Hostile" if row[2].total < 6 else "None" if row[2].total < 11 else "1 Allied" if row[2].total < 16 else "2 Allied" if row[2].total < 21 else "3 Allied"}{NL}' for row in rolltable[0:10] ]) }}
{{ output2 = ''.join([ f'{str(row[0])}. Carousing ({row[1].total}{":warning:" if row[1].total % 10 == 1 else ""}):[1/1] Gold spent: {"10" if classVar == "lower" else "50" if classVar == "middle" else "250"} GP, Contacts({row[2].total}): {"1 Hostile" if row[2].total < 6 else "None" if row[2].total < 11 else "1 Allied" if row[2].total < 16 else "2 Allied" if row[2].total < 21 else "3 Allied"}{NL}' for row in rolltable[10:20] ]) }}
{{ output3 = ''.join([ f'{str(row[0])}. Carousing ({row[1].total}{":warning:" if row[1].total % 10 == 1 else ""}):[1/1] Gold spent: {"10" if classVar == "lower" else "50" if classVar == "middle" else "250"} GP, Contacts({row[2].total}): {"1 Hostile" if row[2].total < 6 else "None" if row[2].total < 11 else "1 Allied" if row[2].total < 16 else "2 Allied" if row[2].total < 21 else "3 Allied"}{NL}' for row in rolltable[20:30] ]) }}
{{ output4 = ''.join([ f'{str(row[0])}. Carousing ({row[1].total}{":warning:" if row[1].total % 10 == 1 else ""}):[1/1] Gold spent: {"10" if classVar == "lower" else "50" if classVar == "middle" else "250"} GP, Contacts({row[2].total}): {"1 Hostile" if row[2].total < 6 else "None" if row[2].total < 11 else "1 Allied" if row[2].total < 16 else "2 Allied" if row[2].total < 21 else "3 Allied"}{NL}' for row in rolltable[30:40] ]) }}
{{ output5 = ''.join([ f'{str(row[0])}. Carousing ({row[1].total}{":warning:" if row[1].total % 10 == 1 else ""}):[1/1] Gold spent: {"10" if classVar == "lower" else "50" if classVar == "middle" else "250"} GP, Contacts({row[2].total}): {"1 Hostile" if row[2].total < 6 else "None" if row[2].total < 11 else "1 Allied" if row[2].total < 16 else "2 Allied" if row[2].total < 21 else "3 Allied"}{NL}' for row in rolltable[40:50] ]) }}
{{ outputContacts = ''.join([f'{contact}{NL}' for contact in contacts]) }}# outputContacts = ''.join([ f'{contact}{NL}' for contact in contacts ]) }}

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
