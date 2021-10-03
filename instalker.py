import instaloader, json

def GetProfileFromUsername(username:str):
	try:
		p = instaloader.Profile.from_username(il.context,username)
	except:
		return None
	return p

def ImprimirStories(user:str):
	profile = GetProfileFromUsername(user)
	if( not (profile == None)):
		il.download_stories([profile.userid],False,profile.username)
	
def GetIdFromUsername(user):
	p = GetProfileFromUsername(user)
	return p.userid

f = open("db.json","r")
user = json.load(f)["conta"]
f.close()

f = open("db.json","r")
usernames = json.load(f)["usernames"]
f.close()
	
il = instaloader.Instaloader()

il.login(user['usuario'],user['senha'])

for user in usernames:
	ImprimirStories(user)


# def BaixarFotoFromPost(post):
# 	il.download_pic(post.pcaption,post.url,post.date_local)

# def ImprimirTudo():
# 	print()

# def ImprimirTodasFotosDoPerfil(user:str):
# 	p = GetProfileFromUsername(user)
# 	postagens = p.get_posts()
# 	for post in postagens:
# 		if(not post.is_video):
# 			try:
# 				BaixarFotoFromPost(post)
# 			except:
# 				break
# 			# post.date_utc.timestamp
			
# def GetNumeroFotos(user):
# 	n = 0
# 	p = GetProfileFromUsername(user)
# 	postagens = p.get_posts()
# 	for post in postagens:
# 		# if(not post.is_video):
# 		n += 1
# 	return n