class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<long> st;
        for (const string& s : tokens) {
            if (s == "+" || s == "-" || s == "*" || s == "/") {
                long el1 = st.top(); st.pop();
                long el2 = st.top(); st.pop();
                
                if (s == "+") st.push(el2 + el1);
                else if (s == "-") st.push(el2 - el1);
                else if (s == "*") st.push(el2 * el1);
                else st.push(el2 / el1);
            } 
            else {
                st.push(stol(s));
            }
        }
        return (int)st.top();
    }
};