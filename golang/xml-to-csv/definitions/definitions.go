package definitions

import "encoding/xml"

// Define structs for each section of the xml file
type PurchaseData struct {
	Root      xml.Name      `xml:"Root"`
	Customers CustomersData `xml:"Customers"`
	Orders    OrdersData    `xml:"Orders"`
}

type CustomersData struct {
	XMLName   xml.Name   `xml:"Customers"`
	Customers []Customer `xml:"Customer"`
}

// definitions for book element
type Customer struct {
	XMLName      xml.Name `xml:"Customer"`
	ID           string   `xml:"CustomerID,attr"`
	CompanyName  string   `xml:"CompanyName"`
	ContactName  string   `xml:"ContactName"`
	ContactTitle string   `xml:"ContactTitle"`
	Phone        string   `xml:"Phone"`
	FullAddress  []Addr   `xml:"FullAddress"`
}

type Addr struct {
	XMLName    xml.Name `xml:"FullAddress"`
	Address    string   `xml:"Address"`
	City       string   `xml:"City"`
	Region     string   `xml:"Region"`
	PostalCode string   `xml:"PostalCode"`
	Country    string   `xml:"Country"`
}

type OrdersData struct {
	XMLName xml.Name `xml:"Orders"`
	Orders  []Order  `xml:"Order"`
}

type Order struct {
	XMLName      xml.Name   `xml:"Order"`
	CustomerID   string     `xml:"CustomerID"`
	EmployeeID   string     `xml:"EmployeeID"`
	OrderDate    string     `xml:"OrderDate"`
	RequiredDate string     `xml:"RequiredDate"`
	ShippingData []ShipInfo `xml:"ShipInfo"`
}

type ShipInfo struct {
	XMLName        xml.Name `xml:"ShipInfo"`
	ShippedDate    string   `xml:"ShippedDate,attr"`
	ShipName       string   `xml:"ShipName"`
	ShipAddr       string   `xml:"ShipAddress"`
	ShipCity       string   `xml:"ShipCity"`
	ShipRegion     string   `xml:"ShipRegion"`
	ShipPostalCode string   `xml:"ShipPostalCode"`
	ShipCountry    string   `xml:"ShipCountry"`
	ShipVia        string   `xml:"ShipVia"`
	Freight        string   `xml:"Freight"`
}
