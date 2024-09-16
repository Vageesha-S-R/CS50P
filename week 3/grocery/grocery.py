d={}
while True:
    try:
        item=input().upper().strip()
        if item not in d:
            d[item]=1
        else:
            d[item]=d[item]+1
    except EOFError:
        s_d=dict(sorted(list(d.items())))
        for item in s_d:
            print(s_d[item],item,sep=" ")
        break
    except KeyError:
        pass
