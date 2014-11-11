defmodule Math do
  def largest_prime_divisor(number) do
    number
    |> factorization
    |> Enum.max
  end

  def factorization(number) do
    do_factorization(number, 2, [])
  end

  defp do_factorization(number, divisor, acc) when divisor > number do
    acc
  end

  defp do_factorization(number, divisor, acc) when rem(number, divisor) == 0 do
    do_factorization(div(number, divisor), divisor, [divisor|acc])
  end

  defp do_factorization(number, divisor, acc) when rem(number, divisor) != 0 do
    do_factorization(number, divisor + 1, acc)
  end
end