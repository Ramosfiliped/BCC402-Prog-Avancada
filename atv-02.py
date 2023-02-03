# Classe para armazenar os dados de um competidor
class Contestant():
    # Número do competidor
    # Número de problemas resolvidos
    # Quais problemas ele já resolveu
    # Tempo acumulado
    def __init__(self, number : int) -> None:
        self.number = number
        self.count_problems_resolved = 0
        self.problems_resolved = []
        self.acumulated_time = 0

    # Adiciona se um problema foi enviado como incorreto ou correto
    # Acumula o tempo e adiciona na lista de problemas resolvidos caso ele tenha acertado
    def add_problem(self, problem : int, status : str, penalty : int):
        if status == 'C':
            self.count_problems_resolved += 1
            self.acumulated_time += penalty
            self.problems_resolved.append(problem)
        if status == 'I':
            self.acumulated_time += penalty

    def get_number(self):
        return self.number
    
    def get_count_problems_resolved(self):
        return self.count_problems_resolved

    def to_string(self):
        print(f"Number: {self.number}  Problems: {self.count_problems_resolved}  Time: {self.acumulated_time}")

# Classe para organizar os dados da competição
class Ranking():
    def __init__(self) -> None:
        self.contestants = []

    #Ordena o ranking
    def _order_ranking(self):
        # Primeiro ordena com base na quantidade de problemas resolvidoss
        self.contestants.sort(key=lambda x : x.count_problems_resolved)
        self.contestants = self.contestants[::-1]

        group_of_same_problems = []
        counter = 0
        # Depois agrupa os competidores
        # por quantidade de problemas resolvidos
        # e reordena com base no tempo acumulado
        for contest in self.contestants:
            if group_of_same_problems == []:
                group_of_same_problems.append(contest)
            elif group_of_same_problems[0].get_count_problems_resolved() == contest.get_count_problems_resolved():
                group_of_same_problems.append(contest)
            else:
                group_of_same_problems.sort(key=lambda x : x.acumulated_time)
                group_of_same_problems = group_of_same_problems[::-1]
                for c in group_of_same_problems:
                    self.contestants[counter] = c
                    counter = counter + 1
                group_of_same_problems = [] 



    def get_contestant_on_ranking(self, number : int):
        for c in self.contestants:
            if c.get_number() == number:
                return c
        
        return None

    def add_contestant(self, contestant : Contestant):
        self.contestants.append(contestant)

    def to_string(self):
        for cont in self.contestants:
            cont.to_string()

if __name__ == "__main__":
    ranking = Ranking()
    number_of_cases = int(input())
    input()
    for _ in range(number_of_cases):
        while(True):
            line = input()
            if line.strip() == "":
                line = input()
                if line.strip() == "":
                    break
                else:
                    continue

            contestant_number = int(line.split(" ")[0])
            problem = int(line.split(" ")[1])
            penalty_time = int(line.split(" ")[2])
            status_problem = str(line.split(" ")[3])
            
            contestant : Contestant = ranking.get_contestant_on_ranking(contestant_number)
            if contestant:
                contestant.add_problem(
                    problem=problem,
                    status=status_problem,
                    penalty=penalty_time
                )
            else:
                new_contestant : Contestant = Contestant(
                    number=contestant_number,
                )
                new_contestant.add_problem(
                    problem=problem,
                    status=status_problem,
                    penalty=penalty_time
                )
                ranking.add_contestant(new_contestant)

        ranking._order_ranking()
        ranking.to_string()


