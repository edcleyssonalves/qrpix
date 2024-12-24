from setuptools import setup, find_packages

setup(
    name='qrpix',
    version='1.0',
    packages=find_packages(),  # Encontrando automaticamente as pastas de código
    install_requires=[
        'crcmod',
        'qrcode[pil]',  # Dependência para gerar QR Codes
    ],
    author='edalves',
    author_email='edcleyssonalves@example.com',
    description='Pacote para gerar QR Codes de pagamento Pix',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/edcleyssonalves/qrpix',  # Coloque o link para o repositório do seu projeto
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Garantindo que funciona em Python 3.6 ou superior
)
