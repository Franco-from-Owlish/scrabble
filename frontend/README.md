# default

## Project setup

```
# yarn
yarn

# npm
npm install

# pnpm
pnpm install
```

### Compiles and hot-reloads for development

```
# yarn
yarn dev

# npm
npm run dev

# pnpm
pnpm dev
```

### Compiles and minifies for production

```
# yarn
yarn build

# npm
npm run build

# pnpm
pnpm build
```

### Customize configuration

See [Configuration Reference](https://vitejs.dev/config/).


## Using the Vue app in Flask

Steps to use the Vue app within Flask:
1- Build the application
2- Copy the ```index.html``` in dist to the templates folder in the backend.
3- Replace all link in the ```index.html``` to read from the static folder. Example shown below.
4- Copy all static files and folders in dist the static folder in flask


```
<head>
    <meta charset="UTF-8" />
    <link rel="icon" href="{{ url_for('static', filename='/favicon.ico') }}" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Scrabble</title>
  <script type="module" crossorigin src="{{ url_for('static', filename='/assets/index.16f8e9f7.js') }}"></script>
  <link rel="stylesheet" href="{{ url_for('static', filename='/assets/index.7c06de23.css') }}">
</head>
```