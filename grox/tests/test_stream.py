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

"""Tests for grox.lib.stream."""

import asyncio
import pytest
from grox.lib.stream import parallel_merge, StreamStatus


class TestParallelMerge:
    @pytest.mark.asyncio
    async def test_empty_streams(self):
        """No streams returns nothing."""
        result = []
        async for item in parallel_merge():
            result.append(item)
        assert result == []

    @pytest.mark.asyncio
    async def test_single_stream(self):
        """Single stream yields all items."""
        async def gen():
            for i in range(3):
                yield i

        result = []
        async for item in parallel_merge(gen()):
            result.append(item)
        assert result == [0, 1, 2]

    @pytest.mark.asyncio
    async def test_two_streams_interleaved(self):
        """Two streams yields interleaved items preserving order within each."""
        async def gen_a():
            for i in [1, 3]:
                yield i

        async def gen_b():
            for i in [2, 4]:
                yield i

        result = []
        async for item in parallel_merge(gen_a(), gen_b()):
            result.append(item)

        # Each generator's items should appear in order
        assert 1 in result
        assert 2 in result
        assert 3 in result
        assert 4 in result
        # Order within each generator preserved
        assert result.index(1) < result.index(3)
        assert result.index(2) < result.index(4)

    @pytest.mark.asyncio
    async def test_stream_propagates_exception(self):
        """Exception in one stream propagates to parallel_merge."""
        async def gen_error():
            raise ValueError("test error")

        async def gen_ok():
            yield 1

        with pytest.raises(ValueError, match="test error"):
            async for _ in parallel_merge(gen_error(), gen_ok()):
                pass


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
