# =============================================================================
# sc_memory.py — Funções de Manipulação de Memória
# =============================================================================


def sc_memset(arr: bytearray, c: int, n: int) -> bytearray:
    """
    Preenche os primeiros n bytes do bytearray com o valor c.
    Retorna o próprio bytearray modificado.
    """
    if arr is None or n == 0:
        return arr
    for i in range(n):
        arr[i] = c & 0xFF
    return arr


def sc_bzero(arr: bytearray, n: int) -> None:
    """
    Zera os primeiros n bytes do bytearray (preenche com 0).
    Não retorna nada.
    """
    if arr is None or n == 0:
        return
    for i in range(n):
        arr[i] = 0


def sc_memcpy(dst: bytearray, src: bytearray, n: int) -> bytearray:
    """
    Copia n bytes de src para dst.
    Regiões não devem se sobrepor. Retorna dst.
    """
    if dst is None or src is None or n == 0:
        return dst
    for i in range(n):
        dst[i] = src[i]
    return dst


def sc_memmove(dst: bytearray, src: bytearray, n: int) -> bytearray:
    """
    Copia n bytes de src para dst, mesmo se as regiões se sobrepõem.
    Usa cópia reversa quando dst > src para evitar corrupção.
    Retorna dst.
    """
    if dst is None or src is None or n == 0:
        return dst
    # Copia para buffer temporário primeiro (resolve sobreposição)
    tmp = bytearray(n)
    for i in range(n):
        tmp[i] = src[i]
    for i in range(n):
        dst[i] = tmp[i]
    return dst


def sc_memchr(arr: bytearray, c: int, n: int):
    """
    Procura o byte c nos primeiros n bytes do bytearray.
    Retorna o índice onde encontrou, ou None se não encontrar.
    """
    if arr is None or n == 0:
        return None
    for i in range(n):
        if arr[i] == (c & 0xFF):
            return i
    return None


def sc_memcmp(arr1: bytearray, arr2: bytearray, n: int) -> int:
    """
    Compara os primeiros n bytes de arr1 e arr2.
    Retorna 0 se iguais, valor positivo se arr1 > arr2, negativo se arr1 < arr2.
    """
    if arr1 is None or arr2 is None or n == 0:
        return 0
    for i in range(n):
        if arr1[i] != arr2[i]:
            return arr1[i] - arr2[i]
    return 0