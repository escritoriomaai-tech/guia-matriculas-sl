# Como colocar o guia no ar

O site é um único arquivo `index.html`, gerado por `python3 -I scripts/build.py`. Rode o script sempre que atualizar os dados.

## Opção 1: GitHub Pages (usada neste repositório)

1. Em Settings > Pages, escolha Source: GitHub Actions. O fluxo em `.github/workflows/pages.yml` roda o `build.py` e publica o resultado a cada alteração na branch `main`.
2. O site fica em `https://escritoriomaai-tech.github.io/guia-matriculas-sl/`.

## Opção 2: Netlify Drop (sem conta técnica)

1. Rode o `build.py` no seu computador.
2. Abra https://app.netlify.com/drop e arraste uma pasta contendo só o `index.html`.
3. Troque o nome em Site settings > Change site name.

## Domínio próprio (opcional)

É possível apontar um subdomínio, como `matriculas.escritorio.ma.ai`, nas configurações do serviço, criando o registro CNAME indicado no seu provedor de DNS.

## Antes de divulgar

- Pedir à SEMED a relação atual de unidades e atualizar `dados/escolas_semed_2022.csv`.
- Conferir pelo menos uma unidade por núcleo no mapa.
- Manter o aviso de que a inscrição é feita no site da Prefeitura e de que o guia é independente.
