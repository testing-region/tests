package main

import (
	"fmt"
	"github.com/briandowns/spinner"
	"io/ioutil"
	"os"
	"os/exec"
	"strconv"
	"time"
)

func main() {
	// get the contents of the directory
	oldFiles, _ := ioutil.ReadDir("./")

	for i, file := range oldFiles {
		exec.Command("mv", file.Name(), "v"+strconv.Itoa(i)+".webm").Run()
	}

	newFiles, _ := ioutil.ReadDir("./")

	// create a file to append content
	f, _ := os.OpenFile("videos.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)

	// close file at the end of the program
	defer f.Close()

	// store file names into videos file
	for _, file := range newFiles {
		f.WriteString("file " + file.Name() + "\n")
	}

	// create a script file
	sf, _ := os.OpenFile("merge.sh", os.O_CREATE|os.O_APPEND|os.O_WRONLY, 0644)

	sf.WriteString("#!/usr/bin/env bash \n")
	sf.WriteString("ffmpeg -f concat -safe 0 -i videos.txt -c copy output.webm \n")

	// close script file
	defer sf.Close()

	fmt.Println("Merging videos")
	s := spinner.New(spinner.CharSets[9], 100*time.Millisecond) // Build our new spinner
	s.Start()                                                   // Start the spinner
	exec.Command("bash", "./merge.sh").Run()
	exec.Command("rm", "videos.txt", "merge.sh").Run()
	s.Stop()

	fmt.Println("Merge Successful")

}
