package main

import (
	"fmt"

	"davesaah/greetings"
)

func main() {
	message := greetings.Hello("Gladys")
	fmt.Println(message)
}