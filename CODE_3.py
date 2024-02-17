# Tentando fazer uma brincadeira com os comandos:
# Descobrindo Idade, e caracteristicas baseadas no mesmo.

Caracteristicas = {
    "Survivor", "Female", "Inteligent", 
    "Tall", "Short", "Young", "Clumsy",
    "Thin", "Chunky", "Male", "Amateur"
    "Muscular", "Cute", "Strong",
    "Very Strong", "Very Weak", "Novice"
    "Weak", "Common (Strenght)", "Experienced"
    "Old","Heavy", "Light", "White",
    "Black", "Asian", "Indigenous"
    "Annoying", "Funny", "Talkative",
    "Introvert", "Infected", "Archery", "Shooting Rifles",
    "Slow (Speed)", "Fast (Speed)", "Common (Speed)",
    "Can Play Guitar", "Common (Weight)", "Likes Jokes",
    "Basic Crafter", "Multi Crafter", "Advanced Crafter", "Sneaking",
    "Shooting Pistols", "Shooting Shotguns", "Blade Meele Weapons", 
    "Hand to Hand Combat", "Stunning Meele Weapons", "Grenades", "Hunting"
} 
my_list = {
    "name": "Joel Miller",
    "age": 56,
    "Tipo": "Survivor",
    "Experience": "Experienced",
    "Height": 185,
    "Gender": "Male",
    "Body": "Muscular",
    "Strength": "Strong",
    "Agility": "Common (Speed)",
    "Race": "White",
    "Communication": "Talkative",
    "Perks": ["Archery", "Multi Crafter", "Sneaking", "Shooting Pistols", "Blade Melee Weapons", 
              "Shooting Rifles", "Shooting Shotguns", "Hunting", "Grenades", "Stunning Meele Weapons"],
    "Fun Fact": "Can Play Guitar",
    "Weight": 83
}

my_list2 = {
    "name": "Ellie",
    "age": 15,
    "Tipo": "Survivor",
    "Experience": "Amateur",
    "Height": 160,
    "Gender": "Female",
    "Body": "Thin",
    "Strength": "Weak",
    "Agility": "Common (Speed)",
    "Race": "White",
    "Communication": "Talkative",
    "Perks": ["Archery", "Basic Crafter", "Sneaking", "Shooting Pistols", "Blade Melee Weapons",
              "Shooting Rifles", "Hunting"],
    "Fun Fact": "Likes Jokes",
    "Weight": 50
}



my_list3 = {
    "name": "Ellie Miller",
    "age": 18,
    "Tipo": "Survivor",
    "Experience": "Experienced",
    "Height": 166,
    "Gender": "Female",
    "Body": "Thin",
    "Strength": "Common (Strenght)",
    "Agility": "Fast (Speed)",
    "Race": "White",
    "Communication": "Talkative",
    "Perks": ["Archery", "Advanced Crafter", "Sneaking", "Shooting Pistols", "Blade Melee Weapons", 
              "Shooting Rifles", "Shooting Shotguns", "Hunting", "Grenades", "Stunning Meele Weapons"],
    "Fun Fact": "Can Play Guitar",
    "Weight": 58
    }

Personagem = 2

if Personagem <= 1 :
    print(my_list)
if Personagem == 2 :
    print(my_list2)
if Personagem == 3 :
    print(my_list3)