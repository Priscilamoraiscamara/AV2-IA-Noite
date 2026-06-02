# =============================================================================
# sc_string.py — Funções de Manipulação de Strings
# =============================================================================


def sc_strlen(s: str) -> int:
    """
    Conta o número de caracteres da string até o fim.
    Retorna 0 se a string for None.
    """
    if s is None:
        return 0
    count = 0
    for _ in s:
        count += 1
    return count


def sc_strlcpy(dst: list, src: str, size: int) -> int:
    """
    Copia src para dst[0], limitando a size-1 caracteres + terminador nulo.
    Retorna o comprimento total de src.
    Em Python, usamos uma lista de 1 elemento como 'ponteiro' para dst.
    """
    src_len = sc_strlen(src)
    if size == 0:
        dst[0] = ""
        return src_len
    dst[0] = src[:size - 1]
    return src_len


def sc_strlcat(dst: list, src: str, size: int) -> int:
    """
    Concatena src ao fim de dst[0], sem ultrapassar size caracteres no total.
    Retorna o comprimento que teria se não houvesse limite.
    """
    dst_len = sc_strlen(dst[0])
    src_len = sc_strlen(src)
    if size <= dst_len:
        return size + src_len
    space = size - dst_len - 1
    dst[0] = dst[0] + src[:space]
    return dst_len + src_len


def sc_strchr(s: str, c: int) -> int:
    """
    Procura a primeira ocorrência do caractere c na string s.
    Retorna o índice onde encontrou, ou -1 se não encontrar.
    """
    if s is None:
        return -1
    for i in range(sc_strlen(s)):
        if ord(s[i]) == c:
            return i
    return -1


def sc_strrchr(s: str, c: int) -> int:
    """
    Procura a ÚLTIMA ocorrência do caractere c na string s.
    Retorna o índice onde encontrou, ou -1 se não encontrar.
    """
    if s is None:
        return -1
    last = -1
    for i in range(sc_strlen(s)):
        if ord(s[i]) == c:
            last = i
    return last


def sc_strncmp(s1: str, s2: str, n: int) -> int:
    """
    Compara os primeiros n caracteres de s1 e s2.
    Retorna 0 se iguais, positivo se s1 > s2, negativo se s1 < s2.
    """
    if s1 is None or s2 is None or n == 0:
        return 0
    for i in range(n):
        c1 = ord(s1[i]) if i < sc_strlen(s1) else 0
        c2 = ord(s2[i]) if i < sc_strlen(s2) else 0
        if c1 != c2:
            return c1 - c2
    return 0


def sc_strnstr(haystack: str, needle: str, n: int) -> int:
    """
    Procura needle dentro dos primeiros n caracteres de haystack.
    Retorna o índice onde encontrou, ou -1 se não encontrar.
    Se needle for string vazia, retorna 0.
    """
    if haystack is None or needle is None:
        return -1
    needle_len = sc_strlen(needle)
    if needle_len == 0:
        return 0
    hay_len = sc_strlen(haystack)
    for i in range(n):
        if i + needle_len > hay_len or i + needle_len > n:
            break
        match = True
        for j in range(needle_len):
            if haystack[i + j] != needle[j]:
                match = False
                break
        if match:
            return i
    return -1


def sc_strdup(s: str) -> str:
    """
    Cria uma cópia independente da string s.
    Retorna None se s for None.
    """
    if s is None:
        return None
    result = ""
    for c in s:
        result += c
    return result