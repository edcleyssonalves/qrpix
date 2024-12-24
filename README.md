# qrpix

Este pacote permite gerar QR Codes de pagamento Pix, com informações personalizáveis como nome do recebedor, chave Pix, valor da transação e cidade.

## Como usar

```python
from payload import Payload

# Inicializando com os dados
payload = Payload(nome="Maria José", chavepix="+5584994226558", valor="0.00", cidade="BRASIL", txtId="TesteQRPIX")

# Gerando o QR Code
codigo_pix = payload.gerarPayload()
print(codigo_pix)  # Exibe o código gerado
