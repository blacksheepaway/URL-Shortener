# URL Shortener

Este projeto é um encurtador de URL simples e eficiente, desenvolvido em Python com o auxílio das bibliotecas `pyshorteners` e `tkinter`. A aplicação permite encurtar URLs longas usando o serviço TinyURL e copiar o resultado para a área de transferência do sistema.

## Técnicas e tecnologias utilizadas

- **Python**: Linguagem de programação utilizada para desenvolver a aplicação.
- **pyshorteners**: Biblioteca Python para interagir com vários serviços de encurtamento de URL.
- **tkinter**: Biblioteca Python para criar interfaces gráficas.

## Conceitos

- **GUI (Interface Gráfica do Usuário)**: Utilizamos a biblioteca `tkinter` para criar uma interface gráfica simples e intuitiva para a aplicação.
- **APIs de encurtamento de URL**: A aplicação faz uso da biblioteca `pyshorteners` para interagir com o serviço de encurtamento de URL TinyURL.

## Modificações e aplicações úteis

Esta aplicação pode ser facilmente adaptada para:

- Suportar outros serviços de encurtamento de URL, como bit.ly ou goo.gl, simplesmente modificando a chamada à biblioteca `pyshorteners`.
- Implementar recursos adicionais, como histórico de URLs encurtadas ou compartilhamento direto do resultado nas redes sociais.
- Integrar a funcionalidade de encurtamento de URL em outras aplicações ou sistemas.

## Como funciona

1. O usuário insere a URL longa no campo de entrada.
2. Ao clicar no botão "Shorten URL", a aplicação chama a função `shorten_url`.
3. A função `shorten_url` usa a biblioteca `pyshorteners` para gerar uma URL encurtada usando o serviço TinyURL.
4. A URL encurtada é exibida em um rótulo abaixo do campo de entrada.
5. O usuário pode clicar no botão "Copiar URL" para copiar a URL encurtada para a área de transferência do sistema.

## Exemplo

![image](https://user-images.githubusercontent.com/50200471/230756666-36f7df15-92a7-4505-a2d3-6464a8d8b486.png)

## Contribuição

Sinta-se à vontade para contribuir com este projeto! Você pode fazer isso de várias maneiras:

1. Reportar bugs e solicitar recursos.
2. Melhorar o código existente ou adicionar novos recursos.
3. Atualizar a documentação ou criar tutoriais e guias.
4. Divulgar o projeto para outras pessoas interessadas.

## Licença

Este projeto está licenciado sob a [Licença MIT] que permite o uso, cópia, modificação e distribuição livre do código-fonte, desde que a licença original seja incluída e os direitos autorais sejam respeitados.
