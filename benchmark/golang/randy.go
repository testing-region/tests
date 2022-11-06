package main

import (
    "math/rand"
    "sort"
)

func main() {
    var mylist []int

    for i := 0; i < 100000; i++ {
	mylist = append(mylist, rand.Intn(100))
    }

    sort.Ints(mylist)
}
