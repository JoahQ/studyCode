package main

import (
	"fmt"
)

func isEven(i int) bool{
	return i%2 == 0
}

func getPrize() (int, string){
	i := 2
	s := "goldfish"
	return i, s


}

func sumNumbers(numbers...int) int{
	taotl := 0
	for _, number := range numbers{
		taotl += number
	}
	return taotl
}
func sayHi() (x, y string){
	x = "hello"
	y = "world"
	return
}

func feeMe(portion int, eaten int) int{
	eaten = portion + eaten
	if eaten >= 5{
		fmt.Printf("I'm full! I've eaten %d\n", eaten)
		return eaten
	}
	fmt.Printf("I'm still hungry! I have eaten %d\n", eaten)
	return feeMe(portion,eaten)
}

func anotherFunction(f func() string) string{
	return f()
}

func main() {
	defer fmt.Println("I am run after the function completes")
	fmt.Printf("%v\n", isEven(1))
	fmt.Printf("%v\n", isEven(2))

	q, p := getPrize()

	fmt.Printf("You won %v %v\n", q, p)
	fmt.Println(sumNumbers(1,2,3,4,5,6,7))
	fmt.Println(sumNumbers(1,2,3))

	fmt.Println(sayHi())

	fmt.Println(feeMe(1,0))


	fn := func() string{
		return "function caled"
	}

	fmt.Println(anotherFunction(fn))

	for i := 1; i<10 ; i++{
		fmt.Println("i is", i)
	}

	nums := []string {"1,2,3,4,5,6,7,8,9,10","abc", "fe"}
	for i,n:=range nums{
		fmt.Println("The index of the loop is", i)
		fmt.Println("The value from the arry is", n)
	}


	var cheeses = make([]string, 2)
	cheeses[0] = "MMMMMMMM"
	cheeses[1] = "eeeeeeee"
	cheeses = append(cheeses, "cccccc","aaa","bbb","ccc","ddd")
	fmt.Println(cheeses[2])
	fmt.Println(cheeses)
	for i, c := range cheeses{
		fmt.Printf("cheeses[%v]=%v\n",i,c)
	}
	cheeses = append(cheeses[:2], cheeses[2+1:]...)
	fmt.Println(cheeses[2])
	fmt.Println(cheeses)
	for i, c := range cheeses{
		fmt.Printf("cheeses[%v]=%v\n",i,c)
	}

	var ddddddd = make([]string,1)
	fmt.Println()
	fmt.Println(ddddddd)
	copy(ddddddd, cheeses)
	fmt.Println(ddddddd)
}