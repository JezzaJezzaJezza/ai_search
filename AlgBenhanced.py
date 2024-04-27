############
############ ALTHOUGH I GIVE YOU THIS TEMPLATE PROGRAM WITH THE NAME 'skeleton.py', 
############ YOU CAN RENAME IT TO ANYTHING YOU LIKE. HOWEVER, FOR THE PURPOSES OF 
############ THE EXPLANATION IN THESE COMMENTS, I ASSUME THAT THIS PROGRAM IS STILL 
############ CALLED 'skeleton.py'.
############
############ IF YOU WISH TO IMPORT STANDARD MODULES, YOU CAN ADD THEM AFTER THOSE BELOW.
############ NOTE THAT YOU ARE NOT ALLOWED TO IMPORT ANY NON-STANDARD MODULES! TO SEE
############ THE STANDARD MODULES, TAKE A LOOK IN 'validate_before_handin.py'.
############
############ DO NOT INCLUDE ANY COMMENTS ON A LINE WHERE YOU IMPORT A MODULE.
############

import os
import sys
import time
import random

############ START OF SECTOR 0 (IGNORE THIS COMMENT)
############
############ NOW PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS.
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############ BY 'DO NOT TOUCH' I REALLY MEAN THIS. EVEN CHANGING THE SYNTAX, BY
############ ADDING SPACES OR COMMENTS OR LINE RETURNS AND SO ON, COULD MEAN THAT
############ CODES MIGHT NOT RUN WHEN I RUN THEM!
############

def read_file_into_string(input_file, ord_range):
    the_file = open(input_file, 'r') 
    current_char = the_file.read(1) 
    file_string = ""
    length = len(ord_range)
    while current_char != "":
        i = 0
        while i < length:
            if ord(current_char) >= ord_range[i][0] and ord(current_char) <= ord_range[i][1]:
                file_string = file_string + current_char
                i = length
            else:
                i = i + 1
        current_char = the_file.read(1)
    the_file.close()
    return file_string

def remove_all_spaces(the_string):
    length = len(the_string)
    new_string = ""
    for i in range(length):
        if the_string[i] != " ":
            new_string = new_string + the_string[i]
    return new_string

def integerize(the_string):
    length = len(the_string)
    stripped_string = "0"
    for i in range(0, length):
        if ord(the_string[i]) >= 48 and ord(the_string[i]) <= 57:
            stripped_string = stripped_string + the_string[i]
    resulting_int = int(stripped_string)
    return resulting_int

def convert_to_list_of_int(the_string):
    list_of_integers = []
    location = 0
    finished = False
    while finished == False:
        found_comma = the_string.find(',', location)
        if found_comma == -1:
            finished = True
        else:
            list_of_integers.append(integerize(the_string[location:found_comma]))
            location = found_comma + 1
            if the_string[location:location + 5] == "NOTE=":
                finished = True
    return list_of_integers

def build_distance_matrix(num_cities, distances, city_format):
    dist_matrix = []
    i = 0
    if city_format == "full":
        for j in range(num_cities):
            row = []
            for k in range(0, num_cities):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    elif city_format == "upper_tri":
        for j in range(0, num_cities):
            row = []
            for k in range(j):
                row.append(0)
            for k in range(num_cities - j):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    else:
        for j in range(0, num_cities):
            row = []
            for k in range(j + 1):
                row.append(0)
            for k in range(0, num_cities - (j + 1)):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    if city_format == "upper_tri" or city_format == "strict_upper_tri":
        for i in range(0, num_cities):
            for j in range(0, num_cities):
                if i > j:
                    dist_matrix[i][j] = dist_matrix[j][i]
    return dist_matrix

