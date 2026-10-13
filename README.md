#  Controle de Níveis de Água

Projeto  simula um sistema simples de monitoramento visual do nível de água de um reservatório via terminal.

##  Descrição do Projeto

O sistema monitora cinco níveis do reservatório e exibe mensagens de alerta com cores progressivas de risco no terminal, utilizando a biblioteca **Colorama**.

## Tabela de Níveis e Cores

  Nível       Situação                    Cor do Terminal 

**Nível 1**   Muito baixo (crítico)       Vermelho 
**Nível 2**   baixo                       Amarelo 
**Nível 3**   Médio                       Verde 
**Nível 4**   Alto                        Ciano 
**Nível 5**   Muito alto (alerta)         Azul 

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Biblioteca Colorama** (`Fore`, `Style`)

## Como Executar o Projeto

1. Certifique-se de que tem o **Python** instalado na sua máquina.
2. Instale a biblioteca `colorama` executando no terminal:
   pip install colorama