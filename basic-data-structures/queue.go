package main

type Queue[T any] struct {
	queue []T
	maxN  int
	head  int
	tail  int
	size  int
}

func NewQueue[T any](n int) *Queue[T] {
	return &Queue[T]{
		queue: make([]T, n),
		maxN:  n,
		head:  0,
		tail:  0,
		size:  0,
	}
}

func (q *Queue[T]) IsEmpty() bool {
	return q.size == 0
}

func (q *Queue[T]) Push(x T) bool {
	if q.size != q.maxN {
		q.queue[q.tail] = x
		q.tail = (q.tail + 1) % q.maxN
		q.size += 1
		return true
	}
	return false
}

func (q *Queue[T]) Pop() T {
	if q.IsEmpty() {
		return nil
	}
	x := q.queue[q.head]
	q.queue[q.head] = nil
	q.head = (q.head + 1) % q.maxN
	q.size -= 1
	return x
}
