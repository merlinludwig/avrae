!alias dtd tembed
#get functions
{{ GVARS = load_json(get_gvar('9e936bdc-7539-4e14-896e-7febbab0df2a')) }}
#initialize function constants
{{ f"{'{'*2} ARGS,ACTS,SERVER = {&ARGS&},{load_json(get_gvar(GVARS.activities))}, 'doghouse' {'}'*2}" }}
{{ activities = load_json(get_gvar(GVARS.activities)) }}
#call setup function
{{ get_gvar(GVARS.setup) }}
#get user function selection
{{ args = &ARGS& }}
{{ activity = args.pop(0) if len(args) > 0 else '' }}
{{ activity = activity.lower() }}
{{ activity = int(activity) if activity.isdigit() else max([ a.index if activity == a.title.lower() else 0 for a in activities ]) }}
#call selected function
{{ get_gvar(GVARS.get(activities[activity].title.lower())) }}
#call display
{{ get_gvar(GVARS.display) }}
