package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
	"strings"
)

func main() {
	baseURL := "https://api.boot.dev/v1/courses_rest_api/learn-http"
	endpoint := "/users"
	params := "?sort=characterName"

	url := strings.Join([]string{baseURL, endpoint}, "")
	fullURL := strings.Join([]string{url, params}, "")

	log.Printf("Requesting data from %v", url)

	req, err := http.NewRequest("GET", fullURL, nil)
	if err != nil {
		log.Fatal(err)
	}

	log.Println("Request successful. Waiting for server's response...")

	res, err := http.DefaultClient.Do(req)
	if err != nil {
		log.Fatal(err)
	}

	body, _ := io.ReadAll(res.Body)

	defer res.Body.Close()

	fmt.Println("\nResponse body:")
	fmt.Println(string(body))
}
