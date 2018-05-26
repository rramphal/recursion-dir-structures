# ================ REFERENCES ================ #

# https://stackoverflow.com/questions/53513/best-way-to-check-if-a-list-is-empty
# https://stackoverflow.com/questions/1720421/how-to-append-list-to-second-list-concatenate-lists
# https://stackoverflow.com/questions/18970196/python-equivalent-to-ruby-array-each-method
# https://stackoverflow.com/questions/13893399/python-print-array-with-new-line

# ============================================ #

# ================== IGNORE ================== #

print("")
print("    1          ")
print("    ├── 2      ")
print("    │   ├── 5  ")
print("    │   ├── 6  ")
print("    │   └── 7  ")
print("    ├── 3      ")
print("    │   └── 8  ")
print("    └── 4      ")
print("        ├── 9  ")
print("        ├── 10 ")
print("        └── 11 ")
print("")

# mock out query function return values
CHILDREN = {
    "1"  : ["2", "3", "4"],
    "2"  : ["5", "6", "7"],
    "3"  : ["8"],
    "4"  : ["9", "10", "11"],
    "5"  : [], # terminal node
    "6"  : [], # terminal node
    "7"  : [], # terminal node
    "8"  : [], # terminal node
    "9"  : [], # terminal node
    "10" : [], # terminal node
    "11" : [], # terminal node
}

# mock query function
def getChildren(node):
    return CHILDREN[node]

# ============================================ #

def generatePaths(node):
    children = getChildren(node)

    if not children:
        return [[node]]

    paths = []

    for child in children:
        paths = paths + list(map((lambda group: [node] + group), generatePaths(child)))

    return paths

output = generatePaths("1")

for group in output:
    print(group)
