package main

import (
	"fmt"
	"sort"
)

type Officer struct {
	rank	string 
}

func main() {
    
    ranks := map[string]int { 
        "2LT": 1,
        "1LT": 2,
        "CPT": 3,
        "MAJ": 4,
        "LTC": 5,
        "COL": 6,
    }

	objects := []Officer {
		Officer{"CPT"},
		Officer{"MAJ"},
		Officer{"2LT"},
		Officer{"COL"},
		Officer{"LTC"},
		Officer{"1LT"},
	}

	sort.Slice(objects, func(i, j int) bool {
        return ranks[objects[i].rank] < ranks[objects[j].rank]
    })
	
	for _, officer := range objects {
		fmt.Println(officer.rank)
	}
}
