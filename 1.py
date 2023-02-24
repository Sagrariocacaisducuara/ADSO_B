def acceso_lista(lista,indice):
    try:
        return lista[indice]
    except IndexError:
        print('error el indice{indice}esta duera de ranfo es errono')
mi_lista = [1,2,3,4,5]
print(acceso_lista(mi_lista,4))