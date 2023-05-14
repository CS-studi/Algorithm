import Foundation

class MyCircularQueue {

    private var data: [Int]
    private var head: Int
    private var tail: Int
    private var size: Int
    private let k: Int
    
    init(_ k: Int) {
        self.data = Array(repeating: 0, count: k)
        self.head = 0
        self.tail = 0
        self.size = 0
        self.k = k
    }
    
    func enQueue(_ value: Int) -> Bool {
        guard !isFull() else { return false }
        data[tail] = value
        tail = tail == k - 1 ? 0 : tail + 1
        size += 1
        return true
    }
    
    func deQueue() -> Bool {
        guard !isEmpty() else { return false }
        head = head == k - 1 ? 0 : head + 1
        size -= 1
        return true
    }
    
    func Front() -> Int {
        guard !isEmpty() else { return -1 }
        return data[head]
    }
    
    func Rear() -> Int {
        guard !isEmpty() else { return -1 }
        return data[tail == 0 ? k - 1 : tail - 1]
    }
    
    func isEmpty() -> Bool {
        size == 0
    }
    
    func isFull() -> Bool {
        size == k
    }
}
