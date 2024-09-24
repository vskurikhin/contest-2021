package main

import (
	"cmp"
	"fmt"
	"math/rand"
	"sort"
)

func CountingSort(array []int, k int) []int {
	countedValues := make([]int, k)
	for _, value := range array {
		countedValues[value]++
	}

	index := 0
	for value := 0; value < k; value++ {
		for amount := 0; amount < countedValues[value]; amount++ {
			array[index] = value
			index++
		}
	}
	return array
}

func MergeSort[C cmp.Ordered](items []C) []C {
	if len(items) < 2 {
		return items
	}
	first := MergeSort(items[:len(items)/2])
	second := MergeSort(items[len(items)/2:])
	return merge(first, second)
}

type Ordered interface {
	Less(other Ordered) bool
	Compare(other Ordered) int
}

func MergeSortOrdered[O Ordered](items []O) []O {
	if len(items) < 2 {
		return items
	}
	first := MergeSortOrdered(items[:len(items)/2])
	second := MergeSortOrdered(items[len(items)/2:])
	return mergeOrdered(first, second)
}

func QuickSort[C cmp.Ordered](arr []C) []C {
	return quickSortHelper(arr, 0, len(arr)-1)
}

func QuickSortOrdered[O Ordered](arr []O) []O {
	return quickSortHelperOrdered(arr, 0, len(arr)-1)
}

func merge[C cmp.Ordered](a []C, b []C) []C {
	final := []C{}
	i := 0
	j := 0
	for i < len(a) && j < len(b) {
		if a[i] < b[j] {
			final = append(final, a[i])
			i++
		} else {
			final = append(final, b[j])
			j++
		}
	}
	for ; i < len(a); i++ {
		final = append(final, a[i])
	}
	for ; j < len(b); j++ {
		final = append(final, b[j])
	}
	return final
}

func MergeSortYandex(array []int) []int {
	if len(array) == 1 { // базовый случай рекурсии
		return array
	}
	// запускаем сортировку рекурсивно на левой половине
	left := MergeSortYandex(array[0 : len(array)/2])

	// запускаем сортировку рекурсивно на правой половине
	right := MergeSortYandex(array[len(array)/2 : len(array)])

	// заводим массив для результата сортировки
	result := make([]int, len(array))

	// сливаем результаты
	l, r, k := 0, 0, 0
	for l < len(left) && r < len(right) {
		// выбираем, из какого массива забрать минимальный элемент
		if left[l] <= right[r] {
			result[k] = left[l]
			l++
		} else {
			result[k] = right[r]
			r++
		}
		k++
	}
	// Если один массив закончился раньше, чем второй, то
	// переносим оставшиеся элементы второго массива в результирующий
	for l < len(left) {
		result[k] = left[l] // перенеси оставшиеся элементы left в result
		l++
		k++
	}
	for r < len(right) {
		result[k] = right[r] // перенеси оставшиеся элементы right в result
		r++
		k++
	}
	return result
}

func mergeOrdered[O Ordered](a []O, b []O) []O {
	final := []O{}
	i := 0
	j := 0
	for i < len(a) && j < len(b) {
		if a[i].Less(b[j]) { // a[i] < b[j]
			final = append(final, a[i])
			i++
		} else {
			final = append(final, b[j])
			j++
		}
	}
	for ; i < len(a); i++ {
		final = append(final, a[i])
	}
	for ; j < len(b); j++ {
		final = append(final, b[j])
	}
	return final
}

func partition[C cmp.Ordered](arr []C, low, high int) ([]C, int) {
	pivotIdx := low + rand.Intn(high-low)
	pivot := arr[pivotIdx]
	i := low
	for j := low; j < high; j++ {
		if arr[j] < pivot {
			arr[i], arr[j] = arr[j], arr[i]
			i++
		}
	}
	arr[i], arr[high] = arr[high], arr[i]
	return arr, i
}

func quickSortHelper[C cmp.Ordered](arr []C, low, high int) []C {
	if low < high {
		var p int
		arr, p = partition(arr, low, high)
		arr = quickSortHelper(arr, low, p-1)
		arr = quickSortHelper(arr, p+1, high)
	}
	return arr
}

func partitionOrdered[O Ordered](arr []O, low, high int) ([]O, int) {
	pivotIdx := low + rand.Intn(high-low)
	pivot := arr[pivotIdx]
	i := low
	for j := low; j < high; j++ {
		if arr[j].Less(pivot) { // arr[j] < pivot
			arr[i], arr[j] = arr[j], arr[i]
			i++
		}
	}
	arr[i], arr[high] = arr[high], arr[i]
	return arr, i
}

func quickSortHelperOrdered[O Ordered](arr []O, low, high int) []O {
	if low < high {
		var p int
		arr, p = partitionOrdered(arr, low, high)
		arr = quickSortHelperOrdered(arr, low, p-1)
		arr = quickSortHelperOrdered(arr, p+1, high)
	}
	return arr
}

var digitLengths = [10]int{4, 4, 3, 3, 6, 4, 5, 4, 6, 6} // длины слов «ноль», «один»,...

func cardStrength(card int) int { // ключ сравнения
	return digitLengths[card]
}

func insertionSortByKey(array []int, key func(int) int) {
	for i := 1; i < len(array); i++ {
		itemToInsert := array[i]
		j := i
		// заменим сравнение itemToInsert < array[j-1] на сравнение ключей
		for j > 0 && key(itemToInsert) < key(array[j-1]) {
			array[j] = array[j-1]
			j--
		}
		array[j] = itemToInsert
	}
}

func isFirstCardWeaker(card1, card2 int) bool { // функция-компаратор
	return digitLengths[card1] < digitLengths[card2]
}

// воспользуемся уже знакомой сортировкой вставками
func insertionSortByComparator(array []int, less func(int, int) bool) {
	for i := 1; i < len(array); i++ {
		itemToInsert := array[i]
		j := i
		// заменим сравнение itemToInsert < array[j-1] на компаратор less
		for j > 0 && less(itemToInsert, array[j-1]) {
			array[j] = array[j-1]
			j--
		}
		array[j] = itemToInsert
	}
}

func keyForCard(card int) []int {
	return []int{-digitLengths[card], card}
}

func main() {
	cards := []int{3, 7, 9, 2, 3}
	sort.Slice(cards, func(i, j int) bool {
		keyI := keyForCard(cards[i])
		keyJ := keyForCard(cards[j])
		if keyI[0] == keyJ[0] {
			return keyI[1] < keyJ[1]
		}
		return keyI[0] < keyJ[0]
	})
	fmt.Println(cards)
	insertionSortByKey(cards, cardStrength)
	fmt.Println(cards)
}
