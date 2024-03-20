           IDENTIFICATION DIVISION.  -- Esta é a primeira divisão de um programa COBOL. Ela contém informações de identificação sobre o programa.
           PROGRAM-ID. Exemplo.     -- Define o nome do programa.

           DATA DIVISION.           -- Esta é a divisão onde todas as variáveis são declaradas.
           WORKING-STORAGE SECTION. -- Esta é a seção onde as variáveis que não são passadas entre programas são declaradas.
           01 Variavel-Numerica PIC 9(5) VALUE 12345. -- Declara uma variável numérica com 5 dígitos, inicializada com 12345.
           01 Variavel-Texto PIC X(10) VALUE 'Exemplo'. -- Declara uma variável de texto com 10 caracteres, inicializada com 'Exemplo'.
           01 Contador PIC 99 VALUE 1. -- Declara uma variável numérica com 2 dígitos, inicializada com 1.

           PROCEDURE DIVISION.      -- Esta é a divisão onde o código real é escrito.
           Inicio.                  -- Este é o ponto de entrada do programa.
               DISPLAY 'Variável Numérica: ' Variavel-Numerica. -- Exibe o valor da variável numérica.
               DISPLAY 'Variável Texto: ' Variavel-Texto. -- Exibe o valor da variável de texto.
               PERFORM Exemplo-Loop. -- Chama o procedimento Exemplo-Loop.
               IF Variavel-Numerica > 10000 THEN -- Verifica se a variável numérica é maior que 10000.
                   DISPLAY 'Variável Numérica é maior que 10000'. -- Se for, exibe esta mensagem.
               END-IF. -- Fim da instrução IF.
               STOP RUN. -- Termina a execução do programa.

           Exemplo-Loop. -- Este é o procedimento Exemplo-Loop.
               PERFORM UNTIL Contador > 5 -- Executa o bloco de código até que a variável Contador seja maior que 5.
                   DISPLAY 'Loop: ' Contador -- Exibe o valor atual do Contador.
                   ADD 1 TO Contador -- Incrementa o valor do Contador em 1.
               END-PERFORM. -- Fim do procedimento PERFORM.