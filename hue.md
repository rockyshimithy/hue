# Multiprocessamento

Um modelo que visa criar programas compatíveis com ambientes preparados para executar instruções de código simultâneamente. (Jan Palach)

Nos modelos antigos de computadores, essas máquinas possuiam uma única ULA (unidade lógica aritmética),  permitindo apenas uma instrução a ser executada por vez. A velocidade do processamento era medida em Hertz.

No que pode ajudar? Velocidade. O fato de poder executar mais de uma coisa ao mesmo tempo (não ser procedural),te faz "ganhar" tempo, ou executar o que precisa ser executado mais rápido.

# Paralelismo

Permite processar coisas de maneira simultânea no mesmo recurso. (um fogão de 6 bocas preparando 6 coisas). Executar tarefas simultâneamente (múltiplos computadores, processadores, ou núcleos).

# Concorrência

Múltiplas tarefas diferentes disputam o mesmo processo (recurso). Ou seja, o sistema processa um pouco de cada um e alterna entre as tarefas de maneira rápida (um cozinheiro preparando 6 pratos).

Importante lembrar que paralelismo e concorrência são coisas que andam juntos.

# Distribuição

N computadores trabalhando em conjunto e que se apresentam ao usuário como um único sistema.

K8S é um ótimo exemplo de distribuição para aplicações ou qualquer load balancer como haproxy.

# Pipeline/Decomposição

Inside em pegar um gargalo do processamento e decompor em tarefas menores

exemplos: bs-analyzer vai recuperar dados de order e orderitemconfig, distribuir em mensagens em uma fila,
que por sua vez será processada simultâneamente por outra tarefa responsável por capturar 
dados de orderitemsimple e quantidade, que por sua vez jogará em outra fila para capturar dados de item...
para depois então ser analisado quadra/trinca/trazer métricas e por fim calcular bottom up.

# O problema

Dado uma pagina de categoria, retornar o nome e preço de todos os produtos acessando as urls dos produtos.

# Processo

Em comparação com as threads, processos são completamente independentes do seu "programa". Ou seja, threads são linhas de execução dentro de um mesmo processo. Processos não compartilham nem mesmo memória com o processo pai.

# GIL (global interpreter lock)

É uma exclusão mútua, uma técnica usada em programação concorrente para evitar que duas threads tenham acesso simultaneamente a um recurso compartilhado.

# How unix works

https://neilkakkar.com/unix.html