package main

import (
	"fmt"
	"time"
)

func daysSinceBirth(birthdate string) (int, error) {
	// Parse the birthdate string
	layout := time.DateOnly
	birth, err := time.Parse(layout, birthdate)
	if err != nil {
		return 0, err
	}

	// Calculate the difference in days
	days := int(time.Since(birth).Hours() / 24)

	return days, nil
}

func main() {
	// Replace this with the actual birthdate in "YYYY-MM-DD" format
	birthdate := "2002-03-20"

	days, err := daysSinceBirth(birthdate)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	fmt.Printf("You have spent %d days on Earth.\n", days)
}
