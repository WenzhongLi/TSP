#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''
import sys
import generator
import itertools
import copy

class TSP(object):
    def __init__(self):
        return

    def run_tsp(self, map, size):
        result = 0
        all_node = []
        for n in range(size):
            all_node.append(n)
        path_for_all_start = dict()
        min_path_for_all_start = dict()
        for start in range(size):
            removed_list = copy.deepcopy(all_node)
            removed_list.remove(start)
            path_for_current_start = dict()
            path_for_current_start_two_element = dict()
            path_for_current_start[2] = path_for_current_start_two_element
            for j in range(size):
                if j == start:
                    continue
                two_node_list = [start, j]
                two_node_list_sorted = sorted(two_node_list)
                path_for_current_start_two_element[(start, tuple(two_node_list_sorted), j)] = two_node_list
            for set_size in range(3, size+1):
                path_for_current_start_num_of_element = dict()
                path_for_current_start[set_size] = path_for_current_start_num_of_element
                all_node_list_with_out_count_current_start = copy.copy(all_node)
                all_node_list_with_out_count_current_start.remove(start)
                for subset in itertools.combinations(all_node_list_with_out_count_current_start, set_size-1):
                    set_list = list(subset)
                    set_list.append(start)
                    set_list = sorted(set_list)
                    for current_end in subset:
                        if current_end == start:
                            print subset, current_end
                            continue
                        set_list_with_out_current_end = copy.copy(set_list)
                        set_list_with_out_current_end.remove(current_end)
                        path_for_last_start_num_of_element = path_for_current_start[set_size-1]
                        # (start,subset,end)
                        min_cost = -1
                        min_path = []
                        for last_internode in set_list_with_out_current_end:
                            if last_internode == start:
                                #print set_list_with_out_current_end, last_internode
                                continue
                            mid_list = copy.deepcopy(set_list)
                            mid_list.remove(current_end)
                            #mid_list.insert(0,start)
                            if (start,tuple(mid_list),last_internode) in path_for_last_start_num_of_element:
                                mid_path = path_for_last_start_num_of_element[(start, tuple(mid_list), last_internode)]
                                current_cost = self.countcost(map, mid_path)
                                if min_cost == -1 or min_cost > current_cost + map[last_internode][current_end]:
                                    min_cost = current_cost + map[last_internode][current_end]
                                    min_path = copy.deepcopy(mid_path)
                                    min_path.append(current_end)
                        if min_cost != -1:
                            current_size_path = path_for_current_start[set_size]
                            current_size_path[(start, tuple(sorted(min_path)), current_end)] = min_path
            path_for_all_start[start] = path_for_current_start
            min_path_for_current_start = []
            min_length_for_current_start = -1
            last_step_map = path_for_current_start[size]
            for path in last_step_map:
                length_of_current = self.countcost(map,last_step_map[path])
                if min_length_for_current_start == -1 \
                        or min_length_for_current_start > length_of_current + map[path[0]][path[2]]:
                    min_length_for_current_start = length_of_current + map[path[0]][path[2]]
                    min_path_for_current_start = copy.copy(last_step_map[path])
                    min_path_for_current_start.append(start)
            if min_length_for_current_start != -1:
                min_path_for_all_start[start] = (min_length_for_current_start, min_path_for_current_start)
                self.countcost(map,min_path_for_current_start)
                print min_path_for_current_start
            else:
                print "error"

        print min_path_for_all_start
        return result

    def countcost(self, map, path):
        last = -1
        cost = 0
        for node in path:
            if last == -1:
                last = node
            else:
                cost += map[node][last]
                last = node
        return cost


if __name__ == "__main__":
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argment", i, sys.argv[i]
    print ('start initialize')
    tsp = TSP()
    size = 10
    max_length = 100
    generator = generator.Generator(size, max_length)
    generator.paint_random()
    generator.print_matrix()
    r = tsp.run_tsp(generator.get_matrix(), size)
    print r
