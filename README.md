# qrpix

`qrpix` é uma biblioteca para gerar códigos QR de pagamentos PIX de maneira simples e eficiente. A biblioteca permite a criação de payloads PIX válidos e a geração de QR Codes para serem usados em pagamentos.

## Instalação

Para instalar o pacote, use o `pip`:

```bash
pip install qrpix==1.0

## Como usar

```python
from payload import Payload

# Inicializando com os dados
payload = Payload(nome="Maria José", chavepix="+5584994226558", valor="0.00", cidade="BRASIL", txtId="TesteQRPIX")

# Gerando o QR Code
codigo_pix = payload.gerarPayload()
print(codigo_pix)  # Exibe o código gerado
