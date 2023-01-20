package main

import (
	"fmt"

	"davesaah/greetings"
)

func main() {
	message := greetings.Hello("David")
	fmt.Println(message)
}
