"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    r=[]
    contador=0
    while contador< len(result):
            r.append(result[contador])
            if contador<len(result):
                r.append('@')
            contador+=1
    result=r
    return result




