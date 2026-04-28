class Solution {
public:
    bool isValid(string s) {
        stack<char>st;
        for(auto &i:s){
            if(i=='(' or i=='{' or i=='['){
                st.push(i);
            }
            else if(!st.empty()){
                if((i==')' and st.top()=='(') or (i=='}' and st.top()=='{') or (i==']' and st.top()=='[')){
                    st.pop();
                }
                else{
                    st.push(i);
                }
            }
            else{
                st.push(i);
            }
        }
        if(st.empty()){
            return true;
        }
        return false;
    }
};