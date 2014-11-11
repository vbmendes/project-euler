defmodule Pe2Test do
  use ExUnit.Case

  test "largest 600851475143 prime divisor" do
    assert Math.largest_prime_divisor(600_851_475_143) == 6_857
  end
end
