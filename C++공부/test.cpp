#include <iostream>
class MyCar {
protected: //상속한 클래스 사용가능
    //멤버변수
    int fuel = 0;
    bool power = false;

public:
    //메소드
    void go() {
        this->fuel--;
    }

    void oiling(int n) {
        this->fuel += n;
    }

    void fuel_check() {
        std::cout << "연료 : " << fuel << std::endl;
    }
};

class MySuv : public MyCar { // 상속
public:
    //메소드
    void go() {
        this->fuel-=2;
    }
};

void main() {
    MySuv car = MySuv(); //MySuv 객체 생성

    //메서드 호출
    car.oiling(100);
    car.fuel_check();
    for (int i = 0; i < 10; i++) car.go();
    car.fuel_check();
    car.oiling(100);
    for (int i = 0; i < 10; i++) car.go();
    car.fuel_check();
}