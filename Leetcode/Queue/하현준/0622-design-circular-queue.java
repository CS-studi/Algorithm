class MyCircularQueue {

    private int[] arr;
    int front, end, max;

    public MyCircularQueue(int k) {
        this.max = k;
        this.front = 0;
        this.end = -1;
        this.arr = new int[k];
    }

    public boolean enQueue(int value) {
        if (isFull()) {
            return false;
        }
        end = (end + 1) % max;
        arr[end] = value;
        return true;
    }

    public boolean deQueue() {
        if (isEmpty()) {
            return false;
        }
        if (front == end) { // when array is empty
            front = 0;
            end = -1;
        } else {
            front = (front + 1) % max;
        }
        return true;
    }

    public int Front() {
        return isEmpty() ? -1 : arr[front];
    }

    public int Rear() {
        return isEmpty() ? -1 : arr[end];
    }

    public boolean isEmpty() {
        return end == -1;
    }

    public boolean isFull() {
        return end != -1 && (end + 1) % max == front;
    }
}