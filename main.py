import sys
import os

from src.sc_char import *
from src.sc_memory import *
from src.sc_string import *
from src.sc_extra import *
from src.sc_list import *

# ══════════════════════════════════════════════════════════════════════════
# Utilitários de interface
# ══════════════════════════════════════════════════════════════════════════

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\n  Pressione ENTER para continuar...")

def titulo(texto):
    print("\n" + "═" * 50)
    print(f"  {texto}")
    print("═" * 50)

def resultado(func, entrada, saida):
    print(f"\n  Função  : {func}")
    print(f"  Entrada : {entrada}")
    print(f"  Saída   : {saida}")

def pedir(msg):
    return input(f"\n  {msg}: ").strip()


# ══════════════════════════════════════════════════════════════════════════
# MENU 1 — Classificação e Conversão
# ══════════════════════════════════════════════════════════════════════════

def menu_char():
    while True:
        limpar()
        titulo("1. Classificação e Conversão de Caracteres")
        print("""
  [1] sc_isalpha  — é letra?
  [2] sc_isdigit  — é dígito?
  [3] sc_isalnum  — é letra ou dígito?
  [4] sc_isascii  — está na tabela ASCII?
  [5] sc_isprint  — é imprimível?
  [6] sc_toupper  — converte para MAIÚSCULA
  [7] sc_tolower  — converte para minúscula
  [8] sc_atoi     — string para inteiro
  [0] Voltar
        """)
        op = pedir("Escolha")

        if op == "0":
            break
        elif op in ("1","2","3","4","5","6","7"):
            c = pedir("Digite um caractere")
            if not c:
                print("  Entrada inválida.")
                pausar()
                continue
            codigo = ord(c[0])
            if   op == "1": resultado("sc_isalpha", c[0], sc_isalpha(codigo))
            elif op == "2": resultado("sc_isdigit", c[0], sc_isdigit(codigo))
            elif op == "3": resultado("sc_isalnum", c[0], sc_isalnum(codigo))
            elif op == "4": resultado("sc_isascii", c[0], sc_isascii(codigo))
            elif op == "5": resultado("sc_isprint", c[0], sc_isprint(codigo))
            elif op == "6": resultado("sc_toupper", c[0], chr(sc_toupper(codigo)))
            elif op == "7": resultado("sc_tolower", c[0], chr(sc_tolower(codigo)))
            pausar()
        elif op == "8":
            s = pedir("Digite uma string (ex: '  -42abc')")
            resultado("sc_atoi", repr(s), sc_atoi(s))
            pausar()
        else:
            print("  Opção inválida.")
            pausar()


# ══════════════════════════════════════════════════════════════════════════
# MENU 2 — Manipulação de Memória
# ══════════════════════════════════════════════════════════════════════════

def menu_memory():
    while True:
        limpar()
        titulo("2. Manipulação de Memória")
        print("""
  [1] sc_memset  — preenche bytes com um valor
  [2] sc_bzero   — zera bytes
  [3] sc_memcpy  — copia bytes
  [4] sc_memmove — move bytes (seguro com sobreposição)
  [5] sc_memchr  — procura byte
  [6] sc_memcmp  — compara bytes
  [0] Voltar
        """)
        op = pedir("Escolha")

        if op == "0":
            break
        elif op == "1":
            texto = pedir("Digite um texto para o buffer (ex: 'HELLO')")
            val   = pedir("Valor do byte a preencher (0-255)")
            n     = pedir("Quantos bytes preencher")
            buf = bytearray(texto.encode())
            sc_memset(buf, int(val), int(n))
            resultado("sc_memset", f"buf={texto!r}, c={val}, n={n}", buf)
            pausar()
        elif op == "2":
            texto = pedir("Digite um texto para o buffer (ex: 'HELLO')")
            n     = pedir("Quantos bytes zerar")
            buf = bytearray(texto.encode())
            sc_bzero(buf, int(n))
            resultado("sc_bzero", f"buf={texto!r}, n={n}", buf)
            pausar()
        elif op == "3":
            src_txt = pedir("Digite o texto fonte (src)")
            n       = pedir("Quantos bytes copiar")
            src = bytearray(src_txt.encode())
            dst = bytearray(len(src))
            sc_memcpy(dst, src, int(n))
            resultado("sc_memcpy", f"src={src_txt!r}, n={n}", dst)
            pausar()
        elif op == "4":
            src_txt = pedir("Digite o texto fonte (src)")
            n       = pedir("Quantos bytes mover")
            src = bytearray(src_txt.encode())
            dst = bytearray(len(src))
            sc_memmove(dst, src, int(n))
            resultado("sc_memmove", f"src={src_txt!r}, n={n}", dst)
            pausar()
        elif op == "5":
            texto = pedir("Digite um texto para o buffer")
            c     = pedir("Caractere a procurar")
            n     = pedir("Quantos bytes pesquisar")
            buf = bytearray(texto.encode())
            idx = sc_memchr(buf, ord(c[0]), int(n))
            resultado("sc_memchr", f"buf={texto!r}, c={c[0]!r}, n={n}",
                      f"índice={idx}" if idx is not None else "Não encontrado")
            pausar()
        elif op == "6":
            t1 = pedir("Primeiro texto")
            t2 = pedir("Segundo texto")
            n  = pedir("Quantos bytes comparar")
            a = bytearray(t1.encode())
            b = bytearray(t2.encode())
            r = sc_memcmp(a, b, int(n))
            resultado("sc_memcmp", f"{t1!r} vs {t2!r}, n={n}",
                      f"{r}  ({'iguais' if r==0 else ('1º maior' if r>0 else '2º maior')})")
            pausar()
        else:
            print("  Opção inválida.")
            pausar()


