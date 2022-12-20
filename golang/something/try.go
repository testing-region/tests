package main

import "fmt"

func main() {
    const num = 8
    if (num % 2 == 1) {
	fmt.Println("This is odd")
    } else {
	fmt.Println("This is even")
    }
}
