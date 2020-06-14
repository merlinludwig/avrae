!alias console embed
<drac2>
stack = []
stack.append('init')
while stack:
    function = stack.pop()
    
    if function == 'init':
        title = ''
        desc = ''
        thumb = ''
        image = ''
        footer = ''
        fields = []
        color = ''
        timeout = 0
        stack.append('process_input')
        continue
        
    if function == 'process_input':
        args = []
        for a in &ARGS&:
            args.append(a.lower())
        pargs = argparse(args)
        if pargs.last('debug',False):
            thumb = 'https://cdn4.iconfinder.com/data/icons/security-soft-1/512/bug_debug_debugger_debugging_security_report_antivirus_test_code-512.png'
            color = '#ff0000'
            timeout = 10
            fields.append(['Args',args,True])
            fields.append(['Parsed Args',pargs,True])
        stack.append('display')
        continue
        
    if function == 'display':
        display_string = f'\
            -title "{title}"\n\
            -desc "{desc}"\n\
            -thumb "{thumb}"\n\
            -image "{image}"\n\
            -footer "{footer}"\n\
            -color "{color}"\n\
            -t "{timeout}"\n\
            '
        for f in fields:
            if f[2]:
                display_string += f'-f "{f[0]}|{f[1]}|inline"\n'
            else:
                display_string += f'-f "{f[0]}|{f[1]}"\n'
        return display_string
err(f'Stack ran out of frames. This shouldn\'t happen. Last function = {function} Please inform merlin#6444')
</drac2>
