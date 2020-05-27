##CLEANUP AND DISPLAY##
{{ f'-title "{title}"' }}
{{ f'-desc "{desc}"' }}
{{ fields.append(f'ONLY TESTING|PLEASE DISREGARD')if TEST else False }}
{{ ''.join([f'-f "{field}"{NL}' for field in fields]) }}
{{ f' -footer "{footer}"' }}
