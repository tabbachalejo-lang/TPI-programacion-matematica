A = [101, 102, 103, 104, 105, 106]
B = [104, 105, 106, 107, 108]
C = [102, 105, 109]
max_posible = 14
todos_los_usuarios = [None] * max_posible
cant_usuarios = 0                   
for usuario in A:
    encontrado = False
    for i in range(cant_usuarios):
        if usuario == todos_los_usuarios[i]:
            encontrado = True
    if not encontrado:
        todos_los_usuarios[cant_usuarios] = usuario
        cant_usuarios += 1
for usuario in B:
    encontrado = False
    for i in range(cant_usuarios):
        if usuario == todos_los_usuarios[i]:
            encontrado = True
    if not encontrado:
        todos_los_usuarios[cant_usuarios] = usuario
        cant_usuarios += 1
for usuario in C:
    encontrado = False
    for i in range(cant_usuarios):
        if usuario == todos_los_usuarios[i]:
            encontrado = True
    if not encontrado:
        todos_los_usuarios[cant_usuarios] = usuario
        cant_usuarios += 1
criticos = [None] * cant_usuarios
no_criticos = [None] * cant_usuarios
cant_criticos = 0
cant_no_criticos = 0
for i in range(cant_usuarios):
    usuario = todos_los_usuarios[i]
    p = False
    for a in A:
        if usuario == a: 
            p = True 
    q = False
    for b in B:
        if usuario == b: 
            q = True
    r = False
    for c in C:
        if usuario == c: 
            r = True

    if (p or q) and r:
        criticos[cant_criticos] = usuario
        cant_criticos += 1
    else:
        no_criticos[cant_no_criticos] = usuario  # Asignación directa por índice
        cant_no_criticos += 1
print("Usuarios Críticos:")
for i in range(cant_criticos):
    print(criticos[i], end=" ")
print()  # Salto de línea

print("Usuarios No Críticos:")
for i in range(cant_no_criticos):
    print(no_criticos[i], end=" ")
print()