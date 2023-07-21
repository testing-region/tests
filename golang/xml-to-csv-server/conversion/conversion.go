package conversion

import (
	"encoding/csv"
	"encoding/xml"
	"log"
	"os"

	def "DaveSaah/xml-to-csv/definitions"
)

func XmlToCsv(file []byte) {
	// create customers.csv
	customerCSV, err := os.Create("public/download/customers.csv")
	if err != nil {
		log.Fatal(err)
	}

	// create orders.csv
	orderCSV, err := os.Create("public/download/orders.csv")
	if err != nil {
		log.Fatal(err)
	}

	// close file at the end of the program
	defer customerCSV.Close()
	defer orderCSV.Close()

	var purchaseData def.PurchaseData

	// convert from xml to data object
	xml.Unmarshal(file, &purchaseData)

	// create csvwriters
	customerCsvWriter := csv.NewWriter(customerCSV)
	orderCsvWriter := csv.NewWriter(orderCSV)

	// set data variables
	customersData := purchaseData.Customers.Customers
	orderData := purchaseData.Orders.Orders

	// add header for customers' data
	customerCsvWriter.Write([]string{
		"Customer ID",
		"Company Name",
		"Contact Name",
		"Contact Title",
		"Phone",
		"Address",
		"City",
		"Region",
		"Postal Code",
		"Country",
	})

	// write data into customers.csv
	for i := 0; i < len(customersData); i++ {
		customerCsvWriter.Write(
			[]string{
				customersData[i].ID,
				customersData[i].CompanyName,
				customersData[i].ContactName,
				customersData[i].ContactTitle,
				customersData[i].Phone,
				customersData[i].FullAddress[0].Address,
				customersData[i].FullAddress[0].City,
				customersData[i].FullAddress[0].Region,
				customersData[i].FullAddress[0].PostalCode,
				customersData[i].FullAddress[0].Country,
			},
		)
	}

	// add header for orders' data
	orderCsvWriter.Write([]string{
		"Customer ID",
		"Employee ID",
		"Order Date",
		"Required Date",
		"Shipped Date",
		"Ship Via",
		"Freight",
		"Ship Name",
		"Ship Address",
		"Ship City",
		"Ship Region",
		"Ship Postal Code",
		"Ship Country",
	})

	// write data into orders.csv
	for i := 0; i < len(orderData); i++ {
		orderCsvWriter.Write(
			[]string{
				orderData[i].CustomerID,
				orderData[i].EmployeeID,
				orderData[i].OrderDate,
				orderData[i].RequiredDate,
				orderData[i].ShippingData[0].ShippedDate,
				orderData[i].ShippingData[0].ShipVia,
				orderData[i].ShippingData[0].Freight,
				orderData[i].ShippingData[0].ShipName,
				orderData[i].ShippingData[0].ShipAddr,
				orderData[i].ShippingData[0].ShipCity,
				orderData[i].ShippingData[0].ShipRegion,
				orderData[i].ShippingData[0].ShipPostalCode,
				orderData[i].ShippingData[0].ShipCountry,
			},
		)
	}

	// flush written buffers to files
	customerCsvWriter.Flush()
	log.Println("Written customers.csv")
	orderCsvWriter.Flush()
	log.Println("Written orders.csv")
}
