# Character
Atk = 1000
DmgBonus = 1.42
TotalDmg = 1.7
CritDMG = 2.9
SkillMultiplier = 1.05 * Atk

# Enemy
EnemyDefense = 100
Resistence = 1.15

# Calculo
def Damage(a, b, c, d):
    return (Atk * DmgBonus * TotalDmg * CritDMG * SkillMultiplier)

Damage
print(Damage) 