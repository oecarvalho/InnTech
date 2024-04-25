from collections import namedtuple


def get_changes(object: object) -> namedtuple:
    '''
    Função para pegar as mudanças ocorridas em um objeto.
    Deve ser chamada dentro de uma funcção save.

    Parâmetros:
        object: objeto que você deseja saber as mudanças.
    Retorno:
        namedtuple: com os campos:
            normais: Lista com os nomes dos campos que mudaram.
            back: Lista com os objetos dos campos que mudaram.
            old_and_new_object: Dicionário com os campos:
                old_object: Objeto antes do save.
                new_object: Objeto durante o save.
    '''

    object_class = object.__class__
    old_object = object_class.objects.get(pk=object.pk)
    new_object = object
    mudancas = namedtuple('mudancas', ['normais', 'back', 'old_and_new_object'])

    def houve_mudanca_normal(field):
        try:
            if getattr(old_object, field.name) != getattr(new_object, field.name):
                return field.name
        except TypeError():
            pass

    def houve_mudanca_back(field):
        try:
            if getattr(old_object, field.name) != getattr(new_object, field.name):
                return field
        except TypeError():
            pass

    change_normal_fields = list(filter(campo_valido, map(houve_mudanca_normal, object._meta.fields)))
    change_back_fields = list(filter(campo_valido, map(houve_mudanca_back, object._meta.get_fields())))
    old_and_new_object = {
        'old_object': old_object,
        'new_object': new_object
    }

    return mudancas(
        change_normal_fields,
        change_back_fields,
        old_and_new_object
    )

def campo_valido(field):
    return True if field else False
