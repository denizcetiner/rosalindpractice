from graphviz import Digraph


class RabbitPairMonth:
    life_expectancy = -1
    give_birth_to = 3
    id_counter = 1
    maturity_month = 1

    def __init__(self, id, birth_time, current_month):
        self.id = id
        self.birth_time = birth_time
        self.current_month = current_month
        self.children = []
        self.older = None

    def __str__(self):
        return "ID={0}, M={1}, B={2}".format(self.id, self.current_month, self.birth_time)

    @staticmethod
    def get_next_id() -> int:
        result = RabbitPairMonth.id_counter
        RabbitPairMonth.id_counter += 1
        return result

    def is_pair_dying(self) -> bool:
        return (self.current_month - self.birth_time) == RabbitPairMonth.life_expectancy - 1

    def is_mature(self) -> bool:
        return (self.current_month - self.birth_time) >= RabbitPairMonth.maturity_month

    def give_birth(self):
        if self.is_mature():
            for i in range(RabbitPairMonth.give_birth_to):
                id_for_child = RabbitPairMonth.get_next_id()
                child_pair = RabbitPairMonth(id_for_child, self.current_month + 1, self.current_month + 1)
                self.children.append(child_pair)

    def grow_older(self):
        alive_next_month = not self.is_pair_dying()
        if alive_next_month:
            self.older = RabbitPairMonth(self.id, self.birth_time, self.current_month + 1)

    def create_next_month(self):
        self.give_birth()
        self.grow_older()


def create_wabbits_heritage(adam_and_eve: 'RabbitPairMonth', observe_for_months: int):
    rabbits_heap_tree = [adam_and_eve]
    index_rabbits_heap_tree = 0
    while index_rabbits_heap_tree < len(rabbits_heap_tree):
        current_pair = rabbits_heap_tree[index_rabbits_heap_tree]
        current_month = current_pair.current_month

        if current_month > observe_for_months:
            break

        current_pair.create_next_month()
        rabbits_heap_tree.extend(current_pair.children)
        if current_pair.older is not None:
            rabbits_heap_tree.append(current_pair.older)
        index_rabbits_heap_tree += 1
    return rabbits_heap_tree


def create_graph(heap_tree: []):
    dot = Digraph(comment='Wabbits Breeding By Month')
    dot.attr(rankdir="LR")
    i = 0
    root = heap_tree[i]
    current = root
    while current.older is not None or len(current.children) > 0:
        if current.older is not None:
            dot.edge(str(current), str(current.older))
        for child in current.children:
            dot.edge(str(current), str(child))
        i += 1
        if i >= len(heap_tree):
            break
        else:
            current = heap_tree[i]
    dot_source = dot.source


def run(input="5 3", maturity_in_months=1):
    params = input.split()
    months = int(params[0])
    gives_birth_to_pairs = int(params[1])
    starting_month = 1
    adam_and_eve = RabbitPairMonth(RabbitPairMonth.get_next_id(), starting_month, starting_month)
    wabbits_heritage = create_wabbits_heritage(adam_and_eve, months)

    create_graph(wabbits_heritage)

    count_of_months = 0
    for pair_month in wabbits_heritage:
        if pair_month.current_month == months:
            count_of_months += 1
    print(count_of_months)
    return  count_of_months