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
{{ mod4 = int(mod4arg.lstrip('+-')) if mod4arg.lstrip('+-').isdigit() else 6 }}
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
{{ output1 = ''.join([ f'{str(row[0])}. Pitfighting ({row[1].total}{":warning:" if row[1].total % 10 == 1 else ""}):[1/1], Athletics:{row[2].total} DC{row[5].total}, Acrobatics:{row[3].total} DC{row[6].total}, Con Check:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{NL}' for row in rolltable[0:5] ]) }}
{{ output2 = ''.join([ f'{str(row[0])}. Pitfighting ({row[1].total}{":warning:" if row[1].total % 10 == 1 else ""}):[1/1], Athletics:{row[2].total} DC{row[5].total}, Acrobatics:{row[3].total} DC{row[6].total}, Con Check:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{NL}' for row in rolltable[5:10] ]) }}
{{ output3 = ''.join([ f'{str(row[0])}. Pitfighting ({row[1].total}{":warning:" if row[1].total % 10 == 1 else ""}):[1/1], Athletics:{row[2].total} DC{row[5].total}, Acrobatics:{row[3].total} DC{row[6].total}, Con Check:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{NL}' for row in rolltable[10:15] ]) }}
{{ output4 = ''.join([ f'{str(row[0])}. Pitfighting ({row[1].total}{":warning:" if row[1].total % 10 == 1 else ""}):[1/1], Athletics:{row[2].total} DC{row[5].total}, Acrobatics:{row[3].total} DC{row[6].total}, Con Check:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{NL}' for row in rolltable[15:20] ]) }}
{{ output5 = ''.join([ f'{str(row[0])}. Pitfighting ({row[1].total}{":warning:" if row[1].total % 10 == 1 else ""}):[1/1], Athletics:{row[2].total} DC{row[5].total}, Acrobatics:{row[3].total} DC{row[6].total}, Con Check:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{NL}' for row in rolltable[20:25] ]) }}
{{ output6 = ''.join([ f'{str(row[0])}. Pitfighting ({row[1].total}{":warning:" if row[1].total % 10 == 1 else ""}):[1/1], Athletics:{row[2].total} DC{row[5].total}, Acrobatics:{row[3].total} DC{row[6].total}, Con Check:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{NL}' for row in rolltable[25:30] ]) }}
{{ output7 = ''.join([ f'{str(row[0])}. Pitfighting ({row[1].total}{":warning:" if row[1].total % 10 == 1 else ""}):[1/1], Athletics:{row[2].total} DC{row[5].total}, Acrobatics:{row[3].total} DC{row[6].total}, Con Check:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{NL}' for row in rolltable[30:35] ]) }}
{{ output8 = ''.join([ f'{str(row[0])}. Pitfighting ({row[1].total}{":warning:" if row[1].total % 10 == 1 else ""}):[1/1], Athletics:{row[2].total} DC{row[5].total}, Acrobatics:{row[3].total} DC{row[6].total}, Con Check:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{NL}' for row in rolltable[35:40] ]) }}
{{ output9 = ''.join([ f'{str(row[0])}. Pitfighting ({row[1].total}{":warning:" if row[1].total % 10 == 1 else ""}):[1/1], Athletics:{row[2].total} DC{row[5].total}, Acrobatics:{row[3].total} DC{row[6].total}, Con Check:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{NL}' for row in rolltable[40:45] ]) }}
{{ output10 = ''.join([ f'{str(row[0])}. Pitfighting ({row[1].total}{":warning:" if row[1].total % 10 == 1 else ""}):[1/1], Athletics:{row[2].total} DC{row[5].total}, Acrobatics:{row[3].total} DC{row[6].total}, Con Check:{row[4].total} DC{row[7].total}, Passes:{row[8]}, Net:{row[9]} GP{NL}' for row in rolltable[45:50] ]) }}
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
