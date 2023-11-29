#include <initializer_list>
#include <string>
#include <vector>
#include <memory>

int main () {
  // Consider auto as a placeholder for the actual type in the following
  // situations:
  
  // Declare local variables with the form auto name = expression 

  auto i = 42;             // int
  auto d = 42.5;           // double
  auto s = "text";         // char const *
  auto v = { 1, 2, 3};     // std::initializer_list<int>

  std::initializer_list<int> V = {1, 2, 3};

  // To declare variables with the auto name = type-id { expression }

  auto b = new char[10]{ 0 };           // char*
  auto s1 = std::string{"text"};        // std::string
  auto v1 = std::vector<int> {1, 2, 3}; // std::vector<int>
  auto p = std::make_shared<int>(42);   // std::shared_ptr<int>

  // To declare named lambda functions, with the form name = lambda-expression,
  // unless the lambda needs to be passed or returned to a function

  auto upper = [](char const c) { return toupper(c); };

  // To declare lambda parameters and return values:

  auto add = [](auto const a, auto const b) { return a + b; };
}

// Declare function return type

template <typename F, typename T>
auto apply(F&& f, T value){
  return f(value);
}
