import random
import time


class Nim:
    def __init__(self, initial=None):
        if initial is None:
            initial = [1, 3, 5, 7]
        self.piles = initial.copy()
        self.player = 0
        self.winner = None

    @staticmethod
    def available_actions(piles):
        actions = set()
        for i, pile in enumerate(piles):
            for j in range(1, pile + 1):
                actions.add((i, j))
        return actions

    @staticmethod
    def other_player(player):
        return 1 - player

    def switch_player(self):
        self.player = self.other_player(self.player)

    def move(self, action):
        pile, count = action
        if self.winner is not None:
            raise Exception("Game already won")
        if pile < 0 or pile >= len(self.piles):
            raise Exception("Invalid pile")
        if count < 1 or count > self.piles[pile]:
            raise Exception("Invalid number of objects")

        self.piles[pile] -= count
        self.switch_player()

        if all(pile == 0 for pile in self.piles):
            self.winner = self.player


class NimAI:
    def __init__(self, alpha=0.5, epsilon=0.1):
        self.q = {}
        self.alpha = alpha
        self.epsilon = epsilon

    def update(self, old_state, action, new_state, reward):
        old_q = self.get_q_value(old_state, action)
        best_future = self.best_future_reward(new_state)
        self.update_q_value(old_state, action, old_q, reward, best_future)

    def get_q_value(self, state, action):
        state = tuple(state)
        return self.q.get(state, {}).get(action, 0)

    def update_q_value(self, state, action, old_q, reward, future_rewards):
        state = tuple(state)
        new_value_estimate = reward + future_rewards
        if state not in self.q:
            self.q[state] = {}
        self.q[state][action] = old_q + self.alpha * (new_value_estimate - old_q)

    def best_future_reward(self, state):
        state = tuple(state)
        if state not in self.q:
            return 0
        return max(self.q[state].values(), default=0)

    def choose_action(self, state, epsilon=True):
        available_actions = list(Nim.available_actions(state))
        if not available_actions:
            return None

        if epsilon and random.random() < self.epsilon:
            return random.choice(available_actions)

        q_values = [(action, self.get_q_value(state, action)) for action in available_actions]
        max_q_value = max(q_values, key=lambda x: x[1], default=(None, 0))[1]

        best_actions = [action for action, q_value in q_values if q_value == max_q_value]
        return random.choice(best_actions) if best_actions else None


def train(n):
    player = NimAI()

    for i in range(n):
        print(f"Playing training game {i + 1}")
        game = Nim()
        last = {0: {"state": None, "action": None}, 1: {"state": None, "action": None}}

        while True:
            state = game.piles.copy()
            action = player.choose_action(game.piles)

            last[game.player]["state"] = state
            last[game.player]["action"] = action

            game.move(action)
            new_state = game.piles.copy()

            if game.winner is not None:
                player.update(state, action, new_state, -1)
                player.update(last[game.player]["state"], last[game.player]["action"], new_state, 1)
                break

            if last[game.player]["state"] is not None:
                player.update(last[game.player]["state"], last[game.player]["action"], new_state, 0)

    print("Done training")
    return player


def play(ai, human_player=None):
    if human_player is None:
        human_player = random.randint(0, 1)

    game = Nim()

    while True:
        print("\nPiles:")
        for i, pile in enumerate(game.piles):
            print(f"Pile {i}: {pile}")

        available_actions = Nim.available_actions(game.piles)
        time.sleep(1)

        if game.player == human_player:
            print("Your Turn")
            while True:
                pile = int(input("Choose Pile: "))
                count = int(input("Choose Count: "))
                if (pile, count) in available_actions:
                    break
                print("Invalid move, try again.")
        else:
            print("AI's Turn")
            pile, count = ai.choose_action(game.piles, epsilon=False)
            print(f"AI chose to take {count} from pile {pile}.")

        game.move((pile, count))

        if game.winner is not None:
            print("\nGAME OVER")
            winner = "Human" if game.winner == human_player else "AI"
            print(f"Winner is {winner}")
            return