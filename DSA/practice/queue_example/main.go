package main

import (
	"fmt"

	"github.com/gdpkg/datastructs/queue"
)

func main() {
	nums := queue.Init[int]()

	for i := 0; i < 10; i++ {
		nums.Enqueue(i)
		fmt.Println(nums.Peek())
		nums.Dequeue()
	}
}