def read_in_algorithm_codes_and_tariffs(alg_codes_file):
    flag = "good"
    code_dictionary = {}   
    tariff_dictionary = {}  
    if not os.path.exists(alg_codes_file):
        flag = "not_exist"  
        return code_dictionary, tariff_dictionary, flag
    ord_range = [[32, 126]]
    file_string = read_file_into_string(alg_codes_file, ord_range)  
    location = 0
    EOF = False
    list_of_items = []  
    while EOF == False: 
        found_comma = file_string.find(",", location)
        if found_comma == -1:
            EOF = True
            sandwich = file_string[location:]
        else:
            sandwich = file_string[location:found_comma]
            location = found_comma + 1
        list_of_items.append(sandwich)
    third_length = int(len(list_of_items)/3)
    for i in range(third_length):
        code_dictionary[list_of_items[3 * i]] = list_of_items[3 * i + 1]
        tariff_dictionary[list_of_items[3 * i]] = int(list_of_items[3 * i + 2])
    return code_dictionary, tariff_dictionary, flag

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY!
############
############ THE RESERVED VARIABLE 'input_file' IS THE CITY FILE UNDER CONSIDERATION.
############
############ IT CAN BE SUPPLIED BY SETTING THE VARIABLE BELOW OR VIA A COMMAND-LINE
############ EXECUTION OF THE FORM 'python skeleton.py city_file.txt'. WHEN SUPPLYING
############ THE CITY FILE VIA A COMMAND-LINE EXECUTION, ANY ASSIGNMENT OF THE VARIABLE
############ 'input_file' IN THE LINE BELOW iS SUPPRESSED.
############
############ IT IS ASSUMED THAT THIS PROGRAM 'skeleton.py' SITS IN A FOLDER THE NAME OF
############ WHICH IS YOUR USER-NAME, E.G., 'abcd12', WHICH IN TURN SITS IN ANOTHER
############ FOLDER. IN THIS OTHER FOLDER IS THE FOLDER 'city-files' AND NO MATTER HOW
############ THE NAME OF THE CITY FILE IS SUPPLIED TO THIS PROGRAM, IT IS ASSUMED THAT 
############ THE CITY FILE IS IN THE FOLDER 'city-files'.
############
############ END OF SECTOR 0 (IGNORE THIS COMMENT)

input_file = "AISearchfile180.txt"

############ START OF SECTOR 1 (IGNORE THIS COMMENT)
############
############ PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS STARTING
############ 'HAVE YOU TOUCHED ...'
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############

if len(sys.argv) > 1:
    input_file = sys.argv[1]

############ END OF SECTOR 1 (IGNORE THIS COMMENT)

############ START OF SECTOR 2 (IGNORE THIS COMMENT)
path_for_city_files = os.path.join("..", "city-files")
############ END OF SECTOR 2 (IGNORE THIS COMMENT)

############ START OF SECTOR 3 (IGNORE THIS COMMENT)
if os.path.isfile(path_for_city_files + "/" + input_file):
    ord_range = [[32, 126]]
    file_string = read_file_into_string(path_for_city_files + "/" + input_file, ord_range)
    file_string = remove_all_spaces(file_string)
    print("I have found and read the input file " + input_file + ":")
else:
    print("*** error: The city file " + input_file + " does not exist in the city-file folder.")
    sys.exit()

location = file_string.find("SIZE=")
if location == -1:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()
    
comma = file_string.find(",", location)
if comma == -1:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()
    
num_cities_as_string = file_string[location + 5:comma]
num_cities = integerize(num_cities_as_string)
print("   the number of cities is stored in 'num_cities' and is " + str(num_cities))

comma = comma + 1
stripped_file_string = file_string[comma:]
distances = convert_to_list_of_int(stripped_file_string)

counted_distances = len(distances)
if counted_distances == num_cities * num_cities:
    city_format = "full"
elif counted_distances == (num_cities * (num_cities + 1))/2:
    city_format = "upper_tri"
elif counted_distances == (num_cities * (num_cities - 1))/2:
    city_format = "strict_upper_tri"
else:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()

dist_matrix = build_distance_matrix(num_cities, distances, city_format)
print("   the distance matrix 'dist_matrix' has been built.")

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY!
############
############ YOU NOW HAVE THE NUMBER OF CITIES STORED IN THE INTEGER VARIABLE 'num_cities'
############ AND THE TWO_DIMENSIONAL MATRIX 'dist_matrix' HOLDS THE INTEGER CITY-TO-CITY 
############ DISTANCES SO THAT 'dist_matrix[i][j]' IS THE DISTANCE FROM CITY 'i' TO CITY 'j'.
############ BOTH 'num_cities' AND 'dist_matrix' ARE RESERVED VARIABLES AND SHOULD FEED
############ INTO YOUR IMPLEMENTATIONS.
############
############ THERE NOW FOLLOWS CODE THAT READS THE ALGORITHM CODES AND TARIFFS FROM
############ THE TEXT-FILE 'alg_codes_and_tariffs.txt' INTO THE RESERVED DICTIONARIES
############ 'code_dictionary' AND 'tariff_dictionary'. DO NOT AMEND THIS CODE!
############ THE TEXT FILE 'alg_codes_and_tariffs.txt' SHOULD BE IN THE SAME FOLDER AS
############ THE FOLDER 'city-files' AND THE FOLDER WHOSE NAME IS YOUR USER-NAME.
############
############ PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS STARTING
############ 'HAVE YOU TOUCHED ...'
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############
############ END OF SECTOR 3 (IGNORE THIS COMMENT)

############ START OF SECTOR 4 (IGNORE THIS COMMENT)
path_for_alg_codes_and_tariffs = os.path.join("..", "alg_codes_and_tariffs.txt")
############ END OF SECTOR 4 (IGNORE THIS COMMENT)

