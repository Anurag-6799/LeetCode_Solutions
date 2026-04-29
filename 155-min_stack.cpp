class MinStack {
private:
    std::vector<std::pair<int, int>> st;

public:
    MinStack() {}
    
    void push(int val) {
        if (st.empty()) {
            st.push_back({val, val});
        } else {
            int currentMin = min(val, st.back().second);
            st.push_back({val, currentMin});
        }
    }
    
    void pop() {
        if (!st.empty()) {
            st.pop_back();
        }
    }
    
    int top() {
        return st.back().first;
    }
    
    int getMin() {
        return st.back().second;
    }
};