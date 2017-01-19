// ================== IGNORE ================== //

console.log("");
console.log("    1          ");
console.log("    ├── 2      ");
console.log("    │   ├── 5  ");
console.log("    │   ├── 6  ");
console.log("    │   └── 7  ");
console.log("    ├── 3      ");
console.log("    │   └── 8  ");
console.log("    └── 4      ");
console.log("        ├── 9  ");
console.log("        ├── 10 ");
console.log("        └── 11 ");
console.log("");

// mock out query function return values
var CHILDREN = {
    "1"  : ["2", "3", "4"],
    "2"  : ["5", "6", "7"],
    "3"  : ["8"],
    "4"  : ["9", "10", "11"],
    "5"  : [], // terminal node
    "6"  : [], // terminal node
    "7"  : [], // terminal node
    "8"  : [], // terminal node
    "9"  : [], // terminal node
    "10" : [], // terminal node
    "11" : [], // terminal node
};

// mock query function
function getChildren (node) {
    return CHILDREN[node];
}

// ============================================ //

function generatePaths (node) {
    var children = getChildren(node);

    if (children.length === 0) { return [[node]]; }

    var my_paths = [];

    children.forEach((child) => {
        my_paths = my_paths.concat(generatePaths(child).map(function (group) {
            return [node].concat(group);
        }));
    });

    return my_paths;
}

var output = generatePaths("1");
console.log(output);