############ START OF SECTOR 5 (IGNORE THIS COMMENT)
code_dictionary, tariff_dictionary, flag = read_in_algorithm_codes_and_tariffs(path_for_alg_codes_and_tariffs)

if flag != "good":
    print("*** error: The text file 'alg_codes_and_tariffs.txt' does not exist.")
    sys.exit()

print("The codes and tariffs have been read from 'alg_codes_and_tariffs.txt':")

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY! SORRY TO GO ON ABOUT THIS BUT YOU NEED TO BE 
############ AWARE OF THIS FACT!
############
############ YOU NOW NEED TO SUPPLY SOME PARAMETERS.
############
############ THE RESERVED STRING VARIABLE 'my_user_name' SHOULD BE SET AT YOUR
############ USER-NAME, E.G., "abcd12"
############
############ END OF SECTOR 5 (IGNORE THIS COMMENT)

my_user_name = "hrwv51"

############ START OF SECTOR 6 (IGNORE THIS COMMENT)
############
############ YOU CAN SUPPLY, IF YOU WANT, YOUR FULL NAME. THIS IS NOT USED AT ALL BUT SERVES AS
############ AN EXTRA CHECK THAT THIS FILE BELONGS TO YOU. IF YOU DO NOT WANT TO SUPPLY YOUR
############ NAME THEN EITHER SET THE STRING VARIABLES 'my_first_name' AND 'my_last_name' AT 
############ SOMETHING LIKE "Mickey" AND "Mouse" OR AS THE EMPTY STRING (AS THEY ARE NOW;
############ BUT PLEASE ENSURE THAT THE RESERVED VARIABLES 'my_first_name' AND 'my_last_name'
############ ARE SET AT SOMETHING).
############
############ END OF SECTOR 6 (IGNORE THIS COMMENT)

my_first_name = "Jeremy"
my_last_name = "Mariani"

############ START OF SECTOR 7 (IGNORE THIS COMMENT)
############
############ YOU NEED TO SUPPLY THE ALGORITHM CODE IN THE RESERVED STRING VARIABLE 'algorithm_code'
############ FOR THE ALGORITHM YOU ARE IMPLEMENTING. IT NEEDS TO BE A LEGAL CODE FROM THE TEXT-FILE
############ 'alg_codes_and_tariffs.txt' (READ THIS FILE TO SEE THE CODES).
############
############ END OF SECTOR 7 (IGNORE THIS COMMENT)

algorithm_code = "GA"

############ START OF SECTOR 8 (IGNORE THIS COMMENT)
############
############ PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS STARTING
############ 'HAVE YOU TOUCHED ...'
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############

if not algorithm_code in code_dictionary:
    print("*** error: the algorithm code " + algorithm_code + " is illegal")
    sys.exit()
print("   your algorithm code is legal and is " + algorithm_code + " -" + code_dictionary[algorithm_code] + ".")

start_time = time.time()

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY! SORRY TO GO ON ABOUT THIS BUT YOU NEED TO BE 
############ AWARE OF THIS FACT!
############
############ YOU CAN ADD A NOTE THAT WILL BE ADDED AT THE END OF THE RESULTING TOUR FILE IF YOU LIKE,
############ E.G., "in my basic greedy search, I broke ties by always visiting the first 
############ city found" BY USING THE RESERVED STRING VARIABLE 'added_note' OR LEAVE IT EMPTY
############ IF YOU WISH. THIS HAS NO EFFECT ON MARKS BUT HELPS YOU TO REMEMBER THINGS ABOUT
############ YOUR TOUR THAT YOU MIGHT BE INTERESTED IN LATER. NOTE THAT I CALCULATE THE TIME OF
############ A RUN USING THE RESERVED VARIABLE 'start_time' AND INCLUDE THE RUN-TIME IN 'added_note' LATER.
############
############ IN FACT, YOU CAN INCLUDE YOUR ADDED NOTE IMMEDIATELY BELOW OR EVEN INCLUDE YOUR ADDED NOTE
############ AT ANY POINT IN YOUR PROGRAM: JUST DEFINE THE STRING VARIABLE 'added_note' WHEN YOU WISH
############ (BUT DON'T REMOVE THE ASSIGNMENT IMMEDIATELY BELOW).
############
############ END OF SECTOR 8 (IGNORE THIS COMMENT)

added_note = ""

