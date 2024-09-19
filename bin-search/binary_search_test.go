package bin_search

import (
	"github.com/stretchr/testify/assert"
	"math"
	"strconv"
	"testing"
)

func TestBinarySearch(t *testing.T) {
	intArray := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	for i := 0; i < 10; i++ {
		assert.Equal(t, i, BinarySearch(intArray, i, 0, len(intArray)))
	}
	assert.Equal(t, math.MinInt, BinarySearch(intArray, -1, 0, len(intArray)))
	assert.Equal(t, math.MinInt, BinarySearch(intArray, 10, 0, len(intArray)))
	float64Array := []float64{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	for i := 0; i < 10; i++ {
		assert.Equal(t, i, BinarySearch(float64Array, float64(i), 0, len(intArray)))
	}
	assert.Equal(t, math.MinInt, BinarySearch(float64Array, -1, 0, len(intArray)))
	assert.Equal(t, math.MinInt, BinarySearch(float64Array, 10, 0, len(intArray)))
	stringArray := []string{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
	for i := 0; i < 10; i++ {
		strconv.Itoa(i)
		assert.Equal(t, i, BinarySearch(stringArray, strconv.Itoa(i), 0, len(intArray)))
	}
	assert.Equal(t, math.MinInt, BinarySearch(stringArray, strconv.Itoa(-1), 0, len(intArray)))
	assert.Equal(t, math.MinInt, BinarySearch(stringArray, strconv.Itoa(10), 0, len(intArray)))
	assert.Equal(t, math.MinInt, BinarySearch(stringArray, "bla", 0, len(intArray)))
}

type ordered struct {
	value int
}

func (o ordered) Less(other Ordered) bool {
	return o.value < other.(ordered).value
}

func (o ordered) Compare(other Ordered) int {
	if o.value < other.(ordered).value {
		return -1
	}
	if o.value > other.(ordered).value {
		return 1
	}
	return 0
}

var _ Ordered = ordered{}

func TestBinarySearchOrdered(t *testing.T) {
	arr := []ordered{{value: 0},
		{value: 1}, {value: 2}, {value: 3},
		{value: 4}, {value: 5}, {value: 6},
		{value: 7}, {value: 8}, {value: 9}}
	for i := 0; i < 10; i++ {
		assert.Equal(t, i, BinarySearchOrdered(arr, ordered{value: i}, 0, len(arr)))
	}
	assert.Equal(t, math.MinInt, BinarySearchOrdered(arr, ordered{value: -1}, 0, len(arr)))
	assert.Equal(t, math.MinInt, BinarySearchOrdered(arr, ordered{value: 10}, 0, len(arr)))
}

func TestLeftBinarySearch(t *testing.T) {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	assert.Equal(t, 0, LeftBinarySearch(0, len(arr)-1, func(i int) bool {
		return arr[i] > -1
	}))
	assert.Equal(t, 1, LeftBinarySearch(0, len(arr)-1, func(i int) bool {
		return arr[i] > 0
	}))
	assert.Equal(t, 6, LeftBinarySearch(0, len(arr)-1, func(i int) bool {
		return arr[i] > 5
	}))
	assert.Equal(t, math.MinInt, LeftBinarySearch(0, len(arr)-1, func(i int) bool {
		return arr[i] > 9
	}))
	assert.Equal(t, math.MinInt, LeftBinarySearch(len(arr)-1, 0, func(i int) bool {
		return arr[i] > -1
	}))
}

func TestRightBinarySearch(t *testing.T) {
	arr := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	assert.Equal(t, 9, RightBinarySearch(0, len(arr)-1, func(i int) bool {
		return arr[i] < 10
	}))
	assert.Equal(t, 8, RightBinarySearch(0, len(arr)-1, func(i int) bool {
		return arr[i] < 9
	}))
	assert.Equal(t, 4, RightBinarySearch(0, len(arr)-1, func(i int) bool {
		return arr[i] < 5
	}))
	assert.Equal(t, math.MinInt, RightBinarySearch(0, len(arr)-1, func(i int) bool {
		return arr[i] < 0
	}))
	assert.Equal(t, math.MinInt, RightBinarySearch(len(arr)-1, 0, func(i int) bool {
		return arr[i] < 10
	}))
}
