package main

import "fmt"

func main() {

	// Create HashMap
	hashMap := make(map[string]int)
        
	// Add to HashMap
	hashMap["ALPHA"] = 10
	hashMap["BRAVO"] = 20
	hashMap["CHARLIE"] = 30
	
	// Check if HashMap contains key
	if val, ok := hashMap["ALPHA"]; ok {

	}
	
	// Get value from HashMap
	value, ok := hashMap["ALPHA"]
	
	// Delete key from HashMap
	delete(hashMap, "ALPHA")
	
	// Iterate through keys in HashMap
	for key, _ := range hashMap {

	}
	
	// Iterate through values in HashMap
	for _, value := range hashMap {

	}
	
	// Iterate through keys and values in HashMap
	for key, value := range hashMap {
		fmt.Println(key + " => " + value) 
	}   
}