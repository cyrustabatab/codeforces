


def games():

    num_teams = int(input())
    

    team_colors = []
    for _ in range(num_teams):
        colors= tuple(map(int,input().split()))
        team_colors.append(colors)



    
    count = 0
    for i in range(len(team_colors) -1 ):
        home_1,away_1 = team_colors[i]
        for j in range(i + 1,len(team_colors)):
            home_2,away_2 = team_colors[j]
            if home_1 == away_2:
                count += 1
            if home_2 == away_1:
                count += 1


    
    print(count)


games()

