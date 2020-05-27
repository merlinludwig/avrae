##HELP##
{{ activities = ''.join([f'{a.index}. {a.title}{NL}' for a in ACTS]) }}
{{ fields.append(f'Activities:|{activities}') }}
