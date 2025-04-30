# Exercício 2: Arquiteturas de Dados Modernas

## Objetivo
Neste exercício, você irá analisar e comparar diferentes arquiteturas de dados modernas, compreendendo seus casos de uso, vantagens e desvantagens.

## Parte 1: Análise Comparativa (50 pontos)

Complete a tabela comparativa abaixo para as seguintes arquiteturas:
- Lambda Architecture
- Kappa Architecture
- Modern Data Stack
- Data Mesh

| Aspecto | Lambda | Kappa | Modern Data Stack | Data Mesh |
|---------|--------|-------|------------------|-----------|
| Complexidade de Implementação | | | | |
| Latência | | | | |
| Custo | | | | |
| Manutenibilidade | | | | |
| Escalabilidade | | | | |
| Casos de Uso Ideais | | | | |
| Principais Desafios | | | | |

## Parte 2: Projeto Arquitetural (50 pontos)

### Cenário
Uma empresa de mídia social deseja implementar uma nova arquitetura de dados com os seguintes requisitos:
- Processamento de 1 milhão de posts por hora
- Análise de sentimentos em tempo real
- Detecção de tendências
- Geração de relatórios de engajamento
- Armazenamento de histórico completo de interações
- Compliance com GDPR/LGPD

### Tarefas

1. Escolha uma das arquiteturas estudadas e desenhe uma solução completa:
   ```
   +----------------+     +-----------+     +---------------+
   |                |     |           |     |               |
   |                +---->|           +---->|               |
   |                |     |           |     |               |
   +----------------+     +-----------+     +-------+-------+
                                                   |
                                           +-------v-------+
                                           |               |
                                           |               |
                                           +---------------+

   ```

2. Justifique sua escolha arquitetural:
   ```
   Sua resposta aqui...
   ```

3. Detalhe os componentes tecnológicos que você utilizaria:
   - Ingestão de Dados:
   ```
   Sua resposta aqui...
   ```
   - Processamento:
   ```
   Sua resposta aqui...
   ```
   - Armazenamento:
   ```
   Sua resposta aqui...
   ```
   - Análise:
   ```
   Sua resposta aqui...
   ```

4. Descreva como sua arquitetura atende aos requisitos de:
   - Escalabilidade
   - Performance
   - Confiabilidade
   - Compliance
   ```
   Sua resposta aqui...
   ```

## Critérios de Avaliação
- Compreensão das arquiteturas (25%)
- Análise comparativa (25%)
- Design da solução (25%)
- Justificativa técnica (25%)

## Entrega
- Prazo: [DATA]
- Formato: Arquivo Markdown
- Submissão: Pull Request para o repositório do curso 