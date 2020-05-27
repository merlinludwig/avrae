##DOWNTIME REVAMPED##
args,commands
{{ functions = load_json(get_gvar(commands)) }}
{{ NL = '\n' }}
{{ cvars = get_raw().get('cvars',{}) }}
{{ selection = args and args.pop(0).lower() or '?' }}

{{ function = ([x for x in functions if selection in x.command]+[functions[0]])[0] }}
{{ f'-title "{name} {function.title}"' }}
