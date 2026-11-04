"""Gera dados/escolas.json e index.html a partir do CSV da SEMED e das coordenadas por bairro.

Uso: python3 -I scripts/build.py   (a partir da pasta do projeto)
"""
import csv, json, pathlib, statistics

ROOT = pathlib.Path(__file__).resolve().parent.parent
ALIAS = {  # variações de grafia na lista da SEMED -> chave de coordenada
    "ANIL": "Anil", "COHAB": "Cohab Anil", "Cohab Anil I": "Cohab Anil",
    "Cohatrac I": "Cohatrac", "Vila Izabel": "Vila Isabel",
    "Gancharia – Anjo da Guarda": "Gancharia", "Matões/Turu": "Matões",
    "Pão de Açúcar/Anil": "Pão de Açúcar", "Vila Mauro Fecury I": "Vila Mauro Fecury",
}
# bairros que o serviço de mapas não localizou: usa a média do núcleo (aproximação maior)
SEM_COORD = {"Angelim Velho", "Iguaraú", "Maiobinha", "Taim", "Tajaçoaba"}


def chave(b):
    b = b.strip().rstrip(".").strip()
    return ALIAS.get(b, b)


geo = {}
for linha in (ROOT / "dados" / "bairros_geo.txt").read_text(encoding="utf-8").splitlines():
    nome, _, par = linha.partition("=")
    lat, lon = par.split(",")
    geo[nome] = (float(lat), float(lon))

linhas = list(csv.reader((ROOT / "dados" / "escolas_semed_2022.csv").open(encoding="utf-8"), delimiter=";"))[1:]
media_nucleo = {}
for r in linhas:
    c = chave(r[4])
    if c in geo:
        media_nucleo.setdefault(r[1], []).append(geo[c])
media_nucleo = {n: (statistics.mean(p[0] for p in v), statistics.mean(p[1] for p in v)) for n, v in media_nucleo.items()}

saida = []
for r in linhas:
    n, nucleo, mod, escola, bairro, end = r
    c = chave(bairro)
    if c in geo:
        lat, lon = geo[c]; precisao = "bairro"
    else:
        lat, lon = media_nucleo[nucleo]; precisao = "nucleo"
    saida.append({"n": int(n), "nucleo": nucleo, "mod": mod, "escola": escola, "bairro": bairro.strip().rstrip("."),
                  "end": end.strip(), "lat": round(lat, 5), "lon": round(lon, 5), "prec": precisao})

(ROOT / "dados" / "escolas.json").write_text(json.dumps(saida, ensure_ascii=False, indent=1), encoding="utf-8")
modelo = (ROOT / "src" / "template.html").read_text(encoding="utf-8")
(ROOT / "index.html").write_text(modelo.replace("/*DATA*/[]", json.dumps(saida, ensure_ascii=False, separators=(",", ":"))), encoding="utf-8")
print(len(saida), "unidades;", sum(1 for s in saida if s["prec"] == "nucleo"), "com posição pela média do núcleo")