############ START OF SECTOR 9 (IGNORE THIS COMMENT)
############
############ NOW YOUR CODE SHOULD BEGIN BUT FIRST A COMMENT.
############
############ IF YOU ARE IMPLEMENTING GA THEN:
############  - IF YOU EXECUTE YOUR MAIN LOOP A FIXED NUMBER OF TIMES THEN USE THE VARIABLE 'max_it' TO DENOTE THIS NUMBER
############  - USE THE VARIABLE 'pop_size' TO DENOTE THE SIZE OF YOUR POPULATION (THIS IS '|P|' IN THE PSEUDOCODE)
############
############ IF YOU ARE IMPLEMENTING AC THEN:
############  - IF YOU EXECUTE YOUR MAIN LOOP A FIXED NUMBER OF TIMES THEN USE THE VARIABLE 'max_it' TO DENOTE THIS NUMBER
############  - USE THE VARIABLE 'num_ants' TO DENOTE THE NUMBER OF ANTS (THIS IS 'N' IN THE PSEUDOCODE)
############
############ IF YOU ARE IMPLEMENTING PS THEN:
############  - IF YOU EXECUTE YOUR MAIN LOOP A FIXED NUMBER OF TIMES THEN USE THE VARIABLE 'max_it' TO DENOTE THIS NUMBER
############  - USE THE VARIABLE 'num_parts' TO DENOTE THE NUMBER OF PARTICLES (THIS IS 'N' IN THE PSEUDOCODE)
############
############ DOING THIS WILL MEAN THAT THIS INFORMATION IS WRITTEN WITHIN 'added_note' IN ANY TOUR-FILE PRODUCED.
############ OF COURSE, THE VALUES OF THESE VARIABLES NEED TO BE ACCESSIBLE TO THE MAIN BODY OF CODE.
############ IT'S FINE IF YOU DON'T ADOPT THESE VARIABLE NAMES BUT THIS USEFUL INFORMATION WILL THEN NOT BE WRITTEN TO ANY
############ TOUR-FILE PRODUCED BY THIS CODE.
############
############ END OF SECTOR 9 (IGNORE THIS COMMENT)


import math
import copy

global length_counter
length_counter = []

class Individual:
    def __init__(self, num_cities, generate_flag) -> None:
        if generate_flag:
            self.tour = list(range(num_cities))
            random.shuffle(self.tour)
            self.length = get_tour_length(self.tour)
        else:
            self.tour = []
            self.length = -1



    def __repr__(self):
        return f"Tour: {self.tour}, Tour Length: {self.length}"


def genetic_algorithm(pop_size, max_it, P):

    for i in range(pop_size): # Generate the initial population
        tmp_individual = Individual(num_cities, True)
        P.append(tmp_individual)

    standard_deviation = 9999999
    best_so_far = Individual(num_cities, False)
    current_fastest = 9999999

    for i in range(max_it):
        print(f'ITERATION: {str(i).zfill(4)} {best_so_far.length}')

        standard_deviation, pop_mean = get_sd(P)

        for j in range(pop_size):
            
            Z = Individual(num_cities, False)

            if standard_deviation < (0.02 * pop_mean):
                X = tournament_selection(P[:pop_size])
                Y = tournament_selection(P[:pop_size])
            else:
                X = binary_tournament_selection(P[:pop_size])
                Y = binary_tournament_selection(P[:pop_size])

            if random.random() < 0.75:
                if standard_deviation < (0.02 * pop_mean):
                    Z.tour = scx_crossover(X.tour, Y.tour)
                    Z.length = get_tour_length(Z.tour)
                    if random.random() < 0.1:
                        Z = two_opt_mutate(Z) 

                else:
                    Z = ox_caller(X, Y)        
                
            else:
                if X.length < Y.length:
                    Z.tour = X.tour.copy()
                    Z.length = X.length
                else:
                    Z.tour = Y.tour.copy()
                    Z.length = Y.length
                
                if random.random() < 0.1:
                    Z.tour = reverse_sequence_mutation(Z.tour)
                    Z.length = get_tour_length(Z.tour)

            if Z.length < current_fastest:
                current_fastest = Z.length
                best_so_far = Z

            P.append(Z)

        del P[:pop_size] # New population is just appended to the original population, then removed

        if standard_deviation < (0.018 * pop_mean): # Use standard deviation as a diversity criterion
            if random.random() < 0.05:
                P = extinction_event(P)

 
    return best_so_far.tour, current_fastest

def extinction_event(P):
    new_pop = []
    P.sort(key=lambda x: x.length)

    for i in range(round(len(P) * 0.1)):
        new_pop.append(P[i])
        new_pop.append(P[-i])
    
    for i in range(len(new_pop), len(P)):
        new_pop.append(Individual(num_cities, True))

    return new_pop

