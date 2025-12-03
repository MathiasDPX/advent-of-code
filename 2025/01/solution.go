package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	body, err := ioutil.ReadFile("input.txt")

	if err != nil {
		log.Fatalf("unable to read file: %v", err)
	}

	lines := strings.Split(string(body), "\n")

	solution1 := 0
	solution2 := 0
	idx := 50

	for _, line := range lines {
		move, err := strconv.ParseInt(strings.TrimSpace(line[1:]), 10, 64)
		if err != nil {
			fmt.Printf("Can't convert string to number %s\n", line[1:])
			continue
		}

		step := 1
		if strings.HasPrefix(line, "L") {
			step = -1
		}

		for move != 0 {
			idx += step
			move -= 1

			idx %= 100

			if idx == 0 {
				solution2 += 1
			}
		}

		if idx == 0 {
			solution1 += 1
		}
	}

	fmt.Printf("Solution for part 1: %d\n", solution1)
	fmt.Printf("Solution for part 2: %d\n", solution2)
	os.Exit(0)
}
