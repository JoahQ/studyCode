package main

import (
	"fmt"
)

// "hello/stringutil"
func Reverse(s string) string {
	r := []rune(s)
	for i, j := 0, len(r)-1; i < len(r)/2; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return string(r)
}
func main() {
	s := "ti esrever dna ti pilf nwod gniht ym yup I"

	fmt.Println(Reverse(s))
}
