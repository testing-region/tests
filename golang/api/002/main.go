package main

import (
	"strings"

	"golang.org/x/net/html"
)

// Make sure that urls that are pointing to the same page receive
// the same output --> normalisation
func NormaliseUrl(url string) string {
	parts := strings.Split(url, "://")                        // split the protocol from the url
	normalUrl := strings.ToLower(strings.Trim(parts[1], "/")) // trim off resource parts
	return normalUrl
}

// Get urls from a page.
// Parse the html document for all <a> tags.
// Retrieve the value stored in the `href` attribute.
// Return a slice of url strings.
func GetUrlsFromHtml(body *html.Node) []string {
	var links []string

	// check if an element == <a>
	// and append to the links slice
	var getLink func(*html.Node)
	getLink = func(n *html.Node) {
		// check if current element is <a>
		if n.Type == html.ElementNode && n.Data == "a" {
			for _, a := range n.Attr {
				if a.Key == "href" {
					links = append(links, NormaliseUrl(a.Val))
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
