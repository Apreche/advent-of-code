#!/usr/bin/env python

import math


def parse_input_file(filename: str):

    with open(filename) as input_file:

        lines = input_file.read().splitlines()
        our_time = int(lines[0])
        clean_bus_ids = []
        bus_ids = []
        second_line = lines[1].split(',')
        for bus_id_str in second_line:
            if bus_id_str == 'x':
                bus_ids.append('x')
            else:
                bus_id_int = int(bus_id_str)
                clean_bus_ids.append(bus_id_int)
                bus_ids.append(bus_id_int)

    return (our_time, sorted(clean_bus_ids), bus_ids)


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


def check_schedule(bus_schedule, bus_ids):
    for offset, bus_id in enumerate(bus_ids):
        if bus_id != 'x':
            if bus_id not in bus_schedule[offset]:
                return False
    return True


def find_special_departure_fastest(bus_ids):
    # Stolen from https://streamable.com/tojflp
    offset_ids = [(offset, bus_id) for offset, bus_id in enumerate(bus_ids) if bus_id != 'x']
    first_offset, first_bus = offset_ids[0]
    time = 0
    matched_buses = [first_bus]
    while len(matched_buses) < len(offset_ids):
        time += math.prod(matched_buses)
        for offset, bus in offset_ids:
            buscheck = ((time + offset) % bus)
            if bus not in matched_buses:
                if buscheck == 0:
                    matched_buses.append(bus)
    return time


def find_special_departure_faster(bus_ids, clean_bus_ids):
    # Better one I came up with myself
    max_bus = max(clean_bus_ids)
    max_bus_offset = bus_ids.index(max_bus)
    current_time = 0 - max_bus_offset
    found_result = False
    while not found_result:
        current_time += max_bus
        for bus_id in clean_bus_ids:
            offset = bus_ids.index(bus_id)
            if (current_time + offset) % bus_id != 0:
                break
            if bus_id == clean_bus_ids[-1]:
                found_result = True
    return current_time


def find_special_departure_slow(bus_ids):
    # The first correct one I came up with myself
    found_result = False
    current_minute = 0
    bus_schedule = []
    max_offset = len(bus_ids)
    while not found_result:
        current_minute += 1
        departing_buses = []
        for bus in bus_ids:
            if bus != 'x':
                if current_minute % bus == 0:
                    departing_buses.append(bus)
        bus_schedule.append(departing_buses)
        if len(bus_schedule) > max_offset:
            bus_schedule.pop(0)
        if len(bus_schedule) == max_offset:
            found_result = check_schedule(
                bus_schedule,
                bus_ids
            )
    return current_minute - (max_offset - 1)


def main():
    parsed_input = parse_input_file("input.txt")
    our_time, clean_bus_ids, bus_ids = parsed_input
    best_bus, best_time = find_best_bus(
        our_time, clean_bus_ids
    )
    wait_time = best_time - our_time
    part_1_result = wait_time * best_bus
    print(f"Part 1: {part_1_result}")

    part_2_result = find_special_departure_fastest(bus_ids)
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
