#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main(){
  stack<char> operators;
  stack<char> expression;
  string input = "7+5*(4-1)";

  for (char x : input){
    if(isdigit(x))
      expression.push(x);
    else{
      if(precedence(x)>precedence(operators.top()))
        operators.push(x);
      else{
        char top = operators.top();
        expression.pop();
        expression.push(top);
        operators.push(x);
      }
    }
  }
  //if prec current > prec stack, push current to stack
  //if prec current <= prec stack, pop stack to current

  return 0;
}

int precedence(char x){
  if (x=='*' || x=='/')
    return 1;
  else if (x=='+' || x=='-')
    return 0;
  return -1;
}