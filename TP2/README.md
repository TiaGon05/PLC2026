# Trabalho Prático 2

- **Autor:** Tiago Daniel Oliveira Leite
- **Identificador de aluno:** a112106
- **Foto:**
  
<img width="250" alt="PXL_20260923_134056275" src="https://github.com/user-attachments/assets/c4ee6e0d-8385-4ef8-96c0-024e2df2519b" /<

- **Resumo**
  O objetivo deste trabalho para casa foi criar um conversor de texto em formato Markdown para HTML recorrendo à biblioteca de expressões regulares re.
  Para a criação do conversor, a implementação seguiu a seguinte ordem de processamento:
  1. Cabeçalhos: Utilizando o padrão re.sub para identificar as linhas iniciadas por cardinais.
  2. Imagens e Links: As imagens foram processadas antes dos links para garantir que a sintaxe das mesmas não era incorretamente capturada pela regra dos hiperlinks.
     Usaram-se quantificadores não greedy para permitir varios links/imagens na mesma linha.
  3. Negrito e Itálico: A conversão do negrito foi executada antes do itálico para prevenir conflitos entre os delimitadores de asteriscos
  4. Listas numeradas: A conversão ocorreu em duas etapas: primeiro, cada item numerado foi convertido na respetiva tag de item (<li></li>). Os blocos de items
     consecutivos foram agrupados dentro das tags de lista ordenada (<ol></ol>)
  
