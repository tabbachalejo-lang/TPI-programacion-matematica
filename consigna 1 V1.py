A = [101, 102, 103, 104, 105, 106]
B = [104, 105, 106, 107, 108]
C = [102, 105, 109]
todos_los_usuarios = []
for lista in [A, B, C]:
    for usuario in lista:
        encontrado = False
        for existente in todos_los_usuarios:
            if usuario == existente:
                encontrado = True
       
        if not encontrado:
            todos_los_usuarios = todos_los_usuarios + [usuario]
criticos = []
no_criticos = []
for usuario in todos_los_usuarios:
    p = False
    for a in A:
        if usuario == a: p = True
    q = False
    for b in B:
        if usuario == b: q = True
    r = False
    for c in C:
        if usuario == c: r = True
    if (p or q) and r:
        criticos = criticos + [usuario]
    else:
        no_criticos = no_criticos + [usuario]
print("Usuarios Críticos:", criticos)
print("Usuarios No Críticos:", no_criticos)