def get_pop_details(P):
    best_length = get_tour_length(P[0])
    avg_length = best_length
    for i in range(1, len(P)):
        tmp = get_tour_length(P[i])
        if tmp < best_length:
            best_length = tmp

        avg_length += best_length
    return best_length, avg_length / len(P)

def get_sd(P):
    pop_mean = sum([x.length for x in P]) / len(P)

    sum_sd = sum((x.length - pop_mean) ** 2 for x in P)
    sum_sd = sum_sd / len(P)
    sum_sd = math.sqrt(sum_sd)

    return sum_sd, pop_mean

def two_point_crossover(X, Y):
    bit_position_1 = random.randint(0, len(X) - 1)
    bit_position_2 = random.randint(0, len(X) - 1)

    if bit_position_1 > bit_position_2:
        temp = bit_position_1
        bit_position_1 = bit_position_2
        bit_position_2 = temp

    prefix_X = X[:bit_position_1]
    middle_X = X[bit_position_1:bit_position_2]
    suffix_X = X[bit_position_2:]
    prefix_Y = Y[:bit_position_1]
    middle_Y = Y[bit_position_1:bit_position_2]
    suffix_Y = Y[bit_position_2:]

    child_1 = prefix_X + middle_Y + suffix_X
    child_2 = prefix_Y + middle_X + suffix_Y

    if random.random() < 0.1:
        child_1 = mutate(child_1)
    child_1 = fix(child_1)

    if random.random() < 0.1:
        child_2 = mutate(child_2)
    child_2 = fix(child_2)

    if get_tour_length(child_1, dist_matrix, num_cities) < get_tour_length(child_2, dist_matrix, num_cities):
        return child_1
    else:
        return child_2
    
def greedy_crossover(X, Y): # Testing average offspring tour length: Standard achieved 2746, greedy 1624

    # Get the best path, using only cities from X or Y
    # Children will start at either the first city in X or Y

    child_1 = [X[0]]
    child_2 = [Y[0]]

    seen = set()

    for i in range(1, len(X)):
        if dist_matrix[child_1[i - 1]][X[i]] < dist_matrix[child_1[i - 1]][Y[i]]:
            child_1.append(X[i])
            seen.add(X[i])
        else:
            child_1.append(Y[i])
            seen.add(Y[i])

        if dist_matrix[child_2[i - 1]][X[i]] < dist_matrix[child_2[i - 1]][Y[i]]:
            child_2.append(X[i])
            seen.add(X[i])
        else:
            child_2.append(Y[i])
            seen.add(Y[i])

    if random.random() < 0.1:
        child_1 = mutate(child_1)
    child_1 = fix(child_1)

    if random.random() < 0.1:
        child_2 = mutate(child_2)
    child_2 = fix(child_2)

    if get_tour_length(child_1, dist_matrix, num_cities) < get_tour_length(child_2, dist_matrix, num_cities):
        length_counter.append(get_tour_length(child_1, dist_matrix, num_cities))
        return child_1
    else:
        length_counter.append(get_tour_length(child_2, dist_matrix, num_cities))
        return child_2
    