# ══════════════════════════════════════════════════════════════════════════
# MENU 3 — Manipulação de Strings
# ══════════════════════════════════════════════════════════════════════════

def menu_string():
    while True:
        limpar()
        titulo("3. Manipulação de Strings")
        print("""
  [1] sc_strlen   — tamanho da string
  [2] sc_strchr   — primeira ocorrência de char
  [3] sc_strrchr  — última ocorrência de char
  [4] sc_strncmp  — compara n caracteres
  [5] sc_strnstr  — procura substring
  [6] sc_strdup   — duplica string
  [7] sc_strlcpy  — copia com limite
  [8] sc_strlcat  — concatena com limite
  [0] Voltar
        """)
        op = pedir("Escolha")

        if op == "0":
            break
        elif op == "1":
            s = pedir("Digite uma string")
            resultado("sc_strlen", repr(s), sc_strlen(s))
            pausar()
        elif op == "2":
            s = pedir("Digite uma string")
            c = pedir("Caractere a procurar")
            idx = sc_strchr(s, ord(c[0]))
            resultado("sc_strchr", f"{s!r}, {c[0]!r}",
                      f"índice={idx}" if idx != -1 else "Não encontrado")
            pausar()
        elif op == "3":
            s = pedir("Digite uma string")
            c = pedir("Caractere a procurar")
            idx = sc_strrchr(s, ord(c[0]))
            resultado("sc_strrchr", f"{s!r}, {c[0]!r}",
                      f"índice={idx}" if idx != -1 else "Não encontrado")
            pausar()
        elif op == "4":
            s1 = pedir("Primeira string")
            s2 = pedir("Segunda string")
            n  = pedir("Quantos caracteres comparar")
            r  = sc_strncmp(s1, s2, int(n))
            resultado("sc_strncmp", f"{s1!r} vs {s2!r}, n={n}",
                      f"{r}  ({'iguais' if r==0 else ('1ª maior' if r>0 else '2ª maior')})")
            pausar()
        elif op == "5":
            h = pedir("String onde procurar (haystack)")
            n = pedir("Quantos chars de haystack considerar")
            nd = pedir("String a encontrar (needle)")
            idx = sc_strnstr(h, nd, int(n))
            resultado("sc_strnstr", f"{h!r}, needle={nd!r}, n={n}",
                      f"índice={idx}" if idx != -1 else "Não encontrado")
            pausar()
        elif op == "6":
            s = pedir("Digite uma string")
            r = sc_strdup(s)
            resultado("sc_strdup", repr(s), repr(r))
            pausar()
        elif op == "7":
            s    = pedir("String fonte (src)")
            size = pedir("Tamanho máximo do buffer (size)")
            dst  = [""]
            ret  = sc_strlcpy(dst, s, int(size))
            resultado("sc_strlcpy", f"src={s!r}, size={size}",
                      f"dst={dst[0]!r}  |  retorno={ret}")
            pausar()
        elif op == "8":
            d    = pedir("String destino (dst)")
            s    = pedir("String a concatenar (src)")
            size = pedir("Tamanho máximo total (size)")
            dst  = [d]
            ret  = sc_strlcat(dst, s, int(size))
            resultado("sc_strlcat", f"dst={d!r}, src={s!r}, size={size}",
                      f"dst={dst[0]!r}  |  retorno={ret}")
            pausar()
        else:
            print("  Opção inválida.")
            pausar()


