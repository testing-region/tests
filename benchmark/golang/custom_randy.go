package main

import (
    "math/rand"
)


func bubble_sort(items []int) []int {
    n := len(items) - 1
    for i := 0; i < n; i++ {
	for j := 0; i < n-i; j++ {
	    if items[j] > items[j+1] {
		items[j], items[j+1] = items[j+1], items[j]
	    }
	}
    }
    return items
}

func main() {
    var mylist []int

    for i := 0; i < 10000; i++ {
	mylist = append(mylist, rand.Intn(100))
    }

    bubble_sort(mylist)
}
