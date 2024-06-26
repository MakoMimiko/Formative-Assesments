#!/usr/bin/env python
# coding: utf-8

# In[47]:


def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
            if tomember is in frommember's follow list
        "followed by" if fromMember is followed by toMember,
            if fromember is followed by tomember
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    status = ""
    #have 2 boolean values then you if statement this
    #is frommember in tomember's followlist?
    from_to = False
    #is tomember in frommember's followlist?
    to_from = False
    if from_member in social_graph.get(to_member).get("following"):
        from_to = True
    if to_member in social_graph.get(from_member).get("following"):
        to_from = True
    if from_to == True & to_from == True:
        status = "friends"
        return status
    elif from_to == True:
        status = "followed by"
        return status
    elif to_from == True:
        status = "follower"
        return status
    else:
        status = "no relationship"
        return status


# In[475]:


def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    #make for loops that adds either the vertical or horizontal element into alist, then count the list if it has the as many same stuff as the size
    #for diagonal, same thing but while loop
    size = len(board)
    win = ""
    x = 0
    y = 0
    z = 0
    another_var = size-1
    vert = []
    diag = []
    diag2 = []
    #horizontal 
    for x in board:
        if x.count(x[0]) == size:
            win = x[0]
            return win
    #vertical
    for x in range(0, size):
        vert = []
        for y in range(0, size):
            vert.append(board[y][x])
            if vert.count(vert[0]) == size:
                win = board[y][x]
                return win
    #diagonal
    while z < size:
        diag.append(board[z][z])
        if diag.count(board[0][0]) == size:
            win = board[0][0]
            return win
        z += 1
    z=0
    while another_var+1 != 0:
        diag2.append(board[z][another_var])
        if diag2.count(diag2[0]) == size :
            win = diag2[0]
            return win
        another_var -=1
        z+=1
    win = "NO WINNER"
    return win


# In[313]:


def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    #looks for the first stop first, then the last stop, it should go backwards?
    #it goes backwards then while it does that it adds the eta then the loop stops when it reachesthe first stop
    #okay bruh its tuples im stu k ina nut and a hard place
    #bruh i swear a for looop to extract the keys just for the extraction keep yourself safe mikko
    current_stop = first_stop
    eta = 0
    done = []
    #while loop that doesn't stop until it reaches the end
    while current_stop != second_stop:
    #from the keys it compares it with the 
        for key in route_map.keys():
            if key[1] == second_stop and key[0] == first_stop:
                eta += route_map.get(key).get("travel_time_mins")
                return eta
            if key[1] not in done:
                if key[0] == first_stop:
                    current_stop = key[1]
                    eta += route_map.get(key).get("travel_time_mins")
                    done.append(key[0])
                    done.append(current_stop)
                elif key[0] == current_stop and key[1] != second_stop and key[1] != first_stop :
                    current_stop = key[1]
                    eta += route_map.get(key).get("travel_time_mins")
                    done.append(current_stop)
                elif key[1] == second_stop and first_stop in done:
                    eta += route_map.get(key).get("travel_time_mins")
                    current_stop = key[1]
                    return eta

