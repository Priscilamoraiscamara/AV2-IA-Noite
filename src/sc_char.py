# =============================================================================
# sc_char.py — Funções de Classificação e Conversão de Caracteres
# =============================================================================


def sc_isalpha(c: int) -> int:
    """Verifica se o caractere é uma letra (a-z ou A-Z)."""
    return 1 if (65 <= c <= 90) or (97 <= c <= 122) else 0


def sc_isdigit(c: int) -> int:
    """Verifica se o caractere é um dígito (0-9)."""
    return 1 if 48 <= c <= 57 else 0


def sc_isalnum(c: int) -> int:
    """Verifica se o caractere é alfanumérico (letra ou dígito)."""
    return 1 if sc_isalpha(c) or sc_isdigit(c) else 0


def sc_isascii(c: int) -> int:
    """Verifica se o valor está na tabela ASCII (0 a 127)."""
    return 1 if 0 <= c <= 127 else 0


def sc_isprint(c: int) -> int:
    """Verifica se o caractere é imprimível (espaço até ~)."""
    return 1 if 32 <= c <= 126 else 0


def sc_toupper(c: int) -> int:
    """Converte letra minúscula para maiúscula. Retorna o mesmo valor se não for minúscula."""
    return c - 32 if 97 <= c <= 122 else c


def sc_tolower(c: int) -> int:
    """Converte letra maiúscula para minúscula. Retorna o mesmo valor se não for maiúscula."""
    return c + 32 if 65 <= c <= 90 else c


def sc_atoi(s: str) -> int:
    """
    Converte uma string para inteiro, ignorando espaços no início.
    Para se encontrar caractere não numérico após os dígitos.
    Retorna 0 se não houver dígitos.
    """
    if s is None:
        return 0

    i = 0
    result = 0
    sign = 1

    # Ignora espaços e caracteres de controle iniciais
    while i < len(s) and s[i] in (' ', '\t', '\n', '\r', '\f', '\v'):
        i += 1

    # Verifica sinal
    if i < len(s) and s[i] in ('+', '-'):
        if s[i] == '-':
            sign = -1
        i += 1

    # Lê os dígitos
    while i < len(s) and 48 <= ord(s[i]) <= 57:
        result = result * 10 + (ord(s[i]) - 48)
        i += 1

    return sign * result