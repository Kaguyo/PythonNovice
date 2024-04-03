# Enemy
Hp = 1200000
EnemyDefense = 500
EnemyResistance = 0.2

# Character
Atk = 1000 - EnemyDefense
print('Atk =', Atk)
SKILLMULTIPLIER = 1.45 * Atk 

# Calculo
def CalculeDamage(Dmg):
  return SKILLMULTIPLIER * DmgBonus * TotalDmg * CritDMG * Dmg * Phys_Resistance
  
DmgBonus = 1.42
print('DmgBonus =', DmgBonus)

TotalDmg = 1.7
print('TotalDmg =', TotalDmg)

CritDMG = 2.9
print('CritDMG =', CritDMG)

Physical_Breach = 2
print('Physical_Breach =', Physical_Breach)

EnemyResistance

Phys_Resistance = Physical_Breach - EnemyResistance
print('Enemys dmg taken increasement/loss =', Phys_Resistance)
Hits = 4

Dmg = CalculeDamage(Hits) 
print(Dmg)





