#include <iostream>
#include <string>

using namespace std;
class Gun
{
public:
    virtual void Shoot() // Virtual 달려있으면 할당된 것에 맞는 함수 부르고, 아니면 본인 타입에 맞는 것 부름
    {
        cout << "Bang!" << endl;
    }

    void Pang()
    {
        cout << "Pang!" << endl;
    }
};

class Pistol : public Gun
{
public:
    void Shoot() override
    {
        cout << "Pew!" << endl;
    }

    void Feng()
    {
        cout << "Feng!" << endl;
    }
};

int Sum(int n)
{
    return n + Sum(n-1);
}

int main()
{
    Gun MyGun;
    Pistol MyPistol;
    cout << &MyGun << endl;
    cout << &MyPistol << endl;

    Gun* Gunptr;

    Gunptr = &MyGun;
    cout << Gunptr << endl;
    Gunptr->Shoot();
    Gunptr->Pang();

    Gunptr = &MyPistol;
    cout << Gunptr << endl;
    Gunptr->Shoot();
    Gunptr->Pang();
    // Gunptr->Feng();

    Sum(10);

    return 0;
}