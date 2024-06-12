# Monitor de Velocidade da Internet

Este é um script Python simples para monitorar a velocidade da sua conexão à internet ao longo do tempo. Ele utiliza a biblioteca `speedtest` para realizar testes de velocidade periódicos e registra os resultados em um arquivo CSV para análise posterior.

## Funcionalidades

- Realiza testes de velocidade de download, upload e latência (ping).
- Registra os resultados dos testes em um arquivo CSV com carimbo de data e hora.
- Obtém o nome e a localização do servidor de teste escolhido durante o teste.

## Como Usar

1. Clone o repositório para o seu ambiente local.
2. Certifique-se de ter Python instalado no seu sistema.
3. Instale a biblioteca `speedtest` utilizando `pip install speedtest-cli`.
4. Execute o script `speedtest_monitor.py`.
5. Pressione `q` a qualquer momento para interromper o monitoramento.

## Requisitos

- Python 3.x
- Biblioteca `speedtest`
