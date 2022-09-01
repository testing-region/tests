// testing named arguments
// put parameters into curly braces
// all named arguments are optional, hence your code should 
// implement a logic that would run if no arguments are passed
// else, you'll get an error
int addNumbers({int x = 0, int y = 0}) {
    return x + y;
}

void main() {
    print(addNumbers(x: 20, y:5));
}
