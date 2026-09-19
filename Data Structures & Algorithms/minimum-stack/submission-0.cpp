class MinStack {
    stack<int> s;        // main stack
    stack<int> min_s;    // stack to track minimums

public:
    MinStack() {}

    void push(int val) {
        s.push(val);
        // push to min_s if empty or val <= current min
        if (min_s.empty() || val <= min_s.top())
            min_s.push(val);
    }

    void pop() {
        if (!s.empty()) {
            int val = s.top();
            s.pop();
            if (val == min_s.top())
                min_s.pop();
        }
    }

    int top() {
        return s.top();
    }

    int getMin() {
        return min_s.top();
    }
};