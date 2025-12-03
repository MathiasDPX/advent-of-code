package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	// How many digits in the "best suite"
	DIGITS := 12

	body, err := os.ReadFile("input.txt")

	if err != nil {
		log.Fatalf("unable to read file: %v", err)
	}

	lines := strings.Split(string(body), "\n")

	result := 0

	for _, line := range lines {
		line = strings.TrimRight(line, "\r")

		if len(line) == 0 {
			continue
		}

		length := len(line)
		selected := make([]string, 0, 12)
		start := 0

		for i := range DIGITS {
			end := length - (DIGITS - 1 - i)
			best_idx := start

			for j := start; j < end; j++ {
				if line[j] > line[best_idx] {
					best_idx = j
				}
			}

			selected = append(selected, string(line[best_idx]))
			start = best_idx + 1
		}

		top, err := strconv.Atoi(strings.Join(selected, ""))

		if err != nil {
			fmt.Println(err)
		}

		result += top
	}

	fmt.Println("Solution:", result)
	os.Exit(0)
}
