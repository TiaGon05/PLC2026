import re

def markdownToHtml(texto_markdown):
    texto_html = texto_markdown

    # Casos '#'
    texto_html = re.sub(r"^### (.*)$", r"<h3>\1</h3>", texto_html, flags=re.M)
    texto_html = re.sub(r"^## (.*)$", r"<h2>\1</h2>", texto_html, flags=re.M)
    texto_html = re.sub(r"^# (.*)$", r"<h1>\1</h1>", texto_html, flags=re.M)

    # Imagens antes de link
    texto_html = re.sub(r"!\[(.*?)\]\((.*?)\)", r'<img src="\2" alt="\1"/>', texto_html)
    texto_html = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2">\1</a>', texto_html)

    # Bold e Italico
    texto_html = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", texto_html)
    texto_html = re.sub(r"\*(.*?)\*", r"<i>\1</i>", texto_html)

    # Listas numeradas
    texto_html = re.sub(r"^\d+\.\s+(.*)$", r"<li>\1</li>", texto_html, flags=re.M) # transforma cada linha "1. texto" em "<li>texto</li>"
    texto_html = re.sub(r"((?:<li>.*?</li>\n?)+)", r"<ol>\n\1</ol>", texto_html) # agrupa blocos de <li> em <ol>

    return texto_html

with open("input.md", "r", encoding="utf-8") as f_in: # Abrir o ficheiro em modo r (leitura)
    conteudo_md = f_in.read()

conteudo_html = markdownToHtml(conteudo_md)

with open("output.html", "w", encoding="utf-8") as f_out:
    f_out.write(conteudo_html)

print("Ficheiro 'output.html' gerado.")