# -------------------------------------------------------------
# EVALUATION: Lab 03 - Build an RPG Character
# NOTES: Independent logic project focusing on deep input parameter validation, string constraints, and character string formatting.
# -------------------------------------------------------------

# USER STORIES TO FULFILL:
# 1. Define a function named create_character(name, strength, intelligence, charisma).
# 2. Validate Name: Must be a string, not empty, <= 10 characters, and cannot contain spaces.
# 3. Validate Stats: All stats must be integers, between 1 and 4 inclusive.
# 4. Validate Total Points: The sum of strength, intelligence, and charisma must exactly equal 7.
# 5. Output Format: Return a 4-line string (Name, followed by STR, INT, and CHA bars).
#    Each stat bar must display filled dots (●) for its value and empty dots (○) padding it out to 10 total dots.

# -------------------------------------------------------------

full_dot = '●'
empty_dot = '○'

def create_character(name, stre, inte, cha):
    if not isinstance(name,str):
        return "The character name should be a string"  
    if name=="":
        return "The character should have a name"
    if len(name)>10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"

    if not (isinstance(stre,int) and isinstance(inte,int) and isinstance(cha,int)):
        return "All stats should be integers"
    if stre<1 or inte<1 or cha<1:
        return "All stats should be no less than 1"
    if stre>4 or inte>4 or cha>4:
        return "All stats should be no more than 4"
    if not stre+inte+cha==7:
        return "The character should start with 7 points"

    return f"{name}\nSTR {full_dot*stre+empty_dot*(10-stre)}\nINT {full_dot*inte+empty_dot*(10-inte)}\nCHA {full_dot*cha+empty_dot*(10-cha)}"

print(create_character("Ren",4,2,1))