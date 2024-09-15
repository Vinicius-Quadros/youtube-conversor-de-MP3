# Conversor de Vídeos para MP3

## Descrição

Este script permite converter vídeos de links (como do YouTube) para o formato MP3. Ele utiliza uma ferramenta para baixar os vídeos e uma biblioteca para converter os arquivos de vídeo baixados em áudio MP3. O script também lê links de um arquivo CSV e extrai automaticamente os títulos dos vídeos.

## Funcionalidades

- **Download de Vídeos**: Baixa vídeos de links fornecidos (como do YouTube).
- **Conversão para MP3**: Converte os vídeos baixados para o formato de áudio MP3.
- **Leitura de Links de Arquivo CSV**: Lê os links de vídeo a partir de um arquivo CSV e extrai automaticamente os títulos dos vídeos.

## Tecnologias Usadas

- Python 3.10 ou superior
- Bibliotecas Python: `yt-dlp`, `moviepy`

## Instalação

1. **Instale o Python 3.10 ou superior**:
   - Visite [python.org](https://www.python.org/downloads/) e faça o download da versão mais recente do Python (3.10 ou superior).

2. **Instale as bibliotecas necessárias**:
   Abra o terminal ou prompt de comando e execute:

    ```sh
    pip install yt-dlp moviepy
    ```

## Como Usar

1. **Prepare o arquivo CSV**:
   - Crie um arquivo CSV contendo os links dos vídeos que deseja converter para MP3. Cada linha do arquivo deve conter um único link de vídeo.

2. **Execute o script**:
   - Abra o terminal ou prompt de comando e execute:
    ```sh
    python Conversor_MP3.py
    ```

3. **Aguarde a conversão**:
   - O script irá baixar os vídeos e convertê-los para MP3, salvando os arquivos na pasta de destino.

## Observações

- Certifique-se de que os links no arquivo CSV estejam acessíveis e válidos.
- O tempo de conversão pode variar dependendo do tamanho dos vídeos e da velocidade da internet.



