defmodule Fibonacci do
	def get_element(x) when x in [1, 2] do
		1
	end

	def get_element(x) do
		get_element(x - 1) + get_element(x - 2)
	end

	def even_elements_until_value(max_value) when is_integer(max_value) and max_value >= 3 do
		Enum.reverse(Enum.filter(seq([1, 1], max_value), fn x -> rem(x, 2) != 0 end))
	end

	def sum_even_elements_until_value(max_value) when is_integer(max_value) and max_value >= 3 do
		Enum.reduce(even_elements_until_value(max_value), 0, &+/2)
	end

	defp seq([head|tail], max_value) when (head + hd(tail)) <= max_value do
		seq([head + hd(tail), head] ++ tail, max_value)
	end

	defp seq([1], max_value) do
		[1, 1]
	end

	defp seq(x, max_value) do
		x
	end
end