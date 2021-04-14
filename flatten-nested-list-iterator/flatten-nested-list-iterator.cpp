class NestedIterator {
    queue<int> data;
    
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        flatten(nestedList);
    }
    
    void flatten(vector<NestedInteger> &list){
        for (NestedInteger i : list){
            if (i.isInteger()) data.push(i.getInteger());
            else flatten(i.getList());
        }
    }
    
    int next() {
        int n = data.front();
        data.pop();
        return n;
    }
    
    bool hasNext() { 
        return data.size() > 0;
    }
};