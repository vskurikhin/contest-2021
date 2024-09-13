package main

import (
	"fmt"
)

type Queue struct {
	queue []interface{}
	maxN  int
	head  int
	tail  int
	size  int
}

func NewQueue(n int) *Queue {
	return &Queue{
		queue: make([]interface{}, n),
		maxN:  n,
		head:  0,
		tail:  0,
		size:  0,
	}
}

func (q *Queue) IsEmpty() bool {
	return q.size == 0
}

func (q *Queue) Push(x interface{}) {
	if q.size != q.maxN {
		q.queue[q.tail] = x
		q.tail = (q.tail + 1) % q.maxN
		q.size += 1
	}
}

func (q *Queue) Pop() interface{} {
	if q.IsEmpty() {
		return nil
	}
	x := q.queue[q.head]
	q.queue[q.head] = nil
	q.head = (q.head + 1) % q.maxN
	q.size -= 1
	return x
}

func main() {
	var s, j string

	_, _ = fmt.Scanf("%s", &s)
	_, _ = fmt.Scanf("%s", &j)

	seen := map[rune]struct{}{}
	for _, letter := range s {
		seen[letter] = struct{}{}
	}

	result := 0
	for _, stone := range j {
		if _, ok := seen[stone]; ok {
			result++
		}
	}

	fmt.Println(result)
}
