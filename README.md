# Vaqueiro Survivors

Relatório de desenvolvimento do jogo Vaqueiro Survivors feito para a disciplina de Introdução a Programação do curso de Engenharia da Computação do CIn/UFPE.

## Integrantes do Grupo

- Arthur Henrique dos Santos Silva
- Lucas José Duarte Cavalcanti
- Pedro Henrique de Andrade Cavalcanti
- Theo William da Rocha Ferreira
- Thiago Tenório de Albuquerque

## Descrição do Jogo

Vaqueiro Survivors é um jogo no qual o Zé Vaqueiro enfrenta um apocalipse de vacas zumbi no Nordeste, e para sair vivo dessa vaqueijada, ele usa sua pistola lendária com balas de microfone e tenta desviar da maior quantidade possível de vacas zumbi. Nessa jornada ele coleta recompensas e aumenta de nível conforme acerta suas microfonadas.

## Arquitetura do Projeto

 Como os códigos foram organizados

### Diretórios

```text
animation/
├── left/
   ├── 0.png
   ├── 1.png
   ├── 2.png
   ├── 3.png
├── right/
   ├── 0.png
   ├── 1.png
   ├── 2.png
   ├── 3.png
```

```text
backgrounds/
├── 1.png
├── 2.png
├── map.png
├── mapa.png
```

```text
coin/
├── 0.png
├── 1.png
├── 2.png
├── 3.png
```

```text
coracao/
├── 0.png
├── 1.png
├── 2.png
├── 3.png
```

```text
fontes/
├── Oxanium-Bold.ttf
├── PressStart2P.ttf
```

```text
inimigo/
├── 0.png
├── 1.png
├── 2.png
├── 3.png
```

```text
screenshots/
├── tela final.png
├── tela gameplay.png
├── tela inicial.png
```

```text
sprites/
├── arma.png
├── gun.png
├── mic.png
├── terrorist.png
```

```text
xp/
├── 0.png
├── 1.png
├── 2.png
├── 3.png
```

### Arquivos

'''text
Main.py
groups.py
personagem.py
settings.py
sprites.py
'''

## Capturas de Tela

<img src="./screenshots/tela inicial.png" width="2000px">
<img src="./screenshots/tela gameplay.png" width="2000px">
<img src="./screenshots/tela final.png" width="2000px">

## Bibliotecas Utilizadas

```bash
pygame==2.6.0
```
```bash
pygame-ce
```
```bash
random
```
```bash
math
```

## Divisão do Trabalho no Grupo

| Time                                                  | Tarefas                                                                                                |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------                 |
| [Arthur Henrique](https://github.com/Alpalone/)       | Responsável pelo código base, desenvolvendo o movimento do player, dos inimigos e do mapa.             |
| [Lucas José](https://github.com/lucascavalcanti/)     | Desenvolveu a parte gráfica do jogo, criando os sprites do jogador, dos coletáveis e dos inimigos.     |
| [Pedro Cavalcanti](https://github.com/Cavuca5529/)    | Responsável pelo desenvolvimento das mecânicas dos coletáveis, das colisões e dos sprites.             |
| [Theo William](https://github.com//)                  | Desenvolveu o background e foi responsável pela organização do código com o uso de POO.                |
| [Thiago Tenório](https://github.com/Tenorio05/)       | Líder da equipe e responsável pelo repertório e pelos slides de apresentação do projeto.               |

## Conceitos Utilizados

Utilizamos os conceitos fundamentais, como estruturas de armazenamento (list, dict, etc.) e estruturas condicionais (if, else, while, for), assim como os princípios da Programação Orientada a Objetos (POO), os quais permitiram manter o código organizado e acessível.

Ademais, outro método essencial para o desenvolvimento do jogo foi o uso de funções, as quais contribuíram significativamente na criação de classes, estruturas que auxiliaram na organização do código e em uma melhor visibilidade.

## Desafios, Erros e Lições

Os principais desafios enfrentados pelo grupo foram a adaptação ao uso de bibliotecas e de sistemas de controle de versão (VCS), assim como a divisão de tarefas da equipe. Assim, pode-se afirmar que, além das hardskills, a principal lição que aprendemos durante o projeto foi o trabalho em equipe.
