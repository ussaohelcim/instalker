# instalker
Programa para baixar stories do instagram em cima do Instaloader.

# Como usar

Este programa foi escrito em cima do Instaloader, logo você precisa ter ele na sua maquina.

```
pip install instaloader
```

Depois modifique o arquivo ``db.json``

```python
{
	"conta":{
		"usuario":"",#digite aqui seu usuario
		"senha":""# digite aqui sua senha
	},
	"usernames":[
		"" # aqui são os usernames das contas que voce quer baixar os stories, separado por virgula
	]
}
```