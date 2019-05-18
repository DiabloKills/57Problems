#include<iostream>
#include<string>

using namespace std;

int main(){

string quote;
string name;


cout <<"please enter a famous quote";
getline(cin,quote);

cout <<" who siad it ";
//cin.ignore();
getline(cin,name);

cout << name << "says" << "\"" << quote << "\""<< endl; 

    return 0;

}