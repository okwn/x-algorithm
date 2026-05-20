# Copyright 2026 X.AI Corp.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for grox.lib.utils."""

import pytest
from grox.lib.utils import camel_to_snake, snake_to_camel


class TestCamelToSnake:
    def test_simple(self):
        assert camel_to_snake("HelloWorld") == "hello_world"

    def test_with_numbers(self):
        assert camel_to_snake("GPT3Model") == "g_p_t3_model"

    def test_already_snake(self):
        assert camel_to_snake("hello_world") == "hello_world"

    def test_single_word(self):
        assert camel_to_snake("Test") == "test"

    def test_empty(self):
        assert camel_to_snake("") == ""

    def test_leading_capitals(self):
        assert camel_to_snake("HTTPServer") == "h_t_t_p_server"


class TestSnakeToCamel:
    def test_simple(self):
        assert snake_to_camel("hello_world") == "HelloWorld"

    def test_single_word(self):
        assert snake_to_camel("test") == "Test"

    def test_already_camel(self):
        assert snake_to_camel("HelloWorld") == "HelloWorld"

    def test_empty(self):
        assert snake_to_camel("") == ""

    def test_multiple_underscores(self):
        assert snake_to_camel("a_b_c_d") == "ABCD"


class TestInverseProperty:
    def test_camel_to_snake_round_trip(self):
        """snake_to_camel(camel_to_snake(x)) == title-cased x for simple names."""
        assert snake_to_camel(camel_to_snake("HelloWorld")) == "HelloWorld"

    def test_snake_to_camel_round_trip(self):
        """camel_to_snake(snake_to_camel(x)) is identity for snake_case."""
        assert camel_to_snake(snake_to_camel("hello_world")) == "hello_world"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
