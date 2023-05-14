/** one queue */
class MyStack {

    private final Queue<Integer> queueA;
    private int flag = 1;

    public MyStack() {
        this.queueA = new LinkedList<>();
    }

    public void push(int x) {
        queueA.add(flag * x);
    }

    public int pop() {
        int last = -1;
        while (!queueA.isEmpty()) {
            last = queueA.poll();
            if (queueA.isEmpty()) {
                break;
            }
            if (flag * queueA.peek() < 0) {
                break;
            }
            queueA.add(-last);
        }
        flag *= -1;
        return Math.abs(last);
    }

    public int top() {
        int last = pop();
        queueA.add(-last);
        return Math.abs(last);
    }

    public boolean empty() {
        return queueA.isEmpty();
    }
}

/** two queues
class MyStack {

    private final Queue<Integer> queueA;
    private final Queue<Integer> queueB;
    private boolean flag = true;

    public MyStack() {
        this.queueA = new LinkedList<>();
        this.queueB = new LinkedList<>();
    }

    public void push(int x) {
        if (flag) {
            queueA.add(x);
        } else {
            queueB.add(x);
        }
    }

    public int pop() {
        int last = -1;
        if (flag) {
            while (!queueA.isEmpty()) {
                last = queueA.poll();
                if (!queueA.isEmpty()) {
                    queueB.add(last);
                }
            }
        } else {
            while (!queueB.isEmpty()) {
                last = queueB.poll();
                if (!queueB.isEmpty()) {
                    queueA.add(last);
                }
            }
        }

        flag = !flag;
        return last;
    }

    public int top() {
        int last = pop();
        if (flag) {
            queueA.add(last);
        } else {
            queueB.add(last);
        }
        return last;
    }

    public boolean empty() {
        if (flag) {
            return queueA.isEmpty();
        }
        return queueB.isEmpty();
    }
}

 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */