package main

import (
	"fmt"

	"github.com/gdpkg/datastructs/stack"
)

func main() {
	nums := stack.Init[int]()

	nums.Push(2)
	nums.Push(2)
	nums.Push(2)
	nums.Push(2)
	nums.Push(2)
	fmt.Println(nums)
	nums.Pop()
	nums.Pop()
	nums.Pop()
	nums.Pop()
	fmt.Println(nums)
}
