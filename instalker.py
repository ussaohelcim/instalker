import instaloader, json, sys

def GetProfileFromUsername(username:str):
	try:
		p = instaloader.Profile.from_username(il.context,username)
	except:
		return None
	return p

def ImprimirStories(user:str):
	profile = GetProfileFromUsername(user)
	if( not (profile == None)):
		il.download_stories([profile.userid],True,profile.username)
	
def GetIdFromUsername(user):
	p = GetProfileFromUsername(user)
	return p.userid

def ImprimirPostagens(user:str):
	p = GetProfileFromUsername(user)
	if( not (p == None)):
		for post in p.get_posts():
			il.download_post(post,p.username+":posts")

def ImprimirHighLights(user:str):
	p = GetProfileFromUsername(user)
	if( not (p == None)):
		il.download_highlights(p,True)

f = open("db.json","r")
user = json.load(f)["conta"]
f.close()

f = open("db.json","r")
usernames = json.load(f)["usernames"]
f.close()

args = sys.argv

il = instaloader.Instaloader(save_metadata=False)

il.login(user['usuario'],user['senha'])

print("Argumentos usados: "+ str(args))
if(len(args) == 1):
	print("Imprimindo apenas stories")
	for user in usernames:
		ImprimirStories(user)
		
elif(args[1] == "--a"):
	print("Selecionado para imprimir tudo")
	print(args[1])
	for user in usernames:
		ImprimirStories(user)
		ImprimirHighLights(user)
		ImprimirPostagens(user)
		
elif(args[1] == "--h"):
	print("Selecionado para imprimir apenas highlights")
	for user in usernames:
		ImprimirHighLights(user)

else:
	print("argumentos usado de maneira errada")