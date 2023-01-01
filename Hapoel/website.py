import csv

def read_info():
    f = open(r"files/players.csv", 'r')
    reader = csv.reader(f)

    players = {}

    fields = next(reader)

    for line in reader:
        players[line[-1]] = line

    print(players)

    f.close()

    return players

def make_html(player_info):
    html_file = open(r"files/hb7/template.htm", "r", encoding="utf-8")
    html_text = html_file.read()
    html_file.close()

    for player in player_info.items():
        f = open(f"files/hb7/{player[0]}.htm", "w", encoding="utf-8")
        player_html = html_text
        player_html = player_html.replace("%%name%%", player[1][1])
        player_html = player_html.replace("%%birth%%", player[1][0])
        player_html = player_html.replace("%%number%%", player[1][2])
        player_html = player_html.replace("%%position%%", player[1][-2])
        player_html = player_html.replace("%%id%%", player[1][-1])
        f.write(player_html)
        f.close()

if __name__ == "__main__":
    players_info = read_info()
    make_html(players_info)
