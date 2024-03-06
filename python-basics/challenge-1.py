# Challenge: Create a small narrative with inputs and print statements
# Bonus: Add color to text

print("=== Adventure Simulator ===")
print()
print('''You are about to embark on an adventure
      You'll be asked a few questions about yourself,
      then we'll create a great narrative starring YOU!!''')
print()
yourName = input("Your name: ")
yourEnemy = input("Your nemesis's name: ")
magicalAbility = input("Your ability: ")
print()
print(yourName, "felt her face pushed into the ground under the immense force of", yourEnemy,"'s kiri.", yourEnemy, "looked down at her with a derisive smile")
print(yourName, "knew the time had come. She had", yourEnemy, "where she wanted him - overconfident and disdainful.")
print(yourName, "drew on what little Kiri she could summon in her weakened state and pushed a bolt of lightning up from the ground through", yourEnemy,"'s feet, up through his spine and into his skull. Despite it's feebleness,", yourEnemy,"'s proximity to her and utter lack of shielding - pride will do that - it would fry him.")

#Color added to text

print("Of course this also meant that", yourName,  "would also", "\033[31m", "die.", "\033[0m", "But she had could rest knowing that", yourEnemy, "would not terrorize the village any longer.")