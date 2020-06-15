!alias console embed
<drac2>
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
stack.append(['main',0])

while stack:
    call = stack.pop()
    
    if call[0] == 'main':
        if call[1] == 0:
            stack.append(['main',1])
            stack.append(['display',0])
        if call[1] == 1:
            pass
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
