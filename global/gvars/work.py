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
{{ output1 = ''.join([ f'{str(row[0])}. Work ({row[1].total}{":warning:" if row[1].total % 10 == 1 else ""}):[1/1], {descriptor}:{row[2].total}, Net:{row[3]} GP{NL}' for row in rolltable[0:5] ]) }}
{{ output2 = ''.join([ f'{str(row[0])}. Work ({row[1].total}{":warning:" if row[1].total % 10 == 1 else ""}):[1/1], {descriptor}:{row[2].total}, Net:{row[3]} GP{NL}' for row in rolltable[5:10] ]) }}
{{ output3 = ''.join([ f'{str(row[0])}. Work ({row[1].total}{":warning:" if row[1].total % 10 == 1 else ""}):[1/1], {descriptor}:{row[2].total}, Net:{row[3]} GP{NL}' for row in rolltable[10:15] ]) }}
{{ output4 = ''.join([ f'{str(row[0])}. Work ({row[1].total}{":warning:" if row[1].total % 10 == 1 else ""}):[1/1], {descriptor}:{row[2].total}, Net:{row[3]} GP{NL}' for row in rolltable[15:20] ]) }}
{{ output5 = ''.join([ f'{str(row[0])}. Work ({row[1].total}{":warning:" if row[1].total % 10 == 1 else ""}):[1/1], {descriptor}:{row[2].total}, Net:{row[3]} GP{NL}' for row in rolltable[20:25] ]) }}
{{ output6 = ''.join([ f'{str(row[0])}. Work ({row[1].total}{":warning:" if row[1].total % 10 == 1 else ""}):[1/1], {descriptor}:{row[2].total}, Net:{row[3]} GP{NL}' for row in rolltable[25:30] ]) }}
{{ output7 = ''.join([ f'{str(row[0])}. Work ({row[1].total}{":warning:" if row[1].total % 10 == 1 else ""}):[1/1], {descriptor}:{row[2].total}, Net:{row[3]} GP{NL}' for row in rolltable[30:35] ]) }}
{{ output8 = ''.join([ f'{str(row[0])}. Work ({row[1].total}{":warning:" if row[1].total % 10 == 1 else ""}):[1/1], {descriptor}:{row[2].total}, Net:{row[3]} GP{NL}' for row in rolltable[35:40] ]) }}
{{ output9 = ''.join([ f'{str(row[0])}. Work ({row[1].total}{":warning:" if row[1].total % 10 == 1 else ""}):[1/1], {descriptor}:{row[2].total}, Net:{row[3]} GP{NL}' for row in rolltable[40:45] ]) }}
{{ output10 = ''.join([ f'{str(row[0])}. Work ({row[1].total}{":warning:" if row[1].total % 10 == 1 else ""}):[1/1], {descriptor}:{row[2].total}, Net:{row[3]} GP{NL}' for row in rolltable[45:50] ]) }}
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
