import csv

def read_info():
    #read the csv file and save the header of each column in fields
    f = open(r"files/players.csv", 'r')
    players = csv.reader(f)
    players_dict = {}
    fields = next(players)

    for player in players: #go over all the players in the csv file, make a new dictionary for each id and assign field values
        players_dict[player[-1]] = {}
        index = 0
        for field in fields:
            players_dict[player[-1]][field] = player[index] #assign new dictionary for each field assign value from player
            index+=1
    print(players_dict)
    f.close()

    return players_dict, fields

def make_html(player_info, fields):
    html_file = open(r"files/hb7/template.htm", "r", encoding="utf-8")
    html_text = html_file.read()
    html_file.close() #copy html template into string to use as template for each player html

    for player in player_info.keys(): #go over every player in the dict and make a new file for them
        f = open(f"files/hb7/{player}.htm", "w", encoding="utf-8")
        player_html = html_text
        for field in fields:
            player_html = player_html.replace(f"%%{field}%%", player_info[player][field]) #replace every field from the csv header line with values
        f.write(player_html) #write the modified html into the new file
        f.close()

if __name__ == "__main__":
    players_info, fields = read_info()
    make_html(players_info, fields)