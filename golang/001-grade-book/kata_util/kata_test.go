package main

import (
	"001-grade-book/kata"
	"testing"
)

func TestGetGradeA(t *testing.T) {
	testA := [...][3]int{{95, 90, 93}, {100, 85, 96}, {92, 93, 94}}
	for _, val := range testA {
		ans := kata.GetGrade(val[0], val[1], val[2])
		if ans != 'A' {
			t.Errorf("want 'A', got %v", ans)
		}
	}

}

func TestGetGradeB(t *testing.T) {
	testB := [...][3]int{{70,70,100}, {82,85,87}, {84,79,85}, {89,89,90}}
	for _, val := range testB {
		ans := kata.GetGrade(val[0], val[1], val[2])
		if ans != 'B' {
			t.Errorf("want 'B', got %v", ans)
		}
	}

}

func TestGetGradeC(t *testing.T) {
	testC := [...][3]int{{70,70,70}, {75,70,79}, {60,82,76}}
	for _, val := range testC {
		ans := kata.GetGrade(val[0], val[1], val[2])
		if ans != 'C' {
			t.Errorf("want 'C', got %v", ans)
		}
	}

}

func TestGetGradeD(t *testing.T) {
	testD := [...][3]int{{65,70,59}, {66,62,68}, {58,62,70}}
	for _, val := range testD {
		ans := kata.GetGrade(val[0], val[1], val[2])
		if ans != 'D' {
			t.Errorf("want 'D', got %v", ans)
		}
	}

}

func TestGetGradeF(t *testing.T) {
	testF := [...][3]int{{44,55,52}, {48,55,52}, {58,59,60}}
	for _, val := range testF {
		ans := kata.GetGrade(val[0], val[1], val[2])
		if ans != 'F' {
			t.Errorf("want 'F', got %v", ans)
		}
	}

}
