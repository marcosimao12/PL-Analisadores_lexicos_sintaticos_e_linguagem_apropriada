Com este projeto pretende-se que os alunos da UC de Processamento de Linguagens adquiram experiencia na definicao de analisadores lexicos e sintaticos, bem como na definicao de acoes semanticas que traduzem as linguagens implementadas.
O processo para a realizacao deste trabalho pratico devera passar pelas seguintes fases:
  1. especificar a gramatica concreta da linguagem de entrada;
  2. construir um reconhecedor lexico (recorrendo a biblioteca lex) para reconhecer
os sımbolos terminais identificados na gramatica, e testar esse reconhecedor com
alguns exemplos de palavras da linguagem de entrada.
  3. construir um reconhecedor sintatico (recorrendo a biblioteca yacc) para reconhecer
a gramatica concreta, e testar esse reconhecedor com alguns exemplos frases da
linguagem de entrada.
  4. planear uma arvore de sintaxe abstrata para representar a linguagem de entrada,
e associar acoes semanticas de tradu¸cao as produ¸coes da gramatica de forma a
construir a correspondente arvore de sintaxe abstrata.
  5. desenvolver o gerador de codigo que produza a resposta solicitada, atraves da
avalia¸cao da arvore de sintaxe abstrata.
