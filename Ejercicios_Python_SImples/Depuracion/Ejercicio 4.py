listin = {'Juan':123456789, 'Pedro':987654321}

def elimina(listin, usuario, nunero):
    listin[usuario] = nunero
    print(listin)
    del listin[usuario]
    return listin

print(elimina(listin, 'Pablo', 123456789))

#Estaba intentando hacer un del de un usuario inexistente despues en el return
#devolvia el diccionario del usuarioeliminado lo cual genera un error.
