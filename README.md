# Widget do tempo

Widget de previsão do tempo a 5 dias para o ambiente de trabalho do Windows (Prior Velho).

- Previsão: Open-Meteo; observação real: aeroporto de Lisboa (METAR); AccuWeather opcional.
- Destaque amarelo no melhor dia para secar roupa (evapotranspiração FAO-56).
- Clicar num dia mostra o detalhe de 4 em 4 horas.

## Atualização automática

Cada computador corre `widget_tempo.pyw` com o Python. Ao arrancar e de 6 em 6 horas, o widget lê
`versao.json` deste repositório. Se houver versão mais recente, descarrega-a, confirma o tamanho,
o SHA-256, que o código é válido e que a versão bate certo, guarda a anterior como
`widget_tempo_anterior.pyw` e reinicia.

## Publicar uma versão nova

1. Aumentar `VERSAO_PROGRAMA` em `widget_tempo.pyw` (formato `ano.mês.dia.número`).
2. `python ferramentas/publicar.py widget_tempo.pyw versao.json`
3. Fazer commit e push dos dois ficheiros para `main`.
