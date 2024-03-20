           IDENTIFICATION DIVISION. -- Início de seção.
           PROGRAM-ID. Exemplo. -- Nome do programa.

           DATA DIVISION. -- Início de seção.
           WORKING-STORAGE SECTION. -- Subseção de variáveis temporárias.
           01 Variavel-Numerica PIC 9(5) VALUE 12345.
           01 Variavel-Texto PIC X(10) VALUE 'Exemplo'.
           01 Contador PIC 99 VALUE 1.

           PROCEDURE DIVISION. -- Início de seção.
           Inicio -- Rótulo para o início do procedimento principal do programa.
               DISPLAY 'Variável Numérica: ' Variavel-Numerica. -- print.
               DISPLAY 'Variável Texto: ' Variavel-Texto.
               PERFORM Exemplo-Loop. -- Chamada de um procedimento.
               IF Variavel-Numerica > 10000 THEN -- Comparação lógica.
                   DISPLAY 'Variável Numérica é maior que 10000'.
               END-IF. -- Fim da comparação.
               STOP RUN. -- Finaliza a execução do programa (return 0).

           Exemplo-Loop. -- Procedimento (função).
               PERFORM UNTIL Contador > 5 -- loop (for).
                   DISPLAY 'Loop: ' Contador -- (print).
                   ADD 1 TO Contador -- Incrementa o valor da variável.
               END-PERFORM. -- Fim do loop.


