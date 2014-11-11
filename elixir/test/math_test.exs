defmodule MathTest do
  use ExUnit.Case

  test "largest 4 prime divisor" do
    assert Math.largest_prime_divisor(4) == 2
  end
end