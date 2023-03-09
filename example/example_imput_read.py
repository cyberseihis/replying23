

#datastructure defined there or own module 
#this datastructure is problem space related

class Pandora:
    #placeholder class
    ...

class Demon:
    #placeholder class
    ...

#this maybe has a better name if it is called optimalization
class Simulation:
    ...

#if there are multiple type of objects, we can use match
#https://peps.python.org/pep-0636/
#https://docs.python.org/3/tutorial/controlflow.html#match-statements


def main(dataset_name):
    print(f"working on {dataset_name}")
    with open(dataset_name) as f:
        firstline = f.readline().split()
        stamina_pandora = int(firstline[0])
        max_stamina = int(firstline[1])
        turns = int(firstline[2])

        pandorina = Pandora(stamina_pandora, max_stamina)
        print(f"Pandora: {pandorina}")

        n_demons = int(firstline[3])
        demons: list[Demon] = []
        for i in range(n_demons):
            line = f.readline().split()
            required_stamina = int(line[0])
            rest_time = int(line[1])
            recovery = int(line[2])
            fragments = []
            if line[3] != 0:
                fragments: list[int] = [int(x) for x in line[4:-1] + [line[-1]]]
            demons.append(Demon(i, required_stamina, rest_time, recovery, fragments))

        simulation = Simulation(dataset_name, turns, pandorina, demons)
        simulation.run()

        print("Defeated demons:")
        for demon in simulation.defeated:
            print(demon)
        print("Remaining demons:")
        for demon in simulation.demons:
            print(demon)
        print(f"Pandora: {pandorina}")

        filename: str = dataset_name.replace("./datasets/", "").replace(".txt", "")
        simulation.write_solution(filename)