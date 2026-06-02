# =============================================================================
# sc_list.py — Funções de Lista Ligada (Bônus)
# =============================================================================


class t_list:
    """Estrutura de nó da lista ligada."""
    def __init__(self, content):
        self.content = content
        self.next = None


def sc_lstnew(content) -> t_list:
    """
    Cria um novo nó com o conteúdo fornecido.
    O ponteiro next é inicializado como None.
    Retorna o novo nó.
    """
    return t_list(content)


def sc_lstadd_front(lst: list, new_node: t_list) -> None:
    """
    Adiciona new_node no início da lista.
    lst é uma lista de 1 elemento usada como ponteiro para o início.
    """
    if new_node is None:
        return
    new_node.next = lst[0]
    lst[0] = new_node


def sc_lstsize(lst: t_list) -> int:
    """
    Conta e retorna o número de nós da lista.
    Retorna 0 se a lista for None.
    """
    count = 0
    current = lst
    while current is not None:
        count += 1
        current = current.next
    return count


def sc_lstlast(lst: t_list) -> t_list:
    """
    Retorna o último nó da lista.
    Retorna None se a lista for None.
    """
    if lst is None:
        return None
    current = lst
    while current.next is not None:
        current = current.next
    return current


def sc_lstadd_back(lst: list, new_node: t_list) -> None:
    """
    Adiciona new_node no final da lista.
    lst é uma lista de 1 elemento usada como ponteiro para o início.
    """
    if new_node is None:
        return
    if lst[0] is None:
        lst[0] = new_node
        return
    last = sc_lstlast(lst[0])
    last.next = new_node


def sc_lstdelone(node: t_list, del_func) -> None:
    """
    Aplica del_func ao conteúdo do nó e o apaga.
    Não apaga o próximo nó.
    """
    if node is None:
        return
    del_func(node.content)
    node.content = None


def sc_lstclear(lst: list, del_func) -> None:
    """
    Apaga todos os nós da lista, aplicando del_func a cada conteúdo.
    Define lst[0] como None no fim.
    """
    if lst is None or lst[0] is None:
        return
    current = lst[0]
    while current is not None:
        next_node = current.next
        del_func(current.content)
        current.content = None
        current = next_node
    lst[0] = None


def sc_lstiter(lst: t_list, f) -> None:
    """
    Percorre a lista e aplica a função f ao conteúdo de cada nó.
    Não retorna nada.
    """
    current = lst
    while current is not None:
        f(current.content)
        current = current.next


def sc_lstmap(lst: t_list, f, del_func) -> t_list:
    """
    Cria uma nova lista aplicando f ao conteúdo de cada nó.
    Se a alocação falhar, limpa tudo com del_func e retorna None.
    Retorna a nova lista.
    """
    if lst is None:
        return None
    new_head = None
    new_lst = [new_head]
    current = lst
    while current is not None:
        new_content = f(current.content)
        new_node = sc_lstnew(new_content)
        if new_node is None:
            sc_lstclear(new_lst, del_func)
            return None
        sc_lstadd_back(new_lst, new_node)
        current = current.next
    return new_lst[0]