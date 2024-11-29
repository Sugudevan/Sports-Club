import mysql.connector


conn=mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="14@Sugudevan",  # Replace with your MySQL password
        database="sports_club"
    )

# Add a team
def add_team():
    team_name = input("Enter team name: ")
    team_id = int(input("Enter the team id: "))
    cursor = conn.cursor()
    cursor.execute("INSERT INTO teams (team_name,team_id) VALUES (%s,%s)", (team_name,team_id))
    conn.commit()
    print("Team added successfully!")
    conn.close()

# Add a player
def add_player():
    player_name = input("Enter player name: ")
    age = int(input("Enter player age: "))
    position = input("Enter player position: ")
    team_id = int(input("Enter team ID: "))
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO players (player_name, age, position, team_id) VALUES (%s, %s, %s, %s)",
        (player_name, age, position, team_id)
    )
    conn.commit()
    print("Player added successfully!")
    conn.close()

# View all teams
def view_teams():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM teams")
    teams = cursor.fetchall()
    print("\nTeams:")
    for team in teams:
        print(f"ID: {team[0]}, Name: {team[1]}")
    conn.close()    

# View players in a team
def view_players():
    team_id = int(input("Enter team ID to view players: "))
    cursor = conn.cursor()
    cursor.execute(
        """SELECT p.player_id, p.player_name, p.age, t.team_name, p.position
            FROM players p
            join teams t
            on p.team_id = t.team_id
            WHERE t.team_id = %s""",
            (team_id,)

    )
    players = cursor.fetchall()
    print("\nPlayers:")
    for player in players:
        print(f"ID: {player[0]}\nName: {player[1]}\nAge: {player[2]}\nGame: {player[3]}\nPosition: {player[4]}")
    conn.close()

# Update a player's information
def update_player():
    player_id = int(input("Enter player ID to update: "))
    new_name = input("Enter new player name: ")
    new_age = int(input("Enter new age: "))
    new_position = input("Enter new position: ")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE players SET player_name = %s, age = %s, position = %s WHERE player_id = %s",
        (new_name, new_age, new_position, player_id)
    )
    conn.commit()
    print("Player information updated successfully!")
    conn.close()    

# Delete a player
def delete_player():
    player_id = int(input("Enter player ID to delete: "))
    cursor = conn.cursor()
    cursor.execute("DELETE FROM players WHERE player_id = %s", (player_id,))
    conn.commit()
    print("Player deleted successfully!")
    conn.close()    
# Menu
def menu():
    while True:
        print("\nSports Club Administration Portal")
        print("1. Add Team")
        print("2. Add Player")
        print("3. View Teams")
        print("4. View Players in a Team")
        print("5. Update Player Information")
        print("6. Delete Player")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            add_team()
        elif choice == 2:
            add_player()
        elif choice == 3:
            view_teams()
        elif choice == 4:
            view_players()
        elif choice == 5:
            update_player()
        elif choice == 6:
            delete_player()
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu
if __name__ == "__main__":
    menu()