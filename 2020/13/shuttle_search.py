#!/usr/bin/env python

def parse_input_file(filename: str):

    with open(filename) as input_file:

        lines = input_file.read().splitlines()
        our_time = int(lines[0])
        bus_ids = []
        for bus_id_str in lines[1].split(','):
            if bus_id_str == 'x':
                continue
            bus_ids.append(int(bus_id_str))

    return (our_time, sorted(bus_ids))


def earliest_bus_time(our_time, bus_id):
    close_bus_time = int(our_time/bus_id) * bus_id
    if close_bus_time != our_time:
        close_bus_time += bus_id
    return close_bus_time


def find_best_bus(our_time, bus_ids):
    earliest_bus = None
    earliest_time = None
    for bus_id in bus_ids:
        bus_time = earliest_bus_time(our_time, bus_id)
        if earliest_time and bus_time < earliest_time:
            earliest_time = bus_time
            earliest_bus = bus_id
        elif earliest_time is None:
            earliest_bus = bus_id
            earliest_time = bus_time
    return (earliest_bus, earliest_time)


def main():
    parsed_input = parse_input_file("input.txt")
    our_time, bus_ids = parsed_input
    best_bus, best_time = find_best_bus(our_time, bus_ids)
    wait_time = best_time - our_time
    part_1_result = wait_time * best_bus
    print(f"Part 1: {part_1_result}")

    part_2_result = None
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
