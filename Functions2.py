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
Rifle = 4
Revolver = 1.3

Rifle_Loaded = 4.1397
Rifle_Loaded_Hollow_Tip = 4.0092 

Revolver_Loaded = 1.3064
Revolver_Loaded_Hollow_Tip = 1.3061

Municao762 = 0.0097
Municao762_Hollow = 0.0092

Municao45ACP = 0.064
Municao45ACP_Hollow = 0.061

Crowbar = 2.2

Knife = 0.4


Backpack = 0.15
"Boosts 10kg capacity"

Basic_Supplements = 0


# Personagem
Nome = "Ellie" 
Ellie = {
"Height": (166, "cm"),
"Age": (18, "cm"),
"Weight": (58, "kg"),
}

# Arma de fogo em posse:
"Rifle"
"Revolver"

# Municao de armas de fogo em posse:

# Numero 1 = Ponta oca.
# Numero 2 = comum.
Revolver_Hollow_Ammo_Type =()
Revolver_Ammo_Type = True

Rifle_Hollow_Ammo_Type = False
Rifle_Ammo_Type =()


# Capacidade Rifle: 1-8
# Capacidade Revolver 1-6
# Disparos Restantes
Rifle_Rounds = 7
Revolver_Rounds = 3



# Equipamento no Corpo
Hands= (Rifle + Municao762_Hollow*8) 

Back= (Crowbar, Backpack)

Belt= (Revolver + Municao45ACP*9)

Garter_Belt= (Knife)

Total_Weight = 58 + Crowbar + Rifle + Municao762_Hollow*Rifle_Rounds + Backpack + Revolver + Municao45ACP*Revolver_Rounds + Knife + Municao762_Hollow*8 + Municao45ACP*9
print("Informacoes do personagem:")
print("Carga limite", 82, "kg", "(+10kg Backpack) ")
print("Carga atual", Total_Weight, "kg")




# Um Trilhao de variaveis com codigos importantes
Rifleloaded = True if Rifle_Rounds == 1 or (2,3,4,5,6,7,8) else()
Rifleloaded_Hollow_Point = True if Rifle_Rounds == 1 or (2,3,4,5,6,7,8) else()

Revolverloaded = True if Revolver_Rounds == 1 or (2,3,4,5,6,7,8) else()
Revolverloaded_Hollow_Point = True if Revolver_Rounds == 1 or (2,3,4,5,6,7,8) else()


if Rifleloaded : Rifle + 0.13
if Rifleloaded_Hollow_Point : Rifleloaded_Hollow_Point + Single_Rifle_Hollow_Point_Bullet_Weight



# Tambor Revolver
Revolver_Rounds_Upperlimit = 6
Revolver_Rounds_Lowerlimit = 1
if Revolver_Rounds > Revolver_Rounds_Upperlimit:
    print("Revolver Rounds: Invalid")
if Revolver_Rounds < Revolver_Rounds_Lowerlimit:
    print("Revolver Rounds: Unloaded")

# Rifle_Maganize
Rifle_Magazine_Weight = 0.13
Rifle_Rounds_Upperlimit = 8
Rifle_Rounds_Lowerlimit = 1
if Rifle_Rounds > Rifle_Rounds_Upperlimit:
    print("Rifle Rounds: Invalid")
if Rifle_Rounds < Rifle_Rounds_Lowerlimit:
    print("Rifle Rounds: Unloaded")

if Rifle > 4 : Rifle + 0.13
if Revolver > 1.3 : Revolver == Revolver_Loaded


if Revolver_Ammo_Type : Revolver_Hollow_Ammo_Type = False
if Revolver_Hollow_Ammo_Type : Revolver_Ammo_Type = False

if Rifle_Ammo_Type : Rifle_Hollow_Ammo_Type = False
if Rifle_Hollow_Ammo_Type : Rifle_Ammo_Type = False