<drac2>
program_id = 'eacc74a3-c680-468e-a354-b93b307544ed'
embed = {'title':[],
    'desc':[],
    'thumb':[],
    'image':[],
    'footer':[],
    'fields':[],
    'color':[],
    'timeout':[]}
stack = []
return_val = []
commands = {'debug':'debugging',
    'help':'help?'
    }
stack.append(['main',0])
while stack:
    call = stack.pop()
    
    if call[0] == 'main':
        if call[1] == 0:
            stack.append(['main',1])
            stack.append(['process_input',0])
        if call[1] == 1:
            stack.append(['display',0])
        continue
        
    if call[0] == 'process_input':
        args = []
        for i in range(0,len(ARGS),1):
            args.append(ARGS.pop().lower())
        if args:
            command = args.pop()
            match = False
            for key in commands:
                if command.lower() in commands[key]:
                    stack.append(args)
                    stack.append([key,0])
                    match = True
                    break
            if match:
                continue
            else:
                err('unknown argument')
        else:
            err('missing argument')
        
    if call[0] == 'debug':
        params = stack.pop()
        embed.title.append('Debug')
        embed.desc.append('Listing arguments passed to the command')
        embed.thumb.append('https://cdn4.iconfinder.com/data/icons/security-soft-1/512/bug_debug_debugger_debugging_security_report_antivirus_test_code-512.png')
        embed.color.append('ff0000')
        embed.fields.append(['Args',params,True])
        embed.fields.append(['Parsed Args',argparse(params),True])
        continue
        
    if call[0] == 'help':
        params = stack.pop()
        embed.title.append('Help')
        embed.desc.append('It looks like you need some help. Here is a list of available commands:')
        embed.thumb.append('https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Blue_question_mark_%28italic%29.svg/240px-Blue_question_mark_%28italic%29.svg.png')
        embed.color.append('0000ff')
        embed.fields.append(['Args',list(commands.keys()),False])
        continue
        
    if call[0] == 'display':
        display_string = ''
        for key in embed:
            if embed[key]:
                if key == 'fields':
                    for f in embed.fields:
                        if f[2]:
                            display_string += f'-f "{f[0]}|{f[1]}|inline"\n'
                        else:
                            display_string += f'-f "{f[0]}|{f[1]}"\n'
                elif key == 'timeout':
                    display_string += f'-t "{embed[key][0]}"\n'
                else:
                    display_string += f'-{key} "{embed[key][0]}"\n'
        return display_string
</drac2>
