# -*- coding: utf-8 -*-
import crcmod
import qrcode
import os


class Payload:
    """
    Classe para gerar um payload Pix Copia e Cola e o respectivo QR Code.

    Atributos:
        nome (str): Nome do recebedor (máximo 25 caracteres recomendado).
        chavepix (str): Chave Pix (telefone, e-mail, CPF/CNPJ ou chave aleatória).
        valor (str): Valor da transação (opcional, use '0' ou '' para omitir).
        cidade (str): Cidade do recebedor (máximo 15 caracteres recomendado).
        txtId (str): Identificador da transação (opcional).
        diretorioQrCode (str): Diretório para salvar o QR Code (opcional).
    """

    def __init__(self, nome, chavepix, valor, cidade, txtId, diretorio=''):
        self.nome = nome.strip()
        self.chavepix = chavepix.strip()
        self.valor = valor.replace(',', '.').strip()
        self.cidade = cidade.strip()
        self.txtId = txtId.strip()
        self.diretorioQrCode = diretorio.strip()
        self._validar_campos()

    def _validar_campos(self):
        """Valida os campos fornecidos ao inicializar a classe."""
        if not self.nome:
            raise ValueError("O nome do recebedor é obrigatório.")
        if not self.chavepix:
            raise ValueError("A chave Pix é obrigatória.")
        if self.valor and not self.valor.replace('.', '').isdigit():
            raise ValueError("O valor deve ser numérico ou vazio.")
        if not self.cidade:
            raise ValueError("A cidade do recebedor é obrigatória.")

    def gerarPayload(self):
        """
        Gera o payload Pix Copia e Cola completo e cria o QR Code.

        Returns:
            str: O código Pix Copia e Cola completo.
        """
        # Merchant Account Information
        merchant_account = f'0014BR.GOV.BCB.PIX01{len(self.chavepix):02}{self.chavepix}'

        # Transaction Amount (removido se valor for 0 ou vazio)
        transaction_amount = ''
        if self.valor and float(self.valor) > 0:
            transaction_amount = f'54{len(self.valor):02}{self.valor}'

        # Additional Data Field (opcional)
        add_data_field = ''
        if self.txtId:
            add_data_field = f'62{len(f"05{len(self.txtId):02}{self.txtId}"):02}05{len(self.txtId):02}{self.txtId}'

        # Montando o payload base
        payload = (
            f'000201'
            f'26{len(merchant_account):02}{merchant_account}'
            f'52040000'
            f'5303986'
            f'{transaction_amount}'
            f'5802BR'
            f'59{len(self.nome):02}{self.nome}'
            f'60{len(self.cidade):02}{self.cidade}'
            f'{add_data_field}'
            f'6304'
        )

        # Adicionando o CRC16
        crc16 = self.gerarCrc16(payload)
        payload_completo = f'{payload}{crc16}'

        # Gerando a imagem do QR Code
        self.gerarQrCode(payload_completo)

        return payload_completo

    def gerarCrc16(self, payload):
        """
        Gera o código CRC16 para o payload.

        Args:
            payload (str): O payload Pix base.

        Returns:
            str: O código CRC16 gerado.
        """
        crc16 = crcmod.mkCrcFun(0x11021, initCrc=0xFFFF, rev=False, xorOut=0x0000)
        crc = crc16(payload.encode('utf-8'))
        return format(crc, '04X')

    def gerarQrCode(self, payload):
        """
        Gera e salva o QR Code baseado no payload.

        Args:
            payload (str): O payload Pix completo.
        """
        dir_path = os.path.expanduser(self.diretorioQrCode) or '.'
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        qr_code = qrcode.make(payload)
        qr_code_path = os.path.join(dir_path, 'pixqrcode.png')
        qr_code.save(qr_code_path)
        print(f"QR Code gerado com sucesso em: {qr_code_path}")
