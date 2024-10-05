package bin_search

import (
	"cmp"
	"math"
)

func BinarySearch[O cmp.Ordered](arr []O, x O, left, right int) int {
	if right <= left {
		// промежуток пуст
		return math.MinInt
	}
	// промежуток не пуст
	middle := (left + right) / 2
	if x == arr[middle] {
		// центральный элемент — искомый
		return middle
	} else if x < arr[middle] {
		// искомый элемент меньше центрального значит следует искать в левой половине
		return BinarySearch(arr, x, left, middle)
	} else {
		// иначе следует искать в правой половине
		return BinarySearch(arr, x, middle+1, right)
	}
}

type Ordered interface {
	Less(other Ordered) bool
	Compare(other Ordered) int
}

func BinarySearchOrdered[O Ordered](arr []O, x O, left, right int) int {
	if right <= left {
		// промежуток пуст
		return math.MinInt
	}
	// промежуток не пуст
	middle := (left + right) / 2
	if x.Compare(arr[middle]) == 0 { // x == arr[middle]
		// центральный элемент — искомый
		return middle
	} else if x.Less(arr[middle]) { // x < arr[middle]
		// искомый элемент меньше центрального значит следует искать в левой половине
		return BinarySearchOrdered(arr, x, left, middle)
	} else {
		// иначе следует искать в правой половине
		return BinarySearchOrdered(arr, x, middle+1, right)
	}
}

func LeftBinarySearch(left, right int, check func(int) bool) int {
	if left > right {
		return math.MinInt
	}
	for left < right {
		middle := (left + right) / 2
		if check(middle) {
			right = middle
		} else {
			left = middle + 1
		}
	}
	if check(left) {
		return left
	}
	return math.MinInt
}

func RightBinarySearch(left, right int, check func(int) bool) int {
	if left > right {
		return math.MinInt
	}
	for left < right {
		middle := (left + right + 1) / 2
		if check(middle) {
			left = middle
		} else {
			right = middle - 1
		}
	}
	if check(left) {
		return left
	}
	return math.MinInt
}
