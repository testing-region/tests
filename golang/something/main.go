package main

import "fmt"

func main() {
    name := "DaveSaah"
    runes := []byte(name)

    length := len(runes) - 1

    // Deducing syntax for `for` loop
    // for initialise_variable; condition; operation_on_loop_vars {
	// code
    // }

    for i, j := 0, length; i < j; i, j = i+1, j-1 {
	runes[i], runes[j] = runes[j], runes[i]
    }
    fmt.Println(string(runes))
}
