import sys
sys.path.insert(0, '../')
from planet_wars import issue_order


def attack_weakest_enemy_planet(state):
    # (1) If we currently have a fleet in flight, abort plan.
    if len(state.my_fleets()) >= 1:
        return False

    # (2) Find my strongest planet.
    strongest_planet = max(state.my_planets(), key=lambda t: t.num_ships, default=None)

    # (3) Find the weakest enemy planet.
    weakest_planet = min(state.enemy_planets(), key=lambda t: t.num_ships, default=None)

    if not strongest_planet or not weakest_planet:
        # No legal source or destination
        return False
    else:
        # (4) Send half the ships from my strongest planet to the weakest enemy planet.
        return issue_order(state, strongest_planet.ID, weakest_planet.ID, strongest_planet.num_ships / 2)

def spread_to_weakest_neutral_planet(state):
    # (1) If we currently have a fleet in flight, just do nothing.
    if len(state.my_fleets()) >= 1:
        return False

    # (2) Find my strongest planet.
    strongest_planet = max(state.my_planets(), key=lambda p: p.num_ships, default=None)

    # (3) Find the weakest neutral planet.
    weakest_planet = min(state.neutral_planets(), key=lambda p: p.num_ships, default=None)

    if not strongest_planet or not weakest_planet:
        # No legal source or destination
        return False
    else:
        # (4) Send half the ships from my strongest planet to the weakest enemy planet.
        return issue_order(state, strongest_planet.ID, weakest_planet.ID, strongest_planet.num_ships / 2)

def defend_weakest_planet(state):
    my_planets = state.my_planets()
    if not my_planets:
        return False
    weakest_planet = min(my_planets, key=lambda p: p.num_ships)
    enemy_fleets = state.enemy_fleets()
    for fleet in enemy_fleets:
        if fleet.destination_planet == weakest_planet.ID:
            strongest_planet = max(my_planets, key=lambda p: p.num_ships)
            if strongest_planet and strongest_planet.num_ships > weakest_planet.num_ships:
                return issue_order(state, strongest_planet.ID, weakest_planet.ID, strongest_planet.num_ships // 2)
    return False

def attack_strongest_enemy_planet(state):
    if len(state.my_fleets()) >= 1:
        return False

    strongest_planet = max(state.my_planets(), key=lambda t: t.num_ships, default=None)
    strongest_enemy_planet = max(state.enemy_planets(), key=lambda t: t.num_ships, default=None)

    if not strongest_planet or not strongest_enemy_planet:
        return False
    else:
        return issue_order(state, strongest_planet.ID, strongest_enemy_planet.ID, strongest_planet.num_ships // 2)