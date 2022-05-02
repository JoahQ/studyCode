package main
import (
	"fmt"
	"reflect"
	"strconv"
)

func addition(x int, y int) int {
	return x + y
}

func main() {
	fmt.Println(addition(2, 4))
	s := "there"
	fmt.Println(addition(1, 2))
	var b bool
	fmt.Println(b)
	b = true
	fmt.Println(b)

	var l [4] string
	l[0] = "1"
	l[1] = "2"
	fmt.Println(l)

	var i int = 10
	var f float32 = 1.3

	fmt.Println(reflect.TypeOf(s))
	fmt.Println(reflect.TypeOf(l))
	fmt.Println(reflect.TypeOf(i))
	fmt.Println(reflect.TypeOf(f))

	fmt.Println(reflect.TypeOf(b))
	var ss string = strconv.FormatBool(true)

	fmt.Println(reflect.TypeOf(ss))
	const greeting string = "Hello, world"

	fmt.Println(greeting)
	fmt.Println(&b)
	fmt.Println(&s)
	

}