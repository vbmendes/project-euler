defmodule Pe2Test do
  use ExUnit.Case
  
  test "sum of fibonacci even numbers lower than four million is 4613732" do
  	assert Fibonacci.sum_even_elements_until_value(4000000) == 4613732
  end
end