# ══════════════════════════════════════════════════════════════════════════
# MENU 4 — Funções Adicionais
# ══════════════════════════════════════════════════════════════════════════

def menu_extra():
    while True:
        limpar()
        titulo("4. Funções Adicionais")
        print("""
  [1]  sc_calloc      — aloca memória zerada
  [2]  sc_substr      — extrai substring
  [3]  sc_strjoin     — junta duas strings
  [4]  sc_strtrim     — remove chars das extremidades
  [5]  sc_split       — divide string por delimitador
  [6]  sc_itoa        — inteiro para string
  [7]  sc_strmapi     — aplica função a cada char (com índice)
  [8]  sc_striteri    — itera imprimindo cada char com índice
  [9]  sc_putchar_fd  — escreve char no stdout
  [10] sc_putstr_fd   — escreve string no stdout
  [11] sc_putendl_fd  — escreve string + newline no stdout
  [12] sc_putnbr_fd   — escreve número no stdout
  [0]  Voltar
        """)
        op = pedir("Escolha")

        if op == "0":
            break
        elif op == "1":
            count = pedir("Número de elementos (count)")
            size  = pedir("Tamanho de cada elemento (size)")
            r = sc_calloc(int(count), int(size))
            resultado("sc_calloc", f"count={count}, size={size}", r)
            pausar()
        elif op == "2":
            s      = pedir("String original")
            start  = pedir("Índice de início")
            length = pedir("Comprimento da substring")
            resultado("sc_substr", f"{s!r}, start={start}, len={length}",
                      repr(sc_substr(s, int(start), int(length))))
            pausar()
        elif op == "3":
            s1 = pedir("Primeira string")
            s2 = pedir("Segunda string")
            resultado("sc_strjoin", f"{s1!r} + {s2!r}",
                      repr(sc_strjoin(s1, s2)))
            pausar()
        elif op == "4":
            s  = pedir("String a processar")
            ch = pedir("Charset (chars a remover das extremidades)")
            resultado("sc_strtrim", f"{s!r}, charset={ch!r}",
                      repr(sc_strtrim(s, ch)))
            pausar()
        elif op == "5":
            s   = pedir("String a dividir")
            sep = pedir("Delimitador")
            resultado("sc_split", f"{s!r}, delim={sep!r}",
                      sc_split(s, sep))
            pausar()
        elif op == "6":
            n = pedir("Digite um número inteiro")
            resultado("sc_itoa", n, repr(sc_itoa(int(n))))
            pausar()
        elif op == "7":
            s = pedir("Digite uma string")
            print(f"\n  Aplicando: maiúscula se índice par, minúscula se ímpar")
            r = sc_strmapi(s, lambda i, c: c.upper() if i % 2 == 0 else c.lower())
            resultado("sc_strmapi", repr(s), repr(r))
            pausar()
        elif op == "8":
            s = pedir("Digite uma string")
            print("\n  Resultado (índice: char):")
            sc_striteri(s, lambda i, c: print(f"    [{i}] = {c!r}"))
            pausar()
        elif op == "9":
            c = pedir("Digite um caractere")
            print("\n  sc_putchar_fd → ", end="")
            sc_putchar_fd(c[0], sys.stdout)
            print()
            pausar()
        elif op == "10":
            s = pedir("Digite uma string")
            print("\n  sc_putstr_fd → ", end="")
            sc_putstr_fd(s, sys.stdout)
            print()
            pausar()
        elif op == "11":
            s = pedir("Digite uma string")
            print("\n  sc_putendl_fd → ", end="")
            sc_putendl_fd(s, sys.stdout)
            pausar()
        elif op == "12":
            n = pedir("Digite um número inteiro")
            print("\n  sc_putnbr_fd → ", end="")
            sc_putnbr_fd(int(n), sys.stdout)
            print()
            pausar()
        else:
            print("  Opção inválida.")
            pausar()


# ══════════════════════════════════════════════════════════════════════════
# MENU 5 — Lista Ligada
# ══════════════════════════════════════════════════════════════════════════

