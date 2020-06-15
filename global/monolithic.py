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
stack.append(['main'])

while stack:
    call = stack.pop()
    
    if call[0] == 'main':
        stack.append(['display'])
        continue
        
    if call[0] == 'display':
        display_string = ''
        for k,v in embed:
            if k == 'fields':
                for f in embed.fields:
                    if f[2]:
                        display_string += f'-f "{f[0]}|{f[1]}|inline"\n'
                    else:
                        display_string += f'-f "{f[0]}|{f[1]}"\n'
            elif k == 'timeout':
                display_string += f'-t "{v[0]}"\n'
            else:
                display_string += f'-{k} "{v[0]}"\n'
        return display_string
</drac2>
