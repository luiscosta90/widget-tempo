"""Gera o versao.json (versão, tamanho e SHA-256) para publicar uma versão nova do widget."""
import hashlib, json, re, sys
caminho_widget, caminho_manifesto = sys.argv[1], sys.argv[2]
conteudo = open(caminho_widget, "rb").read()
versao = re.search(r'VERSAO_PROGRAMA = "([\d.]+)"', conteudo.decode("utf-8")).group(1)
compile(conteudo.decode("utf-8"), "widget_tempo.pyw", "exec")
manifesto = {"versao": versao, "ficheiro": "widget_tempo.pyw", "tamanho": len(conteudo),
             "sha256": hashlib.sha256(conteudo).hexdigest()}
json.dump(manifesto, open(caminho_manifesto, "w"), indent=2)
print(manifesto)
