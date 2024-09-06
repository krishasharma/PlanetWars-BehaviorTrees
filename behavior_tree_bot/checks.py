

def if_neutral_planet_available(state):
    return any(state.neutral_planets())


def have_largest_fleet(state):
    return sum(planet.num_ships for planet in state.my_planets()) \
             + sum(fleet.num_ships for fleet in state.my_fleets()) \
           > sum(planet.num_ships for planet in state.enemy_planets()) \
             + sum(fleet.num_ships for fleet in state.enemy_fleets())

def if_under_attack(state):
    my_planets = state.my_planets()
    enemy_fleets = state.enemy_fleets()
    for fleet in enemy_fleets:
        if any(fleet.destination_planet == p.ID for p in my_planets):
            return True
    return False