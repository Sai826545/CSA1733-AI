neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW', 'T'],
    'T': ['V']
}
colors = ['Red', 'Green', 'Blue']
assignment = {}
def is_valid(region, color):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def csp_backtracking():
    if len(assignment) == len(neighbors):
        return True 
    unassigned = [r for r in neighbors if r not in assignment][0]
    for color in colors:
        if is_valid(unassigned, color):
            assignment[unassigned] = color
            if csp_backtracking():
                return True
            del assignment[unassigned]  
    return False
if csp_backtracking():
    print("Color assignment:")
    for region in sorted(assignment):
        print(f"{region} → {assignment[region]}")
else:
    print("No solution found.")
