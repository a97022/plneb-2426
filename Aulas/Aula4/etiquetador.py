import re
import json

file = open("../../data/livro.txt", encoding="utf8")
texto = file.read()
file.close()

file_conceitos = open("conceitos.json",encoding="utf8")
conceitos = json.load(file_conceitos)
file_conceitos.close()

black_list = ["de","e","os","para"]

def gera_termo_bold(matched):
    text = matched.group(0)
    #print(text)
    if text in conceitos and text not in black_list:
        return f'<a href="../Aula3/dicionario_medico.html#@{text}" target= "_blank" title="{conceitos[text]}">{text}</a>'
    else:
        return text

texto = re.sub(r"\n", "<br/>",texto)
texto = re.sub(r"\f", "<hr/>", texto)
texto = re.sub(r"\b(\w+)\b",gera_termo_bold,texto)

file_html = open("livro.html","w",encoding="utf8")
file_html.write(texto)
file.close()

