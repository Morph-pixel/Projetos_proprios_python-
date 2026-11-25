import random 
import time
personagens = {'3e':['Cool Steel',
    'Harbinger of Dawn',
    'Traveler’s Handy Sword',
    'Fillet Blade',
    'Dark Iron Sword',

    'White Iron Greatsword',
    'Bloodtainted Greatsword',
    'Debate Club',
    'Ferrous Shadow',

    'Black Tassel',
    'White Tassel',
    'Halberd',

    'Magic Guide',
    'Thrilling Tales of Dragon Slayers',
    'Otherworldly Story',

    'Raven Bow',
    'Sharpshooter’s Oath',
    'Slingshot'],'4e':['Amber',
    'Barbara',
    'Beidou',
    'Bennett',
    'Candace',
    'Charlotte',
    'Chevreuse',
    'Chongyun',
    'Collei',
    'Dahlia',
    'Diona',
    'Dori',
    'Faruzan',
    'Fischl',
    'Freminet',
    'Gaming',
    'Gorou',
    'Ifa',
    'Iansan',
    'Jahoda',
    'Kachina',
    'Kaeya',
    'Kirara',
    'Kujou Sara',
    'Kuki Shinobu',
    'Lan Yan',
    'Layla',
    'Lisa',
    'Mika',
    'Ningguang',
    'Noelle',
    'Ororon',
    'Razor',
    'Rosaria',
    'Sayu',
    'Sethos',
    'Shikanoin Heizou',
    'Sucrose',
    'Thoma',
    'Xiangling',
    'Xingqiu',
    'Xinyan',
    'Yanfei',
    'Yaoyao',
    'Yun Jin'],'5e':[ 'Albedo',
    'Alhaitham',
    'Arataki Itto',
    'Arlecchino',
    'Baizhu',
    'Chasca',
    'Chiori',
    'Citlali',
    'Clorinde',
    'Columbina',
    'Cyno',
    'Durin',
    'Emilie',
    'Escoffier',
    'Eula',
    'Flins',
    'Furina',
    'Ganyu',
    'Hu Tao',
    'Kaedehara Kazuha',
    'Kamisato Ayaka',
    'Kamisato Ayato',
    'Kinich',
    'Klee',
    'Lauma',
    'Linnea',
    'Lohen',
    'Lyney',
    'Mavuika',
    'Mualani',
    'Nahida',
    'Navia',
    'Nefer',
    'Neuvillette',
    'Nicole',
    'Nilou',
    'Odette',
    'Raiden Shogun',
    'Sandrone',
    'Sangonomiya Kokomi',
    'Shenhe',
    'Sigewinne',
    'Skirk',
    'Varesa',
    'Varka',
    'Venti',
    'Wanderer',
    'Wriothesley',
    'Xianyun',
    'Xiao',
    'Xilonen',
    'Yae Miko',
    'Yelan',
    'Yoimiya',
    'Zhongli',
    'Zibai',
    'Jean',
    'Diluc',
    'Mona',
    'Keqing',
    'Qiqi',
    'Tighnari',
    'Dehya',
    'Yumemizuki Mizuki']} 
cincoe = {'limitados':['Albedo',
    'Alhaitham',
    'Arataki Itto',
    'Arlecchino',
    'Baizhu',
    'Chasca',
    'Chiori',
    'Citlali',
    'Clorinde',
    'Columbina',
    'Cyno',
    'Durin',
    'Emilie',
    'Escoffier',
    'Eula',
    'Flins',
    'Furina',
    'Ganyu',
    'Hu Tao',
    'Kaedehara Kazuha',
    'Kamisato Ayaka',
    'Kamisato Ayato',
    'Kinich',
    'Klee',
    'Lauma',
    'Linnea',
    'Lohen',
    'Lyney',
    'Mavuika',
    'Mualani',
    'Nahida',
    'Navia',
    'Nefer',
    'Neuvillette',
    'Nicole',
    'Nilou',
    'Odette',
    'Raiden Shogun',
    'Sandrone',
    'Sangonomiya Kokomi',
    'Shenhe',
    'Sigewinne',
    'Skirk',
    'Varesa',
    'Varka',
    'Venti',
    'Wanderer',
    'Wriothesley',
    'Xianyun',
    'Xiao',
    'Xilonen',
    'Yae Miko',
    'Yelan',
    'Yoimiya',
    'Zhongli',
    'Zibai'],'mochileiros':[ 'Jean',
    'Diluc',
    'Mona',
    'Keqing',
    'Qiqi',
    'Tighnari',
    'Dehya',
    'Yumemizuki Mizuki']}
pesos = {'3e':94.3,'4e':5.1,'5e':0.6} 
peso5 = {'limitados':50, 'mochileiros':50}
per4 = []
perl = [] 
perm = []
fifty = 0 
four = 0
pity = 0 
total = 0 
cm = 0 
cl = 0 
cin = 0
def main(): 
    while True:  
        botao = input('[1] Rolar\n[2] Inventário \n[3] Dados \n[4] Pity \n[5] Sair\n').strip()
        if botao != '1' and botao != '2' and botao != '3' and botao != '4' and botao != '5':
                 print('Valor inválido, por favor  digite uma das opções')  
        elif botao == '5': 
            break
        elif botao == '1':
            gacha() 
        elif botao == '2': 
            print(f'Personagens 5 estrelas:{cin}\nLimitados:{perl}\nMochileiros:{perm}\nPersonagens 4 estrelas: {per4}') 
        elif botao == '3': 
            print(f'\n50/50 perdidos:{len(perm)}\nQuantidade total de 4 estrelas:{len(per4)}\nTotal de pulls:{total}')
        else: 
            print(f'Pity:{pity}\n50/50 garantindo:{'Sim' if fifty else 'Não'}')
def gacha(): 
    global fifty 
    global pity
    global cm
    global cl 
    global cin 
    global total 
    global four
    for number in range(1,11):
        time.sleep(0.5)
        raridade = random.choices(list(personagens.keys()),weights = list(pesos.values()))[0] 
        if pity >= 89: 
            raridade = '5e'
        elif four >= 9 and raridade != '5e':
            raridade = '4e'
        if fifty == 1 and raridade == '5e':
            raridade = 'limitados'
            escolhido = random.choice(cincoe[raridade])
            print(f'\033[93m{escolhido}\033[0m')
            cl += 1 
            pity = 0
            fifty = 0 
            total += 1 
            perl.append(escolhido) 
        elif raridade == '5e':
            raridade = random.choices(list(cincoe.keys()),weights = list(peso5.values()))[0]     
            escolhido = random.choice(cincoe[raridade])
            if raridade == 'limitados':
                cl += 1 
                cin += 1
                pity = 0 
                four = 0
                total += 1
                perl.append(escolhido) 
                print(f'\033[93m{escolhido}\033[0m') 
            else: 
                cin += 1
                pity = 0 
                four = 0
                fifty += 1
                cm += 1 
                total += 1
                perm.append(escolhido) 
                print(f'\033[93m{escolhido}\033[0m') 
        elif raridade == '3e':
            escolhido = random.choice(personagens[raridade]) 
            four += 1
            pity+= 1 
            total += 1 
            print(f'\033[94m{escolhido}\033[0m')
        else: 
            escolhido = random.choice(personagens[raridade]) 
            per4.append(escolhido) 
            four = 0
            pity += 1 
            total += 1
            print(f'\033[95m{escolhido}\033[0m') 
if __name__ == "__main__":
    main()