# Documento de Decisões Técnicas (DECISIONS.md)

Este arquivo documenta as principais decisões técnicas e de arquitetura tomadas durante o desenvolvimento do projeto de Monitoramento de Percepção Pública sobre IA no Piauí.

## 1. Escolha da Abordagem para Análise de Sentimento

**> Pergunta: Por que você escolheu a abordagem de regras para análise de sentimento (em vez de um modelo de ML)?** 

A decisão de utilizar uma abordagem baseada em regras (léxicos) para a análise de sentimento foi tomada com base nos seguintes fatores:

* **Simplicidade e Rapidez de Implementação:** A abordagem de regras é direta e rápida de implementar, não exigindo etapas complexas como coleta de dados, treinamento e validação de um modelo de Machine Learning.

* **Interpretabilidade (Transparência):** O resultado da classificação é 100% transparente. É fácil entender por que uma notícia foi classificada como "Positiva" ou "Negativa", bastando verificar as palavras-chave presentes no texto.Isso está alinhado com o princípio de transparência em IA.

* **Ausência de Dados de Treino:** Modelos de Machine Learning supervisionados necessitam de um conjunto de dados previamente rotulado para treinamento. Como tal conjunto de dados não foi fornecido, a abordagem de regras se tornou a mais viável.

* **Adequação ao Escopo do Projeto:** O objetivo do case era criar um "painel simplificado" para monitoramento. Um sistema complexo de ML seria excessivo para o escopo e o tempo de desenvolvimento de um protótipo.

## 2. Tratamento de Erros e Casos Inesperados

**> Pergunta: Como você lidou com possíveis erros ou falta de notícias no feed RSS?** 

O tratamento de erros foi realizado pensando na ausência de informações recebidas do feed RSS, erro durante a leitura das informações em XML:

* **Erros de Requisição HTTP:** A coleta de dados foi encapsulada em um bloco `try...except`. Erros de conexão, timeouts ou respostas de erro do servidor (como 404 ou 503) são capturados. Em caso de falha, o programa exibe uma mensagem de erro no console e retorna uma lista vazia, evitando que a aplicação quebre.

* **Erros de Análise de XML (Parsing):** Foi implementado um tratamento de exceção para `xml.etree.ElementTree.ParseError`. Isso lida com casos em que a resposta do servidor não é um XML válido (por exemplo, uma página de erro em HTML), o que também impede a quebra da aplicação.

* **Falta de Notícias no Feed:** Se a requisição for bem-sucedida mas o feed RSS não contiver nenhuma notícia, a função de coleta retorna uma lista vazia. O dashboard Streamlit foi programado para lidar com essa situação, exibindo os títulos das seções, mas mostrando uma tabela vazia e gráficos sem dados, em vez de gerar um erro.

## 3. Outras Decisões Relevantes

* **Limpeza e Normalização de Texto:** Para a criação da nuvem de palavras e uma futura extensibilidade, foi decidido utilizar a biblioteca `unidecode` para remover acentos e normalizar o texto. Isso garante uma contagem de palavras mais precisa e consistente.

* **Escolha de Bibliotecas de Visualização:** Optei por usar `Plotly Express` para o gráfico de pizza devido à sua simplicidade e capacidade de gerar gráficos interativos com poucas linhas de código, melhorando a experiência do usuário no dashboard.

## 4. Uso da IA durante o desenvolvimento

* **Uso de IA na escrita do código:** Foi utilizada quando houve linhas de códigos repetitivas que a IA, implementada na IDE utlizada, automaticamente adiciona, mas havendo a revisão e entedimento do código escrito

* **Uso de IA no desenvolvimento do projeto:** Foi utilizada para revisar o código sua fucionalidade, por exemplo, para esclarecer a maior quantidade de erros que poderiam ocorrer na requisição do feed RSS. Assim apliando o tratamento de erros.