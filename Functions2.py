# Multiple Return Values:
# Python functions can return multiple values as a tuple, 
# which can then be unpacked into separate variables.

def square_and_cube(x):
    return x**2, x**3

square, cube = square_and_cube(3)
print("Square:", square)
print("Cube:", cube)

# Retornando multiplos valores para diferentes variaveis
# Peso de Equipamentos e Itens


# Rifle
print("Equipamentos e Detalhes:")

def RifleWeight(x):
    return x*4

Rifle = RifleWeight(1)
print("Peso_Rifle_Vazio", Rifle, "kg")

# Revolver
def RevolverWeight(x):
    return x*1.3

Revolver = RevolverWeight(1)
print("Peso_Revolver_Vazio", Revolver, "kg")

# Peso municao de Revolver
def Revolver_bullet(y):
    return y*6.4, y*6.15

Single_Revolver_Bullet_Weight, Single_Revolver_Hollow_Point_Bullet_Weight = Revolver_bullet(0.001)
print("Peso_Municao_Revolver", Single_Revolver_Bullet_Weight, "kg")
print("Peso_Municao_Revolver_Oca", Single_Revolver_Hollow_Point_Bullet_Weight, "kg")


# Peso municao de Rifle
def Rifle_bullet(y):
    return y*9.7, y*9.20

Single_Rifle_Bullet_Weight, Single_Rifle_Hollow_Point_Bullet_Weight = Rifle_bullet(0.001)
print("Peso_Municao_Rifle", Single_Rifle_Bullet_Weight, "kg")
print("Peso_Municao_Rifle_Oca", Single_Rifle_Hollow_Point_Bullet_Weight, "kg")



# Equipamentos Municiados/Detalhados Peso
Recurve_Bow = 1

Rifle = 4.13

Revolver = 1.4

Pistol = 1.2

Municao762 = 0.0097
Municao762_Hollow = 0.0092

Municao45ACP = 0.0064
Municao45ACP_Hollow = 0.0061

Bow_Arrows = 0.025

Crowbar = 2.2

Knife = 0.4

Motorcycle = 80

Backpack = 0.15
"Allows to carry 1 more Long Weapon, up to 5kg of Basic Supplements plus 2 Small Itens and 1 Medium Item or Weapon"

Basic_Supplements = 0


# Categorias de Itens
Small_Itens = { 
    Knife, Municao45ACP, Municao45ACP_Hollow, Municao762, Municao762_Hollow
    }
Medium_Itens = {
    Crowbar, Backpack
}
Large_Itens = { 
    Motorcycle
}

Long_Weapons = { 
    Rifle
}

Medium_Weapons = {
    
}

Small_Weapons = {
    Revolver, Pistol
}

Special_Weapons = {
    Recurve_Bow
}

# Personagem
Nome = "Ellie" 
Ellie = {
"Height": (166, "cm"),
"Age": (18, "cm"),
} 
Weight = 58

# Capacidade Rifle: 1-8
# Capacidade Revolver 1-6
# Disparos Restantes
Rifle_Rounds = 6
Revolver_Rounds = 3
Recurve_Bow_Arrows_Left = 0
Pistol_Rounds = 0

# Corpo Personagem
Hands = Rifle + Municao762_Hollow*Rifle_Rounds

Back = Crowbar + Backpack + Municao45ACP*9

Belt = Revolver + Municao45ACP*Revolver_Rounds

Garter_Belt = Knife

Total_Weight = Weight + Back + Belt + Garter_Belt + Hands

# Item em mãos
Empunhando = Rifle

print("Informacoes do personagem:")
print("Peso de", Nome, Weight,":", "kg")
CargaLimite = Weight * 1.4655172413793104
print("Carga Limite:", CargaLimite, "kg")
if Total_Weight <= 85 : 
    print("Carga atual:", Total_Weight, "kg")
if Total_Weight > 85 :
    print("Carga Limite atingida (",CargaLimite," kg) Desempenho será afetado.")


# Um Trilhao de variaveis com codigos importantes



# Empunhar Item X
if Empunhando == Knife:
    print("Empunhando: Faca")
if Empunhando == Rifle:
    print("Empunhando: Rifle (", Rifle_Rounds, ")")
if Empunhando == Revolver:
    print("Empunhando: Revolver (",Revolver_Rounds, ")")
if Empunhando == Recurve_Bow:
    print("Empunhando: Arco Recurvo (", Recurve_Bow_Arrows_Left, ")")
if Empunhando == Crowbar:
    print("Empunhando: Pé de Cabra")
if Empunhando == Pistol:
    print("Empunhando: Pistol (", Pistol_Rounds, ")")

# Revolver_Chamber
Revolver_Rounds_Upperlimit = 6
Revolver_Rounds_Lowerlimit = 1
if Revolver_Rounds > Revolver_Rounds_Upperlimit and Empunhando == Revolver:
    print("Revolver Rounds: Invalid")
if Revolver_Rounds < Revolver_Rounds_Lowerlimit and Empunhando == Revolver:
    print("Revolver: Unloaded")

# Rifle_Maganize
Rifle_Rounds_Upperlimit = 8
Rifle_Rounds_Lowerlimit = 1

if Rifle_Rounds > Rifle_Rounds_Upperlimit and Empunhando == Rifle:
    print("Rifle Rounds: Invalid")
if Rifle_Rounds < Rifle_Rounds_Lowerlimit and Empunhando == Rifle:
    print("Rifle: Unloaded")

# Pistol_Magazine 
Pistol_Rounds_Upperlimit = 15
Pistol_Rounds_Lowerlimit = 1

if Pistol_Rounds > Pistol_Rounds_Upperlimit and Empunhando == Pistol:
    print("Pistol Rounds: Invalid")
if Pistol_Rounds < Pistol_Rounds_Lowerlimit and Empunhando == Pistol:
    print("Pistol: Unloaded")

# Recurve_Bow_Arrows
Recurve_Bow_Rounds_Upperlimit = 1
Recurve_Bow_Rounds_Lowerlimit = 1

if Recurve_Bow_Arrows_Left > Recurve_Bow_Rounds_Upperlimit and Empunhando == Recurve_Bow:
    print("Nocking Arrow: Invalid")
if Recurve_Bow_Arrows_Left < Recurve_Bow_Rounds_Lowerlimit and Empunhando == Recurve_Bow:
    print("Bow: Unloaded")