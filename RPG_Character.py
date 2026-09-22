def create_character(char_name, stren, intell, charis):
    full_dot = '●'
    empty_dot = '○'
    stats = stren, intell, charis
    if not isinstance(char_name, str):
        return 'The character name should be a string'
    if char_name == '':
        return 'The character should have a name'
    if len(char_name) > 10:
        return 'The character name is too long'
    if ' ' in char_name:
        return 'The character name should not contain spaces'   
    if not all(isinstance(stat, int) for stat in stats):
        return 'All stats should be integers'
    if any(stat < 1 for stat in stats):
        return 'All stats should be no less than 1'
    if any(stat > 4 for stat in stats):
        return 'All stats should be no more than 4'
    if sum(stats) != 7:
        return 'The character should start with 7 points'
    else:
        return char_name + '\n' + 'STR ' + full_dot*stren + empty_dot * (10-stren) + '\n' + 'INT ' + full_dot*intell + empty_dot * (10-intell) + '\n' + 'CHA ' + full_dot*charis + empty_dot * (10-charis)

new_char = create_character('Dave', 4, 2, 1)

print(new_char)