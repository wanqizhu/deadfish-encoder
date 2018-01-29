import math
shortest_path = {(i, i): 'o' for i in range(256)}

SEARCHING = True
def DP(start, target, depth=0):
    """ finds shortest path to change accumulator from start to target """
    global SEARCHING
    if depth == 0:
        SEARCHING = True

    if start in [-1, 256]:
        start = 0

    if (start, target) in shortest_path:
        SEARCHING = False
        return shortest_path[(start, target)]

    if not SEARCHING:
        return 'WAYTOOLONGGG' + 'g'*256

    ans1 = 'i' + DP(start+1, target, depth+1)
    ans2 = 'd' + DP(start-1, target, depth+1)
    
    ans = ans1 if len(ans1) < len(ans2) else ans2

    if start < 17:
        ans3 = 's' + DP(start**2, target, depth+1)
        ans = ans if len(ans) < len(ans3) else ans3
   
    shortest_path[(start, target)] = ans
    return ans


# print(DP(107, 95))
# print(shortest_path)
# print(DP(187, 0))




def encode(s, debug=False):
    """ Encodes input string s into deadfish """
    targets = [0] + [ord(c) for c in s]
    out = ""
    for i in range(len(s)):
        out += DP(targets[i], targets[i+1])

    return out


def decode(s, accumulator=0):
    out = ""
    for cmd in s:
        if accumulator == 256 or accumulator == -1:
            # Overflow, reset accumulator
            accumulator = 0
        # Process input
        if cmd == 'i':
            accumulator += 1 # Increment
        elif cmd == 'd':
            accumulator += -1 # Decrement
        elif cmd == 'o':
            out += chr(accumulator) # Output
        elif cmd == 's':
            accumulator *= accumulator # Square

    return out, accumulator

c = encode("treeCTF{don't_eat_dead_fish_for_dinner}")
print(c, decode(c))
# debug
# print([c for c in shortest_path if len(shortest_path[c]) > 256])