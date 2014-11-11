defmodule FibonacciTest do
  use ExUnit.Case

  test "fibonacci first element should be 1" do
    assert Fibonacci.get_element(1) == 1
  end

  test "fibonacci second element should be 1" do
    assert Fibonacci.get_element(2) == 1
  end

  test "fibonacci third element should be 2" do
    assert Fibonacci.get_element(3) == 2
  end

  test "fibonacci fourth element should be 3" do
    assert Fibonacci.get_element(4) == 3
  end

  test "fibonacci fifth element should be 5" do
    assert Fibonacci.get_element(5) == 5
  end

  test "even fibonacci numbers" do
  	assert Fibonacci.even_elements_until_value(5) == [1,1,3,5]
  end
end
