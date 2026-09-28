# ===== Person =====
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


class Player(Person):
    def __str__(self):
        return f"Player {self.name}"


class Coach(Person):
    def __str__(self):
        return f"Coach {self.name}"


# ===== Team =====
class Team:
    def __init__(self, name, coach):
        self._name = name
        self._coach = coach
        self._players = []

    @property
    def name(self):
        return self._name

    @property
    def coach(self):
        return self._coach

    @property
    def players(self):
        return self._players

    def add_player(self, player):
        if not isinstance(player, Player):
            raise TypeError("Only Player instances allowed")
        self._players.append(player)

    def __str__(self):
        players = ", ".join(p.name for p in self._players)
        return f"{self._name} | Coach: {self._coach.name} | Players: {players}"


# ===== Match =====
class Match:
    def __init__(self, team1, team2):
        self._team1 = team1
        self._team2 = team2
        self._score = {
            team1.name: 0,
            team2.name: 0
        }

    @property
    def team1(self):
        return self._team1

    @property
    def team2(self):
        return self._team2

    def set_score(self, score1, score2):
        self._score[self._team1.name] = score1
        self._score[self._team2.name] = score2

    def winner(self):
        s1 = self._score[self._team1.name]
        s2 = self._score[self._team2.name]

        if s1 > s2:
            return self._team1
        elif s2 > s1:
            return self._team2
        return None

    def __str__(self):
        return (
            f"{self._team1.name} "
            f"{self._score[self._team1.name]} - "
            f"{self._score[self._team2.name]} "
            f"{self._team2.name}"
        )


# ===== Tournament =====
class Tournament:
    def __init__(self, name):
        self._name = name
        self._teams = []
        self._matches = []

    @property
    def teams(self):
        return self._teams

    @property
    def matches(self):
        return self._matches

    def add_team(self, team):
        if not isinstance(team, Team):
            raise TypeError("Team must be a Team instance")
        if team not in self._teams:
            self._teams.append(team)

    def add_match(self, match):
        if not isinstance(match, Match):
            raise TypeError("Match must be a Match instance")
        self._matches.append(match)

    def leaderboard(self):
        points = {team.name: 0 for team in self._teams}

        for match in self._matches:
            winner = match.winner()
            if winner:
                points[winner.name] += 3
            else:
                points[match.team1.name] += 1
                points[match.team2.name] += 1

        return sorted(points.items(), key=lambda x: x[1], reverse=True)

    def show_leaderboard(self):
        print(f"Tournament: {self._name}")
        for rank, (team, pts) in enumerate(self.leaderboard(), start=1):
            print(f"{rank}. {team} - {pts} pts")