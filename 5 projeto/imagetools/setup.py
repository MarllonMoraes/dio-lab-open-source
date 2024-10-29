from setuptools import setup, find_packages

setup(
    name='imagetools',
    version='0.1.0',
    description='Pacote simples para processamento de imagens.',
    author='Seu Nome',
    author_email='seu_email@example.com',
    packages=find_packages(),
    install_requires=[
        'Pillow>=9.0.1'  # Lista de dependências do pacote
    ],
)