def scx_crossover(X, Y):
    # https://ieeexplore.ieee.org/document/10146181
   
    # STEP 1: Choose first city of X
    # STEP 2: Look at cities in X and Y which are only to the right of the first city
    # STEP 3: If both are unseen, choose the closest
    # If one city is unseen (for example city 2 in X), find the first unseen city in X (by going left to right)
    # and compare to the one on the right in Y.
    # If both cities are seen, choose first unseen city in X and compare to first unseen city in Y

    # NOTE: To get child_2, instead of starting from first city of X, start from last city of X
    child = [X[0]]

    X_dict = {X[i]: i for i in range(len(X))}
    Y_dict = {Y[i]: i for i in range(len(Y))}
    seen = set()
    seen.add(X[0])

    k = 0

    while len(child) < num_cities:
            next_Y = (Y_dict[X[k]] + 1) % len(Y) # These values are only for their opposite parent

            if X[(k + 1) % len(X)] not in seen and Y[next_Y] not in seen:
                if dist_matrix[X[k]][X[(k + 1) % len(X)]] <= dist_matrix[X[k]][Y[next_Y]]:
                    child.append(X[(k + 1) % len(X)])
                    seen.add(X[(k + 1) % len(X)])
                    k = (k + 1) % len(X)
                    next_Y = (Y_dict[X[k]] + 1) % len(Y)
                else:
                    child.append(Y[next_Y])
                    seen.add(Y[next_Y])
                    k = X_dict[Y[next_Y]] % len(X)

            elif X[(k + 1) % len(X)] in seen and Y[next_Y] not in seen:
                for i in range(len(X)):
                    if X[i] not in seen:
                        tmp_next = i
                        break
                
                if dist_matrix[X[k]][X[tmp_next]] <= dist_matrix[X[k]][Y[next_Y]]:
                    child.append(X[tmp_next])
                    seen.add(X[tmp_next])
                    k = (tmp_next) % len(X)
                    next_Y = (Y_dict[X[k]]) % len(Y)
                else:
                    child.append(Y[next_Y])
                    seen.add(Y[next_Y])
                    k = X_dict[Y[next_Y]] % len(X)

            elif Y[next_Y] in seen and X[(k + 1) % len(X)] not in seen:
                for i in range(len(Y)):
                    if Y[i] not in seen:
                        tmp_next = i
                        break
                
                if dist_matrix[X[k]][X[(k + 1) % len(X)]] <= dist_matrix[X[k]][Y[tmp_next]]:
                    child.append(X[(k + 1) % len(X)])
                    seen.add(X[(k + 1) % len(X)])
                    k = (k + 1) % len(X)
                    next_Y = (Y_dict[X[k]] + 1) % len(Y)
                else:
                    child.append(Y[tmp_next])
                    seen.add(Y[tmp_next])
                    k = X_dict[Y[tmp_next]] % len(X)

            else:
                for i in range(len(X)):
                    if X[i] not in seen:
                        tmp_next_X = i
                        break
                
                for i in range(len(Y)):
                    if Y[i] not in seen:
                        tmp_next_Y = i
                        break
                
                if dist_matrix[X[k]][X[tmp_next_X]] <= dist_matrix[X[k]][Y[tmp_next_Y]]:
                    child.append(X[tmp_next_X])
                    seen.add(X[tmp_next_X])
                    k = (tmp_next_X) % len(X)
                    next_Y = Y_dict[X[k]] % len(Y)
                else:
                    child.append(Y[tmp_next_Y])
                    seen.add(Y[tmp_next_Y])
                    k = X_dict[Y[tmp_next_Y]] % len(X)

    length_counter.append(get_tour_length(child))

    if random.random() <= 0.1:
        child = reverse_sequence_mutation(child)

    return child

def ox_caller(X, Y):
    child_1 = Individual(num_cities, False)
    child_2 = Individual(num_cities, False)

    child_1.tour = ox(X.tour, Y.tour)
    child_2.tour = ox(Y.tour, X.tour)

    child_1.length = get_tour_length(child_1.tour)
    child_2.length = get_tour_length(child_2.tour)

    if child_1.length < child_2.length:
        return child_1
    else:
        return child_2

def ox(X, Y): # Order Crossover
    seen = set()
    X_set = set(X)

    bit_position_1 = random.randint(0, len(X) - 2)
    bit_position_2 = random.randint(bit_position_1, len(X) - 1)

    child_1 = [-1] * len(X)

    child_1[bit_position_1:bit_position_2] = Y[bit_position_1:bit_position_2]

    for i in range(bit_position_1, bit_position_2):
        seen.add(Y[i])

    X_dict = {i: x for i, x in enumerate(X) if x not in seen}

    # for i in range(len(child_1)):
    #     if child_1[i] == -1:
    #         for j in range(len(X)):
    #             if X[j] not in seen:
    #                 child_1[i] = X[j]
    #                 seen.add(X[j])
    #                 break
    X_fill = iter(X_dict.values())

    for i in range(len(child_1)):
        if child_1[i] == -1:
            
            child_1[i ] = next(X_fill)

        

    if random.random() < 0.1:
        child_1 = reverse_sequence_mutation(child_1)

    return child_1

def mutate(tour):
    index_1 = random.randint(0, len(tour) - 1)
    index_2 = random.randint(0, len(tour) - 1)

    temp = tour[index_1]
    tour[index_1] = tour[index_2]
    tour[index_2] = temp

    return tour

def two_opt_mutate(X):  # Performs several passes of the two-opt algorithm for more exploitative mutation

    for _ in range(10):
        improved = False
        for i in range(1, len(X.tour)-2):
            for j in range(i + 2, len(X.tour) + (1 if i > 1 else 0)):

                v1, v2, v3, v4 = X.tour[i - 1], X.tour[i], X.tour[j - 1], X.tour[j % len(X.tour)]

                old_dist = dist_matrix[v1][v2] + dist_matrix[v3][v4]
                new_dist = dist_matrix[v1][v3] + dist_matrix[v2][v4]
                
                new_tour_length = X.length - old_dist + new_dist

                if new_tour_length < X.length:
                    new_tour = X.tour[:i] + X.tour[i:j][::-1] + X.tour[j:]
                    X.tour = new_tour
                    X.length = new_tour_length
                    improved = True

        if not improved:
            break


    return X

