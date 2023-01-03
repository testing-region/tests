package main

import (
    "testing"
    "fmt"
)


func TestBasicIntMin(t *testing.T) {
    ans := IntMin(2, -2)
    if ans != -2 {
	t.Errorf("want -2, got %d", ans)
    }
}


func TestIntMinTableDriven(t *testing.T) {
    var testsValues = []struct {
	a, b int
	want int
    }{
	{0, 1, 0},
	{1, 0, 0},
	{2, -2, -2},
	{0, -1, -1},
	{-1, 0, -1},
    }

    for _, val := range testsValues {
        testname := fmt.Sprintf("(%d,%d)", val.a, val.b)
        t.Run(testname, func(t *testing.T) {
            ans := IntMin(val.a, val.b)
            if ans != val.want {
                t.Errorf("got %d, want %d", ans, val.want)
            }
        })
    }
}

