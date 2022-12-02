#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <string>

using namespace std;

class A
{
public:
    void foo()
    {
        cout << "foo" << endl;
    }

    virtual void boo()
    {
        cout << "boo" << endl;
    }

    void coo()
    {
        cout << "coo" << endl;
    }
};

class B : public A
{

public:
    void boo() override
    {
        cout << "B boo" << endl;
    }

    void coo()
    {
        cout << "B coo" << endl;
    }
};

int main()
{
    // vector<int> vec; // vector는 메모리 연속적, deque는 메모리 연속 x, 
    // // arraylist에 동기화가 보장된 최적화된 클래스
    // // resize, clear, begin, end <- begin, end는 주소를 리턴, erase : 구간 원소 삭제
    // vec.push_back(5);
    // vec.pop_back();
    // vec.empty();
    
    // stack<int> st;
    // st.push(4);
    // st.pop();
    // st.top();
    // st.empty();
    // st.size();
    
    // queue<int> q;
    // q.push(4);
    // q.pop();
    // q.front();
    // q.empty();
    // q.size();

    // priority_queue<int> p_q; // queue 라이브러리에 포함됨
    // p_q.push(1);
    // p_q.push(9);
    // p_q.top();
    // p_q.pop();

    // deque<int> dq; // 동적 배열, 임의의 위치에 있는 원소 접근과, 앞 뒤 원소 추가 O(1), 삽입 양쪽끝
    // dq.push_front(5);
    // dq.push_back(5);
    // dq.pop_front();
    // dq.pop_back();

    // set<int> s; // 균형잡힌 이진트리, 원소 삽입과 삭제, 탐색 등의 연산은 O(logn) 보장
    // s.insert(5);
    // if (s.find(6) != s.end())
    //     printf("존재합니다.\n");
    // else
    //     printf("없습니다.\n");
    // s.size();
    // s.clear();
    // s.erase(++s.begin()); // 2번째 원소 삭제

    // pair<int, int> p;
    // p = make_pair(4, 5);
    // p = {4, 5}; // C++11부터 가능
    // p.first;
    // p.second;

    // map<int, int> m;
    // m.insert(make_pair(4, 5)); // m[4] = 5; 도 가능
    // m.find(4);
    // m.count(4);
    // m.size();
    // m.clear();
    // m.erase(++m.begin());

    // Algorithm
    // sort, stable_sort, lower_bound, upper_bound, max_element, min_element, 
    // unique : 구간 내 원소들 정렬되어 있어야 하고, 중복 제거
    // next_permutation : 순열, 생성 있으면 true, 없으면 false 


    cout << "Start" << endl;
    A a = A();
    a.boo();
    a.foo();
    a.coo();
    B b = B();
    b.boo();
    b.foo();
    b.coo();

    string str = "123456789";
    for (int i = 0; i < str.size(); ++i)
    {
        cout << int(str[i]);
    }



    return 0;
}