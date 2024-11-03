from random import randint

class Retors:
    def __init__(self,liste_config):
        self.liste_config=liste_config
        config=self.liste_config[randint(0,len(self.liste_config)-1)]

    def modifier_config(self):
        config=liste_config[randint(0,len(self.liste_config)-1)]

    def renvoyer(self,lettre):
        return liste_config[lettre]

class Enigma:
    def __init__(self,liste_retors):
        self.liste_retors=liste_retors

    def coder(self,msg):
        code=""
        for i in msg:
            a=self.liste_retors[1].config[i]
            b=self.liste_retors[2].config[a]
            c=self.liste_retors[3].config[b]
            if c!=i:
                code+=c
            else:
                liste_retors[0,2].modifier_config()
                a=self.liste_retors[1].config[i]
                b=self.liste_retors[2].config[a]
                c=self.liste_retors[3].config[b]
        return code,(self.liste_retors[1].liste_config[i].index(config),self.liste_retors[2].liste_config[i].index(config),self.liste_retors[3].liste_config[i].index(config))

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
configurations=[]
for i in range(26):
    configuration=[(j,alphabet[i-alphabet.index(j)])for j in alphabet]
    configurations.append(configuration)
