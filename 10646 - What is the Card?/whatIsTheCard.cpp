#include <iostream>
#include <deque>
#include <string>

using std::deque;
using std::string;
using std::cin;
using std::cout;
using std::endl;

#define NEXTIGNORE(x) 10 - x;

typedef deque<string> cartas;

bool isBeetween2and9(int c) {
   return c >= 2 && c <= 9;
}

int main() {
   int inputSize;
   int x, y = 0;
   string card;
   cartas hand;
   cartas pile;

   cin >> inputSize;

   while (inputSize--) {
      for (int i = 0; i < 52; ++i){
         cin >> card;
         pile.push_back(card);
      }

      auto it = pile.begin(); 
      for (int i = 0; i < 25; ++i){
         pile.pop_back();
         
      }
   }
}


