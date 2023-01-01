import csv

def read_info():
    f = open(r"files/players.csv", 'r')
    reader = csv.reader(f)
    players = {}
    fields = next(reader)

    """ saving the info of each player as a list 
    
    for line in reader:
        players[line[-1]] = line
    """

    for player in reader:
        players[player[-1]] = {}
        index = 0
        for field in fields:
            players[player[-1]][field] = player[index]
            index+=1
    print(players)
    f.close()

    return players, fields

def make_html(player_info, fields):
    html_file = open(r"files/hb7/template.htm", "r", encoding="utf-8")
    html_text = html_file.read()
    html_file.close()


    for player in player_info.keys():
        f = open(f"files/hb7/{player}.htm", "w", encoding="utf-8")
        player_html = html_text
        for field in fields:
            player_html = player_html.replace(f"%%{field}%%", player_info[player][field])
        f.write(player_html)
        f.close()

if __name__ == "__main__":
    players_info, fields = read_info()
    make_html(players_info, fields)
