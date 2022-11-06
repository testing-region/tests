package main

import "fmt"

func main() {
    var mylist []int

    mylist = append(mylist, 2)
    mylist = append(mylist, 4)
    mylist = append(mylist, 7)
    mylist = append(mylist, 8)
    mylist = append(mylist, 9)
    mylist = append(mylist, 5)

    mylist[0], mylist[1] = mylist[1], mylist[0]

    fmt.Println(mylist[0], mylist[1])
    fmt.Println(len(mylist))
}
