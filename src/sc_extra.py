# =============================================================================
# sc_extra.py — Funções Adicionais
# =============================================================================


def sc_calloc(count: int, size: int) -> bytearray:
    """
    Aloca count * size bytes, todos inicializados a zero.
    Retorna None se count ou size forem 0 ou negativos.
    """
    if count <= 0 or size <= 0:
        return None
    return bytearray(count * size)


def sc_substr(s: str, start: int, length: int) -> str:
    """
    Extrai uma substring de s começando em start com comprimento length.
    Retorna string vazia se start for maior que o tamanho de s.
    Retorna None se s for None.
    """
    if s is None:
        return None
    s_len = 0
    for _ in s:
        s_len += 1
    if start >= s_len:
        return ""
    result = ""
    i = 0
    count = 0
    for c in s:
        if i >= start and count < length:
            result += c
            count += 1
        i += 1
    return result


def sc_strjoin(s1: str, s2: str) -> str:
    """
    Concatena s1 e s2 numa nova string.
    Se um deles for None, trata como string vazia.
    """
    if s1 is None:
        s1 = ""
    if s2 is None:
        s2 = ""
    result = ""
    for c in s1:
        result += c
    for c in s2:
        result += c
    return result


def sc_strtrim(s: str, charset: str) -> str:
    """
    Remove os caracteres presentes em charset do início e do fim de s.
    Retorna None se s for None.
    Retorna string vazia se charset for None ou s for vazia.
    """
    if s is None:
        return None
    if charset is None:
        return s
    # Encontra o início (primeiro char que NÃO está no charset)
    start = 0
    s_len = 0
    for _ in s:
        s_len += 1
    while start < s_len:
        found = False
        for c in charset:
            if s[start] == c:
                found = True
                break
        if not found:
            break
        start += 1
    # Encontra o fim (último char que NÃO está no charset)
    end = s_len - 1
    while end >= start:
        found = False
        for c in charset:
            if s[end] == c:
                found = True
                break
        if not found:
            break
        end -= 1
    # Constrói o resultado
    result = ""
    for i in range(start, end + 1):
        result += s[i]
    return result


def sc_split(s: str, delimiter: str) -> list:
    """
    Divide s em um array de strings usando delimiter como separador.
    Retorna None se s for None.
    Delimitadores consecutivos geram strings vazias — não são ignorados.
    """
    if s is None:
        return None
    if delimiter is None or delimiter == "":
        return [s]
    result = []
    current = ""
    i = 0
    s_len = 0
    for _ in s:
        s_len += 1
    d_len = 0
    for _ in delimiter:
        d_len += 1
    while i < s_len:
        # Verifica se começa o delimitador aqui
        match = True
        if i + d_len > s_len:
            match = False
        else:
            for j in range(d_len):
                if s[i + j] != delimiter[j]:
                    match = False
                    break
        if match:
            result.append(current)
            current = ""
            i += d_len
        else:
            current += s[i]
            i += 1
    result.append(current)
    return result


def sc_itoa(n: int) -> str:
    """
    Converte um inteiro para string.
    Trata números negativos e o zero.
    """
    if n == 0:
        return "0"
    result = ""
    negative = n < 0
    if negative:
        n = -n
    while n > 0:
        digit = n % 10
        result = chr(digit + 48) + result
        n //= 10
    if negative:
        result = "-" + result
    return result


def sc_strmapi(s: str, f) -> str:
    """
    Aplica a função f a cada caractere de s, passando o índice e o caractere.
    Retorna a nova string resultante. Retorna None se s for None.
    """
    if s is None:
        return None
    result = ""
    i = 0
    for c in s:
        result += f(i, c)
        i += 1
    return result


def sc_striteri(s: str, f) -> None:
    """
    Aplica a função f a cada caractere de s (passando índice e caractere).
    Não retorna nada — modifica in place via efeito colateral da função f.
    """
    if s is None:
        return
    i = 0
    for c in s:
        f(i, c)
        i += 1


def sc_putchar_fd(c: str, fd) -> None:
    """Escreve o caractere c no descritor de ficheiro fd."""
    fd.write(c)


def sc_putstr_fd(s: str, fd) -> None:
    """Escreve a string s no descritor de ficheiro fd."""
    if s is None:
        return
    for c in s:
        fd.write(c)


def sc_putendl_fd(s: str, fd) -> None:
    """Escreve a string s seguida de newline no descritor de ficheiro fd."""
    if s is None:
        return
    for c in s:
        fd.write(c)
    fd.write("\n")


def sc_putnbr_fd(n: int, fd) -> None:
    """Escreve o inteiro n no descritor de ficheiro fd."""
    fd.write(sc_itoa(n))