package main

import (
	"fmt"
)

func main() {
	// var buffer bytes.Buffer

	// for i := 0; i < 500;i++{
	// 	buffer.WriteString("z")
	// }
	// fmt.Println(buffer.String())
	var s string
	for i := 0; i < 10500000; i++ {
		s += "z"
	}
	fmt.Println(s)
}
