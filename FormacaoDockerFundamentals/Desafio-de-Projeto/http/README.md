🚀 **Desafio Docker Apache - Passo a Passo!**

Para começar, vamos seguir o passo a passo sugerido e implementar o desafio proposto pelo especialista. Prepare-se para aumentar seu portfólio de projetos no GitHub! 💼

### 1. Criar Arquivo YML para Docker Compose

Vamos começar criando um arquivo YAML para definir nosso ambiente Docker com o servidor Apache (httpd). Nomearemos nosso arquivo de `docker-compose.yml`.

```yaml
version: '3'

services:
  apache:
    image: httpd:latest
    ports:
      - "80:80"
    volumes:
      - ./app:/usr/local/apache2/htdocs
```

### 2. Criar Aplicação HTML Simples
Dentro do diretório `app`, crie um arquivo `index.html` com o conteúdo do seu Hello World:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
    </style>
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>
```
