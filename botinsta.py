from fileinput import close
import instaloader

# Obter instância
loader = instaloader.Instaloader()
#USER= 'marciomoreirabomfimsilva'
USER= 'mardio_moreira'
PASSWORD = 'G@L120486@@'
# Faça login usando as credenciais
loader.login(USER, PASSWORD)
# Use a classe Profile para acessar os metadados da conta
profile = instaloader.Profile.from_username(loader.context, USER)
followers = profile.get_followees()

arquivo = open('lista.txt','w')
for follower in followers:
    arquivo.write(follower.username+str("\n"))
arquivo.close()
print("---------------------------------------------Fim do Script---------------------------------------------")