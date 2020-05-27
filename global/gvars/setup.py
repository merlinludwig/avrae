##SETUP##
{{ ARGS = [a.lower() for a in ARGS ] }}
{{ PARGS = argparse(ARGS) }}
{{ NL = '\n' }}
{{ TB = '\t' }}
{{ RAW = get_raw() }}
{{ WEEKLIMIT = 50 if SERVER=='narwhal' else 2 if SERVER=='doghouse' else 1 }}
#misc modifiers
{{ CHAR = PARGS.last('char',False) }}
{{ HALFLING = RAW.race.lower().find('halfling') if CHAR else PARGS.last('half',False) }}
{{ LUCKY = PARGS.last('luck',False) }}
{{ TEST = PARGS.last('test',False) }}
{{ ADV = PARGS.adv() }}
#activity selection
{{ activityArg = ARGS.pop(0) if len(ARGS) > 0 else '?' }}
{{ activity = activityArg }}
{{ activity = activity.lower() }}
{{ activity = int(activity) if activity.isdigit() else max([ a.index if activity in a.title.lower() else 0 for a in ACTS ]) }}
#set title and description
{{ title = ACTS[activity].title }}
{{ desc = ACTS[activity].desc }}
{{ fields = [f'Resources|{ACTS[activity].resources}',f'Resolution|{ACTS[activity].resolution}',f'Usage|`!downtime \'{title.lower()}\' {ACTS[activity].usage}'] }}
{{ footer = f"COMMAND USED: !downtime \'{activityArg}\' {' '.join(ARGS)}" }}
