package main

import (
	"bytes"
	"fmt"
)

func main() {
	var buffer bytes.Buffer

	for i := 0; i < 1050000000000; i++ {
		buffer.WriteString("z")
	}
	fmt.Println(buffer.String())

}
