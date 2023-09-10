package main

import (
	"flag"
	"fmt"
	"log"
	"net/http"
	"strings"

	"golang.org/x/net/html"
)

// Make sure that urls that are pointing to the same page receive
// the same output --> normalisation
func NormaliseUrl(baseUrl string, url string) string {
	// if the url is relative, return the path
	// relative urls do not have protocol definition
	if !strings.Contains(url, "://") {
		return baseUrl + url
	}

	parts := strings.Split(url, "://")                        // split the protocol from the url
	normalUrl := strings.ToLower(strings.Trim(parts[1], "/")) // trim off resource parts
	return normalUrl
}

// Get urls from a page.
// Parse the html document for all <a> tags.
// Retrieve the value stored in the `href` attribute.
// Return a slice of url strings.
func GetUrlsFromHtml(url string) []string {
	var links []string

	r, err := http.Get("http://" + url)
	if err != nil {
		log.Fatal(err)
	}

	body, err := html.Parse(r.Body)
	if err != nil {
		log.Fatal(err)
	}

	// check if an element == <a>
	// and append to the links slice
	var getLink func(*html.Node)
	getLink = func(n *html.Node) {
		// check if current element is <a>
		if n.Type == html.ElementNode && n.Data == "a" {
			for _, a := range n.Attr {
				if a.Key == "href" {
					links = append(links, NormaliseUrl(url, a.Val))
				}
			}
		}

		// Traverse the current node to find <a> tags
		for c := n.FirstChild; c != nil; c = c.NextSibling {
			getLink(c)
		}
	}

	// Get the links from the html page
	getLink(body)

	return links
}

func main() {
	url := flag.String("i", "", "Set the url to scrape links from")
	flag.Parse()

	if len(*url) == 0 {
		log.Fatal("Enter a web address")
	}

	links := GetUrlsFromHtml(*url)
	for _, v := range links {
		fmt.Println(v)
	}
}
