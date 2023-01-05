import csv

HTML_TEMPLATE = r"files/hb7/template.htm"
PLAYERS_CSV = r"files/players.csv"

def read_info():
    """read the csv file and save the header of each column in csv_fields,
       go over all the players in the csv file, make a new dictionary for each id and assign field values"""
    with open(PLAYERS_CSV, 'r') as f:
        players = csv.reader(f)
        players_dict = {}
        csv_fields = next(players)
        player_index = 1

        for player in players:
            players_dict[player_index] = {}
            field_index = 0
            for field in csv_fields:
                players_dict[player_index][field] = player[field_index]
                field_index+=1
            player_index += 1

        return players_dict, csv_fields

def make_html(player_info, csv_fields):
    """copy html template into string to use as template for each player html,
        go over every player in the dict and make a new file for them,
        replace every field from the csv headers with values, write the modified html into the new file"""
    with open(HTML_TEMPLATE , "r", encoding="utf-8") as html_file:
        html_text = html_file.read()

    for player in player_info.keys():
        with open(f"files/hb7/{player_info[player]['id']}.htm", "w", encoding="utf-8") as f:
            player_html = html_text
            for field in csv_fields:
                player_html = player_html.replace(f"%%{field}%%", player_info[player][field])
            f.write(player_html)

if __name__ == "__main__":
    players_info, csv_fields = read_info()
    make_html(players_info, csv_fields)