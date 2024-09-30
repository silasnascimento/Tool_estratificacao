# Ferramenta Automatizada de Análise Espacial de Propriedades Rurais

Este repositório contém um script Python embutido em uma ferramenta `.atbx` do ArcGIS Pro, que automatiza a análise espacial de propriedades rurais. A ferramenta realiza uma série de operações de recorte, fusão e cálculos em camadas de dados geográficos para identificar e classificar áreas dentro e fora de Áreas de Preservação Permanente (APP) e outras zonas de interesse, como a RPA (Remapeamento de Áreas Prioritárias).

## Funcionalidades

A ferramenta é projetada para:
- **Recortar** camadas geográficas de interesse com base nos limites de uma propriedade rural.
- **Analisar** a sobreposição de feições com Áreas de Preservação Permanente (APP).
- **Classificar** as áreas dentro e fora de APP.
- **Gerar** resultados analíticos integrados que ajudam na identificação de áreas dentro e fora de zonas de interesse específicas.
- **Otimizar** o processo de análise espacial, eliminando a necessidade de procedimentos manuais.

## Fluxo de Operações

1. **Recorte (Clip):** Recorte da camada de base de edição com os limites da propriedade rural.
2. **Análise de APP:** Recorte da camada APP e classificação das áreas como "dentro de APP" ou "fora de APP".
3. **Fusão e Apêndice (Merge e Append):** Mescla as feições classificadas para gerar uma camada de análise final.
4. **Remapeamento (RPA):** Recorte da camada RPA e categorização das áreas dentro e fora da APP.
5. **Geração de Relatórios:** Atualiza campos com informações relevantes para a análise, como nome da propriedade e classificação das áreas.

## Requisitos

- **ArcGIS Pro**: Esta ferramenta foi desenvolvida para ser utilizada dentro do ArcGIS Pro.
- **Extensão de Análise Espacial**: Certifique-se de que a extensão de Análise Espacial está habilitada para usar funcionalidades como `Clip`, `Erase` e `Append`.
- **Python 3.x**: O script utiliza a API do ArcPy, que é integrada ao ArcGIS Pro.

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. **Carregue a ferramenta no ArcGIS Pro**:
   - Abra o ArcGIS Pro.
   - Vá até a aba **Análise** e clique em **Gerenciador de Ferramentas**.
   - Importe o arquivo `.atbx` da ferramenta para usá-la no seu projeto.

## Parâmetros de Entrada

A ferramenta requer os seguintes parâmetros de entrada:

1. **Nome da Propriedade**: O nome da propriedade rural em análise.
2. **Camada da Propriedade**: A camada que contém os limites da propriedade.
3. **Camada de Base de Edição**: A camada que será recortada com base nos limites da propriedade.
4. **Camada de APP**: A camada contendo as Áreas de Preservação Permanente (APP).
5. **Camada de Referência RPA**: A camada de Remapeamento de Áreas Prioritárias (RPA).
6. **Diretório de Saída**: O caminho para salvar os resultados gerados.

## Saídas

A ferramenta gera uma série de arquivos shapefile ou geodatabase no diretório de saída especificado, incluindo:
- Camadas de base recortadas pela propriedade.
- Áreas classificadas como dentro ou fora de APP.
- Camadas de análise final com fusão de todas as áreas processadas.

## Contato

Para dúvidas ou sugestões, entre em contato:

- **Nome**: Silas Olivrira
- **E-mail**: silas@setmapgeo.com
- **LinkedIn**: https://www.linkedin.com/in/silas-oliveira-41a633186/
