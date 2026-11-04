# Guia de Matrículas São Luís

Protótipo de guia para localizar creches e escolas da rede municipal de São Luís (MA), inspirado nos Guias de Creches e de Escolas do GLOBO. A inscrição continua no site da SEMED; o guia só ajuda a encontrar a unidade.

## Conteúdo

| Caminho | O que é |
| --- | --- |
| `index.html` | Página única (abre direto no navegador, sem servidor). Gerada por `scripts/build.py`. |
| `src/template.html` | Código-fonte da página, sem os dados. |
| `dados/escolas_semed_2022.csv` | 254 unidades transcritas do PDF oficial da SEMED (01/11/2022). Separador `;`. |
| `dados/bairros_geo.txt` | Coordenadas de 98 bairros (OpenStreetMap/Nominatim, consulta de 04/11/2026). |
| `dados/escolas.json` | Base final: CSV + coordenadas, com o campo `prec` (`bairro` ou `nucleo`). |
| `scripts/build.py` | Junta tudo e gera `escolas.json` e `index.html`. |
| `PUBLICAR.md` | Passo a passo para colocar o guia no ar. |

## Como atualizar

1. Troque `dados/escolas_semed_2022.csv` pela relação atual da SEMED, mantendo as colunas `N;Núcleo;Modalidade;Escola;Bairro;Endereço`.
2. Se aparecer bairro novo, acrescente uma linha em `dados/bairros_geo.txt` (`Bairro=lat,lon`).
3. Rode `python3 -I scripts/build.py` na pasta do projeto e abra `index.html`.

## Limites conhecidos

- A lista da SEMED é de 2022. Unidades abertas ou fechadas depois não estão nela. Pedir a relação atual à SEMED é o primeiro passo antes de divulgar.
- A posição no mapa vem do centro do bairro, não do endereço. Sete unidades (bairros Maiobinha, Taim, Iguaraú, Tajaçoaba e Angelim Velho) não foram localizadas e aparecem na média do núcleo.
- O mapa usa Leaflet com o mapa-base do OpenStreetMap e precisa de internet. Cada unidade tem o botão "Abrir no Google Maps", que abre a busca pelo nome e endereço.
- O PDF numera de 1 a 256 e pula os números 82 e 154; não se sabe se faltam unidades.
- Não use os PDFs de resultado de transferências da página Matrícula 2026: contêm nomes de alunos menores (LGPD).

## Fontes

- Lista de escolas municipais (PDF, SEMED): https://www.saoluis.ma.gov.br/arquivos/4596_lista_de_escolas_municipais_de_sao_luis_31114747.pdf
- Página de inscrição: https://www.saoluis.ma.gov.br/matricula-2026 (telefone (98) 9138-8210)
- Modelo de referência: https://oglobo.globo.com/brasil/noticia/2026/11/04/vai-matricular-seu-filho-em-2027-guia-do-globo-ajuda-a-encontrar-escola-e-creche-ideais.ghtml