lista_global = [None]

def imprimir_lista():
    if lista_global[0] is None:
        print("  Lista: (vazia)")
        return
    elementos = []
    atual = lista_global[0]
    while atual:
        elementos.append(str(atual.content))
        atual = atual.next
    print("  Lista: [ " + " → ".join(elementos) + " ]")
    print(f"  Tamanho: {sc_lstsize(lista_global[0])}")

def menu_list():
    while True:
        limpar()
        titulo("5. Lista Ligada")
        imprimir_lista()
        print("""
  [1] sc_lstnew       — criar nó
  [2] sc_lstadd_front — adicionar no início
  [3] sc_lstadd_back  — adicionar no fim
  [4] sc_lstsize      — tamanho da lista
  [5] sc_lstlast      — último elemento
  [6] sc_lstiter      — iterar (imprimir cada elemento)
  [7] sc_lstmap       — mapear (multiplicar por 2)
  [8] sc_lstdelone    — apagar primeiro nó
  [9] sc_lstclear     — limpar toda a lista
  [0] Voltar
        """)
        op = pedir("Escolha")

        if op == "0":
            break
        elif op == "1":
            val = pedir("Valor do novo nó")
            no = sc_lstnew(val)
            print(f"\n  Nó criado → content={no.content!r}, next={no.next}")
            pausar()
        elif op == "2":
            val = pedir("Valor a inserir no INÍCIO")
            sc_lstadd_front(lista_global, sc_lstnew(val))
            print("\n  Adicionado no início!")
            imprimir_lista()
            pausar()
        elif op == "3":
            val = pedir("Valor a inserir no FIM")
            sc_lstadd_back(lista_global, sc_lstnew(val))
            print("\n  Adicionado no fim!")
            imprimir_lista()
            pausar()
        elif op == "4":
            resultado("sc_lstsize", "lista atual", sc_lstsize(lista_global[0]))
            pausar()
        elif op == "5":
            last = sc_lstlast(lista_global[0])
            resultado("sc_lstlast", "lista atual",
                      f"content={last.content!r}" if last else "None")
            pausar()
        elif op == "6":
            print("\n  sc_lstiter → conteúdo de cada nó:")
            sc_lstiter(lista_global[0], lambda c: print(f"    → {c!r}"))
            pausar()
        elif op == "7":
            try:
                nova = sc_lstmap(lista_global[0],
                                 lambda c: str(int(c) * 2),
                                 lambda c: None)
                print("\n  sc_lstmap (×2) → nova lista:")
                sc_lstiter(nova, lambda c: print(f"    → {c!r}"))
            except ValueError:
                print("\n  Os valores da lista precisam ser números inteiros para este mapa.")
            pausar()
        elif op == "8":
            if lista_global[0] is None:
                print("\n  Lista já está vazia.")
            else:
                removido = lista_global[0].content
                sc_lstdelone(lista_global[0], lambda c: None)
                lista_global[0] = lista_global[0].next if lista_global[0] else None
                print(f"\n  Primeiro nó removido → era {removido!r}")
                imprimir_lista()
            pausar()
        elif op == "9":
            sc_lstclear(lista_global, lambda c: None)
            print("\n  Lista limpa com sucesso!")
            pausar()
        else:
            print("  Opção inválida.")
            pausar()


# ══════════════════════════════════════════════════════════════════════════
# MENU PRINCIPAL
# ══════════════════════════════════════════════════════════════════════════

def menu_principal():
    while True:
        limpar()
        print("""
╔══════════════════════════════════════════════════╗
║         LibC Python — Testador Interativo        ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║   [1]  Classificação e Conversão de Caracteres   ║
║   [2]  Manipulação de Memória                    ║
║   [3]  Manipulação de Strings                    ║
║   [4]  Funções Adicionais                        ║
║   [5]  Lista Ligada (Bônus)                      ║
║                                                  ║
║   [0]  Sair                                      ║
║                                                  ║
╚══════════════════════════════════════════════════╝
        """)
        op = pedir("Escolha uma opção")

        if   op == "1": menu_char()
        elif op == "2": menu_memory()
        elif op == "3": menu_string()
        elif op == "4": menu_extra()
        elif op == "5": menu_list()
        elif op == "0":
            limpar()
            print("\n  Até logo! 👋\n")
            break
        else:
            print("  Opção inválida.")
            pausar()

if __name__ == "__main__":
    menu_principal()