def reverse_sequence_mutation(tour): #https://arxiv.org/pdf/1203.3099.pdf#:~:text=In%20the%20reverse%20sequence%20mutation,covered%20in%20the%20previous%20operation.
    start = random.randint(0, len(tour) - 2)
    end = random.randint(start + 1, len(tour) - 1)

    tour[start:end] = reversed(tour[start:end])

    return tour

def select_elites(P, iteration_count):
    # Function looks at population size and how many iterations have happened
    # From the information above, the number of elites is determined for the generation
    # The number of elites will slowly grow to a certain point, then remain constant when the iteration count is high enough
    # Should end on 5% elites
    pass

def binary_tournament_selection(P):
    competitors = random.sample(P, 2)

    if competitors[0].length < competitors[1].length:
        return competitors[0]
    else:
        return competitors[1]

def tournament_selection(P):
    competitors = random.sample(P, 30)
    winner = min(competitors, key=lambda x: x.length)
    return winner

def roulette_wheel(P, dist_matrix):
    t = get_threshold(num_cities, dist_matrix)
    all_fitness = get_pop_fitness(P, dist_matrix)

    for fitness in all_fitness:
        fitness = t - fitness
        
    F = sum(all_fitness)

    for fitness in all_fitness:
        fitness = (fitness * 360) / F # Roulette wheel although could do it out of 1

    selected = random.choices(P, weights=all_fitness, k=2)

    return selected

def adaptive_selection(P, pop_max, pop_avg): # Adaptive selection works poorly - might be in need of adjusting fitness function
    children = []
    mating_chance_A = []
    mating_chance_B = []
    mating_chance_C = []
    mating_chance_D = []

    val_dict_a = {}
    val_dict_b = {}

    mating_chance_A, mating_chance_B, mating_chance_C, mating_chance_D, val_dict_a, val_dict_b = get_mating_chances(P, pop_max, pop_avg)
    for i in range(len(mating_chance_A)):
        children.append(scx_crossover(val_dict_a[mating_chance_A[i]], val_dict_b[mating_chance_B[len(mating_chance_B) - i - 1]]))
        children.append(scx_crossover(val_dict_a[mating_chance_C[i]], val_dict_b[mating_chance_D[len(mating_chance_D) - i - 1]]))
    
    return children

