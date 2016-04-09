# https://checkio.org/mission/pep8-break/

def twist(t):
    s,x,y='',',.!?(){}[]<>@#;:$%&*+-/=\^_`|~','.,?!)(}{][><#@:;$%&*+-/=\^_`|~'
    for c in' '.join(t.split()):
        s+=str(9-int(c))if c.isdigit()else c.swapcase()
        s=s[:-1]+y[x.index(c)]if c in x else s
    S,w='',[]
    for c in s:
        if not c.isalpha():
            S=S[::-1]+c;w.append(S);S='';
        else:
            S+=c
    return ''.join(w+[S[::-1]])or' 'if len(t)else''
