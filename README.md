# Projeto LibC - AV2 IA Noite

## Sobre o Projeto

Este projeto consiste na implementação, em Python, de uma biblioteca inspirada na LibC da linguagem C, desenvolvida como atividade prática da disciplina de Algoritmos e Estruturas de Dados.

O objetivo é reproduzir o comportamento de diversas funções clássicas da biblioteca padrão C, além de implementar funções adicionais de manipulação de strings, memória e listas ligadas, respeitando as restrições propostas na atividade.

---

## Aluno

Priscila Morais Câmara

---

## Linguagem Utilizada

- Python

---

## Objetivos da Atividade

- Compreender o funcionamento interno de funções clássicas da linguagem C.
- Desenvolver lógica de programação sem depender de métodos prontos.
- Exercitar manipulação de strings, memória e estruturas de dados.
- Produzir documentação técnica antes da implementação.
- Aplicar conceitos de boas práticas e versionamento utilizando Git e GitHub.

---

## Estrutura do Projeto

### Arquivos Principais

| Arquivo | Descrição |
|----------|-----------|
| sc_char.py | Funções de classificação e conversão de caracteres |
| sc_string.py | Funções de manipulação de strings |
| sc_memory.py | Funções de manipulação de memória |
| sc_extra.py | Funções adicionais propostas na atividade |
| sc_list.py | Implementação das funções de lista ligada |
| testes.py | Casos de teste para validação das funções |
| documentacao_funcoes.md | Documentação técnica das funções |
| README.md | Documentação geral do projeto |

---

## Funcionalidades Implementadas

### Classificação e Conversão

- sc_isalpha()
- sc_isdigit()
- sc_isalnum()
- sc_isascii()
- sc_isprint()
- sc_toupper()
- sc_tolower()
- sc_atoi()

### Manipulação de Memória

- sc_memset()
- sc_bzero()
- sc_memcpy()
- sc_memmove()
- sc_memchr()
- sc_memcmp()

### Manipulação de Strings

- sc_strlen()
- sc_strlcpy()
- sc_strlcat()
- sc_strchr()
- sc_strrchr()
- sc_strncmp()
- sc_strnstr()
- sc_strdup()

### Alocação Dinâmica

- sc_calloc()

### Funções Adicionais

- sc_substr()
- sc_strjoin()
- sc_strtrim()
- sc_split()
- sc_itoa()
- sc_strmapi()
- sc_striteri()
- sc_putchar_fd()
- sc_putstr_fd()
- sc_putendl_fd()
- sc_putnbr_fd()

### Listas Ligadas

- sc_lstnew()
- sc_lstadd_front()
- sc_lstsize()
- sc_lstlast()
- sc_lstadd_back()
- sc_lstdelone()
- sc_lstclear()
- sc_lstiter()
- sc_lstmap()

---

## Restrições do Projeto

Conforme especificado na atividade:

- Não utilizar métodos prontos equivalentes às funções implementadas.
- Não utilizar:
  - .split()
  - .strip()
  - .lstrip()
  - .rstrip()

O objetivo é implementar a lógica manualmente para compreender o funcionamento interno dessas operações.

---

## Como Executar

### Executar os testes

```bash
python testes.py
```

### Executar o programa principal

```bash
python main.py
```

---

## Exemplo de Utilização

```python
from sc_string import sc_strlen

texto = "LibC Python"

resultado = sc_strlen(texto)

print(resultado)
```

Saída:

```text
11
```

---

## Versionamento

O projeto está versionado utilizando Git e hospedado no GitHub para controle de alterações e compartilhamento do código.

---

## Considerações Finais

Este projeto foi desenvolvido com foco no aprendizado dos conceitos fundamentais de manipulação de caracteres, strings, memória e estruturas de dados, reproduzindo funcionalidades clássicas da biblioteca padrão C utilizando Python.