def get_mating_chances(P, pop_max, pop_avg):
    A = []
    B = []

    val_dict_a = {}
    val_dict_b = {}

    fitness = sum()

    for i in range(len(P)):
        a_val = (1 / fitness[i]) + ((1 / pop_max) - (1 / pop_avg)) * random.random()
        b_val = (1 / fitness[i]) + ((1 / pop_max) - (1 / pop_avg)) * random.random()

        A.append(a_val)
        B.append(b_val)

        val_dict_a[a_val] = P[i]
        val_dict_b[b_val] = P[i]

    A.sort(reverse=True)
    B.sort()

    C = A[len(A) // 2:]
    A = A[:len(A) // 2]
    D = B[len(B) // 2:]
    B = B[:len(B) // 2]

    return A, B, C, D, val_dict_a, val_dict_b

def get_tour_length(tour):
    counter = 0

    for i in range(len(tour)):
        counter += dist_matrix[tour[i - 1]][tour[i]]

    return counter

def get_pop_fitness(P):
    fitness = []
    for i in range(len(P)):
        fitness.append(get_tour_length(P[i]))
    return fitness

P = []
max_it = 5000
pop_size = 2000
tour, tour_length = genetic_algorithm(pop_size, max_it, P)
print(tour)
print(tour_length)




















############ START OF SECTOR 10 (IGNORE THIS COMMENT)
############
############ YOUR CODE SHOULD NOW BE COMPLETE AND WHEN EXECUTION OF THIS PROGRAM 'skeleton.py'
############ REACHES THIS POINT, YOU SHOULD HAVE COMPUTED A TOUR IN THE RESERVED LIST VARIABLE 'tour', 
############ WHICH HOLDS A LIST OF THE INTEGERS FROM {0, 1, ..., 'num_cities' - 1} SO THAT EVERY INTEGER
############ APPEARS EXACTLY ONCE, AND YOU SHOULD ALSO HOLD THE LENGTH OF THIS TOUR IN THE RESERVED
############ INTEGER VARIABLE 'tour_length'.
############
############ YOUR TOUR WILL BE PACKAGED IN A TOUR FILE OF THE APPROPRIATE FORMAT AND THIS TOUR FILE'S
############ NAME WILL BE A MIX OF THE NAME OF THE CITY FILE, THE NAME OF THIS PROGRAM AND THE
############ CURRENT DATE AND TIME. SO, EVERY SUCCESSFUL EXECUTION GIVES A TOUR FILE WITH A UNIQUE
############ NAME AND YOU CAN RENAME THE ONES YOU WANT TO KEEP LATER.
############
############ DO NOT EDIT ANY TOUR FILE! ALL TOUR FILES MUST BE LEFT AS THEY WERE ON OUTPUT.
############
############ DO NOT TOUCH OR ALTER THE CODE BELOW THIS POINT! YOU HAVE BEEN WARNED!
############

end_time = time.time()
elapsed_time = round(end_time - start_time, 1)

if algorithm_code == "GA":
    try: max_it
    except NameError: max_it = None
    try: pop_size
    except NameError: pop_size = None
    if added_note != "":
        added_note = added_note + "\n"
    added_note = added_note + "The parameter values are 'max_it' = " + str(max_it) + " and 'pop_size' = " + str(pop_size) + "."

if algorithm_code == "AC":
    try: max_it
    except NameError: max_it = None
    try: num_ants
    except NameError: num_ants = None
    if added_note != "":
        added_note = added_note + "\n"
    added_note = added_note + "The parameter values are 'max_it' = " + str(max_it) + " and 'num_ants' = " + str(num_ants) + "."

if algorithm_code == "PS":
    try: max_it
    except NameError: max_it = None
    try: num_parts
    except NameError: num_parts = None
    if added_note != "":
        added_note = added_note + "\n"
    added_note = added_note + "The parameter values are 'max_it' = " + str(max_it) + " and 'num_parts' = " + str(num_parts) + "."
    
added_note = added_note + "\nRUN-TIME = " + str(elapsed_time) + " seconds.\n"

flag = "good"
length = len(tour)
for i in range(0, length):
    if isinstance(tour[i], int) == False:
        flag = "bad"
    else:
        tour[i] = int(tour[i])
if flag == "bad":
    print("*** error: Your tour contains non-integer values.")
    sys.exit()
if isinstance(tour_length, int) == False:
    print("*** error: The tour-length is a non-integer value.")
    sys.exit()
tour_length = int(tour_length)
if len(tour) != num_cities:
    print("*** error: The tour does not consist of " + str(num_cities) + " cities as there are, in fact, " + str(len(tour)) + ".")
    sys.exit()
flag = "good"
for i in range(0, num_cities):
    if not i in tour:
        flag = "bad"
if flag == "bad":
    print("*** error: Your tour has illegal or repeated city names.")
    sys.exit()
check_tour_length = 0
for i in range(0, num_cities - 1):
    check_tour_length = check_tour_length + dist_matrix[tour[i]][tour[i + 1]]
check_tour_length = check_tour_length + dist_matrix[tour[num_cities - 1]][tour[0]]
if tour_length != check_tour_length:
    flag = print("*** error: The length of your tour is not " + str(tour_length) + "; it is actually " + str(check_tour_length) + ".")
    sys.exit()
print("You, user " + my_user_name + ", have successfully built a tour of length " + str(tour_length) + "!")
len_user_name = len(my_user_name)
user_number = 0
for i in range(0, len_user_name):
    user_number = user_number + ord(my_user_name[i])
alg_number = ord(algorithm_code[0]) + ord(algorithm_code[1])
tour_diff = abs(tour[0] - tour[num_cities - 1])
for i in range(0, num_cities - 1):
    tour_diff = tour_diff + abs(tour[i + 1] - tour[i])
certificate = user_number + alg_number + tour_diff
local_time = time.asctime(time.localtime(time.time()))
output_file_time = local_time[4:7] + local_time[8:10] + local_time[11:13] + local_time[14:16] + local_time[17:19]
output_file_time = output_file_time.replace(" ", "0")
script_name = os.path.basename(sys.argv[0])
if len(sys.argv) > 2:
    output_file_time = sys.argv[2]
output_file_name = script_name[0:len(script_name) - 3] + "_" + input_file[0:len(input_file) - 4] + "_" + output_file_time + ".txt"

f = open(output_file_name,'w')
f.write("USER = {0} ({1} {2}),\n".format(my_user_name, my_first_name, my_last_name))
f.write("ALGORITHM CODE = {0}, NAME OF CITY-FILE = {1},\n".format(algorithm_code, input_file))
f.write("SIZE = {0}, TOUR LENGTH = {1},\n".format(num_cities, tour_length))
f.write(str(tour[0]))
for i in range(1,num_cities):
    f.write(",{0}".format(tour[i]))
f.write(",\nNOTE = {0}".format(added_note))
f.write("CERTIFICATE = {0}.\n".format(certificate))
f.close()
print("I have successfully written your tour to the tour file:\n   " + output_file_name + ".")

############ END OF SECTOR 10 (IGNORE THIS COMMENT)
