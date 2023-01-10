package kata

func GetGrade(a, b, c int) rune {
    average := (a + b + c) / 3
    var grade rune

    switch {
    case average >= 90 && average <= 100:
	grade = 'A'
    case average >= 80 && average <= 90:
	grade = 'B'
    case average >= 70 && average <= 80:
	grade = 'C'
    case average >= 60 && average <= 70:
	grade = 'D'
    case average >= 0 && average <= 60:
	grade = 'F'
    }
    return grade
}

